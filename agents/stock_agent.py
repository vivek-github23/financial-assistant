from data.stocks import get_stock_data
from tools.ticker_tool import find_ticker
from utils.logger import logger

def stock_agent(state):
    if "stocks" not in state.get("required_agents", []):
        logger.info("⏭️ Skipping Stock Agent")
        return {}
    logger.info("📈 Stock Agent")
    companies = state.get("companies", [])
    stocks = {}
    for company in companies:
        ticker = find_ticker(company)
        if not ticker:
            logger.info(f"Ticker not found for {company}")
            continue
        logger.info(f"{company} -> {ticker}")
        try:
            stocks[company] = get_stock_data(ticker)
        except Exception as e:
            logger.error(f"Error occurred while fetching stock data for {company}: {e}")

    return {"stocks": stocks}