from memory.retrieve_memory import (retrieve_memory)

def memory_agent(state):
    print("\n🧠 Memory Agent")
    if "memory" not in state.get("required_agents", []):
        print("⏭️ Skipping Memory Agent")
        return {}
    print("🧠 Memory Agent")
    memories = retrieve_memory(state["question"])
    print(f"Retrieved {len(memories)} memories")
    return {"memories":memories}