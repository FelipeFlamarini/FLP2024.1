stocks = {
    "AAPL": (150.0, 140.0, 160.0),
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84),
    "FB": (177.46, 178.67, 175.79),
}

print(stocks.get("RIM")) # None
print(stocks.get("RIM", "NOT FOUND")) # NOT FOUND
print(stocks.setdefault("GOOG", "INVALID")) # (1235.20, 1242.54, 1231.06)
print(stocks.setdefault("BBRY", (10.87, 10.76, 10.90))) # (10.87, 10.76, 10.90)
print(stocks["BBRY"])   # (10.87, 10.76, 10.90)
print()

stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
print(stocks["GOOG"]) # (1245.21, 1252.64, 1245.18)
print()

print(stocks.items()) # dict_items([('AAPL', (150.0, 140.0, 160.0)), ('GOOG', (1245.21, 1252.64, 1245.18)), ('MSFT', (110.41, 110.45, 109.84)), ('FB', (177.46, 178.67, 175.79)), ('BBRY', (10.87, 10.76, 10.90))])
print(stocks.keys()) # dict_keys(['AAPL', 'GOOG', 'MSFT', 'FB', 'BBRY']
print(stocks.values()) # dict_values([(150.0, 140.0, 160.0), (1245.21, 1252.64, 1245.18), (110.41, 110.45, 109.84), (177.46, 178.67, 175.79), (10.87, 10.76, 10.90)])