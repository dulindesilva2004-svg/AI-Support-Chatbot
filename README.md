# AI Support Chatbot

Group project – AI-Powered Chatbot Development for Customer Support Automation.

A prototype customer support chatbot that answers common questions (order tracking, returns, delivery, account help), and hands over to a live agent when it can't help.

## Project structure

```
src/chatbot/     chatbot source code
data/            intents and FAQ data used by the bot
tests/           automated tests (run by GitHub Actions)
docs/            project documents (schedule, communication plan, CM plan)
.github/         issue/PR templates and CI workflow
```

## Getting started

```bash
pip install -r requirements.txt
python -m src.chatbot.bot      # chat with the bot in the terminal
pytest                         # run the tests
```

## Team

| Member | Role |
|---|---|
| Member 1 | Scope & requirements |
| Member 2 | Scheduling, communication, Jira & configuration management |
| Member 3 | |
| Member 4 | |

## Configuration management

See [docs/CONFIGURATION_MANAGEMENT.md](docs/CONFIGURATION_MANAGEMENT.md) for our branching strategy, commit rules and release process.
