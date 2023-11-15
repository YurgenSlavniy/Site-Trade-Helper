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

# Объединение датасетов
def big_dataset(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True)
    big_df_uniq = big_df.drop_duplicates()
    # что то сделать с индексами, т. к после дубликата их значения сбиваются
    return big_df_uniq

# Проверка при объединении датасетов на дубликаты
def duplicates(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True).drop_duplicates()
    if len(big_df) == len(dataframe_first) + len(dataframe_last):
        print('Полное объединение датасетов. Дубликатов нет.\n'
              'Следует проверить последние и первые даты в датасетах\n'
              'возможно есть промежуточный датасет ')
    else:
        print('Объединение датасетов произошло. Число дубликатов:', len(dataframe_first) + len(dataframe_last) - len(big_df))


# Переформатирование типа колонки время в дататайм формат
def to_datetime(dataframe):
    dataframe['Дата/время'] = pd.to_datetime(dataframe['Дата/время'], format='%d.%m.%Y %H:%M')
    return dataframe

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

# Визуализация данных по Buy и Sell
def visual_buy_sell(dataframe):
    g = sns.countplot(dataframe['Тип'])
    g.set_xticklabels(['buy','sell'])
    plt.show()

# количество сделок в каждой торговой паре
def curr_pair_trade_counts(dataframe):
    print('Колличество сделок в каждой торговой паре:')
    print(dataframe['Валютная пара'].value_counts())

# Статистика

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

# аналитика торговли (применять к одной торговой паре)
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

# Проверка на дисбаланс классов
def dissbalance(dataframe):
    # class count
    class_count_0, class_count_1 = dataframe['Тип'].value_counts()

    # Separate class
    class_0 = dataframe[dataframe['Тип'] == 'buy']
    class_1 = dataframe[dataframe['Тип'] == 'sell']# print the shape of the class
    print('buy class 0:', class_0.shape)
    print('sell class 1:', class_1.shape)

# Изменение начального датасета, добавление демипеременных, избавление от типов object
def prepare_data(dataframe):
    prep_data = pd.concat([dataframe, pd.get_dummies(dataframe['Тип'])], axis=1)
    prep_data.drop(columns=['Тип'], inplace=True)
    prep_data = pd.concat([prep_data, pd.get_dummies(dataframe['Тип комиссии'])], axis=1)
    prep_data.drop(columns=['Тип комиссии'], inplace=True)
    prep_data = pd.concat([prep_data, pd.get_dummies(dataframe['Комиссия %'])], axis=1)
    prep_data.drop(columns=['Комиссия %'], inplace=True)
    prep_data.drop(columns=['Trade ID'], inplace=True)
    prepare_data = to_datetime(prep_data)
    return prepare_data
    
# Число сделок в день
def per_day(dataframe):
    new_vals = []
    vals = dataframe['Дата/время'].values
    for el in vals:
        numb = el[0:2]
        new_vals.append(numb)
    dataframe['days'] = new_vals
    dataframe['days'].value_counts()
    return dataframe['days'].value_counts()

#######################################

# загружаю последнюю историю и самую раннюю скаченную историю торгов
df = pd.read_csv('trade-history-2023-01-21.csv')
df_first = pd.read_csv('trade-history-2021-11-07.csv')

df_all_dates = big_dataset(df, df_first)

duplicates(df, df_first)

# сортировка по годам
df_2021 = df_all_dates[df_all_dates['Дата/время'].str.contains("2021")]
df_2022 = df_all_dates[df_all_dates['Дата/время'].str.contains("2022")]
df_2023 = df_all_dates[df_all_dates['Дата/время'].str.contains("2023")]

# сортировка по месяцам
df_jan_2021 = df_2021[df_2021['Дата/время'].str.contains(".01.2021")]
df_feb_2021 = df_2021[df_2021['Дата/время'].str.contains(".02.2021")]
df_mar_2021 = df_2021[df_2021['Дата/время'].str.contains(".03.2021")]
df_apr_2021 = df_2021[df_2021['Дата/время'].str.contains(".04.2021")]
df_may_2021 = df_2021[df_2021['Дата/время'].str.contains(".05.2021")]
df_jun_2021 = df_2021[df_2021['Дата/время'].str.contains(".06.2021")]
df_jul_2021 = df_2021[df_2021['Дата/время'].str.contains(".07.2021")]
df_avg_2021 = df_2021[df_2021['Дата/время'].str.contains(".08.2021")]
df_sep_2021 = df_2021[df_2021['Дата/время'].str.contains(".09.2021")]
df_oct_2021 = df_2021[df_2021['Дата/время'].str.contains(".10.2021")]
df_nov_2021 = df_2021[df_2021['Дата/время'].str.contains(".11.2021")]
df_dec_2021 = df_2021[df_2021['Дата/время'].str.contains(".12.2021")]

df_jan_2022 = df_2022[df_2022['Дата/время'].str.contains(".01.2022")]
df_feb_2022 = df_2022[df_2022['Дата/время'].str.contains(".02.2022")]
df_mar_2022 = df_2022[df_2022['Дата/время'].str.contains(".03.2022")]
df_apr_2022 = df_2022[df_2022['Дата/время'].str.contains(".04.2022")]
df_may_2022 = df_2022[df_2022['Дата/время'].str.contains(".05.2022")]
df_jun_2022 = df_2022[df_2022['Дата/время'].str.contains(".06.2022")]
df_jul_2022 = df_2022[df_2022['Дата/время'].str.contains(".07.2022")]
df_avg_2022 = df_2022[df_2022['Дата/время'].str.contains(".08.2022")]
df_sep_2022 = df_2022[df_2022['Дата/время'].str.contains(".09.2022")]
df_oct_2022= df_2022[df_2022['Дата/время'].str.contains(".10.2022")]
df_nov_2022 = df_2022[df_2022['Дата/время'].str.contains(".11.2022")]
df_dec_2022 = df_2022[df_2022['Дата/время'].str.contains(".12.2022")]

