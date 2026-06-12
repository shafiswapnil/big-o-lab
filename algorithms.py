import random


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


## What This Code Does
# 
# import random: brings in the random module, which the benchmark harness will use later to generate test data.
# 
# constant_access(data): grabs the first element of a list. Accessing an item by index is O(1) because it takes the same time whether the list has 10 items or 10 million.
# 
# linear_search(data, target): loops through every element to find the target. In the worst case, it checks every single item, making it O(n).
# 
# sort_data(data): wraps Python's sorted() builtin, which returns a new sorted list without modifying the original.
# Timsort is a hybrid algorithm combining merge sort and insertion sort. It's O(n log n) because it repeatedly divides the data into halves (log n splits) and merges them back together (n work per merge level).
#
# data.copy(): creates a copy so the original list isn't modified.
#
# The outer loop (for i in range(n)) runs n times. The inner loop (for j in range(0, n - i - 1)) compares adjacent elements and swaps them if they're out of order.
#
# Because every element is compared against nearly every other element, the total comparisons approach n × n. That's what makes it O(n²).


## Why do both sort functions return the same result?
#
# Both sort_data and bubble_sort produce the same sorted output. The difference isn't in the result. It's in how long they take to get there.
#
# On a list of 5 elements, both finish instantly. On 100,000 elements, that difference becomes dramatic. That's exactly what you'll measure in the next step.