from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os


class ChatApplication:
    def __init__(self, template: str, model_name="gpt-4o-mini"):
        # Get API key from environment variables
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
            
        # Initialize OpenAI API key
        os.environ["OPENAI_API_KEY"] = api_key
        
        # Initialize the language model (GPT-4)
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.0
        )
        
        # Set template
        self.template = template
            
        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_template(self.template)
        
        # Create the chain using the new approach
        self.chain = (
            RunnablePassthrough() 
            | self.prompt 
            | self.llm 
            | StrOutputParser()
        )

