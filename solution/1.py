
class Date:

    def __init__(self, date='03-05-2021'):
        Date.date = date

    @classmethod
    def to_num(cls):
        return int(''.join(cls.date.split('-')))

    @staticmethod
    def is_correct():
        d = [int(el) for el in Date.date.split('-')]

        month = d[0] > 0 and d[0] <= 12
        day   = d[1] > 0 and d[1] <= 31
        year  = d[2] > 0

        return month and day and year

# PX
if Date('01-01-01').is_correct():
    print(Date.to_num())
