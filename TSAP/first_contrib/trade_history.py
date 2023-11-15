import pandas as pd
from scipy import stats
import datetime
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import warnings
import datetime
import pprint
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# Функция для вывода всех торговых пар, которые нашлись в истории торгов
# пары выводятся пронумированными
def enumirated_pairs(dataframe):
    all_pairs_list = dataframe['Валютная пара'].unique().tolist()
    print(f'\nОбщее число торговых пар в которых совершались сделки: {len(all_pairs_list)}')

# функция выводит сообщение о временном периоде проанализированных данных
# начало торгов - самая ранняя сделка в датафрейме
# конец торгов - самая последняя сделка в датафрейме
def time_period(dataframe):
    all_dates = dataframe['Дата/время'].tolist()
    start = all_dates[-1]
    end = all_dates[0]
    start_dtm = datetime.datetime.strptime(start, '%d.%m.%Y %H:%M')
    end_dtm = datetime.datetime.strptime(end, '%d.%m.%Y %H:%M')
    print(f'\nПроизведён анализ временного периода торговли: с {start} по {end}'
          f'\nчто составляет {end_dtm - start_dtm}')

# Общее число сделок
# из них сделок BUY и SELL
def trades_count(dataframe):
    print(f'\nОбщее число сделок во всех торговых парах за проанализированный период времени: {len(dataframe)} из них')
    print('BUY сделки:', len(dataframe.loc[(dataframe['Тип'] == 'buy')]))
    print('SELL сделки:', len(dataframe.loc[(dataframe['Тип'] == 'sell')]))

def trades_count_pair(dataframe):
    print(f'\nОбщее число сделок в торговой паре за проанализированный период времени: {len(dataframe)} из них')
    print('BUY сделки:', len(dataframe.loc[(dataframe['Тип'] == 'buy')]))
    print('SELL сделки:', len(dataframe.loc[(dataframe['Тип'] == 'sell')]))

# количество сделок в каждой торговой паре
def curr_pair_trade_counts(dataframe):
    print('Колличество сделок в каждой торговой паре:')
    print(dataframe['Валютная пара'].value_counts())

# Объединение 2 ух csv файлов
def big_dataset(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True)
    big_df_uniq = big_df.drop_duplicates()
    return big_df_uniq

def moda(dataframe):
    print('\nМОДА')
    print('цена:', stats.mode(dataframe.Цена))  # scipy way
    print('Количество:', stats.mode(dataframe.Количество))  # scipy way
    print('Сумма:', stats.mode(dataframe.Сумма))

def median(dataframe):
    print('\nМЕДИАНА')
    print('цена:', dataframe.Цена.median())  # pandas way
    print('Количество:', dataframe.Количество.median())
    print('Сумма:', dataframe.Сумма.median())

def middle(dataframe):
    print('\nСРЕДНЕЕ')
    print('цена:', dataframe.Цена.mean())  # pandas way
    print('Количество:', dataframe.Количество.mean())
    print('Сумма:', dataframe.Сумма.mean())

def maxmin(dataframe):
    print('\nМАКСИМУМ')
    max = dataframe.Цена.max()
    print('цена:', max)  # pandas way
    print('\nМИНИМУМ')
    print('цена:', dataframe.Цена.min())  # pandas way

def analitica(dataframe, current_pair):
    current_pair_dataset_buy = dataframe.loc[(current_pair_dataset['Тип'] == 'buy')]
    current_pair_dataset_sell = dataframe.loc[(current_pair_dataset['Тип'] == 'sell')]
    currents_list = currents(current_pair)
    print(f'\nминимальная цена по которой покупали: {current_pair_dataset_buy.Цена.min()} '
          f'{currents_list[1]}\n'
          f'максимальная цена по которой продавали: {current_pair_dataset_sell.Цена.max()} '
          f'{currents_list[1]}\n'
          f'oбъём купленной валюты за весь период торгов: {current_pair_dataset_buy.Количество.sum()} '
          f'{currents_list[0]}\n'
          f'oбъём проданной валюты за весь период торгов: {current_pair_dataset_sell.Количество.sum()} '
          f'{currents_list[0]}\n'
          f'потрачено денег за весь период торгов: {current_pair_dataset_buy.Сумма.sum()} '
          f'{currents_list[1]}\n'
          f'заработано денег за весь период торгов: {current_pair_dataset_sell.Сумма.sum()} '
          f'{currents_list[1]}\n\n'
          f'дельта максимальная цена - минимальная: {current_pair_dataset_sell.Цена.max() - current_pair_dataset_buy.Цена.min()} '
          f'{currents_list[1]}\n'
          f'разница объёмов проданный - купленный: {current_pair_dataset_sell.Количество.sum() - current_pair_dataset_buy.Количество.sum()} '
          f'{currents_list[0]}\n'
          f'коэфицент объёмов проданное/купленное: {round(current_pair_dataset_sell.Количество.sum()/current_pair_dataset_buy.Количество.sum(), 2)}\n'
          f'потраченныe деньги минус заработанные: {current_pair_dataset_sell.Сумма.sum() - current_pair_dataset_buy.Сумма.sum()} '
          f'{currents_list[1]}\n'
          f'коэфицент потраченные/заработанные: {round(current_pair_dataset_sell.Сумма.sum()/current_pair_dataset_buy.Сумма.sum(), 2)}\n')

def currents(current_pair):
    pair_list = current_pair.split('_')
    return pair_list
#######################################

# загружаю последнюю историю и самую раннюю скаченную историю торгов
df = pd.read_csv('trade-history-2022-09-06.csv')
df_first = pd.read_csv('trade-history-2021-11-07.csv')

df_all_dates = big_dataset(df, df_first)

time_period(df_all_dates)
trades_count(df_all_dates)
enumirated_pairs(df_all_dates)
curr_pair_trade_counts(df_all_dates)

current_pair = input('\nВведите/выбирете название торговой пары для которой будет произведён анализ: ')
print(50 * '_')
# сортировка по имени торговой пары
current_pair_dataset = df_all_dates.loc[(df_all_dates['Валютная пара'] == current_pair)]

time_period(current_pair_dataset)
trades_count_pair(current_pair_dataset)
analitica(current_pair_dataset, current_pair)
