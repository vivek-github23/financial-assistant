from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

def run_query(query, params=None):

    with driver.session() as session:
        return list(
            session.run(
                query,
                params or {}
            )
        )