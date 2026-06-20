from langchain_ollama import ChatOllama

llm = ChatOllama(
    # model="qwen3:8b",
    model="llama3.2:3b",
    temperature=0
)
