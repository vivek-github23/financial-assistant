import json
import re

from agents.llm import llm

from utils.logger import logger

def analyst(state):
    logger.info("📊 Analyst Agent")
    evidence = state.get("evidence", {})
    prompt = f"""
        You are a senior equity research analyst.

        Question:
        {state["question"]}

        Evidence:
        {evidence}

        Use ONLY the supplied evidence.

        For every key finding,
        mention which evidence item supports it.

        Return JSON:

        {{
            "executive_summary":"The summary based on supplied evidence",
            "key_findings":[
                {{
                    "finding":"",
                    "source":""
                }}
            ],
            "risks":[],
            "opportunities":[],
            "final_outlook":"",
            "confidence_score":0
        }}
    """
    response = llm.invoke(prompt)
    content = response.content
    logger.info(content)
    try:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            content = match.group(0)
        analysis = json.loads(content)
        logger.info(analysis)
    except Exception as e:
        logger.info(f"caught exception: {e}")
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