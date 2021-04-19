#!/usr/bin/env python3
import unittest
import logging
FORMAT = '%(filename)s-%(funcName)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

numcalls = 0
def fib_no_cache(n, stacksize):
    global numcalls
    '''
    Fibonacci implementation without cache
    '''
    numcalls += 1
    logging.info(f"Stack size indicative of space complexity is: {stacksize}")
    logging.info(f"Numcalls indicative of time complexity is: {numcalls}")
    if n <= 1:
        return n
    else:
        return fib_no_cache(n-1, stacksize+1) + fib_no_cache(n-2, stacksize+1)

print(fib_no_cache(15, 1))

numcalls = 0
def fibonacci_deco(f):
    '''
    Decorator used on no cache fibonacci implementation to change it to implementation with cache,
    without modifying the original no cache implementation
    '''
    cache = {}
    def helper(n, stacksize):
        global numcalls
        numcalls += 1
        logging.info(f"n = {n} Enter cache: {cache}")
        logging.info(f"n = {n} Stack size indicative of space complexity is: {stacksize}")
        logging.info(f"n = {n} Numcalls indicative of time complexity is: {numcalls}")
        if n in cache:
            logging.info(f"n = {n} Cache hit")
            return cache[n]
        else:
            return cache.setdefault(n, f(n, stacksize + 1))
    return helper

@fibonacci_deco # simply use decorator to convert no cache implementation to start using cache
def fib_no_cache_decorated(n, stacksize):
    global numcalls
    '''
    Fibonacci implementation without cache
    '''
    numcalls += 1
    logging.info(f"n = {n} Stack size indicative of space complexity is: {stacksize}")
    logging.info(f"n = {n} Numcalls indicative of time complexity is: {numcalls}")
    if n <= 1:
        return n
    else:
        return fib_no_cache_decorated(n-1, stacksize+1) + fib_no_cache_decorated(n-2, stacksize+1)

print(fib_no_cache_decorated(15, 1))

cache = {0:0, 1:1}
numcalls = 0
def fibonacci_with_cache(n, stacksize):
    '''
    Fibonacci implementation with cache
    '''
    global numcalls
    global cache
    numcalls += 1
    logging.info(f"Enter cache for {n}: {cache}")
    logging.info(f"Stack size indicative of space complexity is: {stacksize}")
    logging.info(f"Numcalls indicative of time complexity is: {numcalls}")
    if n in cache:
        logging.info(f"Cache hit for {n}")
        return cache[n]
    else:
        return cache.setdefault(n, fibonacci_with_cache(n-1, stacksize+1) + fibonacci_with_cache(n-2, stacksize+1))

print(fibonacci_with_cache(15, 1))


def fibonacci_iterative(n):
    t0 = 0
    t1 = 1
    for i in range(2, n+1):
        ans = t0 + t1
        t0, t1 = t1, ans
    logging.info(f"answer is {ans}")
    return ans

print(fibonacci_iterative(15))


# @fibonacci_deco
# def fibonacci(n):
#     """
#     Fibonacci implementation with cache using a decorator to not change the original naive (non-cache) implementation
#     :type n: int
#     :rtype: int
#     return the nth Fibonacci term as per the given sequence
#     0th fibonacci term --> 0
#     1st fibonacci term --> 1
#     2nd fibonacci term --> 1
#     3rd fibonacci term --> 2
#     4th fibonacci term --> 3
#     5th fibonacci term --> 5
#     etc.
#     """
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))

# This is a simple decoration demo in python
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

