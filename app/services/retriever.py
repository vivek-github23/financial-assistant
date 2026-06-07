def search(query):

    query_vector=get_embedding(
        query
    )

    results=milvus.search(
        query_vector
    )

    return results