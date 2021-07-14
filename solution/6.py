import sys

def main():
	result = {}

	with open('sub.txt', 'r') as fd:
		for line in fd:
			line = line.split()
			key  = line.pop(0).strip(':')

			num_str = ''
			for ch in ''.join(line):
				if ch.isnumeric():
					num_str += ch

				if not ch.isnumeric():
					num_str += ' '
			
			result[key] = sum([int(el) for el in num_str.split()])

	print(result)

if __name__ == '__main__':
	main()