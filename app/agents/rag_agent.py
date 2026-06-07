from services.retriever import search
from models.llm import generate

def answer(query):

    docs=search(query)

    context="\n".join(
        [d.text for d in docs]
    )

    response=generate(
        context,
        query
    )

    return response