from graph_db.save_graph import save_graph

def graph_memory_agent(state):
    print("Graph Memory Agent")
    save_graph(state)
    return {}