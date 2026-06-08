from agents.llm import llm

def analyst(state):
    print("📊 Analyst Agent")
    news_articles = state.get("news",[])[:5]
    memories = state.get("memories",[])
    news_text = "\n".join([
        f"""
        Title:
        {article.get('title')}
        Description:
        {article.get('description')}
        """
        for article in news_articles])

    prompt = f"""
        Past Memories:
        {memories}
        Question:
        {state["question"]}
        News:
        {news_text}
        Stocks:
        {state["stocks"]}
        Generate a financial analysis.
    """

    response = llm.invoke(prompt)

    return {"analysis":response.content}