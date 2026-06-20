import streamlit as st
from graph.workflow import workflow
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Financial AI Agent",layout="wide")

st.title("📈 Autonomous Financial Intelligence Agent")

question = st.text_input("Ask a financial question")

if st.button("Run Analysis"):
    final_state = {}
    log_placeholder = st.empty()
    agent_traces = []
    for event in workflow.stream({"question": question}):
        for node, output in event.items():
            trace = {"agent": node,"output": output}
            agent_traces.append(trace)
            log_placeholder.code("\n".join([f"✅ {t['agent']}:{t['output']}" for t in agent_traces]))
            if isinstance(output, dict):
                final_state.update(output)

    st.session_state["result"] = final_state