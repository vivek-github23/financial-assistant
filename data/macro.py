import requests

def get_macro_data(country_code="IND"):

    indicators = {
        "gdp": "NY.GDP.MKTP.CD",
        "inflation": "FP.CPI.TOTL.ZG",
        "unemployment": "SL.UEM.TOTL.ZS"
    }

    results = {}

    for name, indicator in indicators.items():

        url = (
            f"https://api.worldbank.org/v2/country/{country_code}/"
            f"indicator/{indicator}?format=json"
        )

        try:
            response = requests.get(url, timeout=10)

            data = response.json()

            latest = next(
                item
                for item in data[1]
                if item["value"] is not None
            )

            results[name] = {
                "year": latest["date"],
                "value": latest["value"]
            }

        except Exception:
            results[name] = None

    return results