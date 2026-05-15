import pandas as pd

from data.market_data import (
    get_live_price
)


def analyze_portfolio(portfolio_df):

    results = []

    total_value = 0

    total_cost = 0

    for _, row in portfolio_df.iterrows():

        symbol = row["Symbol"]

        qty = row["Quantity"]

        avg_price = row["Avg Price"]

        live_price, _ = get_live_price(symbol)

        if live_price is None:
            continue

        invested = qty * avg_price

        current_value = qty * live_price

        pnl = current_value - invested

        pnl_pct = (pnl / invested) * 100

        total_value += current_value

        total_cost += invested

        results.append({
            "Symbol": symbol,
            "Qty": qty,
            "Avg Price": avg_price,
            "Live Price": round(live_price, 2),
            "Invested": round(invested, 2),
            "Current Value": round(current_value, 2),
            "P&L": round(pnl, 2),
            "P&L %": round(pnl_pct, 2)
        })

    portfolio_result = pd.DataFrame(results)

    total_pnl = total_value - total_cost

    total_pnl_pct = (
        (total_pnl / total_cost) * 100
        if total_cost > 0 else 0
    )

    summary = {
        "Total Invested": round(total_cost, 2),
        "Portfolio Value": round(total_value, 2),
        "Total P&L": round(total_pnl, 2),
        "Total P&L %": round(total_pnl_pct, 2)
    }

    return portfolio_result, summary
