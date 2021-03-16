#!/usr/bin/env python3
import unittest

def fibonacci_deco(f):
    cache = {}
    def helper(n):
        print(f"Enter cache for {n}: ", cache)
        if n in cache:
            print(f"hit for {n}")
            return cache[n]
        else:
            return cache.setdefault(n, f(n))
    return helper

@fibonacci_deco
def fibonacci(n):
    """
    :type n: int
    :rtype: int
    return the nth Fibonacci term as per the given sequence
    0th fibonacci term --> 0
    1st fibonacci term --> 1
    2nd fibonacci term --> 1
    3rd fibonacci term --> 2
    4th fibonacci term --> 3
    5th fibonacci term --> 5
    etc.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
# def deco(f):
#     '''
#     main decorator function
#     '''
#     cache = {1:2}
#     def helper(n):
#         '''
#         decorator helper
#         '''
#         print("start decorating")
#         print(cache)
#         f(n)
#         print("end decorating")
#     helper.__doc__ = f.__doc__
#     return helper

# @deco
# def func(n):
#     '''
#     to be decorated
#     '''
#     print(f"Hello n is {n}")

# print(func.__doc__)
# func(5)

