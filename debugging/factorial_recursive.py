#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: factorial
    ------------------
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is calculated.

    Returns:
    int: The factorial of n. If n is 0, returns 1 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read integer from command-line argument and compute factorial
f = factorial(int(sys.argv[1]))
print(f)