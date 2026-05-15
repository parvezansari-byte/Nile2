import streamlit as st
from ui.styles import load_css

st.set_page_config(
    page_title="Nile V2",
    page_icon="📈",
    layout="wide"
)

load_css()

st.title("NILE V2")
st.write("Institutional Terminal")
