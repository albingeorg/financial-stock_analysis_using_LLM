import os
from dotenv import load_dotenv
import streamlit as st
from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.llms.gemini import Gemini
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from llama_index.core import Settings

# Set Google embeddings instead of OpenAI
Settings.embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY is not set in .env")

# Configure Gemini LLM
llm = Gemini(model="models/gemini-1.5-pro", api_key=api_key)

# NEW way: configure settings instead of ServiceContext
Settings.llm = llm

# Load your index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()

# Streamlit app
st.title('📊 Financial Stock Analysis using LlamaIndex + Gemini')

st.header("Reports:")

report_type = st.selectbox(
    'What type of report do you want?',
    ('Single Stock Outlook', 'Competitor Analysis')
)

if report_type == 'Single Stock Outlook':
    symbol = st.text_input("Stock Symbol")

    if symbol:
        with st.spinner(f'Generating report for {symbol}...'):
            response = query_engine.query(
                f"Write a report on the outlook for {symbol} stock from 2023 to 2027. "
                f"Include potential risks and headwinds."
            )
            st.write(str(response))

elif report_type == 'Competitor Analysis':
    symbol1 = st.text_input("Stock Symbol 1")
    symbol2 = st.text_input("Stock Symbol 2")

    if symbol1 and symbol2:
        with st.spinner(f'Generating report for {symbol1} vs. {symbol2}...'):
            response = query_engine.query(
                f"Write a competitor analysis between {symbol1} and {symbol2} stocks."
            )
            st.write(str(response))

