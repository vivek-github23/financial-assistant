from agents.llm import llm

def planner(state):

    print("\n" + "="*50)
    print("🧠 Planner Agent Started")
    print("="*50)

    question = state["question"]

    print(f"Question: {question}")

    response = llm.invoke(
        f"Create a financial analysis plan for: {question}"
    )

    print("Plan Generated")

    return {
        "plan": response.content
    }