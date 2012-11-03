#!/usr/local/bin/python3

"""
Title: treeMap.py
Language: python3
Assignment: Homework 8
Author: Troy Caro <twc9438@rit.edu>
Date: November 1, 2012
Purpose: Create a map structure based on a binary tree.
"""

######################################################################################################
# MAP CLASS DEFINITIONS
######################################################################################################


class EmptyMap():
    """
    Makes an empty map instance.
    """
    __slots__ = ()


class NonEmptyMap():
    """
    Makes a map instance with values left, key, value, and right
    """
    __slots__ = ('left', 'key', 'value', 'right')

######################################################################################################
# MAP CONSTRUCTOR FUNCTIONS
######################################################################################################


def mkEmptyMap():
    """
    Makes an empty map

    Post-conditions:
        Returns an EmptyMap instance
    """
    return EmptyMap()


def mkNonEmptyMap(left, key, value, right):
    """
    Makes a NonEmptyMap instance with data.

    Parameters:
        left (map) - left map object
        key (string) - the key value in the map object
        value (int) - the value associated with the key
        right (map) - right map object
    Pre-conditions:
        left and right are either of type EmptyMap or NonEmptyMap
    Post-conditions:
        Returns and instance of a NonEmptyMap
    """
    m = NonEmptyMap()
    m.left = left
    m.key = key
    m.value = value
    m.right = right
    return m

######################################################################################################
# MAP FUNCTION DEFINITIONS
######################################################################################################


def mapInsert(key, value, map):
    """
    Inserts a new key and value into a map.

    Parameters:
        key (string) - the key value in the map
        value (int) - the value associated with the key
        map (NonEmptyMap) - an instance of NonEmptyMap
    Pre-conditions:
        map is an instance of NonEmptyMap
    Post-conditions:
        Returns an instance of NonEmptyMap with the new key and value added
    """
    if isinstance(map, EmptyMap):
        map = mkNonEmptyMap(mkEmptyMap(), key, value, mkEmptyMap())
    elif (key < map.key):
        if isinstance(map.left, EmptyMap):
            map.left = mkNonEmptyMap(mkEmptyMap(), key, value, mkEmptyMap())
        else:
            mapInsert(key, value, map.left)
    elif (key > map.key):
        if isinstance(map.right, EmptyMap):
            map.right = mkNonEmptyMap(mkEmptyMap(), key, value, mkEmptyMap())
        else:
            mapInsert(key, value, map.right)
    else:
        map.value = value

    return map


def mapToString(map):
    """
    Makes a string that represents a map.

    Parameters:
        map (NonEmptyMap) - instance of NonEmptyMap
    Pre-conditions:
        map is an instance of NonEmptyMap
    Post-conditions:
        Returns a string that represents a map
    """
    if isinstance(map, EmptyMap):
        return "_"
    else:
        return ("(" + mapToString(map.left) + ", " + map.key + "->" + str(map.value) + ", " + mapToString(map.right) + ")")


def mapSearch(key, map):
    """
    Searches a map for a key and gets the value associated with it.

    Parameters:
        key (string) - the key value in the map
        map (NonEmptyMap) - instance of NonEmptyMap
    Pre-conditions:
        map is an instance of NonEmptyMap
    Post-conditions:
        Returns the value associated with the key, or None if the key is not there
    """
    if isinstance(map, EmptyMap):
        return None
    if (map.key == key):
        return map.value
    elif (map.key > key):
        mapSearch(key, map.left)
    elif (map.key < key):
        mapSearch(key, map.right)
