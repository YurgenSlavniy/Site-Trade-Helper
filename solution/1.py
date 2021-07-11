import sys


def calculate(wout, rate, priz):
    return (wout * rate) + priz


def main(argv):

    if (len(argv) < 4):
        print('use to launch -> python ./file.py 1 2 3')
        print(
            '1) выработка в часах',
            '2) ставка в час',
            '3) премия',
            sep='\n')
        sys.exit(1)

    argv.pop(0)
    wout = float(argv.pop(0))
    rate = float(argv.pop(0))
    priz = float(argv.pop(0))

    print(calculate(wout, rate, priz))

    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
