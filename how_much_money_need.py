# Описание.
# Пользователь вводит данные:
# - цену на бирже на даный момент времени ,
# - минимальную цены покупки,
# - максимальную цену продажи,
# - шаг с которым будем расставлять ордера
# (также может  данные можно брать с помощью API непосредственно с биржи EXMO.me)
# Программа расставляет минимальные ордера на заданном отрезке цены
# и выводит пользователю итоговую сумму сколько пользователю понадобится денег (рублей)
# чтобы расставить ордера с заданными параметрами. Комиссия в торговой паре учитывается.

# -------- Библиотека функций -------------

# для расстановки BUY ордеров
def buyMinValueOrderGeneration (buy_trade_intervale, buy_orders_quantity, buy_orders_count):

    if buy_orders_count == buy_orders_quantity:
        orders_count = 1
        order_price = price
        buy_order_value = round(order_price * min_buy_order_value, 2)
        buy_orders_generation = []
        buy_orders_generation.append('{}) цена: {}   количество: {}   сумма: {} '.format(orders_count, order_price, min_buy_order_value, buy_order_value))
        profit_buy_order_value = buy_order_value
        while order_price > min_price:
            orders_count += 1
            order_price = round(order_price - trade_step, 2)
            buy_order_value = round(order_price * min_buy_order_value, 2)
            buy_orders_generation.append('{}) цена: {}   количество: {}   сумма: {} '.format(orders_count, order_price, min_buy_order_value, buy_order_value))
            profit_buy_order_value = profit_buy_order_value + buy_order_value
        print('\nНа отрезке цены от {} до {} RUB с шагом {} RUB\nбудет выставлено {} ордеров \nна общую сумму {} RUB'
              .format(min_price, price, trade_step, orders_count, profit_buy_order_value) )
        return buy_orders_generation, profit_buy_order_value

    else:

        orders_count = 1
        order_price = price
        buy_order_value = round(order_price * min_buy_order_value, 2)
        buy_orders_generation = []
        buy_orders_generation.append(
            '{}) цена: {}   количество: {}   сумма: {} '.format(orders_count, order_price, min_buy_order_value,
                                                                buy_order_value))
        profit_buy_order_value = buy_order_value
        while len(buy_orders_generation) <= buy_orders_count:
            orders_count += 1
            order_price = round(order_price - trade_step, 2)
            buy_order_value = round(order_price * min_buy_order_value, 2)
            buy_orders_generation.append(
                '{}) цена: {}   количество: {}   сумма: {} '.format(orders_count, order_price, min_buy_order_value,
                                                                    buy_order_value))
            profit_buy_order_value = round(profit_buy_order_value + buy_order_value, 2)

        orders_count += 1
        order_price = min_price
        buy_order_value = min_buy_order_value * min_price
        profit_buy_order_value = round(profit_buy_order_value + min_buy_order_value * min_price, 2)

        buy_orders_generation.append('{}) цена: {}   количество: {}   сумма: {} '.format(orders_count, order_price, min_buy_order_value,buy_order_value))
        profit_buy_order_value = round(profit_buy_order_value, 2)

        print('\nНа отрезке цены от {} до {} RUB с шагом {} RUB\nбудет выставлено {} ордеров \nна общую сумму {} RUB'
              .format(min_price, price, trade_step, orders_count, profit_buy_order_value))
        return buy_orders_generation, profit_buy_order_value
# для генерации SELL ордеров:
def sellMinValueOrderGeneration (sell_trade_intervale, sell_orders_quantity, sell_orders_count):

    if sell_orders_count == sell_orders_quantity:
        orders_count = 0
        total_sell_money = round(sell_orders_count * (min_order_value + (min_order_value * trade_comission / 100)) * price, 2)
        profit_sell_money = 0
        buy_for_sale = round( sell_orders_count * (min_order_value + (min_order_value * trade_comission / 100)), 2)
        sell_order_price = price
        sell_orders_generation = []
        while sell_order_price < max_price:
            orders_count += 1
            sell_order_price = round(sell_order_price + trade_step, 2)
            sell_money = round(min_sell_order_value * sell_order_price, 2)
            profit_sell_money = round(profit_sell_money + sell_money, 2)
            sell_orders_generation.append('{}) SELL  цена: {} RUB   количество: {} EXM на сумму: {} {}'.format(orders_count, sell_order_price, min_sell_order_value, sell_money, use_currency))
        print('\nВ интервале цены от {} до {} RUB\nБудет выставлено {} sell ордеров\nДля этого по рыночной цене {} RUB будет куплено {} EXM на сумму: {} RUB'.format(price, max_price, sell_orders_count, price, buy_for_sale, total_sell_money))
        return sell_orders_generation, total_sell_money, profit_sell_money

    else:
        sell_order_price = price
        sell_orders_generation = []
        orders_count = 0
        profit_sell_money = 0
        while len(sell_orders_generation) <= sell_orders_count:
            orders_count += 1
            sell_order_price = round(sell_order_price + trade_step, 2)
            sell_money = round(min_sell_order_value * sell_order_price, 2)
            profit_sell_money = round(profit_sell_money + sell_money, 2)
            sell_orders_generation.append('{}) SELL  цена: {} RUB   количество: {} EXM на сумму: {} {}'.format(orders_count, sell_order_price, min_sell_order_value, sell_money, use_currency))

        del sell_orders_generation[-1]
        sell_order_price = max_price
        sell_money = round(min_sell_order_value * sell_order_price, 2)
        buy_for_sale = round( (sell_orders_count + 1) * (min_order_value + (min_order_value * trade_comission / 100)), 2)
        sell_orders_generation.append(
            '{}) SELL  цена: {} RUB   количество: {} EXM на сумму: {} {}'.format(orders_count, sell_order_price, min_sell_order_value, sell_money, use_currency))
        total_sell_money = round(buy_for_sale * price, 2)
        profit_sell_money = round(profit_sell_money + sell_money, 2)
        print('\nВ интервале цены от {} до {} RUB\nБудет выставлено {} sell ордеров\nДля этого по рыночной цене {} RUB будет куплено {} EXM на сумму: {} RUB'.format(price, max_price, len(sell_orders_generation), price, buy_for_sale, total_sell_money))
        return sell_orders_generation, total_sell_money, profit_sell_money
