from setence_transformers import SenteceTransformer


def text_embeddings(chunked_texts):
    model = SenteceTransformer("./모델")
    embeddings= model.encode(chunked_texts)

    return embeddings