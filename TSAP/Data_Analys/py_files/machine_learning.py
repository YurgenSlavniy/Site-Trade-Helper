import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import datetime
import warnings
if not sys.warnoptions:
       warnings.simplefilter("ignore")

def big_dataset(dataframe_first, dataframe_last):
    big_df = pd.concat([dataframe_first, dataframe_last], ignore_index=True)
    big_df_uniq = big_df.drop_duplicates()
    return big_df_uniq

def trades_count_pair(dataframe):
    print(f'\nОбщее число сделок в торговой паре за проанализированный период времени: {len(dataframe)} из них')
    print('BUY сделки:', len(dataframe.loc[(dataframe['Тип'] == 'buy')]))
    print('SELL сделки:', len(dataframe.loc[(dataframe['Тип'] == 'sell')]))

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
current_pair_dataset = df_all_dates.loc[(df_all_dates['Валютная пара'] == 'EXM_RUB')]


# Посмотрим на баланс классов колонки Тип. У нас есть 2 класса тип сделки (buy/sell)
time_period(current_pair_dataset)
trades_count_pair(current_pair_dataset)

# Посчитаем соотношения классов.

# class count
class_count_buy, class_count_sell = current_pair_dataset['Тип'].value_counts()
# Separate class
class_0 = current_pair_dataset[current_pair_dataset['Тип'] == 'buy']
class_1 = current_pair_dataset[current_pair_dataset['Тип'] == 'sell']
# print the shape of the class
print('class 0: (buy):', class_0.shape)
print('class 1: (sell):', class_1.shape)
print(f'Посчитаем соотношения классов. И получим '
      f'\nclass 0: {class_0.shape}, '
      f'\nclass 1: {class_1.shape}. '
      f'\nНаш дисбаланс классов {len(class_0)} к {len(class_1)}. '
      f'\nЧто составляет: {len(class_0)/len(class_1)}'
      f'\nПреобладания нецелевого классса у нас нет.' )

g = sns.countplot(current_pair_dataset['Тип'])
g.set_xticklabels(['buy','sell'])
plt.show()

# Задача классификации
# Имеется множество объектов (ситуаций), разделённых некоторым образом на классы.
# Для некоторых объектов из этого множества известна их классовая принадлежность -
# это подмножество называется обучающей выборкой.
# Классовая принадлежность остальных объектов не известна.
# Требуется построить алгоритм,
# способный классифицировать произвольный объект из исходного множества.
#
# Классифицировать объект — значит, указать номер (или наименование класса),
# к которому относится данный объект.
#
# Классификация объекта — номер или наименование класса,
# выдаваемый алгоритмом классификации в результате его применения к данному конкретному объекту.

# Бинарная классификация
#
# Данные разделены на два класса,
# необходимо обучить модель определять принадлежность произвольного объекта
# (из рассматриваемого множества) к одному из них.
# На выходе алгоритм должен выдавать либо метку одного из двух классов,
# либо вероятности принадлежности рассматриваемого объекта к каждому из них.


# ПОСТАНОВКА ЗАДАЧИ:
# Требуется на основании истории торгов
# предсказать тип сделки (buy, sell).

# ОПИСАНИЕ ДАТАСЕТА:
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

# наша целевая переменная 'Тип'.
# Таблица с признаками вс остальное.
# Целевой класс - сделки продажи sell  1=да.
# Класс 1 - сделки по продаже валюты
# Класс 0 - сделки по покупке валюты

# импортируем библилтеки, которые нам понадобятся и с которыми будем работать
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Пути к директориям и файлам:
# input
DATASET_PATH = 'EXM_RUB.csv'
# output
PREP_DATASET_PATH = 'current_pair_prep.csv'



exm_rub_df = current_pair_dataset
# Общие данные о датасете. Видим, что пропусков у нас нет.

# Приведение типов :
#  0   Дата/время       2447 non-null   object - дата и время сделки
# колонка с датой и временем имеет формат строковый. Нужно ли перевести к дататайму?
exm_rub_df['Дата/время'] = pd.to_datetime(exm_rub_df['Дата/время'])

# Обзор данных
# Обзор целевой переменной
# посмотрим соотношение классов, чтобы выявить есть ли у нас проблема дисбаланса классов.

# Обзор количественных признаков
# посмотрим характеристики колличественных признаков.
# нет заведомо нереалестичных значений. По числовым признакам всё выглядит вполне себе неплохо.

