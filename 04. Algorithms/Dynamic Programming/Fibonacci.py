"""
Demonstration of calculating Fibonacci numbers using both a naive recursive approach
and a dynamic programming approach (memoization). The dynamic version efficiently
stores previously computed results to avoid redundant calculations.
"""

import time

def fibonacci(n):
    """
    Naive recursive Fibonacci function.
    Returns the n-th Fibonacci number.
    """
    if n < 2:
        return n  # Base cases: fib(0) = 0, fib(1) = 1
    else:
        # Recursively compute fib(n) with overlapping subproblems (inefficient)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Global cache (dictionary) for memoizing results in dynamic_fibonacci
cache = {}

def dynamic_fibonacci(n):
    """
    Efficient recursive Fibonacci using memoization.
    Stores intermediate results in 'cache' to avoid repeated computations.
    """
    if n in cache:
        # If the result is already computed, return it
        return cache[n]
    else:
        # If n < 2, the answer is n itself (base cases).
        if n < 2:
            return n
        else:
            # Recursively compute, store in cache, then return
            cache[n] = dynamic_fibonacci(n - 1) + dynamic_fibonacci(n - 2)
            return cache[n]

# Compare run times of the naive fibonacci and the memoized dynamic_fibonacci
# for fib(30):
t1 = time.time()
print(fibonacci(30))
t2 = time.time()
print(f"Naive recursion time for fib(30): {t2 - t1}")

# Compare with dynamic version for fib(30):
t1 = time.time()
print(dynamic_fibonacci(30))
t2 = time.time()
print(f"Dynamic recursion time for fib(30): {t2 - t1}")

# Call dynamic_fibonacci for larger n to demonstrate efficiency:
t1 = time.time()
print(dynamic_fibonacci(60))
t2 = time.time()
print(f"Dynamic recursion time for fib(60): {t2 - t1}")

t1 = time.time()
print(dynamic_fibonacci(100))
t2 = time.time()
print(f"Dynamic recursion time for fib(100): {t2 - t1}")

t1 = time.time()
print(dynamic_fibonacci(1000))
t2 = time.time()
print(f"Dynamic recursion time for fib(1000): {t2 - t1}")

# Note:
# fibonacci(1000) using the naive approach would be extremely slow and is not attempted.
