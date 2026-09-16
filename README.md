# Debugger Agent

One CrewAI agent. No tools. Paste code, get the bug.

## Run locally

    pip install -r requirements.txt
    export OPENAI_API_KEY=sk-...
    streamlit run app.py

## Deploy

1. Push to a PUBLIC GitHub repo (check your key is not in it)
2. share.streamlit.io -> sign in with GitHub -> Create app
3. Pick the repo, main branch, app.py
4. Advanced settings -> Secrets, paste:
       OPENAI_API_KEY = "sk-..."
5. Deploy (first build takes 3-5 min, crewai is a big install)

## Files

    agent.py    the agent (19 lines)
    app.py      the web page (19 lines)
