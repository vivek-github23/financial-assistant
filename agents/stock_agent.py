from data.stocks import get_stock_data

def stock_agent(state):

    print("📈 Stock Agent")

    stocks = {

        "INFY":
        get_stock_data("INFY.NS"),

        "TCS":
        get_stock_data("TCS.NS")
    }

    return {
        "stocks": stocks
    }