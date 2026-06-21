from graph_db.query_graph import query_graph
from utils.logger import logger

def graph_retriever(state):
    logger.info("🔍 Graph Retriever")

    companies = state.get("companies", [])
    countries = state.get("countries", [])

    graph_context = []

    # Retrieve company-related information
    for company in companies:
        result = query_graph(
            """
            MATCH (c:Company {name:$company})
            OPTIONAL MATCH (c)-[:MENTIONED_IN]->(n:News)
            RETURN
                c.name as company,
                collect(
                    {
                        title:n.title,
                        source:n.source,
                        url:n.url
                    }
                ) as news
            """,
            {"company": company})
        graph_context.extend(result)

    # Retrieve country-related information
    for country in countries:
        result = query_graph(
            """
            MATCH (ct:Country {name:$country})
            OPTIONAL MATCH (company:Company)-[:OPERATES_IN]->(ct)
            RETURN
                ct.name AS country,
                collect(DISTINCT company.name) AS companies
            """,
            {"country": country}
        )
        graph_context.extend(result)

    logger.info(f"Retrieved {len(graph_context)} graph records")

    return {"graph_context": graph_context}