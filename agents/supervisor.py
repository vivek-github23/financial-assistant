import json
from agents.llm import llm


def supervisor(state):
    print("\n👨‍💼 Supervisor Agent")
    prompt = f"""
        You are an AI supervisor.

        Question:
        {state['question']}

        Available Agents:
        - memory
        - news
        - stocks
        - macro

        Decide which agents should run.
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
    content = content.replace("```json","").replace("```","")

    try:
        result = json.loads(content)
        return {
            "required_agents":
            result["agents"]
        }
    
    except:
        return {
            "required_agents": [
                "memory",
                "news",
                "stocks"
            ]
        }