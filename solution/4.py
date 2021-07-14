import sys

def main(argv):

	words = ['один', 'два', 'три', 'четыре']

	with open('strnums.txt', 'r') as rfd:
		lines = rfd.readlines()
		
		with open('new-nums.txt', 'w') as wfd:
			for line in lines:
				n = [el for el in line.split() if el.isnumeric()][0]
				print(words[int(n) - 1] + ' - ' + n, file=wfd)

if __name__ == '__main__':
	main(sys.argv)