#____________________________________________________



# Для простоты мы начнём с одной валютной пары:
# EXM/RUB.
# так как пара конкретная, то и некоторые показатели нам уже точно известны:

pair_name = 'EXM/RUB'
currency = 'EXM'
use_currency = 'RUB'
min_order_value = 10    # минимальный ордер 10 EXM
trade_comission = 1   # 1 %   - торговая комиссия за каждую сделку

# приветственное сообщение
print('\nЭта программа произведёт расчёт количества необходимых ДЕНЕЖНЫХ СРЕДСТВ\n'
      'для расстановки минимальных торговых ордеров с заданным шагом.\n'
      'Расчёт будет производиться для торговой пары {}\n'.format(pair_name))

# здесь можно было бы подключиться по API к бирже, отпаривть запрос и вывести пользователю данные по валютной бирже .
# exmo-api.py.

print('Текущие данные с биржи: цена на бирже = ... и другие данные\n') # формируем сообщение вывода информации с биржи

# пошли запросы , чтобы пользователь вводил данные
print('Введите запрашиваемую информацию, для генерации и расчёта:')
price = input('Запрос 1: Введите цену на бирже: ')
price = float(price)
min_price = input('Запрос 2: Введите минимальную цену за которую готовы купить EXM: ')
min_price = float(min_price) # сперва вводим, потом меняю type даннных.
# При вводе принимает строкой любой ввод и не ругается, когда вводим целое число без точки
max_price = input('Запрос 3: Введите максимальную цену за которую готовы продать EXM: ')
max_price = float(max_price)
trade_step = input('Запрос 4: Введите шаг с которым нужно расставить ордера: ')
trade_step = float(trade_step)

min_buy_order_value = round(min_order_value + (min_order_value * trade_comission / 100), 2)
min_sell_order_value = round(min_order_value + (min_order_value * trade_comission / 100), 2)
buy_trade_intervale = price - min_price
buy_orders_quantity = buy_trade_intervale / trade_step
buy_orders_count = int(buy_orders_quantity)
sell_trade_intervale = max_price - price
sell_orders_quantity = sell_trade_intervale / trade_step
sell_orders_count = int(sell_orders_quantity)

# После ввода данных выводим сообщение с некоторыми расчётами пользователю, для подтверждения готовности генерации.
print('\nПоехали!')
# для генерации BUY ордеров:
buy_parameters = buyMinValueOrderGeneration (buy_trade_intervale, buy_orders_quantity, buy_orders_count)
buy_orders_generation = buy_parameters[0]
money_for_buy =  buy_parameters[1]
enter = input('\nПроизвести генерацию ордеров? (ДА/НЕТ): ')
enter = enter.upper()
if enter == 'ДА':
    for order in buy_orders_generation:
        print(order)
# для генерации SELL ордеров:
sell_parameters = sellMinValueOrderGeneration (sell_trade_intervale, sell_orders_quantity, sell_orders_count)
sell_orders_generation = sell_parameters[0]
money_for_sale = sell_parameters[1]
enter = input('\nПроизвести генерацию ордеров? (ДА/НЕТ): ')
enter = enter.upper()
if enter == 'ДА':
    for order in sell_orders_generation:
        print(order)
buy_orders_count = len(buy_orders_generation)
sell_orders_count = len(sell_orders_generation)
all_ordes_quanity = sell_orders_count + buy_orders_count
how_much_money_need = round(money_for_sale + money_for_buy, 2)
profit_sell_money = sell_parameters[2]
profit = round(profit_sell_money - how_much_money_need, 2)
print('\n    Итоговые данные:'
      '\nЦена на бирже на данный момент: {} RUB'
      '\nНа интервале цены от {} до {} RUB'
      '\nВсего выставленно  ордеров: {} '
      '\nиз них BUY ордеров: {}, SELL ордеров: {} '
      '\nдля этой расстановки вам понадобится средств: '
      '\n--> для BUY ордеров: {} RUB'
      '\n--> для SELL ордеров: {} RUB'
      '\nОбщая сумма которая вам понадобится на расстановку всех ордеров: {} RUB'
      .format(price, min_price, max_price, all_ordes_quanity,buy_orders_count, sell_orders_count, money_for_buy, money_for_sale, how_much_money_need ))
print('\nЕсли все выставленные ордера продадутся, у вас на счёте будет {} RUB\nА ваша прибыль составит {} RUB'.format(profit_sell_money, profit))
# Поехали!

