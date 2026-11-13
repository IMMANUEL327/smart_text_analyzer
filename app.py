# Streamlit builds the page and manages its widgets and session state.
import streamlit as st
# pandas turns saved results into a table that Streamlit can plot.
import pandas as pd

from analyzer import analyze_text


# Configure the browser tab and use the full page width.
st.set_page_config(
    page_title="Smart Text Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS for the background, spacing, headings, and buttons.
st.markdown(
    """
    <style>
        .stApp { background-color: #F5F8FF; }
        .main .block-container { padding-top: 2rem; padding-bottom: 3rem; }
        h1 { color: #153B75; font-weight: 700; }
        .stButton > button {
            background-color: #2563EB; color: white; border-radius: 8px;
            border: none; padding: 0.6rem 1.5rem; font-weight: 600;
        }
        .stButton > button:hover { background-color: #1D4ED8; color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit reruns this file after user actions. Session state keeps these
# values available between reruns while the current session is open.
if "current_page" not in st.session_state:
    st.session_state.current_page = "Workspace"
if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []
if "user_text" not in st.session_state:
    st.session_state.user_text = ""
if "appearance" not in st.session_state:
    st.session_state.appearance = "Light"


def clear_user_text():
    """Clear the text input before Streamlit recreates its widget."""
    st.session_state.user_text = ""

# Choose page colors from the display preference selected on the Settings page.
if st.session_state.appearance == "Dark":
    page_background, page_text, heading_text = "#111827", "#F3F4F6", "#93C5FD"
else:
    page_background, page_text, heading_text = "#F5F8FF", "#1F2937", "#153B75"

# Apply the selected colors after the base CSS above.
st.markdown(
    f"""
    <style>
        .stApp {{ background-color: {page_background}; color: {page_text}; }}
        h1, h2, h3 {{ color: {heading_text}; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Navigation lives in the sidebar. Each button saves its page name so the
# matching page section below knows which content to display.
with st.sidebar:
    st.title("🏠 Smart Analyzer")
    st.caption("🧠 Text Intelligence Dashboard")
    st.divider()
    st.subheader("Navigation")
    for page, label in (
        ("Workspace", "🏠 Workspace"),
        ("Analysis History", "📊 Analysis History"),
        ("Settings", "⚙️ Settings"),
    ):
        if st.button(label, use_container_width=True, key=f"nav_{page}"):
            st.session_state.current_page = page

    st.divider()
    st.caption("Version 1.0.0 | Developed by 🍂 CHUKWUMA IMMANUNEL 🍂")
    st.caption("Brotherly code for a better world.")

st.title("📊 Smart Text Analyzer")
st.write("Transform ordinary text into meaningful insights.")
st.divider()

# Workspace: collect text, show live counts, and run the text analyzer.
if st.session_state.current_page == "Workspace":
    st.header("Text Analysis Workspace")
    st.write("Enter your text below to analyze its word frequencies, numbers, and email addresses.")
    user_text = st.text_area(
        "Enter your text here:",
        height=250,
        placeholder="Paste your text here...",
        key="user_text",
    )

    # split() separates the text at spaces, tabs, and line breaks.
    words = user_text.split()
    col1, col2 = st.columns(2)
    col1.metric("Total Words", len(words))
    col2.metric("Total Characters", len(user_text))

    col1, col2 = st.columns(2)
    with col1:
        analyze_button = st.button("Analyze Text", use_container_width=True)
    with col2:
        st.button(
            "Clear Text",
            use_container_width=True,
            on_click=clear_user_text,
        )

    # Only analyze after the user presses the Analyze Text button.
    if analyze_button:
        if user_text.strip():
            # analyze_text() comes from analyzer.py and returns the counts,
            # cleaned text, common words, numbers, and email addresses.
            result = analyze_text(user_text)
            # Save the newest result first so it appears at the top of history.
            st.session_state.analysis_history.insert(
                0, {"text": user_text, "result": result}
            )
            # Show the main counts and details returned by analyzer.py.
            st.header("Analysis Result")
            col1, col2 = st.columns(2)
            col1.metric("Total Words", result["total_words"])
            col2.metric("Unique Words", result["unique_words"])

            st.subheader("Cleaned Text")
            st.write(result["cleaned_text"])
            st.subheader("Most Frequent Words")
            if result["top_words"]:
                st.bar_chart(dict(result["top_words"]))
            else:
                st.info("No words found.")

            st.subheader("Numbers Found")
            st.write(result["numbers"] or "No numbers found.")
            st.subheader("Email Addresses Found")
            st.write(result["email_addresses"] or "No email addresses found.")
        else:
            st.warning("Please enter some text to analyze.")

elif st.session_state.current_page == "Analysis History":
    # History: show a chart and one expandable record per saved analysis.
    st.header("📊 Analysis History")
    history = st.session_state.analysis_history
    if history:
        # Build a table where each row is an analysis and the two columns
        # compare its total word count with its unique word count.
        chart_data = pd.DataFrame(
            {
                "Total words": [item["result"]["total_words"] for item in history],
                "Unique words": [item["result"]["unique_words"] for item in history],
            },
            index=[f"Analysis {index}" for index in range(1, len(history) + 1)],
        )
        st.subheader("Analysis Overview")
        st.bar_chart(chart_data)

    # This HTML and CSS draw the colored steps of the analysis process.
    # The arrows show the order in which the analyzer handles the text.
    st.subheader("Analysis Flow")
    st.markdown(
        """
        <style>
            .analysis-flow { display:flex; align-items:stretch; gap:10px; margin:10px 0 24px; }
            .analysis-step {
                flex:1; min-width:115px; padding:16px 12px; border-radius:12px;
                color:white; text-align:center; font-weight:650;
                box-shadow:0 3px 10px rgba(15,23,42,.12);
            }
            .analysis-step small { display:block; margin-top:6px; font-weight:400; opacity:.92; }
            .flow-arrow { align-self:center; color:#64748B; font-size:22px; font-weight:700; }
            @media (max-width:700px) {
                .analysis-flow { flex-wrap:wrap; }
                .flow-arrow { display:none; }
            }
        </style>
        <div class="analysis-flow">
            <div class="analysis-step" style="background:#2563EB">1. Input<small>Your text</small></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="analysis-step" style="background:#7C3AED">2. Clean<small>Remove punctuation</small></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="analysis-step" style="background:#0891B2">3. Count<small>Words and frequency</small></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="analysis-step" style="background:#D97706">4. Extract<small>Numbers and emails</small></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="analysis-step" style="background:#16A34A">5. Results<small>Charts and summary</small></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Explain why the chart is empty when there are no saved results yet.
    if not history:
        st.info("Your previous analyses will appear here once you perform an analysis.")
    else:
        # Clear all saved results from this session when requested.
        if st.button("Clear History", key="clear_history"):
            st.session_state.analysis_history = []
            st.rerun()
        # Use an expander for each record so the page stays easy to scan.
        for index, item in enumerate(history, start=1):
            result = item["result"]
            # Shorten long input text before using it in the expander title.
            preview = item["text"].replace("\n", " ")
            if len(preview) > 100:
                preview = preview[:97] + "..."
            with st.expander(f"Analysis {index}: {preview}"):
                col1, col2 = st.columns(2)
                col1.metric("Total Words", result["total_words"])
                col2.metric("Unique Words", result["unique_words"])
                st.write("Cleaned text:", result["cleaned_text"])
                st.write("Most frequent words:", result["top_words"] or "None")
                st.write("Numbers:", result["numbers"] or "None")
                st.write("Email addresses:", result["email_addresses"] or "None")

elif st.session_state.current_page == "Settings":
    # Settings show application details and a simple color-theme preference.
    st.header("⚙️ Settings")
    # Keep basic app details and the display choice together on this page.
    st.subheader("Display preferences")
    st.selectbox("Color theme", ["Light", "Dark"], key="appearance")
    st.caption("Choose a light or dark page background.")

    st.subheader("Application information")
    st.write("Name: Smart Text Analyzer")
    st.write("Version: 1.0.0")
    st.write("Purpose: Analyze text, count words, and find numbers and email addresses.")