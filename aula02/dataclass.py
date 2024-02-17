# https://pedrosiqueira.github.io/ifmspy/flp/06%20Estruturas%20de%20dados%20do%20Python.html

from dataclasses import make_dataclass
Stock = make_dataclass("Stock", ("symbol", "current", "high", "low"))

# maneira tradicional, mais verbosa de dataclass, apenas para comparação
class StockRegular:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low

stock1 = Stock("FB", 177.46, high=178.67, low=175.79)
stock2 = Stock("FB", 177.46, high=178.67, low=175.79)

print(stock1) # Stock(symbol='FB', current=177.46, high=178.67, low=175.79)
print(stock1 == stock2) # True
 
stock1.current = 178.25
stock1.unexpected_attribute = "allowed"
 
print(stock1)   # Stock(symbol='FB', current=178.25, high=178.67, low=175.79)
print(stock1 == stock2) # False

print()
print(stock1.__dict__)
print(stock1.__dict__.items())
print(stock1.__dict__.keys())
print(stock1.__dict__.values())