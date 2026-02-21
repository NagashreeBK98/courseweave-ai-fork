import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load env
load_dotenv()

API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Init client
pc = Pinecone(api_key=API_KEY)

# Connect to index
index = pc.Index(INDEX_NAME)

# Test
stats = index.describe_index_stats()

print("Connected to Pinecone!")
print("Index stats:", stats)