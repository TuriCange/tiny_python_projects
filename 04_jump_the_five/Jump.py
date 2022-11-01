#!/usr/bin/env python
"""Cross the five"""

# usage: jump.py [str]

import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input_s', metavar='str', help='Input text')
    return parser.parse_args()


def get_cross_the_five_number(num_bfr_cross_five):
    # given an input number it return as output the number obtained by crossing the five
    five_dict = dict()
    five_dict['1'] = '9'
    five_dict['2'] = '8'
    five_dict['3'] = '7'
    five_dict['4'] = '6'
    five_dict['6'] = '4'
    five_dict['7'] = '3'
    five_dict['8'] = '2'
    five_dict['9'] = '1'
    num_after_cross_five = five_dict.get(num_bfr_cross_five, 'NA')
    return num_after_cross_five


def get_cross_the_five_input(input_string):
    # given the entire input string it return the output string where all the number have crossed the five
    output_string = ''
    list_input_string = list(input_string)
    for i in range(0,len(list_input_string)):
        input_character = list_input_string[i]
        input_character_substitution = get_cross_the_five_number(input_character)
        output_string_ch = input_character_substitution if input_character_substitution != 'NA' else input_character
        output_string = output_string + output_string_ch
    return output_string


def main():
    args = get_args()
    input_str = args.input_s
    output_str = get_cross_the_five_input(input_str)
    print(output_str)

# --------------------------------------------------
if __name__ == '__main__':
    main()