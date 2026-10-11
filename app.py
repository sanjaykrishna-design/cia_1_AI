"""Agent Arena AI Quiz - Streamlit app.
Run locally:  pip install streamlit   then   streamlit run app.py
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Agent Arena AI Quiz", layout="wide")

# remove Streamlit's default padding so the game fills the page
st.markdown(
    "<style>.block-container{padding:1rem 0.5rem 0} header, footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)

# the game itself (HTML, CSS and JavaScript) lives in quiz.html
game = Path(__file__).with_name("quiz.html").read_text(encoding="utf-8")
components.html(game, height=950, scrolling=True)
