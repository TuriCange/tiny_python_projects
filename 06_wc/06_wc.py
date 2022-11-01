#!/usr/bin/env python3
# Purpose: Emulate wc (word count)

# usage: wc.py [-h] [FILE [FILE ...]]
import argparse
import sys

# Read argument with get_args


def get_args():
    # read zero or more text files. In case of 0 it will be taken from the system
    # This function provide us a list of file handler
    parser = argparse.ArgumentParser(description='Emulate wc (word count)',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('positional', metavar='file', nargs='*',
                        type=argparse.FileType('rt'), default=[sys.stdin], help='Input file(s)')
    return parser.parse_args()


def main():
    num_lines = 0
    num_words = 0
    num_bytes = 0
    tot_lines = 0
    tot_words = 0
    tot_bytes = 0
    num_lines_header = '# Lines'
    num_words_header = '# Words'
    num_bytes_header = '# Bytes'

    args = get_args()
    pos_arg = args.positional

    print(f'{num_lines_header:>8} | {num_words_header:>8} | {num_bytes_header:>8}')

    for fh in pos_arg:

        for line in fh:
            num_lines += 1
            words_of_line = line.split()
            num_words += len(words_of_line)
            num_bytes += len(line)
        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes

        print(f'{num_lines:8} | {num_words:8} | {num_bytes:8}')
    print(f'{tot_lines:8} | {tot_words:8} | {tot_bytes:8}')


if __name__ == '__main__':

    main()
    # final print
    # >>> 'Pi is {:0.02f}'.format(math.pi)

# Read argument with get_args
# provide value to variable
# verify the file exist
# verify the file is not empty
# count each word letter and bytes
# provide back result

# parser.add_argument('-f', '--file', default=None, metavar='FILE', type=argparse.FileType('r'), help='A readable file')

# the pipe operator (|) to funnel that output as input into our program via STDIN
# $ cat ../inputs/fox.txt | ./wc.py

# Another option is to use the < operator to redirect input from a file:
# $ ./wc.py < ../inputs/fox.txt

# we wanted to find all the lines of text that contain the word “scarlet” in all the files in the input directory
# the asterisk (*) is a wildcard that will match anything, so *.txt will match any file ending with “.txt.”
# $ grep scarlet ../inputs/*.txt

# To count the lines found by grep, we can pipe that output into our wc.py program
# $ grep scarlet ../inputs/*.txt | ./wc.py

# We can verify that this matches what wc finds:
# grep scarlet ../inputs/*.txt | wc

# nargs='+' to indicate one or more items for our picnic.
# os.path.isfile()
#
