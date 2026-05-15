import streamlit as st


def metric_card(
    title,
    value,
    delta=None
):

    st.markdown(
        f"""
        <div style="
            background: rgba(15,23,42,0.7);
            padding:20px;
            border-radius:20px;
            border:1px solid rgba(255,255,255,0.08);
            margin-bottom:10px;
        ">

            <div style="
                color:#94a3b8;
                font-size:14px;
                font-weight:600;
            ">
                {title}
            </div>

            <div style="
                color:white;
                font-size:28px;
                font-weight:800;
                margin-top:10px;
            ">
                {value}
            </div>

            <div style="
                color:#22c55e;
                margin-top:6px;
                font-size:14px;
            ">
                {delta if delta else ""}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def signal_card(signal):

    colors = {
        "STRONG BUY": "#22c55e",
        "BUY": "#16a34a",
        "HOLD": "#f59e0b",
        "SELL": "#ef4444"
    }

    color = colors.get(signal, "#94a3b8")

    st.markdown(
        f"""
        <div style="
            background:{color}20;
            border:1px solid {color};
            padding:24px;
            border-radius:22px;
            text-align:center;
        ">

            <div style="
                color:{color};
                font-size:32px;
                font-weight:900;
            ">
                {signal}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
