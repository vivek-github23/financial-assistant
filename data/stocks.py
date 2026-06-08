import yfinance as yf

def get_stock_data(ticker):
    hist = yf.download(
        ticker,
        period="1mo",
        progress=False,
        auto_adjust=True
    )

    if hist.empty:
        return {"error": "No data returned"}

    close = hist["Close"][ticker].dropna()

    if len(close) < 2:
        return {"error": "Insufficient close price data"}

    latest_close = float(close.iloc[-1])
    first_close = float(close.iloc[0])

    return {
        "latest_close": latest_close,
        "monthly_return": round(
            ((latest_close - first_close) / first_close) * 100,
            2
        )
    }

# print(get_stock_data("INFY.NS"))