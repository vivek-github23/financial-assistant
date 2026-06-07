from agents.llm import llm

def analyst(state):

    print("📊 Analyst Agent")

    news_articles = state.get(
        "news",
        []
    )[:5]

    news_text = "\n".join([

        f"""
        Title:
        {article.get('title')}

        Description:
        {article.get('description')}
        """

        for article in news_articles
    ])

    prompt = f"""
    Question:
    {state['question']}

    Plan:
    {state['plan']}

    News:
    {news_text}

    Stocks:
    {state['stocks']}

    Generate a financial analysis.
    """

    response = llm.invoke(prompt)

    return {

        "analysis":
        response.content
    }