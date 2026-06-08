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
        # Merge node output into final state
        if isinstance(output, dict):
            final_state.update(output)

print("\n✅ Workflow Completed")

# Save memory if analysis exists
if "analysis" in final_state:
    save_memory(
        question=question,
        analysis={
            "analysis": final_state.get("analysis"),
            "critique": final_state.get("critique")
        }
    )
else:
    print("⚠️ No analysis found to save")