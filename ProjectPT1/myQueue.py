"""
file: myQueue.py
language: python2/3
author: Sean Strout
description: A linked node implementation of a queue
"""

from .myNode import *


class Queue:
    __slots__ = ("front", "back")

    def __init__(self):
        self.front = EmptyListNode()    # The front node in the queue
        self.back = EmptyListNode()     # The back node in the queue


def enqueue(element, queue):
    """Insert an element into the back of the queue"""
    newnode = ListNode(element)
    if emptyQueue(queue):
        queue.front = newnode
    else:
        queue.back.next = newnode
    queue.back = newnode


def dequeue(queue):
    """Remove the front element from the queue (returns None)"""
    if emptyQueue(queue):
        raise IndexError("dequeue on empty queue")
    queue.front = queue.front.next
    if emptyQueue(queue):
        queue.back = EmptyListNode()


def front(queue):
    """Access and return the first element in the queue without removing it"""
    if emptyQueue(queue):
        raise IndexError("front on empty queue")
    return queue.front.data


def back(queue):
    """Access and return the last element in the queue without removing it"""
    if emptyQueue(queue):
        raise IndexError("back on empty queue")
    return queue.back.data


def emptyQueue(queue):
    """Is the queue empty?"""
    return isinstance(queue.front, EmptyListNode)
