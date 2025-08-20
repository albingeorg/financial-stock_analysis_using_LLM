import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Load environment variables
load_dotenv()

# Load documents
documents = SimpleDirectoryReader('articles').load_data()

# Build index
index = VectorStoreIndex.from_documents(documents)

# Persist storage
index.storage_context.persist()
