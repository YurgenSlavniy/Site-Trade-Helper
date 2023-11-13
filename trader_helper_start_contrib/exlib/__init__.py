import requests
from pprint import pprint

# входящие данные из вне.
order_size    = 10.0
comission     = 1.0
price         = 6.0
min_price     = 0.1
max_price     = 7.0
trade_step    = 0.2

 
def calc_buy(order_size, comission, price, min_price, trade_step) -> list:
	"""Вычисляет результат покупки и возвращает его в виде списка словарей"""
	result = []

	while condition:
		result.append({
				'price': 0,
				'quantity': 0,
				'sum': 0,
			})
	result.append({'profit': 0})
	return result


def calc_sell(order_size, comission, price, max_price, trade_step) -> list:
	"""Вычисляет результат продажи и возвращает его в виде списка словарей"""
	result = []

	return result


def get_current_price(pair: str) -> float:
	"""Получает текущую цену крипто-валюты"""
	result = requests.post('https://api.exmo.com/v1.1/ticker')

	assert result.status_code == 200, f'response status code 200'
	result = result.json()

	return float(result[pair]['avg'])



buy_result  = calc_buy(order_size, comission, price, min_price, trade_step)
sell_result = calc_sell(order_size, comission, price, max_price, trade_step)

pprint(buy_result)
pprint(sell_result)