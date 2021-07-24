
class MyZeroDivisionError(Exception):
	pass

try:
	num = int(input() or '0')
	if num == 0:
		raise MyZeroDivisionError('Деление на ' + str(num) + ' запрещено.')
	print(10 / num)
except MyZeroDivisionError as e:
	print(e)