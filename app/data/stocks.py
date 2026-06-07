import yfinance as yf

def get_stock(ticker):

    stock=yf.Ticker(ticker)

    return stock.history(period="1mo")

if __name__ == "__main__":
    print(get_stock("AAPL"))