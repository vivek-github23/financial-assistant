import json
from agents.llm import llm
from utils.logger import logger

def supervisor(state):
    logger.info("\n👨‍💼 Supervisor Agent")
    prompt = f"""
        You are an AI supervisor.

        Question:
        {state['question']}

        Available Agents:
        - memory
        - news
        - stocks
        - macro

        Decide which agents should run. Only choose the agents that are necessary to answer the question. If the question is not specific to business, stocks, companiesor macroeconomic factors, you can return an empty list of agents.

        Return JSON only.
        Example:
        {{
            "agents": [
                "memory",
                "news",
                "stocks"
            ]
        }}
    """
    response = llm.invoke(prompt)
    content = response.content
    logger.info(f"Supervisor Response: {content}")
    content = content.replace("```json","").replace("```","")

    try:
        result = json.loads(content)
        return {
            "required_agents":
            result["agents"]
        }
    
    except:
        logger.error("Failed to parse supervisor response")
        return {
            "required_agents": []
        }