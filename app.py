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
from analytics.indicators import compute_indicators
st.set_page_config(
    page_title="Nile V2",
    page_icon="📈",
    layout="wide"
)
from ui.charts import (
    make_candlestick_chart,
    make_rsi_chart
)
from analytics.scoring import (
    compute_score,
    get_signal,
    conviction_level
)
from analytics.scanner import run_scanner

load_css()

st.title("NILE V2")

# Sidebar
symbol = st.sidebar.selectbox(
    "Select Stock",
    UNIVERSE
)
run_scan = st.sidebar.button(
    "Run Institutional Scan"
)

# Fetch Data
raw_df = get_history(symbol)

df = compute_indicators(raw_df)
score = compute_score(df)

signal = get_signal(score)

conviction = conviction_level(score)

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
st.subheader("Technical Indicators")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "RSI 14",
        round(df["RSI14"].iloc[-1], 2)
    )

with c2:
    st.metric(
        "SMA20",
        round(df["SMA20"].iloc[-1], 2)
    )

with c3:
    st.metric(
        "SMA50",
        round(df["SMA50"].iloc[-1], 2)
    )

with c4:
    st.metric(
        "ATR14",
        round(df["ATR14"].iloc[-1], 2)
    )
st.subheader("Charts")

left, right = st.columns([2, 1])

with left:

    st.plotly_chart(
        make_candlestick_chart(df, symbol),
        use_container_width=True
    )

with right:
    st.subheader("AI Institutional Engine")

a1, a2, a3 = st.columns(3)

with a1:
    st.metric(
        "Institutional Score",
        f"{score}/100"
    )

with a2:
    st.metric(
        "AI Signal",
        signal
    )

with a3:
    st.metric(
        "Conviction",
        conviction
    )

    st.plotly_chart(
        make_rsi_chart(df),
        use_container_width=True
    )
if run_scan:

    st.subheader("Institutional Scanner")

    with st.spinner("Scanning market..."):

        scan_df = run_scanner(UNIVERSE)

    st.dataframe(
        scan_df,
        use_container_width=True
    )
