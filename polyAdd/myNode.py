"""
File: myNode.py
Author: Sean Strout <sps@cs.rit.edu>
Language: Python 3
Description:  A representation of a single linked node intended
to be used as the building blocks for a linked list.
"""

###########################################################
# NODE CLASS DEFINITIONS
###########################################################


class EmptyNode():
    """A representation for an empty list"""
    __slots__ = ()


class Node():
    """A representation of a non-empty list"""
    __slots__ = ('data', 'next')

###########################################################
# NODE CLASS BUILDERS
###########################################################


def mkEmptyNode():
    """
    Constructs and returns an empty list.

    Parameters:
        None
    Returns:
        An EmptyNode instance
    """
    return EmptyNode()


def mkNode(data, next):
    """
    Constructs and returns a non-empty list.

    Parameters:
        data (any type) - The data to be stored in this node instance
        next (Node or EmptyNode) - The next element in the list
    """

    node = Node()
    node.data = data
    node.next = next
    return node
