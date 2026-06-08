import json
import os

MEMORY_FILE = "memory/memory_store.json"

def retrieve_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        memories = json.load(f)

    return memories[-5:]