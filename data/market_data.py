import pandas as pd
import yfinance as yf
import streamlit as st


@st.cache_data(ttl=900)
def get_history(symbol, period="1y", interval="1d"):
    try:
        df = yf.download(
            symbol,
            period=period,
            interval=interval,
            auto_adjust=True,
            progress=False,
            threads=False
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [c[0] for c in df.columns]

        return df.dropna()

    except Exception:
        return pd.DataFrame()


@st.cache_data(ttl=1800)
def get_info(symbol):
    try:
        return yf.Ticker(symbol).info
    except Exception:
        return {}


@st.cache_data(ttl=300)
def get_live_price(symbol):
    try:
        df = get_history(symbol, period="5d")

        if len(df) < 2:
            return None, None

        last = float(df["Close"].iloc[-1])
        prev = float(df["Close"].iloc[-2])

        change = ((last / prev) - 1) * 100

        return last, change

    except Exception:
        return None, None
