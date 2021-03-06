#!/usr/bin/python
"""Prints values >= startval and values <= endval in name."""
import argparse as ap
import csv

from dit_flow.dit_widget.common.logger_message import logger_message


def chk_print_num_in_range_equal(startval, endval, input_data_file=None,
                                 output_data_file=None, log_file=None):
    # Prints values >= startval and values <= endval in input_data_file.
    logger = logger_message(__name__, log_file)
    assert input_data_file is not None, 'An input CSV file with columns of values.'
    count = 0
    record = 0
    with open(input_data_file, newline='') as _in:
        logger.info('Print values >= {} and <= {}'.format(startval, endval))
        logger.info('{:>10} {:>20}'.format('Record', 'Value'))
        reader = csv.reader(_in)
        for line in reader:
            for item in line:
                record = record + 1
                if (float(item) >= float(startval)) and (float(item) <= float(endval)):
                    count = count + 1
                    logger.info('{:10.0f} {:>20}'.format(float(record), item))
        logger.info('\n\t Total number >= {} and <= {}: {:10.0f}'.format(startval,
                                                                         endval, float(count)))


def parse_arguments():
    parser = ap.ArgumentParser(description="Prints values >= startval \
                               and values <= endval in input_data_file.")

    parser.add_argument('startval', type=float, help='start of range.')
    parser.add_argument('endval',   type=float, help='end of range.')

    parser.add_argument('-i', '--input_data_file',
                        help='Step file containing input data to manipulate.')
    parser.add_argument('-o', '--output_data_file', help='unused')
    parser.add_argument('-l', '--log_file', help='Step file to collect log information.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    chk_print_num_in_range_equal(args.startval, args.endval,
                                 args.input_data_file, args.output_data_file, args.log_file)
