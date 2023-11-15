# ПОСТАНОВКА ЗАДАЧИ:

# У нас есть три файла формата .csv c моей историей торгов на бирже ексмо.
# Необходимо объединить эти данные в одну таблицу.
# На основании этой таблицы я хочу знать:

# + 1) Сколько всего сделок я совершил за всю историю торгов? шт.
# + 2) Сколько из них Бай сделки, сколько селл сделки?
# + 3) За какой период данных я имею информацию?
# + 4) Количество сделок по месяцам?
# + 5) В скольки торговых парах велась торговля?
# 6) Для каждой торговой пары просчитать объёмы торгов: сколько купленно, на какую сумму купленно, также с проданно.
# сколько продано? На какую сумму продано?
# + 7) Число сделок в каждой валютной паре

# Продумать как это будет выглядить на выходе.


import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint

df = pd.read_csv('trade-history-2021-11-07.csv')
df1 = pd.read_csv('trade-history-2022-10-10.csv')
df2 = pd.read_csv('trade-history-2023-06-02.csv')

# Функция, объединяющая датасеты.
def big_dataset(dataframe_first, dataframe_last):
    return pd.concat([dataframe_first, dataframe_last], ignore_index=True).drop_duplicates()


# Применение функции и создание объединёного датасета big_df.
df_first = pd.read_csv('trade-history-2021-11-07.csv')
df_middle = pd.read_csv('trade-history-2022-10-10.csv')
df_last = pd.read_csv('trade-history-2023-06-02.csv')

big_df_1 = pd.concat([df_middle, df_first], ignore_index=True).drop_duplicates()
print(len(df_first), len(df_middle), len(df_last), len(big_df_1))

big_df = pd.concat([df_last, big_df_1], ignore_index=True).drop_duplicates()
print(len(df_first), len(df_middle), len(df_last), len(big_df_1), len(big_df))

# Определение даты самой ранней сделки и самой последней сделки. Подсчёт временного периода торговли
def time_period(dataframe):
    all_dates = dataframe['Дата/время'].tolist()
    start = all_dates[-1]
    end = all_dates[0]
    start_dtm = datetime.datetime.strptime(start, '%d.%m.%Y %H:%M')
    end_dtm = datetime.datetime.strptime(end, '%d.%m.%Y %H:%M')
    print(f'\nПроизведён анализ временного периода торговли: с {start} по {end}'
            f'\nчто составляет {end_dtm - start_dtm}')


# Прогорняю через функцию, имеющиеся датафреймы.
time_period(df)
time_period(df1)
time_period(df2)
time_period(big_df_1)
time_period(big_df)

# Вывод названий всех торговых пар в которых велась торговля и показывает число сделок в каждой торговой паре
def all_pairs_count(dataframe):
    return dataframe['Валютная пара'].value_counts()

# Общее число отторговавшихся ордеров
print(f'ОБЩЕЕ ЧИСЛО ОТТОРГОВАВШИХСЯ ОРДЕРОВ: {len(big_df)}')

# Число BUY и SELL ордеров
def buy_sell_count(dataframe):
    return dataframe['Тип'].value_counts()

# Пользуясь функцией вывожу информацию о числе BUY и SELL ордеров
print(buy_sell_count(big_df))

# Визуализация данных по Buy и Sell
def visual_buy_sell(dataframe):
    plt.figure(figsize=(8, 5))

    sns.countplot(x='Тип', data=dataframe)
    plt.title('Target variable distribution')
    plt.show()

# Прогорняю через функцию самый большой объединёный датафрейм и вывожу число валютных пар и сделок
print(f'ЧИСЛО ВАЛЮТНЫХ ПАР В КОТОРЫХ СОВЕРШАЛИСЬ СДЕЛКИ:{len(all_pairs_count(big_df))} \nЧИСЛО СДЕЛОК В КАЖДОЙ ВАЛЮТНОЙ ПАРЕ:\n ' , all_pairs_count(big_df))

# Датасет по валютной паре
def df_curr_pair(dataframe, current_pair):
    current = str(current_pair.upper())
    df_curpair = dataframe.loc[(dataframe['Валютная пара'] == current)]
    return df_curpair

# Число сделок в день, сортировка по дате
from collections import Counter

def per_day_date(dataframe):
    new_vals = []
    vals = dataframe['Дата/время'].values
    for el in vals:
        numb = el[0:2]
        new_vals.append(numb)
    count = Counter(new_vals)

    return dict(sorted(count.items()))

# Датасеты сортированные

df_2021 = big_df[big_df['Дата/время'].str.contains("2021")]
df_2022 = big_df[big_df['Дата/время'].str.contains("2022")]
df_2023 = big_df[big_df['Дата/время'].str.contains("2023")]

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


time_period(df_may_2023)
print(f'ОБЩЕЕ ЧИСЛО ОТТОРГОВАВШИХСЯ ОРДЕРОВ: {len(df_may_2023)}')
print(f'ЧИСЛО ВАЛЮТНЫХ ПАР В КОТОРЫХ СОВЕРШАЛИСЬ СДЕЛКИ:{len(all_pairs_count(df_may_2023))} \nЧИСЛО СДЕЛОК В КАЖДОЙ ВАЛЮТНОЙ ПАРЕ:\n ' , all_pairs_count(df_may_2023))
print(buy_sell_count(df_may_2023))
pprint(per_day_date(df_may_2023))

# Количество сделок по месяцам
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

# аналитика торговли (применять к одной торговой паре)
# Список торговых пар, которые будут прогоняться через определённую статистику.
# После общей статистики идёт статистика по парам.  На вход функция будет принимать датафрейм и выдавать текстовую статистику - интерпритацию.

def all_pairs_list(dataframe):
    return dataframe['Валютная пара'].unique().tolist()

# Сортировка по валютной паре
def df_curr_pair(dataframe, current_pair):
    current = str(current_pair.upper())
    df_curpair = dataframe.loc[(dataframe['Валютная пара'] == current)]
    return df_curpair

# Функция разбивает валюты в торговой паре
def currents(current_pair):
    pair_list = current_pair.split('_')
    return pair_list

# аналитика торговли (применять к одной торговой паре)
def analitica(dataframe, current_pair):
    current_pair_dataset = df_curr_pair(dataframe, current_pair)
    current_pair_dataset_buy = current_pair_dataset.loc[(current_pair_dataset['Тип'] == 'buy')]
    current_pair_dataset_sell = current_pair_dataset.loc[(current_pair_dataset['Тип'] == 'sell')]
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



# Вывод временного периода
print('*' * 100)
time_period(df_may_2023)
# Вывод всех валютных пар где были сделки с числом сделок
print(all_pairs_count(df_may_2023))

# Для каждой валютной паре выводим период торгов за который велось наблюдение
for el in all_pairs_list(df_may_2023):
    print('\n' + el)
    print(f'ОБЩЕЕ ЧИСЛО ОТТОРГОВАВШИХСЯ ОРДЕРОВ: {len(df_curr_pair(df_may_2023, el))}')
    print(buy_sell_count(df_curr_pair(df_may_2023, el)))
    analitica(df_may_2023, el)