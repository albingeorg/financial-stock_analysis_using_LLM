import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage

# Load environment variables
load_dotenv()

# Load the index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Query engine
query_engine = index.as_query_engine()

response = query_engine.query("Tell me about Google's new supercomputer.")
print(response)
