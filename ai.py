def detect_emotion(text):
    text = text.lower()

    if "stress" in text or "pressure" in text:
        return "stress"
    if "sad" in text or "lonely" in text:
        return "sad"
    if "anxious" in text or "fear" in text:
        return "anxiety"
    if "happy" in text:
        return "happy"

    return "neutral"


def generate_response(emotion):
    responses = {
        "stress": "Let’s slow down. Take a deep breath with me.",
        "sad": "I’m here with you. You’re not alone.",
        "anxiety": "Try grounding: name 3 things you can see.",
        "happy": "That’s great to hear! Keep going 😊",
        "neutral": "Tell me more about how you feel."
    }
    return responses.get(emotion, "I’m listening.")
