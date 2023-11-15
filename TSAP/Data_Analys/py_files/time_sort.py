import pandas as pd
from scipy import stats
from datetime import date
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

def big_dataset(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True)
    big_df_uniq = big_df.drop_duplicates()
    return big_df_uniq

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

# сортировка по дням
def trades_count_per_month(dataframe):
    df1 = dataframe[0:1]
    df2 = dataframe[1:]

    all_dates = dataframe['Дата/время'].tolist()
    cut_dates = []
    for el in all_dates:
        cut_el = el[0:2]
        cut_dates.append(cut_el)
    a = pd.Series(cut_dates)
    return a.value_counts()

def trades_count_per_day(dataframe):
    print('Сделок за указанный месяц:', len(dataframe))
    print(dataframe.shape, dataframe.columns, dataframe.info())


df = pd.read_csv('trade-history-2022-09-25.csv')
df_first = pd.read_csv('trade-history-2021-11-07.csv')
df_all_dates = big_dataset(df, df_first)

# сортировка по годам
df_2021 = df_all_dates[df_all_dates['Дата/время'].str.contains("2021")]
df_2022 = df_all_dates[df_all_dates['Дата/время'].str.contains("2022")]

print(f'сделок за 2021 год: {len(df_2021)}'
      f'\nсделок за 2022 год: {len(df_2022)}')

print(time_period(df_2021))
print(trades_count(df_2021))
print(time_period(df_2022))
print(trades_count(df_2022))

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

# сортировка по дням
a = trades_count_per_month(df_sep_2022)

trades_count_per_day(df_sep_2022)

