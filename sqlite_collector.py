import sys
import time
import datetime
import requests
import sqlite3

DBNAME = './example.sqlite' 
# создается в текущей директории ...
# это обычный файл, просто в нем бинарные данные
# вместо привычного текста, там как в "Матрице"
# Если я открываю в своем редакторе, вот что там имеется
# 5351 4c69 7465 2066 6f72 6d61 7420 3300
# 1000 0101 0040 2020 0000 00af 0000 00c0
# 0000 0000 0000 0000 0000 00ac 0000 0004
# 0000 0000 0000 0000 0000 0001 0000 0000
# 0000 0000 0000 0000 0000 0000 0000 0000
# 0000 0000 0000 0000 0000 0000 0000 00af
# 002e 1cb0 0500 0000 110f a600 0000 00bb

# Почему в верхнем регистре? в Python не костант
# Это говорит, что эта переменая не изменяема
# Это обычное соглашение в сообшестве,
# которое не является правилом

class Connector:
	"""Соеденение с базой данных sqlite
	Я это класс добавил для понимания with"""
	
	def __init__(self, dbname) -> None:
		self.dbname = 'Путь к базе данных'
		self.dbname = dbname
		# результат ее работы объект None
		# __init__ не создает объектов
		# это присходит не явно
		# можно указать явно
		return None

	def __enter__(self):
		"""Получает файловый дескриптор"""
		# дескриптор это то окуда мы Читаем и Пишем
		# есть такое понятие, что все есть Файл
		# монитор, клавиатура, обычный файл и.т.д
		# чтобы записать или прочитать нужно сперва получить дескриптор
		# здесь происходит примерно это -> file_descriptop = open('fname')
		# 
		self.connect = sqlite3.connect(self.dbname)
		# cursor это файловый дескриптор
		self.cursor = self.connect.cursor()

		return self.cursor

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Закрывает файловый дескриптор"""
		# здесь происходит примерно это -> file_descriptop.close()
		# 
		# фиксируем изменения
		self.connect.commit()
		# закрываем дескриптор
		self.cursor.close()
		# закрываем соединение
		self.connect.close()
'''
Небольшой пример только с Файлом
это уже реализованно в open(), реализуем еще раз
чтобы использовать в конструкции with class Opener
нужно сделать так:

class Opener:
	def __init__(self, file_name):
		self.file_name = file_name
		self.descriptor = 0

	def __enter__(self):
		# здесь мы возвращаем файловый дескриптор
		self.descriptor = open(self.file_name)
		return self.descriptor

	def __exit__(self, exc_type, exc_val, exc_tb):
		# здесь закрываем файловый дескриптор
		self.descriptor.close()

with Opener('filename') as file_descriptor:
	здесь должно быть понятно, ты использовал with


'''
class Collector:
	'''статические методы это обычные функции
	и думать о них нужно как об обчных функциях'''
	@staticmethod
	def create_tables(currency_list):
		"""Создает таблицы в базе данных"""
		# Пример с Opener должен все разъяснить
		# мы можем сделать это без класса Connector
		# 
		# так:
		with sqlite3.connect(DBNAME) as connection:
			cursor = connection.cursor()
			# обходим полученные данные
			# в качестве имент таблиц выступает название вылюты
			for currency_name in currency_list:
				try:
					# Это язык программирования SQL
					# Язык запросов и сам запрос
					# Создать таблицу если нет таблицы с именем currency_name
					# 
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
			# Вставляем полученные данные
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

# Эта конструкция говорит
# Если этот файл является исполняемым
# Это значит мы его запускаем из терминала 
# При import наша фунция main() не запустится
# На вход main принимает время ожидания
# мы зарускаем вот так -> python ./script [через пробел время ожидания]
if __name__ == '__main__':
	# argv это аргументы командной строки list = [./script.py, ...]
	# если не знаешь, узнай что такое
	# аргументы, короткие и длинные опции командной строки
	main(sys.argv)
