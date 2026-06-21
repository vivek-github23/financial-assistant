from graph_db.neo4j_client import driver

def query_graph(query, params=None):
    with driver.session() as session:
        result = session.run(query, params or {})

        return [record.data() for record in result]