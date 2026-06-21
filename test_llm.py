from agents.llm import llm

response = llm.invoke("hello")

print(response.content)