import streamlit as st
import pandas as pd

from analytics.portfolio import (
    analyze_portfolio
)

from ui.cards import (
    metric_card
)


def render_portfolio():

    st.title("Portfolio Analytics")

    st.write(
        "Institutional portfolio dashboard"
    )

    # Portfolio Input
    portfolio_text = st.text_area(
        "Portfolio Input",
        value="""
RELIANCE.NS,10,2450
TCS.NS,5,3800
HDFCBANK.NS,20,1650
""",
        height=150
    )

    # Parse Portfolio
    portfolio_rows = []

    for line in portfolio_text.strip().splitlines():

        try:

            parts = line.split(",")

            portfolio_rows.append({
                "Symbol": parts[0].strip(),
                "Quantity": float(parts[1]),
                "Avg Price": float(parts[2])
            })

        except:
            pass

    portfolio_df = pd.DataFrame(
        portfolio_rows
    )

    # Portfolio Analytics
    if not portfolio_df.empty:

        portfolio_result, summary = (
            analyze_portfolio(
                portfolio_df
            )
        )

        st.subheader(
            "Portfolio Summary"
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

        st.subheader(
            "Holdings"
        )

        st.dataframe(
            portfolio_result,
            use_container_width=True
        )
