from graph_db.save_graph import save_graph
from utils.logger import logger

def graph_writer(state):
    logger.info("💾 Graph Writer")
    save_graph(state)
    return {}