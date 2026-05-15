# NIFTY 50
NIFTY_50 = [
    "RELIANCE.NS","TCS.NS","HDFCBANK.NS","BHARTIARTL.NS",
    "ICICIBANK.NS","SBIN.NS","INFY.NS","HINDUNILVR.NS",
]

# NIFTY NEXT 50
NIFTY_NEXT_50 = [
    "ABB.NS","ADANIGREEN.NS","BANKBARODA.NS","DLF.NS",
]

# Combined Universe
UNIVERSE = sorted(list(dict.fromkeys(NIFTY_50 + NIFTY_NEXT_50)))

# Sector Map
SECTOR_MAP = {}

for s in ["TCS.NS","INFY.NS"]:
    SECTOR_MAP[s] = "IT"

for s in ["HDFCBANK.NS","ICICIBANK.NS","SBIN.NS"]:
    SECTOR_MAP[s] = "Financials"

for s in ["RELIANCE.NS"]:
    SECTOR_MAP[s] = "Energy"
