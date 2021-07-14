import sys

def main():
	values = 0
	with open('person.txt', 'r') as fd:
		for line in fd:
			person = line.split()
			v = float(person[1])

			if v < 20000:
				values += v
				print(person[0], person[1])
	
	print(':', values)


if __name__ == '__main__':
	main()