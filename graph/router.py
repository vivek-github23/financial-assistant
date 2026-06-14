from langgraph.graph import END

def reflection_router(state):
    score = state.get("score", 0)
    iterations = state.get("iterations", 0)
    print(f"\nRouter -> score={score}, iterations={iterations}")
    if score >= 0.8 or iterations >= 1:
        return END
    return "revision"
