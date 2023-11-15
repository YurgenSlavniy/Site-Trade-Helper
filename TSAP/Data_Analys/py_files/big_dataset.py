import pandas as pd
import datetime

# переформатирование колонки время сделки в дататайм
def to_datetime(dataframe):
    dataframe['Дата/время'] = pd.to_datetime(dataframe['Дата/время'], format='%d.%m.%Y %H:%M')
    return dataframe

# Объединение датасетов
def big_dataset(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True)
    big_df_uniq = big_df.drop_duplicates()
    # что то сделать с индексами, т. к после дубликата их значения сбиваются
    return big_df_uniq


# Анализ  датасета
def data_analys(dataframe):
    print('*' * 33)
    all_dates = dataframe['Дата/время'].tolist()
    start = all_dates[-1]
    end = all_dates[0]
    start_dtm = datetime.datetime.strptime(start, '%d.%m.%Y %H:%M')
    end_dtm = datetime.datetime.strptime(end, '%d.%m.%Y %H:%M')
    print(f'размер датасета: {len(dataframe)} строк записей\n'
          f'начало сбора данных: {start_dtm}\n'
          f'конец сбора данных: {end_dtm}')
    print('*' * 33)

# Проверка при объединении датасетов на дубликаты
def duplicates(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True).drop_duplicates()
    if len(big_df) == len(dataframe_first) + len(dataframe_last):
        print('Полное объединение датасетов. Дубликатов нет.')
    else:
        print('Число дубликатов:', len(dataframe_first) + len(dataframe_last) - len(big_df))



# загружаю последний скаченный датасет
df_last = pd.read_csv('trade-history-2023-05-06.csv')
# загружаю самый ранний скаченный датасет
df_first = pd.read_csv('trade-history-2021-11-07.csv')




# форматирую колонку время и перевожу её в формат datetime в загруженных датасетах
df_last['Дата/время'] = pd.to_datetime(df_last['Дата/время'])
df_first['Дата/время'] = pd.to_datetime(df_first['Дата/время'])
all_dates_last = df_last['Дата/время'].tolist()
start_last = all_dates_last[-1]
end_last = all_dates_last[0]

all_dates_first = df_first['Дата/время'].tolist()
start_first = all_dates_first[-1]
end_first = all_dates_first[0]




if start_first > end_last:
    print('начало последнего датасета позже конца первого', end_last - start_first )
    big_df = pd.concat([df_last, df_first], ignore_index=True)
else:
    print('значения пересекаются')
    indx = all_dates_last.index(end_first)

    print('самая последняя сделка', df_last['Дата/время'].iloc[0])
    print('самая первая сделка в позднем датасете', df_last['Дата/время'].iloc[-1])
    print('самая последняя сделка в раннем датасете', df_first['Дата/время'].iloc[0])
    print('самая ранняя сделка', df_first['Дата/время'].iloc[-1])
    print(df_first['Дата/время'].iloc[indx])
