import sys

def main(argv):
	if (len(argv) < 2):
		print("help -> python ./script.py file.txt")

	with open(argv[1], 'w') as fd:
		for line in sys.stdin:
			if line == '\n':
				break
			fd.write(line)


if __name__ == '__main__':
	main(sys.argv)