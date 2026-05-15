import streamlit as st
from pages.dashboard import (
    render_dashboard
)

from pages.scanner import (
    render_scanner
)

from pages.portfolio import (
    render_portfolio
)

from pages.heatmap import (
    render_heatmap
)

from pages.reports import (
    render_reports
)
import pandas as pd

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
from ui.cards import (
    metric_card,
    signal_card
)
from reports.pdf_engine import generate_stock_report
from analytics.portfolio import analyze_portfolio
from analytics.relative_strength import (
    build_rs_ranking 
)
from analytics.sector_heatmap import (
    build_sector_heatmap
)

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
st.sidebar.subheader("Portfolio")

portfolio_text = st.sidebar.text_area(
    "Portfolio Input",
    value="""
RELIANCE.NS,10,2450
TCS.NS,5,3800
HDFCBANK.NS,20,1650
""",
    height=150
)
st.sidebar.title("NILE V2")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Scanner",
        "Portfolio",
        "Heatmap",
        "Reports"
    ]
)
if page == "Dashboard":

    render_dashboard()

elif page == "Scanner":

    render_scanner()

elif page == "Portfolio":

    render_portfolio()

elif page == "Heatmap":

    render_heatmap()

elif page == "Reports":

    render_reports()
portfolio_rows = []

for line in portfolio_text.strip().splitlines():

    try:

        parts = line.split(",")

        portfolio_rows.append({
            "Symbol": parts[0].strip(),
            "Quantity": float(parts[1]),
            "Avg Price": float(parts[2])
        })

    except Exception:
        pass


portfolio_df = pd.DataFrame(portfolio_rows)
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

top1, top2, top3 = st.columns(3)

with top1:
    metric_card(
        "Live Price",
        f"₹{price:.2f}",
        f"{change:.2f}%"
    )

with top2:
    metric_card(
        "Sector",
        SECTOR_MAP.get(symbol, "Unknown")
    )

with top3:
    metric_card(
        "Market Cap",
        str(info.get("marketCap", "N/A"))
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

c1, c2, c3 = st.columns(3)

with c1:
    metric_card(
        "Institutional Score",
        f"{score}/100"
    )

with c2:
    signal_card(signal)

with c3:
    metric_card(
        "Conviction",
        conviction
    )

    st.plotly_chart(
        make_rsi_chart(df),
        use_container_width=True
    )

    if not portfolio_df.empty:
        st.subheader("Relative Strength Ranking")

with st.spinner("Calculating momentum rankings..."):

    rs_df = build_rs_ranking(
        UNIVERSE
    )

st.dataframe(
    rs_df.head(15),
    use_container_width=True
)
st.subheader("Sector Heatmap")

sector_df = build_sector_heatmap(
    UNIVERSE
)

st.dataframe(
    sector_df,
    use_container_width=True
)
# Portfolio Analytics

if not portfolio_df.empty:

    st.subheader("Portfolio Analytics")

    portfolio_result, summary = analyze_portfolio(
        portfolio_df
    )

    p1, p2, p3, p4 = st.columns(4)

    with p1:
        metric_card(
            "Total Invested",
            f"₹{summary['Total Invested']:,.0f}"
        )

    with p2:
        metric_card(
            "Portfolio Value",
            f"₹{summary['Portfolio Value']:,.0f}"
        )

    with p3:
        metric_card(
            "Total P&L",
            f"₹{summary['Total P&L']:,.0f}"
        )

    with p4:
        metric_card(
            "Return %",
            f"{summary['Total P&L %']}%"
        )

    st.dataframe(
        portfolio_result,
        use_container_width=True
    )
# PDF REPORT
signal = get_signal(score)

conviction = conviction_level(score)

pdf_data = generate_stock_report(
    symbol=symbol,
    price=price,
    signal=signal,
    score=score,
    conviction=conviction,
    rsi=df["RSI14"].iloc[-1]
)

st.download_button(
    label="Download Institutional PDF Report",
    data=pdf_data,
    file_name=f"{symbol}_report.pdf",
    mime="application/pdf"
)

