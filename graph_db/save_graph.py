from datetime import datetime
import json
from graph_db.neo4j_client import run_query


def neo4j_safe(value):
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value)
    return value


def save_graph(state):

    question = state.get("question", "")

    companies = state.get("companies", [])
    countries = state.get("countries", [])

    analysis = state.get("analysis", {})
    news = state.get("news", [])
    stocks = state.get("stocks", {})

    market_sentiment = state.get("market_sentiment", "Neutral")

    run_query(
        """
        MERGE (q:Question {text:$question})
        """,
        {"question": question}
    )

    run_query(
        """
        MERGE (a:Analysis {question:$question})
        SET a.summary=$summary,
            a.outlook=$outlook,
            a.confidence=$confidence,
            a.created_at=$created_at
        """,
        {
            "question": question,
            "summary": neo4j_safe(
                analysis.get("executive_summary", "")
            ),
            "outlook": neo4j_safe(
                analysis.get("final_outlook", "")
            ),
            "confidence": analysis.get(
                "confidence_score",
                0
            ),
            "created_at": datetime.utcnow().isoformat()
        }
    )

    run_query(
        """
        MATCH (q:Question {text:$question})
        MATCH (a:Analysis {question:$question})
        MERGE (q)-[:GENERATED]->(a)
        """,
        {"question": question}
    )

    for company in companies:

        run_query(
            """
            MERGE (c:Company {name:$name})
            """,
            {"name": company}
        )

        run_query(
            """
            MATCH (q:Question {text:$question})
            MATCH (c:Company {name:$company})
            MERGE (q)-[:ASKED_ABOUT]->(c)
            """,
            {
                "question": question,
                "company": company
            }
        )

        run_query(
            """
            MATCH (a:Analysis {question:$question})
            MATCH (c:Company {name:$company})
            MERGE (a)-[:ANALYZES]->(c)
            """,
            {
                "question": question,
                "company": company
            }
        )

    for country in countries:

        run_query(
            """
            MERGE (c:Country {name:$name})
            """,
            {"name": country}
        )

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

    for company, data in stocks.items():

        run_query(
            """
            MERGE (c:Company {name:$company})
            SET c.latest_close=$close,
                c.monthly_return=$monthly_return
            """,
            {
                "company": company,
                "close": data.get("latest_close"),
                "monthly_return": data.get("monthly_return")
            }
        )

    run_query(
        """
        MERGE (s:Sentiment {value:$value})
        """,
        {"value": market_sentiment}
    )

    for article in news[:10]:

        url = article.get("url")

        if not url:
            continue

        source_value = article.get("source", "")

        if isinstance(source_value, dict):
            source_value = source_value.get("name", "")

        run_query(
            """
            MERGE (n:News {url:$url})
            SET n.title=$title,
                n.description=$description,
                n.source=$source,
                n.published_at=$published_at
            """,
            {
                "url": url,
                "title": neo4j_safe(article.get("title")),
                "description": neo4j_safe(article.get("description")),
                "source": neo4j_safe(source_value),
                "published_at": neo4j_safe(article.get("publishedAt"))
            }
        )

        run_query(
            """
            MATCH (n:News {url:$url})
            MATCH (s:Sentiment {value:$sentiment})
            MERGE (n)-[:HAS_SENTIMENT]->(s)
            """,
            {
                "url": url,
                "sentiment": market_sentiment
            }
        )

        run_query(
            """
            MATCH (a:Analysis {question:$question})
            MATCH (n:News {url:$url})
            MERGE (a)-[:BASED_ON]->(n)
            """,
            {
                "question": question,
                "url": url
            }
        )

        for company in companies:
            run_query(
                """
                MATCH (c:Company {name:$company})
                MATCH (n:News {url:$url})
                MERGE (c)-[:MENTIONED_IN]->(n)
                """,
                {
                    "company": company,
                    "url": url
                }
            )

    for finding in analysis.get("key_findings", []):
        if isinstance(finding, dict):
            text = str(finding.get("finding") or finding.get("text") or "")
            source = finding.get("source", "")
            if isinstance(source, dict):
                source = source.get("source") or json.dumps(source)
            elif isinstance(source, list):
                source = json.dumps(source)
            else:
                source = str(source)

        else:
            text = str(finding)
            source = ""

        if not text:
            continue

        run_query(
            """
            MERGE (f:Finding {
                text:$text,
                source:$source
            })
            """,
            {
                "text": neo4j_safe(text),
                "source": neo4j_safe(source)
            }
        )

        run_query(
            """
            MATCH (a:Analysis {question:$question})
            MATCH (f:Finding {
                text:$text,
                source:$source
            })
            MERGE (a)-[:HAS_FINDING]->(f)
            """,
            {
                "question": question,
                "text": neo4j_safe(text),
                "source": neo4j_safe(source)
            }
        )