stocks = {
    "AAPL": (150.0, 140.0, 160.0),
    "GOOGL": {
        "high": 1100.0,
        "low": 1000.0,
    }
}

print(stocks["AAPL"]) # (150.0, 140.0, 160.0)
print(stocks["GOOGL"]) # {'high': 1100.0, 'low': 1000.0}
print(stocks["GOOGL"]["high"]) # 1100.0