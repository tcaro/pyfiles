#!/usr/local/bin/python3

"""
Title: polyAdd.py
Language: Python3
Assignment: Lab
Author: Troy Caro <twc9438@rit.edu>
Date: October 29, 2012
Purpose: Add two polynomials together.
"""

from myNode import *
from myListIter import *

############################################################
# POLYNOMIAL TERM CLASS DEFINITION
############################################################


class polyTerm():
    """
    A class that contains data for a single term in a
        polynomial.
    """
    __slots__ = ('coefficient', 'power')

############################################################
# POLYNOMIAL TERM CLASS CONSTRUCTOR
############################################################


def buildTerm(coeff, power):
    """
    Constructs and returns a polynomial term.

    Parameters:
        coeff (int) - the coefficient of the term
        power (int) - the power that the term is raised to
    Post-conditions:
        Returns a polyTerm object with data
     """
    t = polyTerm()
    t.coefficient = coeff
    t.power = power

    return t

############################################################
# USER INPUT AND FILE FUNCTIONS
############################################################


def ui():
    """
    Gets the users input for the file location containing
        the polynomial data.

    Parameters:
        None.
    Pre-conditions:
        The files exist.
        The files are formatted correctly.
    Post-conditions:
        Returns the file names for the polynomials.
    """
    return (input("Enter polynomial A file: "), input("Enter polynomial B file: "))


def handleFile(fileName):
    """
    Opens a file containing polynomial data and inputs the
        data into a linked list.

    Parameters:
        fileName (string) - the file to open
    Pre-conditions:
        The file is formatted correctly.
    Post-conditions:
        Returns a linked list object containing the polynomial data.
    """
    f = open(fileName)
    lst = mkMyList()

    for line in f:
        l = line.split()
        append(lst, buildTerm(int(l[0]), int(l[1])))

    return lst

############################################################
# POLYNOMIAL LINKED LIST FUNCTIONS
############################################################


def checkPoly(lst):
    """
    Checks the polynomial to add like terms together

    Parameters:
        lst (myList) - linked list containing polynomial terms
    Pre-conditions:
        lst is sorted in descending order
    Post-conditions:
        lst is returned with like terms combined
    """
    index = 0
    node = lst.head

    while isinstance(node, EmptyNode) is False:
        if isinstance(node.next, EmptyNode):
            # If the next node is empty, break the while loop
            break
        if (node.data.power == node.next.data.power):
            node.data.coefficient += node.next.data.coefficient
            pop(lst, index + 1)  # Pop off the element after the current one
        else:
            node = node.next
            index += 1

    return lst


def printPoly(lst):
    """
    Prints a polynomial from a linked list.

    Parameters:
        lst (myList) - linked list containing polynomial terms
    Pre-conditions:
        lst has been sorted by descending power
    Post-conditions:
        Polynomial has been printed out correctly.
    """
    node = lst.head
    total = ""

    while isinstance(node, EmptyNode) is False:
        if (node.data.coefficient == 0):
            node = node.next
        elif (node.data.power == 1 and node.data.coefficient == 1):
            total += " + x"
            node = node.next
        elif (node.data.power == 1):
            total += (" + " + str(node.data.coefficient) + "x")
            node = node.next
        elif (node.data.power == 0):
            total += (" + " + str(node.data.coefficient))
            node = node.next
        elif (node.data.coefficient == -1):
            total += " + -x"
            node = node.next
        elif (node.data.coefficient == 1):
            total += (" + x^" + str(node.data.power))
            node = node.next
        elif (total == ""):
            total += (str(node.data.coefficient) + "x^" + str(node.data.power))
            node = node.next
        else:
            total += (" + " + str(node.data.coefficient) + "x^" + str(node.data.power))
            node = node.next
    return total


def insertionSort(pylst):
    """
    Sorts a list of data using the insertion sort algorithm.

    Parameters:
        data (list) - the list of data to sort
    Pre-condition:
        The list contains only polyTerm objects
    Post-conditions:
        The data list has been sorted.
    """
    for index in range(1, len(pylst)):
        holder = pylst[index]
        val = index
        while val > 0 and pylst[val - 1].power < holder.power:
            pylst[val] = pylst[val - 1]
            val -= 1
        pylst[val] = holder


def sort(lst):
    """
    Sorts a linked list of polyTerm objects in descending order.

    Parameters:
        lst (myList) - a myList object containing polyTerm objects
    Post-conditions:
        returns a myList object that has been sorted
    """
    pylst = myListToPyList(lst)
    insertionSort(pylst)
    newList = mkMyList()
    newList = pyListToMyList(pylst)

    return newList


def addPoly(firstTerm, secondTerm):
    """
    Adds two linked list polynomials together.

    Parameters:
        firstTerm (myList) - a myList object containing polynomial data
        secondTerm (myList) - a myList object containing polynomial data
    Pre-conditions:
        firstTerm/secondTerm only contain polyTerm objects
    Post-conditions:
        returns a myList object containing polynomial data of the combined terms
    """
    nodeA = firstTerm.head
    nodeB = secondTerm.head
    newPoly = mkMyList()

    while isinstance(nodeA, EmptyNode) is False:
        append(newPoly, nodeA.data)
        nodeA = nodeA.next

    while isinstance(nodeB, EmptyNode) is False:
        append(newPoly, nodeB.data)
        nodeB = nodeB.next

    return newPoly

############################################################
# MAIN FUCNTION DEFINITION
############################################################


def main():
    """
    Main function call that runs the program and outputs the results
    """
    (fileNameA, fileNameB) = ui()
    file1 = handleFile(fileNameA)
    file2 = handleFile(fileNameB)
    firstTerm = checkPoly(sort(file1))
    secondTerm = checkPoly(sort(file2))

    print()
    print("   " + printPoly(firstTerm))
    print("+  " + printPoly(secondTerm))
    print("--------------------------------------------------------")
    print("=  " + printPoly(checkPoly(sort(addPoly(firstTerm, secondTerm)))))

# Program execution
main()
