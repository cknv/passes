from . import multi_gen
import argparse


def main():
    parser = argparse.ArgumentParser(description='Make random passwords.')
    parser.add_argument('-l', '--length', type=int, default=10)
    parser.add_argument('-n', '--number', type=int, default=1)
    parser.add_argument('-c', '--chars')

    args = parser.parse_args()

    print('Generating: {}'.format(args.number))
    print('Password length: {}'.format(args.length))
    print('Using charset: {}'.format(args.chars or 'default'))

    for i, result in enumerate(multi_gen(args.number, args.length)):
        print('{}\t{}'.format(i, result))
