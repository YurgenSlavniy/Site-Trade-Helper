import sys

print('Завершения ввода Ctrl+D')

class OnlyNumListError(Exception):
	pass

class OnlyNumList():
	
	def __init__(self):
		self.nlist = []
		for n in sys.stdin:
			try:
				self._set(n.strip())
			except OnlyNumListError as e:
				print(e)
				continue

	def _set(self, el):
		if el.isnumeric():
			self.nlist.append( int(el) )
		else:
			raise OnlyNumListError('Вводить можно только числа')

	def get_list(self):
		return self.nlist
		

nlist = OnlyNumList().get_list()

print(nlist)