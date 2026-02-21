import os
import json
from dotenv import load_dotenv
from pinecone import Pinecone

# Load env
load_dotenv()

API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=API_KEY)
index = pc.Index(INDEX_NAME)

EXPORT_PATH = "data/embeddings/pinecone_exports/vectors.jsonl"


os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)

# Stats
stats = index.describe_index_stats()
total = stats["total_vector_count"]

print("Total vectors:", total)

# Collect IDs
id_list = []

for page in index.list():
    for vid in page:
        id_list.append(vid)

print("Collected IDs:", len(id_list))

# Fetch + export
BATCH_SIZE = 100

with open(EXPORT_PATH, "w") as f:
    for i in range(0, len(id_list), BATCH_SIZE):
        batch_ids = id_list[i:i + BATCH_SIZE]

        res = index.fetch(ids=batch_ids)

        for vid, vec in res.vectors.items():
            record = {
                "id": vid,
                "values": vec.values,
                "metadata": vec.metadata or {}
            }

            f.write(json.dumps(record) + "\n")

print("Export completed:", EXPORT_PATH)