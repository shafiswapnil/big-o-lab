import random
from functools import lru_cache


def constant_access(data):
    """O(1) - Access the first element regardless of list size."""
    return data[0]


def linear_search(data, target):
    """O(n) - Search through every element until target is found."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def sort_data(data):
    """O(n log n) - Python's built-in Timsort."""
    return sorted(data)


def bubble_sort(data):
    """O(n^2) - Classic nested loop sort."""
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def fib_naive(n):
    """O(2^n) - Naive recursive Fibonacci."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)
def fib_memoized(n):
    """O(n) - Memoized Fibonacci using lru_cache."""
    if n <= 1:
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)
