from utils.logger import logger

def evidence_collector(state):
    logger.info("📂 Evidence Collector")

    evidence = []

    for article in state.get("news", [])[:5]:
        evidence.append({
            "type": "news",
            "source": article.get("source", {}).get("name"),
            "title": article.get("title"),
            "description": article.get("description"),
            "source":article.get("url")
        })

    for company, data in state.get("stocks", {}).items():
        evidence.append({
            "type": "stock",
            "company": company,
            "data": data
        })

    for metric, data in state.get("macro_data", {}).items():
        evidence.append({
            "type": "macro",
            "metric": metric,
            "data": data
        })

    metrics = {
        "news_articles": len(state.get("news", [])),
        "companies_found": len(state.get("companies", [])),
        "countries_found": len(state.get("countries", [])),
        "stocks_analyzed": len(state.get("stocks", {})),
        "memories_retrieved": len(state.get("memories", []))
    }

    return {
        "evidence": evidence,
        "metrics": metrics
    }