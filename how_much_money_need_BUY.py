pair_name = 'EXM/RUB'
# приветственное сообщение
print('\nЭта программа произведёт расчёт количества необходимых ДЕНЕЖНЫХ СРЕДСТВ\n'
      'для расстановки минимальных торговых ордеров с заданным шагом.\n'
      'Расчёт будет производиться для торговой пары {}\n'.format(pair_name))

# глобальные данные:
currency = 'EXM'
use_currency = 'RUB'
min_order_value = 10
trade_comission = 1
print('Введите запрашиваемую информацию, для генерации и расчёта:')
price = input('Запрос 1: Введите цену на бирже: ')
price = float(price)
min_price = input('Запрос 2: Введите минимальную цену за которую готовы купить EXM: ')
min_price = float(min_price)
trade_step = input('Запрос 3: Введите шаг с которым нужно расставить ордера: ')
trade_step = float(trade_step)

min_buy_order_value = round(min_order_value + (min_order_value * trade_comission / 100), 2)


def buyMinValueOrderGeneration ():

    buy_trade_intervale = price - min_price
    buy_orders_quantity = buy_trade_intervale/trade_step
    buy_orders_count = int(buy_orders_quantity)
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
        enter = input('\nПроизвести генерацию ордеров? (ДА/НЕТ): ')
        enter = enter.upper()
        if enter == 'ДА':
            for order in buy_orders_generation:
                print(order)
    else:
        print('Здесь участок код для растановки при нецелочисленном делении')

buyMinValueOrderGeneration()
