import os
import openai
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

def generate_embeddings(input_json="data/fashion_mock_data.json", output_pkl="outputs/embeddings.pkl"):
    df = pd.read_json(input_json)
    df["embedding"] = df["desc"].apply(get_embedding)
    df.to_pickle(output_pkl)
    print("✅ Embeddings generated and saved:", output_pkl)

if __name__ == "__main__":
    generate_embeddings()
