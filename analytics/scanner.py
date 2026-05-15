import pandas as pd

from data.market_data import get_history

from analytics.indicators import compute_indicators

from analytics.scoring import (
    compute_score,
    get_signal
)


def scan_stock(symbol):

    try:
        raw_df = get_history(symbol)

        if raw_df.empty:
            return None

        df = compute_indicators(raw_df)

        if len(df) < 50:
            return None

        latest = df.iloc[-1]

        score = compute_score(df)

        signal = get_signal(score)

        return {
            "Symbol": symbol,
            "Close": round(latest["Close"], 2),
            "RSI": round(latest["RSI14"], 2),
            "SMA20": round(latest["SMA20"], 2),
            "SMA50": round(latest["SMA50"], 2),
            "Score": score,
            "Signal": signal
        }

    except Exception:
        return None


def run_scanner(stock_list):

    results = []

    for symbol in stock_list:

        result = scan_stock(symbol)

        if result:
            results.append(result)

    if not results:
        return pd.DataFrame()

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="Score",
        ascending=False
    )

    return df
