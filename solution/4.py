
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([
	n
	for n in lst
	if lst.count(n) < 2
])