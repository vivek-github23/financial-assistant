def route_news(state):

    agents = state.get(
        "required_agents",
        []
    )

    if "news" in agents:
        return "news"

    return "analyst"


def route_stocks(state):

    agents = state.get(
        "required_agents",
        []
    )

    if "stocks" in agents:
        return "stocks"

    return "analyst"