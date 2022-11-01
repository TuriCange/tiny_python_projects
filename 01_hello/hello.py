#!/usr/bin/env python3
# Purpose: Say hello

# usage: hello.py [-h] [-n str]
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say Hello', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('positional', metavar='str', help='A positional argument')
    parser.add_argument('-a', '--arg', default=' ', metavar='str', type=str, help='A named string argument')
    parser.add_argument('-i', '--int', default=0, metavar='int', type=int, help='A named integer argument')
    parser.add_argument('-f', '--file', default=None, metavar='FILE', type=argparse.FileType('r'), help='A readable file')
    parser.add_argument('-o', '--on', help='A boolean flag', action='store_true')
    return parser.parse_args()


def main():
    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg=args.on
    pos_arg=args.positional

    print(f'str_arg= "{str_arg}"')
    print(f'int_arg= "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg= "{flag_arg}"')
    print(f'positional= "{pos_arg}"')

if __name__ == '__main__':
    main()
