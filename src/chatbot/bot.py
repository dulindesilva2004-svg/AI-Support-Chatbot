"""Simple keyword-based support chatbot (prototype).

The NLP model will replace match_intent() in a later sprint.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "intents.json"


def load_intents(path=DATA_FILE):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def match_intent(message, data):
    text = message.lower()
    for intent in data["intents"]:
        if any(k in text for k in intent["keywords"]):
            return intent["tag"]
    return None


def get_response(message, data=None):
    data = data or load_intents()
    tag = match_intent(message, data)
    if tag is None:
        return data["fallback"]
    return next(i["response"] for i in data["intents"] if i["tag"] == tag)


def main():
    data = load_intents()
    print("Support Bot: Hi! Type 'quit' to exit.")
    while True:
        msg = input("You: ")
        if msg.strip().lower() in ("quit", "exit"):
            break
        print("Support Bot:", get_response(msg, data))


if __name__ == "__main__":
    main()
