#!/usr/bin/env python3
# Purpose: Say hello

# !/usr/bin/env python3
# Purpose: Greet Someone
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Crow\'s Nest -- choose the correct article', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='A word')
    #parser.add_argument('-a', '--arg', default=' ', metavar='str', type=str, help='A named string argument')
    return parser.parse_args()


def main():
    args = get_args()
    #str_arg = args.arg
    word=args.word
    #print(f'str_arg= "{str_arg}"')
    print(word)

if __name__ == '__main__':
    main()
