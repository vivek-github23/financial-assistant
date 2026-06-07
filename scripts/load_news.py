articles=get_news()

for article in articles:

    text=article["title"]

    vector=get_embedding(text)

    insert_into_milvus(
        text,
        vector
    )