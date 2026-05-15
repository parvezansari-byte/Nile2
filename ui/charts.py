import plotly.graph_objects as go


def make_candlestick_chart(df, symbol):

    fig = go.Figure()

    # Candlestick
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price"
        )
    )

    # SMA 20
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA20"],
            name="SMA20"
        )
    )

    # SMA 50
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA50"],
            name="SMA50"
        )
    )

    fig.update_layout(
        title=f"{symbol} Price Chart",
        template="plotly_dark",
        height=600,
        xaxis_rangeslider_visible=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig


def make_rsi_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI14"],
            name="RSI 14"
        )
    )

    fig.add_hline(
        y=70,
        line_dash="dot"
    )

    fig.add_hline(
        y=30,
        line_dash="dot"
    )

    fig.update_layout(
        title="RSI Momentum",
        template="plotly_dark",
        height=300,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig
