# Financial Stock Analysis using LlamaIndex + Gemini

This project is a **Retrieval-Augmented Generation (RAG)** application that uses **Google Gemini** via LlamaIndex to analyze financial stock data and articles.  
It allows you to fetch news articles, index them with embeddings, and query them interactively using **Streamlit**.

---

## 🚀 Features
- Fetch and unzip financial articles automatically
- Build a vector index using **LlamaIndex + Gemini**
- Persist the index for reuse across sessions
- Query the indexed articles via command line or Streamlit
- Generate:
  - Single Stock Outlook (2023–2027 with risks & headwinds)
  - Competitor Analysis between two stocks

---

## 📂 Project Structure
```
.
├── 01_fetch_data.py      # Download & summarize articles with Gemini
├── 02_index_news.py      # Build index from articles
├── 03_query_news.py      # Query index via CLI
├── app.py                # Streamlit app for stock analysis
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── storage/              # Persisted vector index
└── articles/             # Unzipped dataset
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/albingeorg/RAG_Application_using_Gemini-Pro.git
cd RAG_Application_using_Gemini-Pro
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables
Create a `.env` file in the project root and add your **Gemini API Key**:

```ini
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Running the Project

### Step 1: Fetch and Index Articles
```bash
python 01_fetch_data.py
```

### Step 2: (Optional) Rebuild Index
```bash
python 02_index_news.py
```

### Step 3: Query Articles via CLI
```bash
python 03_query_news.py
```

### Step 4: Run Streamlit App
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📝 Example Queries
- **Single Stock Outlook**:  
  *"Write a report on the outlook for TSLA stock from the years 2023–2027. Include risks and headwinds."*

- **Competitor Analysis**:  
  *"Write a report on the competition between AAPL stock and MSFT stock."*

- **General Query**:  
  *"Tell me about Google's new supercomputer."*

---

## 📦 Requirements
Your `requirements.txt` should contain:

```txt
google-generativeai
llama-index
llama-index-llms-gemini
streamlit
python-dotenv
pandas
ib_insync
jinja2
```
