from collections import namedtuple
 
Stock = namedtuple("Stock", ("symbol", "current", "high", "low"))
stock1 = Stock("FB", 177.46, 178.67, 175.79)
print(stock1.high, stock1[3])
stock2 = Stock("AAPL", 150.0, 140.0, 160.0)
symbol, current, high, low = stock2
print(symbol, current)

print()
print(stock1.__dict__)