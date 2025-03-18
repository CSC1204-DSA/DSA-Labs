"""
Demonstration of memoization techniques in Python.

Three approaches are shown:
1. No memoization: squaring_without_memoization
2. Manual memoization: squaring_with_memoization (uses a dictionary cache)
3. Built-in memoization via functools.lru_cache
"""

import time
import random
from functools import lru_cache

# List to store the execution times of each approach
times = []

def squaring_without_memoization(number):
    """
    Returns the square of 'number' without any memoization.
    This function performs a straightforward computation every time it's called.
    """
    return number ** 2

# Generate an array of random integers between 1 and 10 (inclusive)
# Adjust the size as needed for testing performance.
array = [random.randint(1, 10) for _ in range(10000000)]

# ------------------------------
# 1. No memoization approach
# ------------------------------
t1 = time.time()
for num in array:
    print(squaring_without_memoization(num))  # Each call performs the square operation
t2 = time.time()
times.append(t2 - t1)  # Record the time taken


# ------------------------------
# 2. Manual memoization
# ------------------------------
cache = {}  # Dictionary to store previously computed results

def squaring_with_memoization(number):
    """
    Returns the square of 'number' using manual memoization.
    If the result is in 'cache', it returns it immediately.
    Otherwise, it computes the square, stores it in the cache,
    and returns the result.
    """
    if number in cache:
        return cache[number]  # Return cached result
    else:
        # Compute and store in the cache
        cache[number] = number ** 2
        return cache[number]

t1 = time.time()
for num in array:
    print(squaring_with_memoization(num))
t2 = time.time()
times.append(t2 - t1)


# ------------------------------
# 3. Memoization with functools.lru_cache
# ------------------------------
@lru_cache(maxsize=10000)
def squaring(number):
    """
    Returns the square of 'number', using LRU (Least Recently Used) cache.
    'maxsize' defines the maximum cache size before older entries are discarded.
    """
    return number ** 2

print(array)  # Display the generated array (optional)
t1 = time.time()
for num in array:
    print(squaring(num))
t2 = time.time()
times.append(t2 - t1)

# Print the recorded times to see the performance of each approach
print(times)
# Example output for array size = 10,000,000:
# [203.95188665390015, 148.48580384254456, 148.26833629608154]

# Print the manual cache dictionary
print(cache)
# Example: {8: 64, 7: 49, 6: 36, 1: 1, 4: 16, 9: 81, 2: 4, 5: 25, 3: 9, 10: 100}

# Print the lru_cache info
print(squaring.cache_info())
# Example output for array size = 10,000,000:
# CacheInfo(hits=9999990, misses=10, maxsize=10000, currsize=10)
