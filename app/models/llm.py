from langchain_community.llms import Ollama

llm=Ollama(
    model="qwen3:8b"
)

def generate(context,question):

    prompt=f"""
    Context:
    {context}

    Question:
    {question}

    """

    return llm.invoke(
        prompt
    )