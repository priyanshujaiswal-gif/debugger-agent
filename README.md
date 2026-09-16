# Debugger Agent

One CrewAI agent. No tools. Paste code, get the bug.

## Run locally

    pip install -r requirements.txt

Put your key in `.env` (already created, gitignored — never committed):

    OPENAI_API_KEY=sk-...

Then:

    streamlit run app.py

## Deploy

1. Push to a GitHub repo (`.env` is gitignored, so your key never leaves your machine — double check with `git status` before committing)
2. share.streamlit.io -> sign in with GitHub -> Create app
3. Pick the repo, main branch, app.py
4. Advanced settings -> Secrets, paste:
       OPENAI_API_KEY = "sk-..."
5. Deploy (first build takes 3-5 min, crewai is a big install)

## Files

    agent.py    the agent (19 lines)
    app.py      the web page (19 lines)
