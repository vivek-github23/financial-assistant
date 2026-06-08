import uuid
from qdrant_client.models import PointStruct
from memory.embeddings import create_embedding
from memory.qdrant_client import (client,COLLECTION_NAME)

def save_memory(question,analysis):
    embedding = create_embedding(question)

    client.upsert(
        collection_name=
        COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"question":question,"analysis":analysis}
            )
        ]
    )
    print("💾 Memory Saved")