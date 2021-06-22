import requests as request
from pprint import pprint

"""
Чтобы запустить примеры нужно выполнить pip install requirements.txt
"""

print('*' * 80)
print('--> История сделок для пары EXM_RUB\n(List of the deals on currency pairs EXM_RUB or EXM_RUB,BTC_USD) ')
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
print('\nПоказывает историю ордеров: '
      '\ntype -  тип ордера: buy и sell.'
      '\namount - объём сделки в EXM'
      '\nprice - цена по которой произошла сделка RUB'
      '\nquantity - объём сделки в  RUB')

print('*' * 80)


print('*' * 80)
print('--> Книга текущих ордеров по валютной паре\n'
      'The book of current orders on the currency pair')
pair = input('EXM_RUB<').upper() or 'BTC_USD'
print('the number of displayed positions (default: 100, max: 1000)')
limit = int(input('limit:') or 100)
result = request.post('https://api.exmo.com/v1.1/order_book',
                       data={'pair': pair, 'limit': limit}).json()
print(result)
print('Это 6.05, 300.66074312, 1818.99749587 похоже на ордера цена RUB 6.05     300 EXM    1818 RUB - total')
print('*' * 80)

print('*' * 80)
print('-->Статистика. Цены и объём торгов.\n(Statistics on prices and volume of trades by currency pairs)')
result = request.post('https://api.exmo.com/v1.1/ticker').json()
currency_name = input('EXM_RUB<').upper() or 'BTC_USD'
pprint(result[currency_name])
print('\navg - цена на рынке на данный момент! ЗАПРОС №1  в нашем помощнике - укажите цену на рынке'
      '\nbuy_price - цена покупки'
      '\nhigh - цена Max за последние 24 часа'
      '\nlast_trade - Последняя цена по которой совершилась сделка'
      '\nlow - цена Min за последние 24 часа'
      '\nsell_price - цена продажи'
      '\nupdated - ?'
      '\nvol - Объём торгов в RUB\nvol_curr - Объём торгов в EXM')
print('*' * 80)

print('*' * 80)
print('--> Настройка торговой пары \n(Currency pairs settings)')
result = request.post('https://api.exmo.com/v1.1/pair_settings').json()
currency_name = input('EXM_RUB<').upper() or 'BTC_USD'
pprint(result[currency_name])
print('\nОТЛИЧНО! ВСЕ НУЖНЫЕ НАСТРОЙКИ ПАРЫ В ОДНОМ ЗАПРОСЕ!:\n\n'
      'commission_maker_percent - комиссия за BUY сделки %\n'
      'commission_taker_percent - комиссия за SELL сделки %\n'
      'max_amount - максимальная сумма EXM \n'
      'max_price - максимально возможная цена RUB\n'
      'max_quantity - максимальное количеество EXM\n'
      'min_amount - минимальная сумма EXM \n'
      'min_price - мминимальная цена RUB\n'
      'min_quantity - минимальное количеество EXM\n'
      'price_precision - ??? точность цены ???\n')
print('*' * 80)


print('*' * 80)
print('-->расширенный список валют\n(Extended list of currencies)')
result = request.get('https://api.exmo.com/v1.1/currency/list/extended')
pprint(result.json())
print('\nСписок валют и их сокращёное обозначение.\nВозможно список всех валюты на этой бирже')
print('*' * 80)


print('*' * 80)
print('--> Расчет суммы покупки определенного количества валюты для конкретной валютной пары')
pair = input('EXM_RUB<').upper() or 'BTC_USD'
quantity = int(input('количество для покупки >') or 1)
result = request.post(
    'https://api.exmo.com/v1.1/required_amount', data={'pair': pair, 'quantity': 10})
pprint(result.json())
print('\namount - сумма RUB'
      '\navg_price - рыночная цена RUB'
      '\nquantity - количество EXM\nОчень похоже на расчёт минимальной сделки по рыночной цене')
print('*' * 80)


print('*' * 80)
print('Список провайдеров криптографии')
result = request.get(
    'https://api.exmo.com/v1.1/payments/providers/crypto/list').json()
currency_name = input('EXM <').upper() or 'BTC'
pprint(result[currency_name])

print('Не совсем понятные для меня данные. \nЧто то звязанное с транзакциями как я понимаю. \nНе вижу тут интересующих пока данных')
print('*' * 80)
