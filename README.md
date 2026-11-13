# Smart Text Analyzer

A simple Streamlit app for exploring text and viewing analysis results.

## Features

- Workspace with live word and character counts
- Total and unique word counts, cleaned text, and top three words
- Word-frequency chart, number extraction, and email extraction
- Session-based history with a comparison chart, colored flow diagram, and clear-history button
- Light and dark display preferences, plus application information

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Analysis history is kept in the current Streamlit session and is cleared when that session ends.
