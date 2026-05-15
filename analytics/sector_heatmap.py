import pandas as pd

from core.constants import SECTOR_MAP

from analytics.relative_strength import (
    calculate_relative_strength
)


def build_sector_heatmap(stock_list):

    sector_data = {}

    for symbol in stock_list:

        result = calculate_relative_strength(
            symbol
        )

        if not result:
            continue

        sector = SECTOR_MAP.get(
            symbol,
            "Others"
        )

        rs = result["RS Strength"]

        if sector not in sector_data:
            sector_data[sector] = []

        sector_data[sector].append(rs)

    rows = []

    for sector, values in sector_data.items():

        avg_rs = sum(values) / len(values)

        rows.append({
            "Sector": sector,
            "Avg RS": round(avg_rs, 2),
            "Stocks": len(values)
        })

    df = pd.DataFrame(rows)

    df = df.sort_values(
        by="Avg RS",
        ascending=False
    )

    return df
