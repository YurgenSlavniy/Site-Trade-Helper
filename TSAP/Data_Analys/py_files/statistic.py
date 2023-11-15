import pandas as pd

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

# загрузка датасетов
df_last = pd.read_csv('trade-history-2022-06-27.csv')
df_first = pd.read_csv('trade-history-2021-11-07.csv')

# объединение датасетов
df_all_dates = big_dataset(df_last, df_first)

# датасет по конкретной торговой паре. Выборка из объединёного датасета
current_pair_dataset = df_all_dates.loc[(df_all_dates['Валютная пара'] == 'XTZ_RUB')]

current_pair_dataset.info()
### СТАТИСТИКА ###

# Меры центральной тенденции
# Мода (mode) – значение измеряемого признака, которое встречается максимально часто. Мод может быть несколько.
print('\nМОДА:')

import pandas as pd
print('цена:', current_pair_dataset.Цена.mode()) # pandas way
print('Количество:', current_pair_dataset.Количество.mode())
print('Сумма:', current_pair_dataset.Сумма.mode())

from scipy import stats
print('цена:', stats.mode(current_pair_dataset.Цена))  # scipy way
print('Количество:', stats.mode(current_pair_dataset.Количество))  # scipy way
print('Сумма:', stats.mode(current_pair_dataset.Сумма))  # scipy way

# Медиана (median) – значение признака, которое делит упорядоченное множество данных пополам.
# Берем множество значений признака, сортируем и берем центральное значение
print('\nМЕДИАНА:')
print('цена:', current_pair_dataset.Цена.median()) # pandas way
print('Количество:', current_pair_dataset.Количество.median())
print('Сумма:', current_pair_dataset.Сумма.median())

import numpy as np
print('цена:', np.median(current_pair_dataset.Цена))  # numpy way
print('Количество:', np.median(current_pair_dataset.Количество))
print('Сумма:', np.median(current_pair_dataset.Сумма))

# Среднее (mean, среднее арифметическое) –
# сумма всех значений измеренного признака, деленная на количество измеренных значений.
print('\nСРЕДНЕЕ:')
print('цена:', current_pair_dataset.Цена.mean()) # pandas way
print('Количество:', current_pair_dataset.Количество.mean())
print('Сумма:', current_pair_dataset.Сумма.mean())

print('цена:', np.mean(current_pair_dataset.Цена))  # numpy way
print('Количество:', np.mean(current_pair_dataset.Количество))
print('Сумма:', np.mean(current_pair_dataset.Сумма))

# Максимальное значение в столбце
print('\nМАКСИМУМ:')
print('цена:', current_pair_dataset.Цена.max()) # pandas way
print('Количество:', current_pair_dataset.Количество.max())
print('Сумма:', current_pair_dataset.Сумма.max())

print('цена:', np.max(current_pair_dataset.Цена))  # numpy way
print('Количество:', np.max(current_pair_dataset.Количество))
print('Сумма:', np.max(current_pair_dataset.Сумма))

# Минимальное значение в столбце
print('\nМИНИМУМ:')
print('цена:', current_pair_dataset.Цена.min()) # pandas way
print('Количество:', current_pair_dataset.Количество.min())
print('Сумма:', current_pair_dataset.Сумма.min())

print('цена:', np.min(current_pair_dataset.Цена))  # numpy way
print('Количество:', np.min(current_pair_dataset.Количество))
print('Сумма:', np.min(current_pair_dataset.Сумма))