df_jan_2023 = df_2023[df_2023['Дата/время'].str.contains(".01.2023")]
df_feb_2023 = df_2023[df_2023['Дата/время'].str.contains(".02.2023")]
df_mar_2023 = df_2023[df_2023['Дата/время'].str.contains(".03.2023")]
df_apr_2023 = df_2023[df_2023['Дата/время'].str.contains(".04.2023")]
df_may_2023 = df_2023[df_2023['Дата/время'].str.contains(".05.2023")]
df_jun_2023 = df_2023[df_2023['Дата/время'].str.contains(".06.2023")]
df_jul_2023 = df_2023[df_2023['Дата/время'].str.contains(".07.2023")]
df_avg_2023 = df_2023[df_2023['Дата/время'].str.contains(".08.2023")]
df_sep_2023 = df_2023[df_2023['Дата/время'].str.contains(".09.2023")]
df_oct_2023 = df_2023[df_2023['Дата/время'].str.contains(".10.2023")]
df_nov_2023 = df_2021[df_2021['Дата/время'].str.contains(".11.2023")]
df_dec_2023 = df_2023[df_2023['Дата/время'].str.contains(".12.2023")]


# time_period(df_all_dates)
# trades_count(df_all_dates)
# enumirated_pairs(df_all_dates)
# curr_pair_trade_counts(df_all_dates)

time_period(df_all_dates)
trades_count(df_all_dates)
enumirated_pairs(df_all_dates)
curr_pair_trade_counts(df_all_dates)


print(f'\nСделки за 2021 год. Общее количество: {len(df_2021)}'
      f'\nЯнварь 2021: {len(df_jan_2021)}'
      f'\nФевраль 2021: {len(df_feb_2021)}'
      f'\nМарт 2021: {len(df_mar_2021)}'
      f'\nАпрель 2021: {len(df_apr_2021)}'
      f'\nМай 2021: {len(df_may_2021)}'
      f'\nИюнь 2021: {len(df_jun_2021)}'
      f'\nИюль 2021: {len(df_jul_2021)}'
      f'\nАвгуст 2021: {len(df_avg_2021)}'
      f'\nСентябрь 2021: {len(df_sep_2021)}'
      f'\nОктябрь 2021: {len(df_oct_2021)}'
      f'\nНоябрь 2021: {len(df_nov_2021)}'
      f'\nДекабрь 2021: {len(df_dec_2021)}')

print(f'\nСделки за 2022 год. Общее количество: {len(df_2022)}'
      f'\nЯнварь 2022: {len(df_jan_2022)}'
      f'\nФевраль 2022: {len(df_feb_2022)}'
      f'\nМарт 2022: {len(df_mar_2022)}'
      f'\nАпрель 2022: {len(df_apr_2022)}'
      f'\nМай 2022: {len(df_may_2022)}'
      f'\nИюнь 2022: {len(df_jun_2022)}'
      f'\nИюль 2022: {len(df_jul_2022)}'
      f'\nАвгуст 2022: {len(df_avg_2022)}'
      f'\nСентябрь 2022: {len(df_sep_2022)}'
      f'\nОктябрь 2022: {len(df_oct_2022)}'
      f'\nНоябрь 2022: {len(df_nov_2022)}'
      f'\nДекабрь 2022: {len(df_dec_2022)}')

print(f'\nСделки за 2023 год. Общее количество: {len(df_2023)}'
      f'\nЯнварь 2023: {len(df_jan_2023)}'
      f'\nФевраль 2023: {len(df_feb_2023)}'
      f'\nМарт 2023: {len(df_mar_2023)}'
      f'\nАпрель 2023: {len(df_apr_2023)}'
      f'\nМай 2023: {len(df_may_2023)}'
      f'\nИюнь 2023: {len(df_jun_2023)}'
      f'\nИюль 2023: {len(df_jul_2023)}'
      f'\nАвгуст 2023: {len(df_avg_2023)}'
      f'\nСентябрь 2023: {len(df_sep_2023)}'
      f'\nОктябрь 2023: {len(df_oct_2023)}'
      f'\nНоябрь 2023: {len(df_nov_2023)}'
      f'\nДекабрь 2023: {len(df_dec_2023)}')

current_pair = input('\nВведите/выбирете название торговой пары для которой будет произведён анализ: ')
print(50 * '_')

# сортировка по имени торговой пары
current_pair_dataset = df_all_dates.loc[(df_all_dates['Валютная пара'] == current_pair)]

time_period(current_pair_dataset)
trades_count_pair(current_pair_dataset)
analitica(current_pair_dataset, current_pair)
moda(current_pair_dataset)
maxmin(current_pair_dataset)
middle(current_pair_dataset)
median(current_pair_dataset)

#####################################
time_period(df_2023)
trades_count(df_2023)
enumirated_pairs(df_2023)
curr_pair_trade_counts(df_2023)
current_pair = input('\nВведите/выбирете название торговой пары для которой будет произведён анализ: ')
print(50 * '_')
current_pair_dataset = df_all_dates.loc[(df_all_dates['Валютная пара'] == current_pair)]
time_period(current_pair_dataset)
trades_count_pair(current_pair_dataset)
analitica(current_pair_dataset, current_pair)
moda(current_pair_dataset)
maxmin(current_pair_dataset)
middle(current_pair_dataset)
median(current_pair_dataset)
########################################