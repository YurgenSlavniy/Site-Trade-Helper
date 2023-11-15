import numpy as np
import pandas as pd
import datetime
from scipy import stats

from scipy.stats import shapiro
from scipy.stats import probplot
from scipy.stats import ttest_ind, mannwhitneyu
from scipy.stats import chi2_contingency
# from statsmodels.stats.weightstats import zconfint

import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.simplefilter('ignore')

# бъединение датасетов
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


###############################
order = {'buy_price': 1,
         'sell_price': 2
         }

# загрузка датасетов
df = pd.read_csv('trade-history-2022-09-06.csv')
df_first = pd.read_csv('trade-history-2021-11-07.csv')
# объединение датасетов
df_all_dates = big_dataset(df, df_first)
# получаю данные по интересующей валютной паре
current_pair_dataset = df_all_dates.loc[(df_all_dates['Валютная пара'] == 'EXM_BTC')]
current_pair_dataset_buy = current_pair_dataset.loc[(current_pair_dataset['Тип'] == 'buy')]
current_pair_dataset_sell = current_pair_dataset.loc[(current_pair_dataset['Тип'] == 'sell')]

time_period(current_pair_dataset)
print(f'Число сделок:{len(current_pair_dataset)}\n'
      f'buy: {len(current_pair_dataset_buy)}\n'
      f'sell: {len(current_pair_dataset_sell)}')
price_min(current_pair_dataset_buy)
price_max(current_pair_dataset_sell)
max_summ(current_pair_dataset_buy)
max_value(current_pair_dataset)
value_all_buy(current_pair_dataset_buy)
value_all_sell(current_pair_dataset_sell)
sum_all_buy(current_pair_dataset_buy)
sum_all_sell(current_pair_dataset_sell)
delta(current_pair_dataset_sell)


# какой объём информации можем рассказать пользователю?

# какова была максимальная цена.
# когда была максимальная цена.
# какова была минимальная цена.
# когда была минимальная цена цена.

