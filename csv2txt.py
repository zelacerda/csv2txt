#!/usr/bin/python3

import sys

def csv2txt(src, dest):

    with open(src) as file:
        col_names = file.readline()[:-1].split(',')
        output = ""
        line = file.readline()

        while line != '':
            line_values = line.split(',')
            output += "## " + line_values[0] + '\n\n'

            for column, value in zip(col_names[1:], line_values[1:]):
                output += "**" + column + "**: " + value + "\n"

            line = file.readline()

    with open(dest, mode='w') as file:
        file.writelines(output)

if __name__ == '__main__':
    csv2txt(sys.argv[1], sys.argv[2])

