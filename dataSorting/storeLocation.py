"""
Title: storeLocation.py
Language: pyhton3
Assignment: Lab 05
Author: Troy Caro <twc9438@rit.edu>
Date: October 10, 2012
Purpose: Calculate and print the optimal location for a store and the sum
    of the distances that people would have to travel to reach the store from each
    given location.
"""

import sys
import getopt
import store
import time


def sort(lst):
    """
    @description:
                        Perform an insertion sort on a list of data.

    @parameters:
                        lst (list) - the list of data to be sorted

    @pre-conditions:
                        The length of the list is not 0

    @post-conditions:
                        Returns the sorted list
    """
    for mark in range(len(lst) - 1):
        insert(lst, mark)

    return lst


def swap(lst, a, b):
    """
    @description:
                    Swaps two elements in a list.

    @parameters:
                    lst (list) - the list of elements
                    a (int) - the position of the first element
                    b (int) - the positino of the second element

    @pre-conditions:
                    The list length is not 0
                    a and b >= 0

    @post-conditions:
                    Elements at positions a and b have been swapped
    """
    (lst[a], lst[b]) = (lst[b], lst[a])


def insert(lst, mark):
    """
    @description:
                        Move the value at index mark + 1 so that it's in the correct position

    @parameters:
                        lst (list) - the list of integers
                        mark (int) - represents cutting the list between
                                       index mark and index mark + 1

    @preconditions:
                        Length of the list is not 0
                        mark is > 0
    """
    index = mark

    while index > - 1 and lst[index] > lst[index + 1]:
        swap(lst, index, index + 1)
        index = index - 1


def median(lst):
    """
    @description:
                        Gets the median of a list of unsorted integers using insertion sort.

    @parameters:
                        lst (list) = The list of unsorted integers

    @pre-conditions:
                        The list contains only integers and in unsorted.
                        The length of the list is not 0

    @post-condtions:
                        Returns the median of the list.
    """
    newData = sort(lst)

    if (len(newData) % 2 == 0):
        return  (newData[len(newData) // 2] + newData[(len(newData) // 2) - 1]) / 2
    else:
        return newData[len(newData) // 2]


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
