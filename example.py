import requests as request
from pprint import pprint

"""
Чтобы запустить примеры нужно выполнить pip install requirements.txt
"""

print('*' * 80)
print('List of the deals on currency pairs EXM_RUB or EXM_RUB,BTC_USD')
pair = input('EXM_RUB<').upper() or 'EXM_RUB'
result = request.post('https://api.exmo.com/v1.1/trades', data={'pair': pair})
result = result.json()
for currency in result:
    pprint(currency)
    for el in result[currency]:
        s = '{:<15} {:<25} {:<20} {:<20}'.format(
            'type: ' + el['type'],
            'amount: ' + el['amount'],
            'price: ' + el['price'],
            'quantity: ' + el['quantity']
        )
        print(s)
print('*' * 80)


# print('*' * 80)
# print('The book of current orders on the currency pair')
# pair = input('EXM_RUB<').upper() or 'BTC_USD'
# print('the number of displayed positions (default: 100, max: 1000)')
# limit = int(input('limit:') or 100)
# result = request.post('https://api.exmo.com/v1.1/order_book',
#                       data={'pair': pair, 'limit': limit}).json()
# pprint(result)
# print('*' * 80)

# print('*' * 80)
# print('Statistics on prices and volume of trades by currency pairs')
# result = request.post('https://api.exmo.com/v1.1/ticker').json()
# currency_name = input('EXM_RUB<').upper() or 'BTC_USD'
# pprint(result[currency_name])
# print('*' * 80)

# print('*' * 80)
# print('Currency pairs settings')
# result = request.post('https://api.exmo.com/v1.1/pair_settings').json()
# currency_name = input('EXM_RUB<').upper() or 'BTC_USD'
# pprint(result[currency_name])
# print('*' * 80)


# print('*' * 80)
# print('Extended list of currencies')
# result = request.get('https://api.exmo.com/v1.1/currency/list/extended')
# pprint(result.json())
# print('*' * 80)


# print('*' * 80)
# print('Расчет суммы покупки определенного количества валюты для конкретной валютной пары')
# pair = input('EXM_RUB<').upper() or 'BTC_USD'
# quantity = int(input('количество для покупки >') or 1)
# result = request.post(
#     'https://api.exmo.com/v1.1/required_amount', data={'pair': pair, 'quantity': 10})
# pprint(result.json())
# print('*' * 80)


# print('*' * 80)
# print('Список провайдеров криптографии')
# result = request.get(
#     'https://api.exmo.com/v1.1/payments/providers/crypto/list').json()
# currency_name = input('EXM <').upper() or 'BTC'
# pprint(result[currency_name])
# print('*' * 80)
