from yahooquery import search

def find_ticker(company, country=None):

    query = company

    if country:
        query = f"{company} {country}"

    try:

        result = search(query)

        quotes = result.get("quotes", [])

        if not quotes:
            return None

        return quotes[0]["symbol"]

    except Exception:
        return None