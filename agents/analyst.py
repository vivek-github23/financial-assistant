from agents.llm import llm

def analyst(state):
    print("📊 Analyst Agent")
    news_articles = state.get("news",[])[:5]
    memory_context = ""
    for memory in state.get("memories",[]):
        memory_context += f"""
            Question:
            {memory['question']}
            Analysis:
            {memory['analysis']}
        """
    news_text = "\n".join([
        f"""
        Title:
        {article.get('title')}
        Description:
        {article.get('description')}
        """
        for article in news_articles])

    prompt = f"""
        Past Similar Analyses:
        {memory_context}
        Current Question:
        {state["question"]}
        News:
        {news_text}
        Stocks:
        {state["stocks"]}
        Generate analysis.
    """

    response = llm.invoke(prompt)

    return {"analysis":response.content}