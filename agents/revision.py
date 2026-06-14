from agents.llm import llm

def revision(state):
    print("\n✏️ Revision Agent")

    prompt = f"""
        Improve the following analysis based on the critique.

        Analysis:
        {state['analysis']}

        Critique:
        {state['critique']}
    """

    response = llm.invoke(prompt)

    return {
        "analysis": response.content,
        "iterations": state.get("iterations", 0) + 1
    }