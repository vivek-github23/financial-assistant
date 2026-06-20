from graph_db.neo4j_client import run_query
from utils.logger import logger

def graph_retriever(state):

    logger.info("🕸️ Graph Retriever")

    companies = state.get("companies", [])
    countries = state.get("countries", [])

    graph_context = []

    for company in companies:

        result = run_query(
            """
            MATCH (c:Company {name:$company})
            OPTIONAL MATCH (c)-[r]->(n)
            RETURN c.name as company,
                   type(r) as relation,
                   n.name as target
            """,
            {"company": company}
        )
        graph_context.extend(result)

    for country in countries:
        result = run_query(
            """
            MATCH (c:Country {name:$country})
            OPTIONAL MATCH (c)-[r]->(n)
            RETURN c.name as country,
                   type(r) as relation,
                   n.name as target
            """,
            {"country": country}
        )

        graph_context.extend(result)

    return {"graph_context": graph_context}