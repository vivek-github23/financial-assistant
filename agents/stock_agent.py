from data.stocks import get_stock_data
from tools.ticker_tool import find_ticker

def stock_agent(state):
    if "stocks" not in state.get("required_agents", []):
        print("⏭️ Skipping Stock Agent")
        return {}
    print("📈 Stock Agent")
    companies = state.get("companies", [])
    stocks = {}
    for company in companies:
        ticker = find_ticker(company)
        if not ticker:
            print(f"Ticker not found for {company}")
            continue
        print(f"{company} -> {ticker}")
        try:
            stocks[company] = get_stock_data(ticker)
        except Exception as e:
            print(e)

    return {"stocks": stocks}