# -*- coding: utf-8 -*-
"""
small-fibonacci-number.py

Task:          Given an integer n, find the n-th Fibonacci number Fn.
Input format:  The input consists of a single integer n.
Constraints:   0 <= n <= 45
Output format: Output Fn
Time limits:   Python: 5 seconds
Memory limit:  512 MB
"""


def Fibonacci(n):
    """
    Args:
        n (int): The index n of the fibonacci number

    Returns:
        int: the n-th Fibonacci number
    """
    # create fibonacci list
    fib = []
    fib.append(0)  # fib[0] = 0
    fib.append(1)  # fib[1] = 1
    for i in range(2, n+1):  # loops from 2 through n inclusive
        fib.append(fib[i-1] + fib[i-2])  # appends new fibonacci for every i

    return fib[n]  # returns last fibonacci(Fn)


# get input
n = int(input())

# print n-th Fibonacci number
print(Fibonacci(n))
