Smart Text Analyzer

Turn raw text into useful insights.

Smart Text Analyzer is a lightweight Python web application that helps users explore text, identify word patterns, and extract useful information through a clean, interactive dashboard.

Features

- Text Analysis: Word count, unique words, and cleaned text.
- Word Frequency: Identify the three most frequently used words and visualise them in a chart.
- Information Extraction: Extract numbers and email addresses.
- Live Statistics: Track word and character counts as you type.
- Analysis History: Review and manage previous analyses within the active session.
- Settings: Access application information and basic display preferences.

Built With

- Python
- Streamlit
- Regular Expressions
- Collections ("Counter")

Getting Started

1. Clone the repository

git clone https://github.com/IMMNUEL327/smart-text-analyzer.git
cd smart-text-analyzer

2. Create and activate a virtual environment

python -m venv .venv
source .venv/Scripts/activate

For Windows PowerShell, use ".venv\Scripts\Activate.ps1" instead.

3. Install dependencies

python -m pip install -r requirements.txt

4. Run the application

python -m streamlit run app.py

Project Structure

smart-text-analyzer/
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
└── .gitignore

What's Next?

Planned improvements include sentence and paragraph statistics, reading-time estimation, keyword search, and downloadable analysis reports.

About

Built by Chukwuma Emmanuel Chiagozie.

"GitHub Profile" (https://github.com/IMMNUEL327)


Simple interface. Meaningful insights.