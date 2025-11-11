from src.vibe_matcher import vibe_matcher

if __name__ == "__main__":
    print("✨ Welcome to Vibe Matcher ✨")
    user_vibe = input("Enter your vibe (e.g., 'urban edgy cool'): ")
    result = vibe_matcher(user_vibe)
    print("\nTop Matches:\n", result)
