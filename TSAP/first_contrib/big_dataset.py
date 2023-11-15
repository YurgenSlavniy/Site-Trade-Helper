import pandas as pd

# загружаю последний скаченный датасет
df_last = pd.read_csv('trade-history-2022-06-09.csv')
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

# объединение 2 ух датасетов
# big_df = pd.concat([df_last, df_first], ignore_index=True)

import pandas as pd

# загружаю последний скаченный датасет
df_last = pd.read_csv('trade-history-2022-06-09.csv')
# загружаю самый ранний скаченный датасет
df_first = pd.read_csv('trade-history-2021-11-07.csv')

big_df = pd.concat([df_last, df_first], ignore_index=True)
big_df_uniq = big_df.drop_duplicates()
big_df_uniq['Дата/время'] = pd.to_datetime(df_last['Дата/время'])

print(len(big_df), len(big_df_uniq))
