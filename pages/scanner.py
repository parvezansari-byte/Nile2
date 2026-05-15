import streamlit as st

from core.constants import UNIVERSE

from analytics.scanner import (
    run_scanner
)


def render_scanner():

    st.title("Institutional Scanner")

    st.write(
        "AI-powered market scanning engine"
    )

    run_scan = st.button(
        "Run Institutional Scan"
    )

    if run_scan:

        with st.spinner(
            "Scanning market..."
        ):

            scan_df = run_scanner(
                UNIVERSE
            )

        st.subheader(
            "Top Ranked Stocks"
        )

        st.dataframe(
            scan_df,
            use_container_width=True
        )
