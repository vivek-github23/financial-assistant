from graph.workflow import workflow

question = "How safe is it to invest in TCS right now?"

for event in workflow.stream(
    {
        "question": question
    }
):

    for node_name, output in event.items():

        print("\n" + "="*60)

        print(
            f"🤖 {node_name.upper()} AGENT"
        )

        print("="*60)

        print(output)