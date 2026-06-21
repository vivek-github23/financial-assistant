import yfinance as yf
import pandas as pd

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    hist = stock.history(period="3mo")

    if hist.empty:
        return {}

    hist["MA20"] = hist["Close"].rolling(20).mean()
    hist["Returns"] = hist["Close"].pct_change()

    latest_close = round(hist["Close"].iloc[-1],2)

    monthly_return = round(
        (
            (hist["Close"].iloc[-1] -
             hist["Close"].iloc[-22])
             /
             hist["Close"].iloc[-22]
        ) * 100,
        2
    )

    volatility = round(
        hist["Returns"].std() * (252**0.5),
        4
    )

    return {
        "latest_close": latest_close,
        "monthly_return": monthly_return,
        "high_90d": round(hist["Close"].max(),2),
        "low_90d": round(hist["Close"].min(),2),
        "ma20": round(hist["MA20"].iloc[-1],2),
        "volatility": volatility,
        "price_history": [
            {
                "date": str(idx.date()),
                "close": round(row["Close"],2)
            }
            for idx,row in hist.tail(90).iterrows()
        ]
    }