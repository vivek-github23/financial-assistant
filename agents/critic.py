from agents.llm import llm
import json

def critic(state):
    print("\n🔍 Critic Agent")

    prompt = f"""
        Evaluate the financial analysis.

        Analysis:
        {state["analysis"]}

        Score from 0 to 1.

        Return JSON only.

        {{
            "critique": "",
            "score": 0.85
        }}
    """

    response = llm.invoke(prompt)
    content = response.content.replace("```json", "").replace("```", "").strip()

    try:
        result = json.loads(content)
        return {
            "critique": result["critique"],
            "score": float(result["score"])
        }
    except:
        return {
            "critique": response.content,
            "score": 0.7
        }