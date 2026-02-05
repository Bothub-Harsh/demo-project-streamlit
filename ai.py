def detect_emotion(text):
    text = text.lower()

    if "stress" in text:
        return "stress"
    if "sad" in text or "lonely" in text:
        return "sad"
    if "anxious" in text:
        return "anxiety"
    if "happy" in text:
        return "happy"

    return "neutral"


def generate_response(emotion):
    responses = {
        "stress": "Take a deep breath. I'm here with you.",
        "sad": "I'm really sorry you're feeling this way.",
        "anxiety": "Try grounding yourself by naming 3 things you see.",
        "happy": "That's great to hear! 😊",
        "neutral": "Tell me more about how you're feeling."
    }
    return responses.get(emotion, "I'm listening.")
