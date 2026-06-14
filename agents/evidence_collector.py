def evidence_collector(state):
    print("📂 Evidence Collector")
    evidence = {
    "memories": state.get("memories", []),
    "news": state.get("news", []),
    "news_sentiment": state.get("news_sentiment", []),
    "stocks": state.get("stocks", {}),
    "macro": state.get("macro_data", {}),
    "market_sentiment": state.get("market_sentiment")
    }
    return {"evidence": evidence}