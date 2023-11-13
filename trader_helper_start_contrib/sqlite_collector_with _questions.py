import sys
import time
import datetime
import requests
import sqlite3
# ^ импортируем модули ^

DBNAME = 'example.sqlite'
# создаём переменную -
# причём почему то в верхнем регистре
# и присваиваем ей строку причём страка
# - это имя файла с расширением .sqlite
# МОЖЕТ ЭТО ССЫЛКА НА БАЗУ ДАННЫХ

class Connector:
    """Соеденение с базой данных sqlite"""
# класс с тремя методами,
# класс - это типа чертёж объекта
# предназначен для соединения с базо данных

# функция инит вроде как создаёт объект.
# конструктор объектов.
# Параметр этого метода - 1 переменная,
# и называется как DBNAME.
#    ?Это мы создаём объект - базу данных?

    def __init__(self, dbname):
        self.dbname = dbname
# функция ничего не возвращает -
# результат её работы - объект dbname ?

    def __enter__(self):
# это мне вообще не понятно что такое дискриптр.
# расшифратор скриптов..
# попробую по строчкам разобратьься и понять
    # self.connect = sqlite3.connect(self.dbname)
# переменная функции connect
# и ей присваиваем значение равное
# sqlite3. эту функцию мы применяем к переменной connect
# а параметром функции идёт созданный в ините объект

        """Получает дескриптор"""
        self.connect = sqlite3.connect(self.dbname)
        self.cursor = self.connect.cursor()
     # self.cursor = self.connect.cursor()
# создали вторую переменную в функции __enter (ввод)
# и присвоили ей значение ...
    # ? не понимаю self.connect.cursor() ?
        return self.cursor
# возвращаем эту самую последнюю переменную мне непонятную

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрывает дескриптор"""
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
# здесь тоже не понимаю что происходит в этой функции

class Collector:
# Класс с 2 умя функциями (методами) работает с базой данных.
# причём оба метода статические
    @staticmethod
    def create_tables(currency_list):
        """Создает таблицы в базе данных"""
# объект класса Connector с...
# с объектами пока сложно мне бы подробно разъяснить.
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
# это полученные данные мы запихиваем в БД?
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

# эту кончтрукцию не понимаю . функцию создал и как то обратился к ней
# if __name__ == '__main__':
#     main(sys.argv)
# это я встречал но рне понимаю пока.
# надо лезть повторять обучение.
# чтобы лучше всё запомнить.
# а в идеале разобрать бы этот пример чуть ли не построчно,
# чтобы понимать какая строа что делает

def main(argv):
    # если аргументов недостаточно
    if len(argv) < 2:
        print("Usage: python %s wite_time" % argv[0])
        sys.exit(1)

    wait_time = int(argv[1])

    request_url = "https://api.exmo.com/v1.1/ticker"
    response = requests.post(request_url)

    # если статус ответа успешный
    if int(response.status_code) == 200:
        currency_list = response.json()
        # создаем таблицы под валюту
        Collector.create_tables(currency_list)
        # вставляем данные из первого запроса
        Collector.insert(currency_list)
# здесь после разъяснений понятна каждая строчка
        while True:
            response = requests.post(request_url)
            if int(response.status_code) == 200:
                currency_list = response.json()
                Collector.insert(currency_list)
# а после первой записи зациклили запросы с нужным промежутком времени
            time.sleep(wait_time)

    else:
        print("Запрос %s не выполнен" % request_url)
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
