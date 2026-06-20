import json
import re

from sympy import content
from agents.llm import llm
from utils.logger import logger

def planner(state):
    logger.info("\n🧠 Planner Agent")
    prompt = f"""
        You are a financial planning agent.

        User Question:
        {state["question"]}

        Determine:

        1. Analysis Plan
        2. News Search Query
        3. Required Agents
        4. Companies
        5. Countries

        The News Search Query must be contanining relevant keywords to fetch useful news articles for the analysis without any special characters. The News Search Query should not have values like "stock price" or anything related to stock price.  

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
            "required_agents": ["news","stocks"],
            "companies": ["TCS","INFY"],
            "countries": ["India"]
        }}
    """

    response = llm.invoke(prompt)

    content = response.content
    logger.info("LLM Response", content)
    match = re.search(r'\{.*?\}', content, re.DOTALL)
    json_text="{}"
    if match:
        json_text = match.group(0)
    logger.info("Result",json_text)  
    
    try:
        result = json.loads(json_text)
        return {
            "plan": result["plan"],
            "news_query": result["news_query"],
            "required_agents": result["required_agents"],
            "companies": result.get("companies", []),
            "countries": result.get("countries", [])
        }

    except Exception as e:
        logger.error(f"Error: {type(e).__name__}")
        logger.error(f"Details: {e}")
        logger.error(f"JSON Text: {json_text}")
        return {
            "plan": state["question"],
            "news_query": state["question"].replace("?",""),
            "required_agents": [
                "news",
                "stocks"
            ],
            "companies": ["TCS","INFY"],
            "countries": ["India"]
        }