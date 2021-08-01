import sys
import time
import datetime
import requests
import sqlite3

DBNAME = 'example.sqlite'

class Connector:
	"""Соеденение с базой данных sqlite"""
	def __init__(self, dbname):
		self.dbname  = dbname

	def __enter__(self):
		"""Получает дескриптор"""
		self.connect = sqlite3.connect(self.dbname)
		self.cursor = self.connect.cursor()

		return self.cursor

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Закрывает дескриптор"""
		self.connect.commit()
		self.cursor.close()
		self.connect.close()

class Collector:
	@staticmethod
	def create_tables(currency_list):
		"""Создает таблицы в базе данных"""
		with Connector(DBNAME) as cursor:
			for currency_name in currency_list:
				try:

					SQL = '''CREATE TABLE IF NOT EXISTS %s
					(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					buy_price VARCHAR(40),
					sell_price VARCHAR(40),
					last_trade VARCHAR(40),
					high VARCHAR(40),
					low VARCHAR(40),
					avg VARCHAR(40),
					vol VARCHAR(40),
					vol_curr VARCHAR(40),
					updated VARCHAR(40),
					sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
					)''' % currency_name.lower()

					cursor.execute(SQL)
				except sqlite3.Error as err:
					print(err)
					break

	@staticmethod
	def insert(currency_list):
		"""Вставляет новые данные"""
		with Connector(DBNAME) as cursor:
			for currency_name in currency_list:
				try:
					SQL = '''INSERT INTO {} 
					(
					buy_price, sell_price, last_trade,
					high, low, avg, vol, vol_curr, updated
					) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})'''.format(
						currency_name.lower(),
						currency_list[currency_name]['buy_price'],
						currency_list[currency_name]['sell_price'],
						currency_list[currency_name]['last_trade'],
						currency_list[currency_name]['high'],
						currency_list[currency_name]['low'],
						currency_list[currency_name]['avg'],
						currency_list[currency_name]['vol'],
						currency_list[currency_name]['vol_curr'],
						currency_list[currency_name]['updated'],
						)
					cursor.execute(SQL)
				except sqlite3.Error as err:
					print(err)
					break

def main(argv):
	# если аргументов недостаточно
	if len(argv) < 2:
		print("Usage: python %s wite_time" % argv[0])
		sys.exit(1)

	wait_time = int(argv[1])

	request_url = "https://api.exmo.com/v1.1/ticker"
	response    = requests.post(request_url)

	# если статус ответа успешный
	if int(response.status_code) == 200:
		currency_list = response.json()
		# создаем таблицы под валюту
		Collector.create_tables(currency_list)
		# вставляем данные из первого запроса
		Collector.insert(currency_list)

		while True:
			response = requests.post(request_url)
			if int(response.status_code) == 200:
				currency_list = response.json()
				Collector.insert(currency_list)
			
			time.sleep(wait_time)
	
	else:
		print("Запрос %s не выполнен" % request_url)
		sys.exit(1)

	sys.exit(0)

if __name__ == '__main__':
	main(sys.argv)
