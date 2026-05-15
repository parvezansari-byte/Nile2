import pandas as pd


def compute_score(df):

    latest = df.iloc[-1]

    score = 0

    # Trend
    if latest["Close"] > latest["SMA20"]:
        score += 15

    if latest["Close"] > latest["SMA50"]:
        score += 20

    # SMA Trend Structure
    if latest["SMA20"] > latest["SMA50"]:
        score += 15

    # RSI
    if 50 <= latest["RSI14"] <= 70:
        score += 15

    # MACD
    if latest["MACD"] > latest["MACD_SIGNAL"]:
        score += 20

    # Volume Confirmation
    avg_volume = df["Volume"].tail(20).mean()

    latest_volume = latest["Volume"]

    if latest_volume > avg_volume:
        score += 15

    return min(score, 100)


def get_signal(score):

    if score >= 80:
        return "STRONG BUY"

    elif score >= 60:
        return "BUY"

    elif score >= 40:
        return "HOLD"

    else:
        return "SELL"


def conviction_level(score):

    if score >= 85:
        return "Very Strong"

    elif score >= 70:
        return "Strong"

    elif score >= 50:
        return "Moderate"

    else:
        return "Weak"


def signal_color(signal):

    colors = {
        "STRONG BUY": "green",
        "BUY": "green",
        "HOLD": "orange",
        "SELL": "red"
    }

    return colors.get(signal, "white")
