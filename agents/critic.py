from agents.llm import llm

def critic(state):

    print("🔍 Critic Agent")

    response = llm.invoke(

        f"""
        Review this analysis.

        Analysis:
        {state['analysis']}

        Check:
        - Unsupported claims
        - Missing evidence
        - Weak reasoning

        Provide critique.
        """
    )

    return {

        "critique":
        response.content
    }