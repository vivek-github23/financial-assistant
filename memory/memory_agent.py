from memory.retrieve_memory import (retrieve_memory)
from utils.logger import logger

def memory_agent(state):
    logger.info("\n🧠 Memory Agent")
    if "memory" not in state.get("required_agents", []):
        logger.info("⏭️ Skipping Memory Agent")
        return {}
    logger.info("🧠 Memory Agent")
    memories = retrieve_memory(state["question"])
    logger.info(f"Retrieved {len(memories)} memories")
    return {"memories":memories}