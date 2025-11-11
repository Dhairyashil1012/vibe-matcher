import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from src.embedding_utils import get_embedding

def vibe_matcher(query, embeddings_path="outputs/embeddings.pkl"):
    df = pd.read_pickle(embeddings_path)
    q_emb = get_embedding(query)
    product_embs = np.vstack(df["embedding"].values)
    sims = cosine_similarity([q_emb], product_embs)[0]

    df["similarity"] = sims
    top = df.sort_values("similarity", ascending=False).head(3)

    if top["similarity"].max() < 0.5:
        return "⚠️ No strong vibe match found. Try another vibe!"
    return top[["name", "desc", "similarity"]]
