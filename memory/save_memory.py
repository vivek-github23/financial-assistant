import json
import os

MEMORY_FILE = "memory/memory_store.json"

def save_memory(question, analysis):
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memories = json.load(f)
    else:
        memories = []

    memories.append({
        "question": question,
        "analysis": analysis
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(memories,f,indent=4)