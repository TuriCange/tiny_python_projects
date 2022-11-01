#!/usr/bin/env python3
# Purpose: Say hello
import argparse

def get_args():

    parser = argparse.ArgumentParser(description='Say Hello', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('positional', metavar='str', help='A positional argument')
    parser.add_argument('-a', '--arg', default=' ', metavar='str', type=str, help='Name to greet')
    parser.add_argument('-i', '--int', default=0, metavar='int', type=int, help='Name to greet')
    parser.add_argument('-f', '--file', default=0, metavar='int', type=int, help='A readable file')
    parser.add_argument('-o', '--on', help='A boolean flag', action='store_true')
    return parser.parse_args


def main():
    args = get_args()
    str_arg = args.arg
    int_arg = args.int


if __name__ == '__main__':
    main()
