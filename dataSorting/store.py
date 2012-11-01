"""
Title: store.py
Language: python3
Assignment: Lab 05
Author: Troy Caro <twc9438@rit.edu>
Date: Octoober 10, 2012
Purpose: Implement functions that will be used in both programs for the 'store' lab.
"""


def sum_distance(lst, best_loc):
    """
    @description:
                        Sums the total distance that people will have to walk
                        given a list of unsorted office locations, and the new
                        office location.

    @parameters:
                        lst (list) - unsorted list of integers
                        best_loc (int) - the best location for the new store

    @pre-condtions:
                        The list contains only integers.
                        The length of the list is greater than 0
                        best_loc >= 0

    @post-conditions:
                        Returns the total distance that people would have to walk."""
    total = 0

    for element in lst:
        if (best_loc >= element):
            total += (best_loc - element)
        else:
            total += (element - best_loc)

    return total


def usage():
    """
    @description:
                        Usage instructions on how to run the program.
    """
    print()
    print("This program will determine the optimal location to place a new store")
    print("given a file of office locations. It will calculate and print out the")
    print("optimal location for the store, and the total distance from each of the")
    print("office buildings.")
    print()
    print("Usage: pyton3 (storeLocation.py/selectMedian.py) [options]")
    print("*The program will run with no options")
    print()
    print("Options:")
    print("-h help - prints out this helpful message")
    print("-f [location..] file name - the exact location of the file to use")
    print()


def output(optimal_location, total_distance, start_time, end_time):
    """
    @description:
                        Outputs the main information for the program.

    @parameters:
                        optimal_location (int) - the best location to place a new store
                        total_distance (int) - the total distance that people will have to walk
                        start_time (int) - the cpu start time before it finds the median
                        end_time (int) - the cpu end time after if finds the median
    """
    print()
    print("The optimal location for the store is at position " + str(optimal_location))
    print("The total distances that people would have to trave is " + str(total_distance))
    print("The total time that is took to find the median was " + str((end_time - start_time)))
    print()


def ui():
    """
    @description:
                        Gets the user input for the exact location for the file.

    @post-conditions:
                        Returns the file name."""
    # User input for file location
    return input("Enter the exact location of the file: ")


def handleFile(fileName):
    """
    @description:
                        Opens the file and creates a list of store locations

    @parameters:
                        fileName (string) - the file name to be opened

    @pre-conditions:
                        the file already exists.

    @post-conditions:
                        returns the list of integer store locations
    """
    # Open the file and parse it into a list of only integers (unsorted)
    f = open(fileName)
    shuffled_lst = []

    for line in f:
        split = line.split()
        shuffled_lst.append(int(split[1]))

    return shuffled_lst
