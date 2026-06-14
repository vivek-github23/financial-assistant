from data.macro import get_macro_data

COUNTRY_CODES = {
    "india": "IND",
    "united states": "USA",
    "usa": "USA",
    "china": "CHN",
    "japan": "JPN",
    "germany": "DEU",
    "france": "FRA",
    "united kingdom": "GBR",
    "uk": "GBR",
    "canada": "CAN",
    "australia": "AUS",
    "singapore": "SGP"
}

def macro_agent(state):
    if "macro" not in state.get("required_agents", []):
        print("⏭️ Skipping Macro Agent")
        return {}
    print("🌍 Macro Agent")
    countries = state.get("countries", [])
    macro_results = {}
    for country in countries:
        country_code = COUNTRY_CODES.get(country.lower())
        if not country_code:
            continue
        macro_results[country] = get_macro_data(country_code)
    return {"macro_data": macro_results}