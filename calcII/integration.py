#!/usr/local/bin/python3-32

"""
Title: integration.py
Language: python3
Assignment: Project-Based Calc II
Author: Troy Caro <twc9438@rit.edu>
Purpose: Calculate the definite integral of an arbitrary function over an arbitraty interval
    using the Right and Left endpoint rules, the midpoint rule, the trapezoid rule, and finally
    simpson's rule.
"""

################################################################################################
# USER INPUT
################################################################################################


def ui():
    """
    Gets the user input for the equation to integrate, and the interval.

    Pre-conditions:
        The input is formatted correctly
    Post-conditions:
        The funtion returns the expression
    """
    print()
    print("Enter the expression to evalue the integral for.")
    print("Example: 3x**2+2x+9")
    expression = input("y = ")
    print()
    print("Enter the interval to integrate over.")
    print("Example: 2 5")
    print("*Values are seperated by a space")
    interval = input("Interval: ")
    line = interval.split()
    print()
    print("Enter the number of sub-intervals.")
    print("Example: 4")
    n = int(input("Sub-intervals: "))

    return (expression, int(line[0]), int(line[1]), n)

################################################################################################
# RIGHT ENDPOINT RULE
################################################################################################


def rightEndpointRule(expression, a, b, n):
    """
    Evaluates the expression using the right endpoint rule
    """
    dx = (b - a) / n
    area = 0

    for i in range(1, n + 1):
        x = (dx * i)
        area += dx * eval(expression)

    return area

################################################################################################
# LEFT ENDPOINT RULE
################################################################################################


def leftEndpointRule(expression, a, b, n):
    """
    Evaluates the expression using the left endpoint rule.
    """
    dx = (b - a) / n
    area = 0

    for i in range(n):
        x = (dx * i)
        area += dx * eval(expression)

    return area

################################################################################################
# MIDPOINT RULE
################################################################################################


def midpointRule(expression, a, b, n):
    """
    Evaluates the expression using the midpoint rule.
    """
    dx = (b - a) / n
    area = 0

    for i in range(n):
        x0 = (dx * i)
        x1 = (dx * (i + 1))
        x = (x1 + x0) / 2
        area += dx * eval(expression)

    return area

################################################################################################
# TRAPEZOID RULE
################################################################################################


def trapezoidRule(expression, a, b, n):
    """
    Evaluates the expression using the trapezoid rule
    """
    dx = (b - a) / n
    area = 0

    for i in range(n):
        x = (dx * i)
        a0 = eval(expression)
        x = (dx * (i + 1))
        a1 = eval(expression)

        area += (dx / 2) * (a0 + a1)

    return area

################################################################################################
# SIMPSON'S RULE
################################################################################################


def simpsonsRule(expression, a, b, n):
    """
    Evaluates the expression using simpson's rule.
    """
    return ((2 * midpointRule(expression, a, b, n)) + trapezoidRule(expression, a, b, n)) / 3

################################################################################################
# MAIN FUNCTION
################################################################################################


def main():
    (expression, a, b, n) = ui()
    print()
    print("Expression: " + expression)
    print("A value: " + str(a))
    print("B value: " + str(b))
    print("Sub-intervals: " + str(n))
    print()
    print("Left endpoint rule area: " + str(leftEndpointRule(expression, a, b, n)))
    print("Right endpoint rule area: " + str(rightEndpointRule(expression, a, b, n)))
    print("Midpoint rule area: " + str(midpointRule(expression, a, b, n)))
    print("Trapezoid rule area: " + str(trapezoidRule(expression, a, b, n)))
    print("Simpson's rule area: " + str(simpsonsRule(expression, a, b, n)))

# Program execution
main()
