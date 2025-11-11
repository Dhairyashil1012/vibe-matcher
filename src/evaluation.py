import time
import pandas as pd
from src.vibe_matcher import vibe_matcher
import matplotlib.pyplot as plt

def evaluate_vibes():
    queries = ["energetic urban chic", "relaxed cozy comfort", "vintage retro cool"]
    times = []
    results = []

    for q in queries:
        start = time.time()
        res = vibe_matcher(q)
        end = time.time()
        times.append(end - start)
        results.append((q, res))
        print(f"\n🔍 Query: {q}")
        print(res)

    plt.bar(range(len(times)), times)
    plt.xticks(range(len(times)), [q for q, _ in results], rotation=45)
    plt.ylabel("Seconds")
    plt.title("Vibe Matcher Query Latency")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    evaluate_vibes()
