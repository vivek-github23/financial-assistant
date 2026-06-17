from graph_db.neo4j_client import run_query

def save_graph(state):
    companies = state.get("companies", [])
    countries = state.get("countries", [])
    
    for company in companies:
        run_query("MERGE (c:Company {name:$name})",{"name": company})

    for country in countries:
        run_query("MERGE (c:Country {name:$name})",{"name": country})
        
    for company in companies:
        for country in countries:
            run_query(
                """
                MERGE (co:Company {name:$company})
                MERGE (ct:Country {name:$country})

                MERGE (co)-[:OPERATES_IN]->(ct)
                """,
                {
                    "company": company,
                    "country": country
                }
            )