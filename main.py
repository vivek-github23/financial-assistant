from graph.workflow import workflow
from memory.save_memory import save_memory

question = "How safe is it to invest in TCS right now?"

final_state = {"question": question}

for event in workflow.stream({"question": question}):
    for node_name, output in event.items():
        print("\n" + "=" * 60)
        print(f"🤖 {node_name.upper()} AGENT")
        print("=" * 60)
        print(output)

        if isinstance(output, dict):
            final_state.update(output)

print("\nWorkflow Completed")

if final_state.get("analysis"):
    save_memory(
        question=question,
        analysis=final_state["analysis"]
    )
    print("Memory Saved")
else:
    print("No analysis found to save")

print("\nFinal State Keys:")
print(list(final_state.keys()))