"""
Title: generateFile.py
Language: python3
Assignment: Lab
Author: Troy Caro <twc9438@rit.edu>
Purpose: Generates a file of a given number of lines
"""

import getopt
import sys
import random


def usage():
    print()
    print("Usage: python3 generateFile.py [opitons]")
    print("Example: python3 generatedFile.py -o fileName.txt -n 10000 -b 0 -t 9999")
    print()
    print("Options:")
    print("-h : Displays this wonderful help message")
    print("-o [fileName..] : The name for the output file")
    print("-n [integer..] : The number of lines that the file will have")
    print("-b [integer..] : The smallest random number to be generated")
    print("-t [integer..] : The largest random number to be generated")
    print()


def randomList(lines, top, bottom):
    randLst = []

    for x in range(lines):
        randLst.append("Store_" + str(x) + " " + str(random.randrange(bottom, top + 1)))

    return randLst


def writeLstToFile(fileName, lst):
    f = open(fileName, 'w')

    for element in lst:
        f.write(str(element) + "\n")

    f.close()


def main(arguments):
    _fileName = ""
    _top = 0
    _bottom = 0
    _lines = 0

    if (len(arguments) == 0):
        usage()
        sys.exit(2)

    try:
        optLst, argLst = getopt.getopt(arguments, "ht:b:n:o:", ["help", "top", "bottom", "number-lines", "output"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for option, arg in optLst:
        if option in ("-h", "--help"):
            usage()
            sys.exit(2)

        elif option in ("-t", "--top"):
            _top = int(arg)

        elif option in ("-b", "--bottom"):
            _bottom = int(arg)

        elif option in ("-n", "--number-lines"):
            _lines = int(arg)

        elif option in ("-o", "--output"):
            _fileName = arg

    writeLstToFile(_fileName, randomList(_lines, _top, _bottom))
    sys.exit(0)

main(sys.argv[1:])
