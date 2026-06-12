import time
import random
from algorithms import constant_access, linear_search, sort_data, bubble_sort


def measure_time(func, *args):
    """Measure execution time of a function using perf_counter."""
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


def run_benchmarks():
    """Run all algorithms across increasing input sizes."""
    sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]
    results = {
        "O(1) - Constant Access": [],
        "O(n) - Linear Search": [],
        "O(n log n) - Timsort": [],
        "O(n^2) - Bubble Sort": [],
    }

    for size in sizes:
        data = [random.randint(1, 1000000) for _ in range(size)]
        target = data[-1]

        # O(1)
        t = measure_time(constant_access, data)
        results["O(1) - Constant Access"].append(t)

        # O(n)
        t = measure_time(linear_search, data, target)
        results["O(n) - Linear Search"].append(t)

        # O(n log n)
        t = measure_time(sort_data, data)
        results["O(n log n) - Timsort"].append(t)

        # O(n^2) - skip very large sizes to avoid long waits
        if size <= 10000:
            t = measure_time(bubble_sort, data)
            results["O(n^2) - Bubble Sort"].append(t)
        else:
            results["O(n^2) - Bubble Sort"].append(None)

    return sizes, results


if __name__ == "__main__":
    sizes, results = run_benchmarks()

    print(f"{'Size':<10}", end="")
    for name in results:
        print(f"{name:<28}", end="")
    print()
    print("-" * 120)

    for i, size in enumerate(sizes):
        print(f"{size:<10}", end="")
        for name in results:
            t = results[name][i]
            if t is not None:
                print(f"{t:<28.6f}", end="")
            else:
                print(f"{'skipped':<28}", end="")
        print()



## Command to Run

# python3 benchmark.py