from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from utils.agents import ChatApplication
from utils.templates import classify_intention_template, info_template, validate_news_template
from utils.tools import SearchTools
from dotenv import load_dotenv
import os

load_dotenv()

class State(TypedDict):
    input: str  
    decision: str
    error: str  
    output: str


classify_intention_chat = ChatApplication(classify_intention_template)
info_chat = ChatApplication(info_template)
validate_news_chat = ChatApplication(validate_news_template)
search_hlp = SearchTools()


def classify_intention(state: State) -> State:

    """Classifies the user's intention based on the input."""

    try:
        state["decision"] = classify_intention_chat.chain.invoke(
            {"input": state["input"]}
        )
    except Exception as e:
        state["error"] = f"Error in classify_intention: {str(e)}"

    return state


def route_decision(state: State):
    """Maps the decision to the correct function."""
    
    decision = "informational"
    try:
        decision = state["decision"].strip().lower()
    except Exception as e:
        state["error"] = f"Error in route_decision: {str(e)}"    
    
    return decision


def generate_info_answer(state: State) -> State:
    """Generates an informational answer based on the user's input."""
    
    try:
        state["output"] = info_chat.chain.invoke(state["input"])
    except Exception as e:
        state["error"] = f"Error in generate_info_answer: {str(e)}"
    
    return state


def call_news_api(state: State) -> State:
    """Calls the news API to get the latest news based on the user's input."""
    
    try:
        state["input"] = search_hlp.search_internet(state["input"])
    except Exception as e:
        state["error"] = f"Error in call_news_api: {str(e)}"
    
    return state


def validate_news(state: State) -> State:
    """Validates the news obtained from the API."""
    
    try: 
        state["output"] = validate_news_chat.chain.invoke(state["input"])
    except Exception as e:
        state["error"] = f"Error in validate_news: {str(e)}"
        
    return state


def build_workflow():
    """Constructs the parallel workflow."""
    workflow = StateGraph(State)
    
    workflow.add_node("classify_intention", classify_intention)
    workflow.add_node("generate_info_answer", generate_info_answer)
    workflow.add_node("call_news_api", call_news_api)
    workflow.add_node("validate_news", validate_news)

    workflow.add_edge(START, "classify_intention")
    workflow.add_conditional_edges(
        "classify_intention",
        route_decision,
        {
            "informational": "generate_info_answer",
            "news": "call_news_api",
        },
    )
    workflow.add_edge("generate_info_answer", END)
    workflow.add_edge("call_news_api", "validate_news")
    workflow.add_edge("validate_news", END)

    return workflow.compile()

    
def run_streamlit():
    """Run the Streamlit app."""
    import streamlit as st

    st.title("News Genie")
    user_input = st.text_input("Type your input:")

    workflow = build_workflow()
    
    if st.button("Submit"):
        state = workflow.invoke({"input": user_input, "error": "", "output": ""})
        
        if state["error"]:
            st.subheader("Error:")
            st.error(f"Error: {state['error']}")
        else:
            st.subheader("Detected Choice:")
            st.write(state["decision"].capitalize())
            st.subheader("Answer:")
            st.write(state["output"])


if __name__ == "__main__":
    run_streamlit()
