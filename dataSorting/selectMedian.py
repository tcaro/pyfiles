"""
Title: selectMedian.py
Language: Python3
Author: Troy Caro <twc9438@rit.edu>
Date: October 10, 2012
Purpose: Implement the quick sort algorithm.
"""

import store
import sys
import getopt
import time


def median(lst):
    """
    @description:
                        Gets the median of a list of unsorted integers using quickSelect.

    @parameters:
                        lst (list) = The list of unsorted integers

    @pre-conditions:
                        The list contains only integers and in unsorted.
                        The length of the list is not 0

    @post-condtions:
                        Returns the median of the list.
    """
    lstLen = len(lst)

    if (lstLen % 2 == 0):
        lower = quickSelect(lst, ((len(lst) // 2) - 1))
        upper = quickSelect(lst, (len(lst) // 2))
        return (upper + lower) / 2
    else:
        return quickSelect(lst, len(lst) // 2)


def quickSelect(lst, k):
    """
    @description:
                        Given a list of unsorted integers, the function finds the k'th
                        smallest number.

    @parameters:
                        lst (list) - The list of unsorted integers
                        k (int) - The k'th smallest number in the list

    @pre-conditions:
                        The list contains only integers.
                        The length of the list is not 0.
                        k is >= 0

    @post-conditions:
                        Returns the k'th smallet number in a list
    """
    if (len(lst) == 0):
        pass
    else:
        pivot = lst[len(lst) // 2]
        smallerLst = []
        largerLst = []
        count = 0

        for element in lst:
            if (element == pivot):
                count += 1
            elif (element > pivot):
                largerLst.append(element)
            else:
                smallerLst.append(element)

        m = len(smallerLst)

        if (k >= m and k < (m + count)):
            return pivot
        elif (m > k):
            return quickSelect(smallerLst, k)
        else:
            return quickSelect(largerLst, k - m - count)


def main(arguments):
    """
    @description:
                        Main function call that runs the program.

    @parameters:
                        arguments (list) - any arguents that were passed to the prgram
                                            from the commmand line.

    @pre-conditions:
                        None.

    @post-condtions:
                        Program finds the optimal location to place a new store
                        given a file of office locations.
    """
    _fileName = ""

    try:
        optList, argList = getopt.getopt(arguments, "hf:", ["help", "file_name="])
    except getopt.GetoptError:
        store.usage()
        sys.exit(2)

    # For the option, and the argument following it
    for option, arg in optList:
        if option in ("-h", "--help"):
            store.usage()
            sys.exit(0)

        elif option in ("-f", "--file_name"):
            _fileName = arg

    if (_fileName == ""):
        _fileName = store.ui()

    shuffled_lst = store.handleFile(_fileName)

    start_time = time.clock()
    optimalLocation = median(shuffled_lst)
    end_time = time.clock()

    totalDistance = store.sum_distance(shuffled_lst, optimalLocation)

    store.output(optimalLocation, totalDistance, start_time, end_time)

# Runs the program
main(sys.argv[1:])
