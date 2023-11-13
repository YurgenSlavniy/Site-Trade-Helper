
class MyComplex(complex):

	def __init__(self, left):
		self.left = left

	def __add__(self, right):
		return self.left + right

	def __mul__(self, right):
		return self.left * right

n1 = MyComplex(2)
n2 = MyComplex(4)

print(n1 + n2)
print(n1 * n2)