# Обзор номинативных признаков
# смотрим теперь на значения категориальных (номинативных) признаков
# Для этого мы сначала создали список из категориальных признаков cat_colname.
# Tо есть мы перебираем все признаки из них нас интересуют признаки типа include='object',
# если мы находим такой признак то для этого признака выводим на экран сообщение.
# Название признака (колонки): str(cat_colname),
# str(df[cat_colname].value_counts()) - подсчёт сколько каких уникальных значений у нас имеется,
# '*' * 100 - выводим 100 звёздочек
for cat_colname in exm_rub_df.select_dtypes(include='object').columns:
    print(str(cat_colname) + '\n\n' + str(exm_rub_df[cat_colname].value_counts()) + '\n' + '*' * 100 + '\n')

# мы имеем у признака пола 'Тип' 2 значения: BUY, SELL 2 .
# 'Валютная пара' 1 значение
# 'Тип комиссии' 2 значения: maker, taker
# 'Комиссия %' 1 значение

# ОБРАБОТКА ПРОПУСКОВ
# пропуски отсутствуют
# проверим остались ли у нас NaN значения. количество попусков = 0, пропусков нет.
len(exm_rub_df) - exm_rub_df.count()

# ОБРАБОТКА ВЫБРОСОВ
# Смотрим на выбросы наших числовых признаков.
# Видим выбросы только сверху. (всё что находится выше верхнего уса, эти кружочки)
plt.boxplot(exm_rub_df['Количество'])
plt.title('Анализ выбросов для признака Количество')
plt.boxplot(exm_rub_df['Сумма'])
plt.title('Анализ выбросов для признака Сумма')
plt.boxplot(exm_rub_df['Цена'])
plt.title('Анализ выбросов для признака Цена')

# Построение новых признаков
# Id
# задаём новую колонку 'ID', которая представляет собой индексы.
exm_rub_df['ID'] = exm_rub_df.index.tolist()

# Dummies
# делаем кодировку категориальных признаков.
# В признаке пол 'Тип' переходим от кодировки Buy, sell к кодировке 0, 1.
# Все категориальные переменные переводим в дамми переменные.

exm_rub_df['type'] = exm_rub_df['Тип'].map({'sell':'1', 'buy':'0'}).astype(int)
exm_rub_df['comission_type'] = exm_rub_df['Тип комиссии'].map({'maker':'1', 'taker':'0'}).astype(int)

for cat_colname in exm_rub_df.select_dtypes(include='object').columns[1:]:
    exm_rub_df_prep = pd.concat([exm_rub_df, pd.get_dummies(exm_rub_df[cat_colname], prefix=cat_colname)], axis=1)


# колонки Тип, Валютная пара, Trade ID, комиссия % - эти три колонки не несут информационной нагрузки.
# Считаю возможным их удалить
exm_rub_df_prep = exm_rub_df_prep.drop(['Тип', 'Валютная пара', 'Trade ID', 'Тип комиссии', 'Комиссия %', 'Комиссия %_0.3%'], axis=1)
exm_rub_df_prep.info()
print(exm_rub_df_prep.head(3))

# сохранение датасетов
# current_pair_dataset.to_csv(PREP_DATASET_PATH, index=False, encoding='utf-8')
exm_rub_df_prep.to_csv('exm_rup_prep.csv', index=False, encoding='utf-8')

#  Что такое статистическая гипотеза?

# Статистическая гипотеза - предположение о виде распределения и свойствах случайной величины,
# которое можно подтвердить или опровергнуть применением статистических методов к данным выборки.
#
# Нулевая гипотеза - некоторое, принимаемое по-умолчанию предположение,
# о том, что не существует связи между двумя наблюдаемыми событиями,
# отклонения показателей и других неожиданных результатов, словом нет никакого эффекта.
#
# Альтернативная гипотеза - в качестве альтернативы, как правило, выступает проверяемое предположение,
# но также бывает, что альтернатива не задана явно,
# в этом случаем рассматривают отрицание утверждение, заданного в нулевой гипотезе.
#
# Проверка статистической гипотезы - это процесс принятия решения о том,
# противоречит ли рассматриваемая статистическая гипотеза наблюдаемой выборке данных.
#
# Статистический тест или статистический критерий - строгое математическое правило,
# по которому принимается или отвергается статистическая гипотеза.

# Выделение целевой переменной и групп признаков
TARGET_NAME = 'Тип'
BASE_FEATURE_NAMES = exm_rub_df.columns.drop(TARGET_NAME).tolist()
NEW_FEATURE_NAMES = exm_rub_df_prep.columns.drop([TARGET_NAME] + BASE_FEATURE_NAMES)

# Анализ целевой переменной
# Обзор распределения
exm_rub_df_prep[TARGET_NAME].value_counts()

