import pandas as pd
import numpy as np
import datetime



# Объединение датасетов
df_first = pd.read_csv('trade-history-2021-11-07.csv')
df_middle = pd.read_csv('trade-history-2022-10-10.csv')
df_last = pd.read_csv('trade-history-2023-08-01.csv')

big_df = pd.concat([df_last, pd.concat([df_middle, df_first], ignore_index=True).drop_duplicates()], ignore_index=True).drop_duplicates()

df_all_dates = big_df

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
df_oct_2022 = df_2022[df_2022['Дата/время'].str.contains(".10.2022")]
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



# Считаем временой период торговли
def time_period(dataframe):
    all_dates = dataframe['Дата/время'].tolist()
    start = all_dates[-1]
    end = all_dates[0]
    start_dtm = datetime.datetime.strptime(start, '%d.%m.%Y %H:%M')
    end_dtm = datetime.datetime.strptime(end, '%d.%m.%Y %H:%M')
    print(f'\nПроизведён анализ временного периода торговли: с {start} по {end}'
          f'\nчто составляет {end_dtm - start_dtm} \n')

# Считаем число сделок и сколько из них buy сколько sell
def buy_sell_count(dataframe):
	print(f"Общее число сделок: {len(dataframe)}, из них \n"
		  f"BUY: {len(dataframe[dataframe['Тип'] == 'buy'])} \n"
		  f"SELL: {len(dataframe[dataframe['Тип'] == 'sell'])} \n")

# список всех валютных пар 
def all_pairs_list(dataframe):
    return dataframe['Валютная пара'].unique().tolist()

# Список валют которыми велась торговля
def currents(pair_list):
    currents_list = []
    for el in pair_list:
        curs = el.split('_')
        for el in curs:
            currents_list.append(el)
    return set(currents_list)

# число сделок в каждой валютной паре
def all_pairs_count(dataframe):
    return dataframe['Валютная пара'].value_counts()


# выводим информацию по числу торговых пар
def all_pairs_info(dataframe):
	cur_pairs = dataframe['Валютная пара'].unique().tolist()
	curs = currents(all_pairs_list(dataframe))

	print(f'Число торговых пар в которых велась торговля: {len(cur_pairs)} \n'  
	      f'Число валют в которых велась торговля: {len(curs)} \n'
	      f'Список валют в которых велась торговля: {curs}  \n')

	print(cur_buy_sell_all_df(dataframe))



################################################################################
# Датасет по валютной паре 
def df_curr_pair(dataframe, current_pair):
    current = str(current_pair.upper())
    return dataframe.loc[(dataframe['Валютная пара'] == current)]

# Список датасетов по каждой валютной паре
def dataframe_pairs_list(dataframe):
	all_pairs_list = dataframe['Валютная пара'].unique().tolist()	
	dataframe_all_pairs_list = []
	for el in all_pairs_list:
		dataframe_all_pairs_list.append(df_curr_pair(dataframe, el))
	return dataframe_all_pairs_list

# Первичный сводный датасет с:
# - названием валютной пары
# - общее число сделок
# - число BUY сделок
# - число SELL сделок

def buy_sell_all_count(solodataframe):
	cur_pair = solodataframe['Валютная пара'].unique()[0]
	all_count = len(solodataframe)
	buy_count = 0
	sell_count = 0

	a = solodataframe['Тип'].value_counts()


	if len(a) == 2:
		buy_count = len(solodataframe[solodataframe['Тип'] == 'buy'])
		sell_count = len(solodataframe[solodataframe['Тип'] == 'sell'])

	else:
		if str(solodataframe['Тип']) == 'buy':
			buy_count = len(solodataframe)
		else:
			sell_count = len(solodataframe)

	return(cur_pair, all_count, buy_count, sell_count)


