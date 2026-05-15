import numpy as np
import pandas as pd


def compute_indicators(df):

    if df.empty:
        return df

    d = df.copy()

    # SMA
    d["SMA20"] = d["Close"].rolling(20).mean()

    d["SMA50"] = d["Close"].rolling(50).mean()

    # RSI
    delta = d["Close"].diff()

    gain = delta.clip(lower=0).rolling(14).mean()

    loss = (-delta.clip(upper=0)).rolling(14).mean()

    rs = gain / loss.replace(0, np.nan)

    d["RSI14"] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = d["Close"].ewm(span=12, adjust=False).mean()

    ema26 = d["Close"].ewm(span=26, adjust=False).mean()

    d["MACD"] = ema12 - ema26

    d["MACD_SIGNAL"] = d["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    # ATR
    tr1 = d["High"] - d["Low"]

    tr2 = (
        d["High"] - d["Close"].shift()
    ).abs()

    tr3 = (
        d["Low"] - d["Close"].shift()
    ).abs()

    tr = pd.concat(
        [tr1, tr2, tr3],
        axis=1
    ).max(axis=1)

    d["ATR14"] = tr.rolling(14).mean()

    return d.dropna()
