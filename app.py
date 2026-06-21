import streamlit as st
import pandas as pd
from graph.workflow import workflow
import plotly.graph_objects as go
import plotly.express as px
import warnings
import time

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Financial AI Agent",layout="wide")
st.title("📈 Autonomous Financial Intelligence Agent")

question = st.text_input("Ask a financial question",placeholder="Example: Analyze Samsung stock performance")

if st.button("Run Analysis"):
    final_state = {}
    agent_traces = []

    execution_log = st.empty()
    start_time = time.time()

    with st.spinner("Running Financial Agents..."):
        for event in workflow.stream({"question": question}):
            for node, output in event.items():
                agent_traces.append({"agent": node,"output": output})

                execution_log.code("\n".join([f"{trace['agent']}:{trace['output']}" for trace in agent_traces]))
                if isinstance(output, dict):
                    final_state.update(output)

    runtime = round(time.time() - start_time, 2)

    st.session_state["result"] = final_state
    st.session_state["traces"] = agent_traces
    st.session_state["runtime"] = runtime

if "result" in st.session_state:
    result = st.session_state["result"]
    analysis = result.get("analysis", {})

    st.divider()
    st.header("📊 Financial Intelligence Dashboard")

    # =====================================================
    # TOP METRICS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Confidence Score",analysis.get("confidence_score", "N/A") if isinstance(analysis, dict) else "N/A")

    with col2:
        st.metric("Evidence Used",len(result.get("evidence", [])))

    with col3:
        st.metric("Companies",len(result.get("companies", [])))

    with col4:
        st.metric("Runtime (sec)",st.session_state.get("runtime", 0))

    st.divider()

    # =====================================================
    # SENTIMENT GAUGE
    # =====================================================

    sentiment = result.get("market_sentiment", "Neutral")

    st.subheader("📈 Market Sentiment")

    sentiment_score = {
        "Bullish": 80,
        "Positive": 70,
        "Neutral": 50,
        "Negative": 30,
        "Bearish": 20
    }.get(sentiment, 50)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=sentiment_score,
            title={"text": sentiment},
            gauge={"axis": {"range": [0, 100]}}))

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    if isinstance(analysis, dict):
        st.subheader("Executive Summary")
        st.info(analysis.get("executive_summary",""))

        # ============================================
        # FINDINGS
        # ============================================

        with st.expander("🔍 Key Findings"):
            findings = analysis.get("key_findings", [])
            if findings:
                for idx, finding in enumerate(findings, 1):
                    if isinstance(finding, dict):
                        st.markdown(f"**{idx}. {finding.get('finding', '')}**")
                        source = finding.get("source")
                        if source:
                            st.link_button("View Source",source,key=f"finding_{idx}")
                        st.divider()
                    else:
                        st.markdown(f"**{idx}. {finding}**")
        # ============================================
        # RISKS
        # ============================================

        st.subheader("⚠️ Risks")

        risk_rows = []

        for item in analysis.get("risks",[]):
            if isinstance(item, dict):
                risk_rows.append({"Risk": item.get("risk",""),"Source": item.get("source","")})
            else:
                risk_rows.append({"Risk": item,"Source": ""})

        if risk_rows:
            st.dataframe(pd.DataFrame(risk_rows),use_container_width=True)

        # ============================================
        # OPPORTUNITIES
        # ============================================

        st.subheader("🚀 Opportunities")

        opp_rows = []

        for item in analysis.get("opportunities",[]):
            if isinstance(item, dict):
                opp_rows.append({"Opportunity": item.get("opportunity",""),"Source": item.get("source","")})
            else:
                opp_rows.append({"Opportunity": item,"Source": ""})

        if opp_rows:
            st.dataframe(pd.DataFrame(opp_rows),use_container_width=True)

        st.subheader("📌 Final Outlook")

        st.success(
            analysis.get("final_outlook",""))

    else:
        st.subheader("Analysis")
        st.write(analysis)

    st.divider()

    # =====================================================
    # STOCK OVERVIEW
    # =====================================================

    stocks = result.get("stocks",{})

    if stocks:
        st.subheader("📈 Stock Overview")

        cols = st.columns(len(stocks))

        for idx, (company,data) in enumerate(stocks.items()):
            with cols[idx]:
                st.metric(company,data.get("latest_close","N/A"),f"{data.get('monthly_return',0)}%")
                st.caption(f"Volatility: {round(data.get('volatility',0),2)}%")

        st.subheader("📊 Stock Price Trends")

        for company, data in stocks.items():
            history = data.get("price_history",[])

            if history:
                chart_df = pd.DataFrame(history)
                chart_df["date"] = pd.to_datetime(chart_df["date"])

                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=chart_df["date"],
                        y=chart_df["close"],
                        mode="lines",
                        name=company
                    )
                )

                fig.update_layout(
                    title=f"{company} Stock Price",
                    xaxis_title="Date",
                    yaxis_title="Close",
                    hovermode="x unified",
                    height=500
                )
                st.plotly_chart(fig,use_container_width=True)
    st.divider()

    # =====================================================
    # EVIDENCE DISTRIBUTION
    # =====================================================

    evidence = result.get("evidence",[])

    if evidence:
        counts = {}
        for item in evidence:
            typ = item.get("type","other")

            counts[typ] = (counts.get(typ,0) + 1)

        evidence_df = pd.DataFrame({"Type": counts.keys(),"Count": counts.values()})

        st.subheader("📂 Evidence Distribution")
        fig = px.pie(evidence_df,names="Type",values="Count")

        st.plotly_chart(fig,use_container_width=True)

    # =====================================================
    # KNOWLEDGE GRAPH
    # =====================================================

    st.subheader("🕸️ Knowledge Graph")

    companies = result.get("companies",[])

    countries = result.get("countries",[])

    if companies:
        st.write("**Companies:**",", ".join(companies))

    if countries:
        st.write("**Countries:**",", ".join(countries))

    # =====================================================
    # NEWS
    # =====================================================

    with st.expander("📰 News Articles"):
        news = result.get("news", [])
        if news:
            for article in news:
                st.subheader(article.get("title", "Untitled"))
                st.write(f"**Source:** {article.get('source', {}).get('name', 'Unknown')}")
                st.write(f"**Published:** {article.get('publishedAt', 'N/A')}")
                if article.get("description"):
                    st.write(article["description"])
                st.link_button("🔗 Read Article",article.get("url", "#"))
                st.divider()
        else:
            st.info("No news found")
    # =====================================================
    # TIMELINE
    # =====================================================

    with st.expander("🤖 Agent Timeline"):
        traces = st.session_state.get("traces",[])
        timeline_df = pd.DataFrame([{"Step": i + 1,"Agent": t["agent"]}for i, t in enumerate(traces)])
        st.dataframe(timeline_df,use_container_width=True)
        selected = st.selectbox("Inspect Agent",[t["agent"] for t in traces])

        for trace in traces:
            if (trace["agent"]== selected):
                st.json(trace["output"])
                break

    # =====================================================
    # DEBUG
    # =====================================================

    with st.expander("🔧 Raw Final State"):
        st.json(result)