def cur_buy_sell_all_df(dataframe):
	pair_list = []
	trade_counts_list = []
	buy_count_list = []
	sell_count_list = []

	for el in dataframe_pairs_list(dataframe):	

		solodata = buy_sell_all_count(el)

		pair_list.append(solodata[0])
		trade_counts_list.append(solodata[1])
		buy_count_list.append(solodata[2])
		sell_count_list.append(solodata[3])

		cur_all_buy_sell_df = pd.DataFrame({'cur_pair' : pair_list,
                          'trd_count' : trade_counts_list,
                          'sell_count': sell_count_list,
                          'buy_count': buy_count_list
                         },
                           columns=['cur_pair','trd_count', 'sell_count', 'buy_count'])
	return cur_all_buy_sell_df

def months(big_df):
	df_all_dates = big_df

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
	df_oct_2022 = df_2022[df_2022['Дата/время'].str.contains(".10.2022")]
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


	print(f'\nСделки за 2021 год. Общее количество: {len(df_2021)}, BUY: {len(df_2021[df_2021["Тип"] == "buy"])}, SELL: {len(df_2021[df_2021["Тип"] == "sell"])}'
      f'\nЯнварь 2021: {len(df_jan_2021)}, BUY: {len(df_jan_2021[df_jan_2021["Тип"] == "buy"])}, SELL: {len(df_jan_2021[df_jan_2021["Тип"] == "sell"])}'
      f'\nФевраль 2021: {len(df_feb_2021)}, BUY: {len(df_feb_2021[df_feb_2021["Тип"] == "buy"])}, SELL: {len(df_feb_2021[df_feb_2021["Тип"] == "sell"])}'
      f'\nМарт 2021: {len(df_mar_2021)}, BUY: {len(df_mar_2021[df_mar_2021["Тип"] == "buy"])}, SELL: {len(df_mar_2021[df_mar_2021["Тип"] == "sell"])}'
      f'\nАпрель 2021: {len(df_apr_2021)}, BUY: {len(df_apr_2021[df_apr_2021["Тип"] == "buy"])}, SELL: {len(df_apr_2021[df_apr_2021["Тип"] == "sell"])}'
      f'\nМай 2021: {len(df_may_2021)}, BUY: {len(df_may_2021[df_may_2021["Тип"] == "buy"])}, SELL: {len(df_may_2021[df_may_2021["Тип"] == "sell"])}'
      f'\nИюнь 2021: {len(df_jun_2021)}, BUY: {len(df_jun_2021[df_jun_2021["Тип"] == "buy"])}, SELL: {len(df_jun_2021[df_jun_2021["Тип"] == "sell"])}'
      f'\nИюль 2021: {len(df_jun_2021)}, BUY: {len(df_jul_2021[df_jul_2021["Тип"] == "buy"])}, SELL: {len(df_jul_2021[df_jul_2021["Тип"] == "sell"])}'
      f'\nАвгуст 2021: {len(df_avg_2021)}, BUY: {len(df_avg_2021[df_avg_2021["Тип"] == "buy"])}, SELL: {len(df_avg_2021[df_avg_2021["Тип"] == "sell"])}'
      f'\nСентябрь 2021: {len(df_sep_2021)}, BUY: {len(df_sep_2021[df_sep_2021["Тип"] == "buy"])}, SELL: {len(df_sep_2021[df_sep_2021["Тип"] == "sell"])}'
      f'\nОктябрь 2021: {len(df_oct_2021)}, BUY: {len(df_oct_2021[df_oct_2021["Тип"] == "buy"])}, SELL: {len(df_oct_2021[df_oct_2021["Тип"] == "sell"])}'
      f'\nНоябрь 2021: {len(df_nov_2021)}, BUY: {len(df_nov_2021[df_nov_2021["Тип"] == "buy"])}, SELL: {len(df_nov_2021[df_nov_2021["Тип"] == "sell"])}'
      f'\nДекабрь 2021: {len(df_dec_2021)}, BUY: {len(df_dec_2021[df_dec_2021["Тип"] == "buy"])}, SELL: {len(df_dec_2021[df_dec_2021["Тип"] == "sell"])}')

	print(f'\nСделки за 2022 год. Общее количество: {len(df_2022)}, BUY: {len(df_2022[df_2022["Тип"] == "buy"])}, SELL: {len(df_2022[df_2022["Тип"] == "sell"])}'
      f'\nЯнварь 2022: {len(df_jan_2022)}, BUY: {len(df_jan_2022[df_jan_2022["Тип"] == "buy"])}, SELL: {len(df_jan_2022[df_jan_2022["Тип"] == "sell"])}'
      f'\nФевраль 2022: {len(df_feb_2022)}, BUY: {len(df_feb_2022[df_feb_2022["Тип"] == "buy"])}, SELL: {len(df_feb_2022[df_feb_2022["Тип"] == "sell"])}'
      f'\nМарт 2022: {len(df_mar_2022)}, BUY: {len(df_mar_2022[df_mar_2022["Тип"] == "buy"])}, SELL: {len(df_mar_2022[df_mar_2022["Тип"] == "sell"])}'
      f'\nАпрель 2022: {len(df_apr_2022)}, BUY: {len(df_apr_2022[df_apr_2022["Тип"] == "buy"])}, SELL: {len(df_apr_2022[df_apr_2022["Тип"] == "sell"])}'
      f'\nМай 2022: {len(df_may_2022)}, BUY: {len(df_may_2022[df_may_2022["Тип"] == "buy"])}, SELL: {len(df_may_2022[df_may_2022["Тип"] == "sell"])}'
      f'\nИюнь 2022: {len(df_jun_2022)}, BUY: {len(df_jun_2022[df_jun_2022["Тип"] == "buy"])}, SELL: {len(df_jun_2022[df_jun_2022["Тип"] == "sell"])}'
      f'\nИюль 2022: {len(df_jun_2022)}, BUY: {len(df_jul_2022[df_jul_2022["Тип"] == "buy"])}, SELL: {len(df_jul_2022[df_jul_2022["Тип"] == "sell"])}'
      f'\nАвгуст 2022: {len(df_avg_2022)}, BUY: {len(df_avg_2022[df_avg_2022["Тип"] == "buy"])}, SELL: {len(df_avg_2022[df_avg_2022["Тип"] == "sell"])}'
      f'\nСентябрь 2022: {len(df_sep_2022)}, BUY: {len(df_sep_2022[df_sep_2022["Тип"] == "buy"])}, SELL: {len(df_sep_2022[df_sep_2022["Тип"] == "sell"])}'
      f'\nОктябрь 2022: {len(df_oct_2022)}, BUY: {len(df_oct_2022[df_oct_2022["Тип"] == "buy"])}, SELL: {len(df_oct_2022[df_oct_2022["Тип"] == "sell"])}'
      f'\nНоябрь 2022: {len(df_nov_2022)}, BUY: {len(df_nov_2022[df_nov_2022["Тип"] == "buy"])}, SELL: {len(df_nov_2022[df_nov_2022["Тип"] == "sell"])}'
      f'\nДекабрь 2022: {len(df_dec_2022)}, BUY: {len(df_dec_2022[df_dec_2022["Тип"] == "buy"])}, SELL: {len(df_dec_2022[df_dec_2022["Тип"] == "sell"])}')

	print(f'\nСделки за 2023 год. Общее количество: {len(df_2023)}, BUY: {len(df_2023[df_2023["Тип"] == "buy"])}, SELL: {len(df_2023[df_2023["Тип"] == "sell"])}'
      f'\nЯнварь 2023: {len(df_jan_2023)}, BUY: {len(df_jan_2023[df_jan_2023["Тип"] == "buy"])}, SELL: {len(df_jan_2023[df_jan_2023["Тип"] == "sell"])}'
      f'\nФевраль 2023: {len(df_feb_2023)}, BUY: {len(df_feb_2023[df_feb_2023["Тип"] == "buy"])}, SELL: {len(df_feb_2023[df_feb_2023["Тип"] == "sell"])}'
      f'\nМарт 2023: {len(df_mar_2023)}, BUY: {len(df_mar_2023[df_mar_2023["Тип"] == "buy"])}, SELL: {len(df_mar_2023[df_mar_2023["Тип"] == "sell"])}'
      f'\nАпрель 2023: {len(df_apr_2023)}, BUY: {len(df_apr_2023[df_apr_2023["Тип"] == "buy"])}, SELL: {len(df_apr_2023[df_apr_2023["Тип"] == "sell"])}'
      f'\nМай 2023: {len(df_may_2023)}, BUY: {len(df_may_2023[df_may_2023["Тип"] == "buy"])}, SELL: {len(df_may_2023[df_may_2023["Тип"] == "sell"])}'
      f'\nИюнь 2023: {len(df_jun_2023)}, BUY: {len(df_jun_2023[df_jun_2023["Тип"] == "buy"])}, SELL: {len(df_jun_2023[df_jun_2023["Тип"] == "sell"])}'
      f'\nИюль 2023: {len(df_jun_2023)}, BUY: {len(df_jul_2023[df_jul_2023["Тип"] == "buy"])}, SELL: {len(df_jul_2023[df_jul_2023["Тип"] == "sell"])}'
      f'\nАвгуст 2023: {len(df_avg_2023)}, BUY: {len(df_avg_2023[df_avg_2023["Тип"] == "buy"])}, SELL: {len(df_avg_2023[df_avg_2023["Тип"] == "sell"])}'
      f'\nСентябрь 2023: {len(df_sep_2023)}, BUY: {len(df_sep_2023[df_sep_2023["Тип"] == "buy"])}, SELL: {len(df_sep_2023[df_sep_2023["Тип"] == "sell"])}'
      f'\nОктябрь 2023: {len(df_oct_2023)}, BUY: {len(df_oct_2023[df_oct_2023["Тип"] == "buy"])}, SELL: {len(df_oct_2023[df_oct_2023["Тип"] == "sell"])}'
      f'\nНоябрь 2023: {len(df_nov_2023)}, BUY: {len(df_nov_2023[df_nov_2023["Тип"] == "buy"])}, SELL: {len(df_nov_2023[df_nov_2023["Тип"] == "sell"])}'
      f'\nДекабрь 2023: {len(df_dec_2023)}, BUY: {len(df_dec_2023[df_dec_2023["Тип"] == "buy"])}, SELL: {len(df_dec_2023[df_dec_2023["Тип"] == "sell"])}')


