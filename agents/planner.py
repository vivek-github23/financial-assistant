import json
import re
from agents.llm import llm


def planner(state):

    print("\n🧠 Planner Agent")

    prompt = f"""
        You are a financial planning agent.

        User Question:
        {state["question"]}

        Determine:

        1. Analysis Plan
        2. News Search Query
        3. Required Agents

        The News Search Query must be contanining relevant keywords to fetch useful news articles for the analysis without any special characters.

        Available Agents:

        - news
        - stocks
        
        HARD RULES
        - Return ONLY JSON as shown below.
        - The JSON must have keys: plan, news_query, required_agents
        - Do NOT include any explanations or text outside the JSON.
        - Do NOT include any markdown code blocks, only raw JSON.

        OUTPUT JSON FORMAT
        {{
            "plan": "Analyze Indian IT sector",
            "news_query": "Infosys TCS Wipro",
            "required_agents": ["news","stocks"]
        }}
    """

    response = llm.invoke(prompt)

    content = response.content
    print("LLM Response", content)
    match = re.search(r'\{.*\}', content, re.DOTALL)
    json_text="{}"
    if match:
        json_text = match.group(0)
    print("Result",json_text)
    try:

        result = json.loads(json_text)
        
        return {
            "plan": result["plan"],
            "news_query": result["news_query"],
            "required_agents": result["required_agents"]
        }

    except Exception:

        return {
            "plan": state["question"],
            "news_query": state["question"],
            "required_agents": [
                "news",
                "stocks"
            ]
        }