import pandas as pd

from data.market_data import get_history

from analytics.indicators import compute_indicators


def calculate_relative_strength(symbol):

    try:

        raw_df = get_history(
            symbol,
            period="6mo"
        )

        if raw_df.empty:
            return None

        df = compute_indicators(raw_df)

        if len(df) < 50:
            return None

        latest = df.iloc[-1]

        close = latest["Close"]

        sma50 = latest["SMA50"]

        rsi = latest["RSI14"]

        momentum = (
            (close / sma50) - 1
        ) * 100

        return {
            "Symbol": symbol,
            "RS Strength": round(momentum, 2),
            "RSI": round(rsi, 2),
            "Close": round(close, 2)
        }

    except:
        return None


def build_rs_ranking(stock_list):

    results = []

    for symbol in stock_list:

        result = calculate_relative_strength(
            symbol
        )

        if result:
            results.append(result)

    if not results:
        return pd.DataFrame()

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="RS Strength",
        ascending=False
    )

    return df
