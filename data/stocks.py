import yfinance as yf

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    hist = stock.history(period="1mo")

    return {
        "latest_close":
        float(hist["Close"].iloc[-1]),

        "monthly_return":
        float(
            (
                hist["Close"].iloc[-1]
                -
                hist["Close"].iloc[0]
            )
            /
            hist["Close"].iloc[0]
            *100
        )
    }
# print(get_stock_data("INFY.NS"))