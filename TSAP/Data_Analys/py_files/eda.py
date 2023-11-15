#  Визуализация и анализ данных.

# для анализа возьму конкретную торговую пару в которой было совершено больше всего сделок
# EXM_RUB

# EDA
# Загрузка данных
# 1. Распределение целевой переменной
# 2. Анализ признаков
# 2.1 Количественные признаки
# 2.2 Категориальные признаки
# 2.3 Бинарные признаки
# 2.4 Матрица корреляций
# 3. Анализ зависимости таргета от фичей
# 3.1 Количественные признаки
# 3.2 Категориальные / бинарные признаки

# EDA - Exploratory Data Analysis
# _________________________________________________

# ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ:

import numpy as np
import pandas as pd

import matplotlib
import matplotlib.image as img
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

import warnings
warnings.filterwarnings('ignore')
# _________________________________________________

# ФУНКЦИИ:

# Объединение таблиц
def big_dataset(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True)
    big_df_uniq = big_df.drop_duplicates()
    return big_df_uniq
# _________________________________________________

# ЗАГРУЗКА ДАННЫХ

df = pd.read_csv('trade-history-2022-06-27.csv')
df_first = pd.read_csv('trade-history-2021-11-07.csv')

df_all_dates = big_dataset(df, df_first)
# из общего датасета делаю выборку по валютной паре
df_exm_rub = df_all_dates.loc[(df_all_dates['Валютная пара'] == 'EXM_RUB')]
# _________________________________________________

# Описание датасета
df_exm_rub.info()

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 2447 entries, 79 to 19231
# Data columns (total 10 columns):
#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   Дата/время       2447 non-null   object - дата и время сделки
#  1   Trade ID         2447 non-null   int64  - ай ди делки
#  2   Тип              2447 non-null   object - тип сделки (buy/sell)
#  3   Валютная пара    2447 non-null   object - название валютной пары
#  4   Количество       2447 non-null   float64 - количество купленной валюты
#  5   Цена             2447 non-null   float64 - цена по которой куплена валюта
#  6   Сумма            2447 non-null   float64 - сумма потраченная на покупку валюты
#  7   Тип комиссии     2447 non-null   object - тип комиссии (maker/taker)
#  8   Размер комиссии  2447 non-null   float64 - сумма уплаченной комиссии
#  9   Комиссия %       2447 non-null   object - процентная ставка комиссии
# dtypes: float64(4), int64(1), object(5)
# memory usage: 210.3+ KB
# _________________________________________________

# 1) РАСПРЕДЕЛЕНИЕ ЦЕЛЕВОЙ ПЕРЕМЕННОЙ:

# целевая переменная - "Цена".

# Помните про различие среднего арифметическое, медианы, моды
# Среднее арифметическое (мат ожидание) подходят для нормальных распределений = SUM / N
# Медиана (quantile 50%) - практически для любых распределений = Середина отранжированного ряда
# Мода - для категориальных переменных = наиболее часто встречающееся значение в выборке

target_mean = round(df_exm_rub['Цена'].mean(), 2)
target_median = df_exm_rub['Цена'].median()
target_mode = df_exm_rub['Цена'].mode()[0]
target_max = df_exm_rub['Цена'].max()
target_min = df_exm_rub['Цена'].min()

print(target_mean, target_median, target_mode, target_max, target_min)

plt.figure(figsize = (16, 8))

sns.distplot(df_exm_rub['Цена'], bins=50)

y = np.linspace(0, 0.000005, 10)
plt.plot([target_mean] * 10, y, label='?',  linewidth=4)
plt.plot([target_median] * 10, y, label='?',  linewidth=4)
plt.plot([target_mode] * 10, y, label='?', linewidth=4)
plt.plot([target_max] * 10, y, label='?', linewidth=4)
plt.plot([target_min] * 10, y, label='?', linewidth=4)

plt.title('Distribution of median_house_value')
plt.legend()
plt.show()