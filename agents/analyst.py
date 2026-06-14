import json
import re

from agents.llm import llm


def analyst(state):
    print("📊 Analyst Agent")
    evidence = state.get("evidence", {})
    prompt = f"""
    You are a senior financial analyst.
    Question:
    {state["question"]}
    Evidence:
    {evidence}
    Return ONLY valid JSON.
    {{
        "executive_summary": "",
        "key_findings": [
            ""
        ],
        "risks": [
            ""
        ],
        "opportunities": [
            ""
        ],
        "final_outlook": "",
        "confidence_score": 85
    }}
    """
    response = llm.invoke(prompt)
    content = response.content
    try:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            content = match.group(0)
        analysis = json.loads(content)
    except Exception:
        analysis = {
            "executive_summary": content,
            "key_findings": [],
            "risks": [],
            "opportunities": [],
            "final_outlook": "",
            "confidence_score": 50
        }

    return {
        "analysis": analysis
    }