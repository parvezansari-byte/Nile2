import streamlit as st

from ui.styles import load_css
from core.constants import (
    NIFTY_50,
    NIFTY_NEXT_50,
    UNIVERSE,
    SECTOR_MAP
)

st.set_page_config(
    page_title="Nile V2",
    page_icon="📈",
    layout="wide"
)

load_css()

st.title("NILE V2")

st.write("Universe Size:", len(UNIVERSE))

symbol = st.selectbox(
    "Select Stock",
    UNIVERSE
)

st.write("Selected:", symbol)

st.write("Sector:", SECTOR_MAP.get(symbol, "Unknown"))
