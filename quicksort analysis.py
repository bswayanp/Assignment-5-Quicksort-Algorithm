"""
Assignment 5: Quicksort Algorithm Implementation, Analysis, and Randomization
Author: Bhaghava
Course: Algorithms / Data Structures

This file implements:
1. Deterministic Quicksort
2. Randomized Quicksort
3. Empirical performance comparison
"""

import random
import time
import sys
sys.setrecursionlimit(1000000)



def partition(arr, low, high):
    """
    Partition using last element as pivot (deterministic).
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)




def randomized_partition(arr, low, high):
    """
    Choose a random pivot and swap with last element.
    """
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# ==========================================================
# PART 3: EMPIRICAL ANALYSIS
# ==========================================================

def generate_data(size, distribution="random"):
    if distribution == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Unknown distribution type")


def measure_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr, 0, len(arr) - 1)
    end_time = time.perf_counter()
    return end_time - start_time


def empirical_test():
    sizes = [1000, 5000, 10000]
    distributions = ["random", "sorted", "reverse"]

    print("\n===== EMPIRICAL ANALYSIS RESULTS =====\n")

    for size in sizes:
        print(f"\nInput Size: {size}")
        for dist in distributions:
            data = generate_data(size, dist)

            arr1 = data.copy()
            arr2 = data.copy()

            det_time = measure_time(deterministic_quicksort, arr1)
            rand_time = measure_time(randomized_quicksort, arr2)

            print(f"Distribution: {dist}")
            print(f"Deterministic Time: {det_time:.6f} seconds")
            print(f"Randomized Time:    {rand_time:.6f} seconds")
            print("-" * 40)


if __name__ == "__main__":
    empirical_test()