from memory.retrieve_memory import (retrieve_memory)

def memory_agent(state):
    print("\n🧠 Memory Agent")
    memories = retrieve_memory(state["question"])
    print(f"Retrieved {len(memories)} memories")
    return {"memories":memories}