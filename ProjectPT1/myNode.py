"""
file: myNode.py
language: python2/3
author: Sean Strout
description: Definitions for a singly linked list node, and an
    empty list node
"""


class EmptyListNode:
    __slots__ = ()


class ListNode:
    __slots__ = ("data", "next")  # the only valid attributes for node

    def __init__(self, dataVal, nextVal=EmptyListNode()):
        """Initialize the node"""
        self.data = dataVal         # the node's element
        self.next = nextVal         # the node's next

    def __str__(self):
        """Return a string representation of the node"""
        return "Node val: " + str(self.data)
