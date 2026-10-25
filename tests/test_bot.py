from src.chatbot.bot import load_intents, match_intent, get_response

data = load_intents()


def test_greeting():
    assert match_intent("Hello there", data) == "greeting"


def test_order_tracking():
    assert match_intent("Where is my order?", data) == "order_tracking"


def test_returns():
    assert match_intent("I want a refund", data) == "returns"


def test_handover_to_agent():
    assert match_intent("Can I speak to a real person", data) == "human_agent"


def test_fallback():
    assert get_response("blah blah", data) == data["fallback"]
