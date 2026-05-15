import streamlit.components.v1 as components


def metric_card(title, value, delta=""):

    html = f"""
    <div style="
        background: rgba(15,23,42,0.75);
        padding:20px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,0.08);
        margin-bottom:10px;
        box-shadow:0 10px 25px rgba(0,0,0,0.25);
        font-family:sans-serif;
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
            font-size:30px;
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
            {delta}
        </div>

    </div>
    """

    components.html(
        html,
        height=170
    )


def signal_card(signal):

    colors = {
        "STRONG BUY": "#22c55e",
        "BUY": "#16a34a",
        "HOLD": "#f59e0b",
        "SELL": "#ef4444"
    }

    color = colors.get(signal, "#94a3b8")

    html = f"""
    <div style="
        background:{color}20;
        border:1px solid {color};
        padding:28px;
        border-radius:22px;
        text-align:center;
        font-family:sans-serif;
    ">

        <div style="
            color:{color};
            font-size:34px;
            font-weight:900;
        ">
            {signal}
        </div>

    </div>
    """

    components.html(
        html,
        height=140
    )
