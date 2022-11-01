import os
import sys
import argparse


#        fh.seek(0)
#        fh.read()

def get_args():
    parser = argparse.ArgumentParser(description='Howler (upper-cases input)',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='str', help='Input string or file')
    parser.add_argument('-o', '--output', metavar='str', help='show this help message and exit')
    return parser.parse_args()


def get_full_path(laptop_path, pycharm_path, file_name):
    full_path = laptop_path + pycharm_path + file_name
    return full_path


def main():
    # file path args
    laptop_path = '/Users/salvatorecangelosi/'
    pycharm_path = 'PycharmProjects/HelloWorld/05_howk/'

    # Acquisition of the args
    args = get_args()

    text_arg = args.text
    output_arg = args.output

    # string vs file check

    potential_input_full_path = get_full_path(laptop_path, pycharm_path, text_arg)
    isinputafile = True if os.path.isfile(potential_input_full_path) else False
    # TODO 1: Add missing file management in case of isInputafile equal True

    # Definition of the output path if any
    potential_output_full_path = get_full_path(output_arg, pycharm_path, text_arg) if output_arg else False



    # Output computation
    if isinputafile:
        fh_in = open(potential_input_full_path)
        file_content = fh_in.read()
        output_content = file_content.upper()
    else:
        output_content = text_arg.upper()

        # Output provision
    out_fh = open(output_arg, 'wt') if output_arg is not None else sys.stdout
    out_fh.write(output_content + '\n')
    out_fh.close()


if __name__ == '__main__':
    main()
