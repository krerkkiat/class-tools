#!/bin/python2
# -*- coding: utf-8 -*-
'''
A simple recreation of p1p2_mkhtml (or labs_mkhtml) of
Mr. John Dolan at Ohio University.

This will allow student to use their own machince to turn
the output of the project 4 program into a HTML file.

This might reduce the time to transfer the output file
from local machince to the Prime server (and other way
arond to get the HTML file back).

Although this module is part of the mkhtml_server, a flask
web application, it can be called from command line with both
Python2 or Python3 to locally parse the output file.
'''
import re
import argparse

# Regular Expression patterns.
swatch_pattern = re.compile('[\da-zA-Z]{6,6}\s+\d{2,3}\s+\d{2,3}')
space_pattern = re.compile('\s+')

def parse_swatches(swatches, extra_width=6, extra_height=4, swatches_per_row=20):
    '''
    Parse the output in list object swatches, then return the HTML string.

    The HTML string is the table tags that each of them represent
    one set of output (the set of output is separated by two
    newline characters).

    User is allow to change some settings of the output string
    through the keyword arguments of this function.
    '''
    html_text = '<table><tr>'
    swatch_template = '<td><div style="background-color:#{color};width:{width}px;height:{height}px;"></div></td>'
    
    separator_counter = 0
    counter = 0

    for line in swatches:
        # The space is registered as the separator of each
        # group of the output
        if line.strip() == '':
            separator_counter = separator_counter + 1
            if separator_counter == 2:
                html_text = html_text + '</tr></table><table><tr>'
                counter = 0
                separator_counter = 0
            continue
        elif not swatch_pattern.match(line):
            continue    # Ignore some other text.

        # Check for the amount of swatches per row.
        if counter != 0 and counter % swatches_per_row == 0:
            counter = 0
            html_text = html_text + '</tr><tr>'

        # Remove white space, and split the data into list.
        data = space_pattern.split(line)

        # Fill value in the template and write it out.
        html_text = html_text + swatch_template.format(color=data[0], \
            width=int(data[1]) + extra_width, \
            height=int(data[2]) + extra_height)
        counter = counter + 1
    html_text = html_text + '</tr></table>'
    return html_text

if __name__ == '__main__':
    # Argument parse and usage message.
    parser = argparse.ArgumentParser(description='Turn an output file of CS2401\'s Project 4 into a HTML file.')
    parser.add_argument('filename', type=str, help='the name of the file to be processed')
    parser.add_argument('-c', '--columns', type=int, default=20, \
        help='the number of swatches to be shown in one row')
    parser.add_argument('--extra_width', type=int, default=6, \
        help='the extra width that will be added to the width of each swatches')
    parser.add_argument('--extra_height', type=int, default=4, \
        help='the extra height that will be added to the height of each swatches')

    args = parser.parse_args()

    # Set up all variables and template.
    title = 'HTML output of ' + args.filename
    style = 'div{margin:auto;} table{padding-bottom:60px;}'
    header = '<html><head><title>' + title + \
        '</title><style type="text/css">' + style + \
        '</style></head><body>'

    footer = '</body></html>'

    with open(args.filename + '.html', 'w') as output_file:
        output_file.write(header)
        with open(args.filename, 'r') as data_file:
            body = parse_swatches(data_file,\
                    extra_width=args.extra_width,\
                    extra_height=args.extra_height,\
                    swatches_per_row=args.columns);
        output_file.write(body)
        output_file.write(footer)