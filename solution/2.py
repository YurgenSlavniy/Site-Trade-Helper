import sys

def main(argv):
	if (len(argv) < 2):
		print("help -> python ./script.py file.txt")

	with open(argv[1], 'r') as fd:
		nlines = len(fd.readlines())
		print(nlines)

if __name__ == '__main__':
	main(sys.argv)