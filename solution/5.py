import sys

def main():

	with open('count-nums.txt', 'w') as fd:
		for n in range(1, 101):
			print(n, sep=' ', end=' ', file=fd)

	with open('count-nums.txt', 'r') as fd:
		lines = [int(n) for n in fd.read().split()]
		print(lines)
		print('sum:', sum(lines))
		

if __name__ == '__main__':
	main()