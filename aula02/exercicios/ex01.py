# API de Preços de Ações
# Crie uma API que mantém uma lista dos preços de fechamento de várias ações ao longo dos dias. 
# Utilize dicionários, em que as chaves representam o código da ação e os valores são listas de tuplas 
# contendo a data e o preço de fechamento. Implemente os seguintes métodos:

# add(code, date, closing_price): adiciona informações de preço de fechamento para uma ação específica em uma determinada data.
# Certifique-se de lidar com casos em que a ação ainda não possui uma entrada no dicionário, usando defaultdict.
# get_prices(code): Retorna a lista de tuplas contendo a data e o preço de fechamento para uma ação específica.
# get_all_stocks(): Retorna uma lista com todos os códigos de ações presentes no dicionário.
# average_price(code): Retorna a média dos preços de fechamento de uma ação específica.
# recent_prices(code, date): Retorna uma lista com os preços de fechamento de uma ação específica a partir da data date.

from collections import defaultdict, namedtuple
import datetime
class Stocks:
    date = namedtuple("date", ("year", "month", "day"))
    stockValue = namedtuple("StockValue", ("date", "closing_price"))
        
    def __init__(self):
        """
        Métodos:\n
        add\n
        get_prices\n
        get_all_stocks\n
        average_price\n
        recent_prices\n
        """
        self._stocks = defaultdict(list)
    
    def add(self, code:str, date:tuple, closing_price:float):
        """
        adiciona informações de preço de fechamento para uma ação específica em uma determinada data.

        Args:
            code (str): código da ação. Ex: "GOOG"
            date (tuple): data de fechamento da ação, tupla no formato (ano, mês, dia). Exemplo: (2003, 04, 30)
            closing_price (float): preço de fechamento. Ex: 33.4
        """
        self._stocks[code].append(self.stockValue(self.date(*date), closing_price))
    
    def get_prices(self, code:str):
        """
        Retorna a lista de tuplas contendo a data e o preço de fechamento para uma ação específica.

        Args:
            code (str): código da ação. Ex: "GOOG"

        Returns:
            (tuple): data e preço de fechamento para a ação. Ex: ((2021, 03, 24), 23.4)
        """
        return self._stocks[code]
    
    def get_all_stocks(self):
        """
        Retorna uma lista com todos os códigos de ações neste objeto.

        Returns:
            (list): todos os códigos de ações neste objeto. Ex: ['GOOG', 'TTWO']
        """
        return list(self._stocks.keys())
    
    def average_price(self, code:str):
        """
        Retorna um float contendo a média dos preços de fechamento de uma ação específica.

        Args:
            code (str): código da ação. Ex: "GOOG"

        Returns:
            (float): média dos preços de fechamento de uma ação específica.
        """
        
        prices = [price for _, price in self._stocks[code]]
        return sum(prices) / len(prices) if prices else None
    
    def recent_prices(self, code:str, date:tuple):
        """
        Retorna uma lista com os preços de fechamento de uma ação específica a partir da data date.

        Args:
            code (str): código da ação. Ex: "GOOG"
            date (tuple): data de fechamento da ação, tupla no formato (ano, mês, dia). Exemplo: (2003, 04, 30)

        Returns:
            (list): lista com os preços de fechamento de uma ação específica a partir da data date.
        """
        return [price for price in self.get_prices(code) if datetime.date(*(price.date)) >= datetime.date(*date)]
    
stocks1 = Stocks()
stocks1.add("GOOG", (2024, 5, 1), 150.2)
stocks1.add("GOOG", (2024, 5, 2), 151.2)
stocks1.add("TTWO", (2024, 3, 1), 140.0)

print(stocks1.get_prices("GOOG"))

print(stocks1.average_price("GOOG"))

print(stocks1.get_all_stocks())

print(stocks1.recent_prices("GOOG", (2024, 5, 2)))