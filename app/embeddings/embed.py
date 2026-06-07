from sentence_transformers import SentenceTransformer

model=SentenceTransformer(
    "BAAI/bge-large-en-v1.5"
)

def get_embedding(text):

    return model.encode(text)

if __name__ == "__main__":
    vector=get_embedding(
        "Technology stocks increased"
    )
    print(vector.shape)