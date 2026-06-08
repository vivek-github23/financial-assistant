from memory.embeddings import create_embedding
from memory.qdrant_client import client, COLLECTION_NAME

def retrieve_memory(query, top_k=3):

    embedding = create_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=top_k
    )

    memories = []

    for point in results.points:

        memories.append({
            "question": point.payload.get("question"),
            "analysis": point.payload.get("analysis"),
            "score": point.score
        })

    return memories