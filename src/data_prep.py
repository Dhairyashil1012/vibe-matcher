import pandas as pd
import json

def create_mock_data():
    data = [
        {"name": "Boho Dress", "desc": "Flowy, earthy tones for festival vibes", "vibes": ["boho", "free-spirited"]},
        {"name": "Street Hoodie", "desc": "Urban oversized hoodie with graffiti print", "vibes": ["urban", "edgy"]},
        {"name": "Chic Blazer", "desc": "Sleek black blazer for confident modern style", "vibes": ["chic", "professional"]},
        {"name": "Cozy Sweater", "desc": "Soft knit sweater for relaxed weekend comfort", "vibes": ["cozy", "casual"]},
        {"name": "Sporty Sneakers", "desc": "Bright sneakers built for movement and energy", "vibes": ["sporty", "energetic"]},
        {"name": "Vintage Jacket", "desc": "Retro denim jacket with classic 90s flair", "vibes": ["retro", "cool"]},
    ]
    df = pd.DataFrame(data)
    df.to_json("data/fashion_mock_data.json", orient="records", indent=2)
    print("✅ Mock data saved in data/fashion_mock_data.json")

if __name__ == "__main__":
    create_mock_data()
