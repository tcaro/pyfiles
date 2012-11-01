#!/usr/local/bin/python3

"""
File: myListIter.py
Author: Sean Strout <sps@cs.rit.edu>
Contributor: Troy Caro <twc9438@rit.edu>
Language: Python 3
Description:  An iterative implementation of a node based single linked list
data structure.
Purpose: LECTURE VERSION
"""

from myNode import *

###########################################################
# LINKED LIST CLASS DEFINITION
###########################################################


class MyList():
    """A class that encapsulates a node based linked list"""
    __slots__ = ('head', 'size', 'cursor')

###########################################################
# LINKED LIST CLASS BUILDER
###########################################################


def mkMyList():
    """
    Constructs and returns an empty list.

    Parameters:
        None
    Returns:
        An empty list
    """

    lst = MyList()
    lst.head = mkEmptyNode()
    lst.size = 0
    lst.cursor = mkEmptyNode()
    return lst

###########################################################
# LINKED LIST CURSOR FUNCTIONS
###########################################################


def reset(lst):
    """
    Resets the cursor to the start of the list

    Paramters:
        lst (MyList) - the linked list
    Returns:
        None
    """

    lst.cursor = lst.head


def hasNext(lst):
    """
    Returns True if the list has more elements.

    Paramters:
        lst (MyList) - the linked list
    Returns:
        True (bool) if the cursor is value
    """

    return not isinstance(lst.cursor, EmptyNode)


def next(lst):
    """
    Returns the next element in the iteration.

    Paramters:
        lst (MyList) - the linked list
    Preconditions:
        If cursor is invalid, raises an IndexError exception
    Returns:
        The value (any type) referenced by the cursor
    """

    if isinstance(lst.cursor, EmptyNode):
        raise IndexError("cursor is invalid")

    val = lst.cursor.data
    lst.cursor = lst.cursor.next
    return val

###########################################################
# LINKED LIST FUNCTIONS
###########################################################


def clear(lst):
    """
    Make a list empty.
    Parameters:
        lst (MyList) - the linked list
    Returns:
        None
    """

    lst.head = mkEmptyNode()
    lst.size = 0
    lst.cursor = mkEmptyNode()


def toString(lst):
    """
    Converts our linked list into a string form that is similar to Python's
    printed list.

    Parameters:
        lst (MyList) - The linked list
    Returns:
        A string representation of the list (e.g. '[1,2,3]')
    """

    result = '['
    curr = lst.head
    while not isinstance(curr, EmptyNode):
        if isinstance(curr.next, EmptyNode):
            result += str(curr.data)
        else:
            result += str(curr.data) + ', '
        curr = curr.next
    result += ']'

    return result


def append(lst, value):
    """
    Add a node containing the value to the end of the list.

    Parameters:
        lst (MyList) - The linked list
        value (any type) - The data to append to the end of the list
    Returns:
        None
    """

    if isinstance(lst.head, EmptyNode):
        lst.head = mkNode(value, EmptyNode())
    else:
        curr = lst.head
        while not isinstance(curr.next, EmptyNode):
            curr = curr.next
        curr.next = mkNode(value, EmptyNode())

    lst.size += 1


def insert(lst, index, value):
    """
    Insert a new element before the index.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to insert before
        value (any type) - The data to be inserted into the list
    Preconditions:
            0 <= index <= lst.size, raises IndexError exception
    Returns:
        None
    """

    if index < 0 or index > lst.size:
        raise IndexError(str(index) + ' is out of range.')

    if index == 0:
        lst.head = mkNode(value, lst.head)
    else:
        prev = lst.head
        while index > 1:
            prev = prev.next
            index -= 1
        prev.next = mkNode(value, prev.next)

    lst.size += 1


def get(lst, index):
    """
    Returns the element that is at index in the list.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to get
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception
    Returns:
        None
    """

    if index < 0 or index >= lst.size:
        raise IndexError(str(index) + ' is out of range.')

    curr = lst.head
    while index > 0:
        curr = curr.next
        index -= 1
    return curr.data


def set(lst, index, value):
    """
    Sets the element that is at index in the list to the value.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to set
        value (any type)
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception
    Returns:
        None
    """

    if index < 0 or index >= lst.size:
        raise IndexError(str(index) + ' is out of range.')

    curr = lst.head
    while index > 0:
        curr = curr.next
        index -= 1
    curr.data = value


def pop(lst, index):
    """
    Remove and return the element at index.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to remove
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception
    Returns:
        The value (any type) being popped
    """

    if index < 0 or index >= lst.size:
        raise IndexError(str(index) + ' is out of range.')

    lst.cursor = mkEmptyNode()
    if index == 0:
        value = lst.head.data
        lst.head = lst.head.next
    else:
        prev = lst.head
        while index > 1:
            prev = prev.next
            index -= 1
        value = prev.next.data
        prev.next = prev.next.next

    lst.size -= 1
    return value


def index(lst, value):
    """
    Returns the index of the first occurrence of a value in the list

    Parameters:
        lst (MyList) - The list to insert value into
        value (any type) - The data being searched for
    Preconditions:
        value exists in list, otherwise raises ValueError exception
    Returns:
        The index (int) of value or None if value is not present in the list
    """

    pos = 0
    curr = lst.head
    while not isinstance(curr, EmptyNode):
        if curr.data == value:
            return pos
        pos += 1
        curr = curr.next

    raise ValueError(str(value) + " is not present in the list")

###########################################################
# LINKED LIST FUNCTIONS
#
# Author: Troy Caro <twc9438@rit.edu>
# Date: October 24, 2012
# Assignment: Homework 7
# Description: Iterative implementaion of count,
#       myListToPyList, PyListToMyList, and remove.
###########################################################


def count(lst, value):
    """
    @description:
                        Counts the number of times an item occurs in a linked list.

    @parameters:
                        lst (MyList) - a MyList object
                        value (typeless) - value to count number of occurances

    @pre-conditions:
                        lst is a MyList objecct

    @post-conditions:
                        returns an integer for the number of times value occurs.
    """
    total = 0
    node = lst.head

    while isinstance(node, EmptyNode) is False:
        if node.data == value:
            total += 1
        node = node.next

    return total


def myListToPyList(lst):
    """
    @description:
                        Converts a linked list to a python list.

    @parameters:
                        lst (MyList) - a MyList object

    @pre-conditions:
                        lst is a MyList object

    @post-conditions:
                        returns a python list containing the same data
    """
    newList = []
    node = lst.head

    while isinstance(node, EmptyNode) is False:
        newList.append(node.data)
        node = node.next

    return newList


def pyListToMyList(pylst):
    """
    @description:
                        Converts a python list to a linked list (MyList).

    @parameters:
                        pylst (list) - python list to be converted

    @pre-conditions:
                        None.

    @post-conditions:
                        returns a MyList object containing the same data
    """
    lst = mkMyList()

    for element in pylst:
        append(lst, element)

    return lst


def remove(lst, value):
    """
    @description:
                        Removes the first occurance of a value from a linked list.

    @parameters:
                        lst (MyList) - a MyList object
                        value (typeless) - the value to be removed

    @pre-conditions:
                        lst is a MyList object

    @post-conditions:
                        value has been removed from the list.
                        If the value is not in the list, a ValueError exception
                        will be raised.
    """
    index = 0
    removed = False
    node = lst.head

    while isinstance(node, EmptyNode) is False:
        if (node.data == value):
            pop(lst, index)
            removed = True
            break
        else:
            index += 1
            node = node.next

    if removed is False:
        raise ValueError(str(value) + " is not present in the list")