# Функции под результирующую таблицу в датафрейме. 
def total_info_df(dataframe):

	pair_list = all_pairs_list(dataframe)
	trade_pair_list = []
	trade_counts_list = []
	buy_count_list = []
	sell_count_list = []
	all_cur_value = []
	buy_cur_value = []
	sell_cur_value = []
	delta_value = []
	min_price = []
	max_price = []
	delta_max_min = []
	value = []
	buy_value = []
	sell_value = []
	delta_sum = []
	moda_value = []
	moda_price = []
	moda_sum = []
	median_value = []
	median_price = []
	median_sum = []
	mean_value = []
	mean_price = []
	mean_sum = []
	max_value = []
	max_sum = []
	min_value = []
	min_sum = []



	for el in pair_list:
		trade_pair_list.append(el)

		df_el = dataframe.loc[(dataframe['Валютная пара'] == el)]
		trade_counts_list.append(len(df_el))
		buy_count_list.append(len(df_el[df_el['Тип'] == 'buy']))
		sell_count_list.append(len(df_el[df_el['Тип'] == 'sell']))
		all_cur_value.append(df_el['Количество'].sum())
		buy_cur_value.append(df_el[df_el['Тип'] == 'buy']['Количество'].sum())
		sell_cur_value.append(df_el[df_el['Тип'] == 'sell']['Количество'].sum())
		delta_value.append(df_el[df_el['Тип'] == 'sell']['Количество'].sum() - df_el[df_el['Тип'] == 'buy']['Количество'].sum()) 
		value.append(df_el['Сумма'].sum())
		buy_value.append(df_el[df_el['Тип'] == 'buy']['Сумма'].sum())
		sell_value.append(df_el[df_el['Тип'] == 'sell']['Сумма'].sum())
		delta_sum.append(df_el[df_el['Тип'] == 'sell']['Сумма'].sum() - df_el[df_el['Тип'] == 'buy']['Сумма'].sum())
		moda_value.append(stats.mode(df_el.Количество))
		moda_price.append(stats.mode(df_el.Цена))
		moda_sum.append(stats.mode(df_el.Сумма))
		median_value.append(df_el.Количество.median()) 
		median_price.append(df_el.Цена.median()) 
		median_sum.append(df_el.Сумма.median()) 
		mean_value.append(df_el.Количество.mean()) 
		mean_price.append(df_el.Цена.mean()) 
		mean_sum.append(df_el.Сумма.mean()) 
		max_value.append(df_el.Количество.max()) 
		max_sum.append(df_el.Сумма.max()) 
		min_value.append(df_el.Количество.min()) 
		min_sum.append(df_el.Сумма.min()) 



		a = df_el['Тип'].value_counts()
		if len(a) == 2:
			min_price.append(df_el[df_el['Тип'] == 'buy']['Цена'].min())
			max_price.append(df_el[df_el['Тип'] == 'sell']['Цена'].max())
			delta_max_min.append(df_el[df_el['Тип'] == 'sell']['Цена'].max() - df_el[df_el['Тип'] == 'buy']['Цена'].min())

		else:
			if str(df_el['Тип']) == 'buy':
				min_price.append(df_el['Цена'].min())
				max_price.append(df_el['Цена'].max())
				delta_max_min.append(df_el['Цена'].max() - df_el['Цена'].min())
			else:
				min_price.append(df_el['Цена'].min())
				max_price.append(df_el['Цена'].max())
				delta_max_min.append(df_el['Цена'].max() - df_el['Цена'].min())



	total_info = pd.DataFrame({'pair' : trade_pair_list,
							'trd_count' : trade_counts_list,
							'buy' : buy_count_list,
							'sell' : sell_count_list,
							'vol': all_cur_value,
							'buy_vol': buy_cur_value, 
							'sell_vol': sell_cur_value,
							'delta_vol': delta_value,
							'min_price': min_price,
							'max_price': max_price,
							'delta_maxmin': delta_max_min,
							'money': value,
							'buy_money': buy_value,
							'sell_money': sell_value,
							'delta_money': delta_sum,
							'moda_value': moda_value,
							'moda_price': moda_price,
							'moda_sum': moda_sum,
							'median_value': median_value,
							'median_price': median_price,
							'median_sum': median_sum,
							'mean_value': mean_value,
							'mean_price': mean_price,
							'mean_sum': mean_sum,
							'max_value': max_value,
							'max_sum': max_sum,
							'min_value': min_value,
							'min_sum': min_sum,
                         },
                           columns=['pair', 
                           'trd_count', 
                           'buy', 
                           'sell',
                           'vol',
                           'buy_vol',
                           'sell_vol', 
                           'delta_vol',
                           'min_price',
                           'max_price',
                           'delta_maxmin',
                           'money',
                           'buy_money',
                           'sell_money',
                           'delta_money',
                           'moda_value',
                           'moda_price',
                           'moda_sum',
                           'median_value',
                           'median_price',
                           'median_sum',
                           'mean_value',
                           'mean_price',
                           'mean_sum',
                           'max_value',
                           'max_sum',
                           'min_value',
                           'min_sum',
                           ])

	return total_info

################################################################################

def total(dataframe):

	time_period(dataframe)
	buy_sell_count(dataframe)
	all_pairs_info(dataframe)


total(df_jul_2023)
total(big_df)
months(big_df)
