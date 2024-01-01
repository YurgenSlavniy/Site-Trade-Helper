# При запуске скрипт выводит в консоль информацию полученную с биржи exmo.me
# все торговые пары, которые торгуются с рублём и цены, отсортированные по возрастанию.

import pandas as pd
import requests
from datetime import datetime

# функция которая принимает в параметр название валютной пары, 
# делает апиай запрос на биржу 
# и возвращает ответ, преобразованный в датафрейм в 9 столбцов:

# 1. 'cur_pair'
# 2.  ask'
# 3. 'ask_amount'
# 4. 'ask_quantity'
# 5. 'ask_top', 
# 6. 'bid'
# 7. 'bid_amount'
# 8. 'bid_quantity'
# 9. 'bid_top'

def order_book_df(cur_pair):
    url = "https://api.exmo.me/v1.1/order_book"

    payload='pair=' + cur_pair + '&limit=100'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    df = pd.read_json(response.text, orient='records')
    cur_pair = df.columns.tolist()[0]
    
    curtent_pair = []
    ask = []
    ask_amount = []
    ask_quantity = []
    ask_top = []
    bid = []
    bid_amount = []
    bid_quantity = []
    bid_top = []
    
    curtent_pair.append(cur_pair)
    ask.append(df.T['ask'].tolist()[0])
    ask_amount.append(df.T['ask_amount'].tolist()[0])
    ask_quantity.append(df.T['ask_quantity'].tolist()[0])
    ask_top.append(df.T['ask_top'].tolist()[0])
    bid.append(df.T['bid'].tolist()[0])
    bid_amount.append(df.T['bid_amount'].tolist()[0])
    bid_quantity.append(df.T['bid_quantity'].tolist()[0])
    bid_top.append(df.T['bid_top'].tolist()[0])
    
    order_book_df = pd.DataFrame({'cur_pair' : curtent_pair,
                                  'ask': ask,
                                  'ask_amount': ask_amount,
                                  'ask_quantity':  ask_quantity,
                                  'ask_top':  ask_top,
                                  'bid':  bid,
                                  'bid_amount':  bid_amount,
                                  'bid_quantity':  bid_quantity,
                                  'bid_top':  bid_top
                         },
                           columns=['cur_pair',
                                  'ask',
                                  'ask_amount',
                                  'ask_quantity',
                                  'ask_top',
                                  'bid',
                                  'bid_amount',
                                  'bid_quantity',
                                  'bid_top'
                                   ])
    return order_book_df

# функция принимает датасет возвращаемый функцией order_book_df
# и возвращает датафрейм по спросу. 4 столбца.

def ask_df(df):
    
    cur_pair = df['cur_pair'][0]
    cur_pair_ask = []
    price_ask = []
    amount_ask = []
    quantity_ask = []
    
    for el in range(0, len(df['ask'][0])):
        cur_pair_ask.append(cur_pair)
        price_ask.append(float(df['ask'][0][el][0]))
        amount_ask.append(float(df['ask'][0][el][1]))
        quantity_ask.append(float(df['ask'][0][el][2]))

    ask_df = pd.DataFrame({'cur_pair': cur_pair_ask,
                       'price_ask': price_ask,
                       'amount_ask': amount_ask,
                       'quantity_ask': quantity_ask
                      },
                     columns=['cur_pair',
                       'price_ask',
                       'amount_ask',
                       'quantity_ask'])
    return ask_df

# функция принимает датасет возвращаемый функцией order_book_df
# и возвращает датафрейм по предложению. 4 столбца.

def bid_df(df):

    cur_pair = df['cur_pair'][0]
    cur_pair_bid = []
    price_bid = []
    amount_bid = []
    quantity_bid = []
    
    for el in range(0, len(df['bid'][0])):
        cur_pair_bid.append(cur_pair)
        price_bid.append(float(df['bid'][0][el][0]))
        amount_bid.append(float(df['bid'][0][el][1]))
        quantity_bid.append(float(df['bid'][0][el][2]))

    bid_df = pd.DataFrame({'cur_pair': cur_pair_bid,
                       'price_bid': price_bid,
                       'amount_bid': amount_bid,
                       'quantity_bid': quantity_bid
                      },
                     columns=['cur_pair',
                       'price_bid',
                       'amount_bid',
                       'quantity_bid'])
    return bid_df
 
# функция принимает датасет возвращаемый функцией order_book_df
# возвращает датафрейм в 2 столбца: валютная пара - цена. 
def price_cur_df(df):
    
    cur_pair = df['cur_pair'][0]
    price_ask = float(df['ask'][0][0][0])
    price_bid = float(df['bid'][0][0][0])
    
    price = (price_ask + price_bid)/2
    
    price_cur_df = pd.DataFrame({'cur_pair': cur_pair,
                       'price': [price]
                      },
                     columns=['cur_pair',
                       'price'])
    
    return price_cur_df

# функция принимает список валютных пар 
# и возвращает датафрейм из 2 ух столбцов. Валютная пара, цена. 
# отсортированный по цене по всем валютным парам в одном датафрейме
def price_list(pair_list):
    currents_list = []
    price_list = []

    for el in pair_list:
        a = order_book_df(el)
        currents_list.append(a['cur_pair'][0])
        price_list.append((float(a['ask_top'][0]) + float(a['bid_top'][0]))/2)
    
    price_list_df = pd.DataFrame({'cur_pair': currents_list,  
                              'price':price_list }, 
                            columns=['cur_pair', 'price'])

    return price_list_df.sort_values(by='price', ascending=True)

# в качестве параметра функция принимает датафрейм, сгенерированный функцией price_list(pair_list)
def output(df):
    cur_pair_list = list(df['cur_pair']) 
    prices = list(df['price'])
    i = 0

    while i < len(cur_pair_list):
        if prices[i] < 0.1:
            print(f'{i + 1}. {cur_pair_list[i]} : {round(prices[i], 6)}')
        elif prices[i] < 1:
            print(f'{i + 1}. {cur_pair_list[i]} : {round(prices[i], 4)}')
        elif prices[i] > 1 and prices[i] < 10:     
            print(f'{i + 1}. {cur_pair_list[i]} : {round(prices[i], 3)}')
        else:
            print(f'{i + 1}. {cur_pair_list[i]} : {round(prices[i], 2)}')
        i += 1

#####################

rub_pair_list = ['DAI_RUB', 
                 'DOGE_RUB', 
                 'EXM_RUB', 
                 'SHIB_RUB', 
                 'XLM_RUB', 
                 'XRP_RUB', 
                 'XTZ_RUB', 
                 'BTC_RUB',
                 'LTC_RUB',
                 'ETH_RUB',
                 'DASH_RUB',
                 'ZEC_RUB',
                 'WAVES_RUB',
                 'USDT_RUB',
                 'ETC_RUB',
                 'BCH_RUB',
                 'TRX_RUB',
                 'NEO_RUB',
                 'GUSD_RUB',
                 'ALGO_RUB']

df = price_list(rub_pair_list)
output(df)
now = datetime.now()
print('\n', now.strftime("%d.%m.%y %H:%M"))  
