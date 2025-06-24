# NewsGenie

**An AI-Powered News and Information Assistant**

NewsGenie is your intelligent companion for navigating the news and staying informed. Whether you need fast answers to general questions or a reliable way to verify headlines, NewsGenie uses cutting-edge AI to simplify how you access and understand information.

![News Query Diagram](images/news-genie.png)

## 🚀 Features

- **Smart Query Detection**: Automatically distinguishes between general knowledge and current news questions.
- **Instant Answers**: Provides concise responses to factual questions using OpenAI's GPT-4o-mini model.
- **Real-Time News Search**: Performs web searches for recent news-related queries.
- **Fake News Detection**: Uses AI to evaluate the credibility of news articles and summaries.
- **Summarization**: Breaks down complex news stories into digestible highlights.
- **Trending Topics**: Tracks what's trending across major media outlets, personalized to your interests.
- **Conversational AI**: Engage with an adaptive chatbot in natural language.

![News Query Example](images/news-query.png)

## 🧠 How It Works

1. User submits a query via the input box.
2. NewsGenie determines if the query is **informational** or **news-based**:
   - Informational: e.g., "What is the capital of France?"
     - Answered directly via GPT-4o-mini.
   - News-based: e.g., "Was a new Pope elected yesterday?"
     - Searched via web APIs.
     - Validated and summarized using a chatbot pipeline to avoid misinformation.

## ⚙️ Installation

### 1. Create a Conda Environment

```bash
conda create -n news-genie-env python=3.10
conda activate news-genie-env
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your-openai-key
SERPER_API_KEY=your-serper-api-key
```

Or use the echo command:

```bash
echo "OPENAI_API_KEY=your-openai-key" >> .env
echo "SERPER_API_KEY=your-serper-api-key" >> .env
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🙌 Acknowledgements

- [OpenAI](https://openai.com/)
- [Serper.dev](https://serper.dev/)
- [Streamlit](https://streamlit.io/)
