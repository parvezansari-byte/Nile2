import streamlit as st

from ui.styles import load_css

from core.constants import (
    UNIVERSE,
    SECTOR_MAP
)

from data.market_data import (
    get_history,
    get_info,
    get_live_price
)

st.set_page_config(
    page_title="Nile V2",
    page_icon="📈",
    layout="wide"
)

load_css()

st.title("NILE V2")

# Sidebar
symbol = st.sidebar.selectbox(
    "Select Stock",
    UNIVERSE
)

# Fetch Data
df = get_history(symbol)

info = get_info(symbol)

price, change = get_live_price(symbol)

# Display
st.subheader(symbol)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Live Price",
        f"₹{price:.2f}" if price else "N/A",
        f"{change:.2f}%"
    )

with col2:
    st.metric(
        "Sector",
        SECTOR_MAP.get(symbol, "Unknown")
    )

with col3:
    st.metric(
        "Market Cap",
        info.get("marketCap", "N/A")
    )

st.dataframe(df.tail())
