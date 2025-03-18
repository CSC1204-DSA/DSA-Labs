"""
Demonstration of calculating the factorial of a given number using two methods:

1. Iterative approach (iterative_factorial)
2. Recursive approach (recursive_factorial)

Examples:
- factorial(0) = 1
- factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
"""

def iterative_factorial(number):
    """
    Computes factorial of 'number' iteratively.
    Iterates from 1 to 'number', multiplying together the sequence of integers.

    Example:
      iterative_factorial(5) -> 120
    """
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Test the iterative factorial function
print(iterative_factorial(0))   # Expected output: 1
print(iterative_factorial(5))   # Expected output: 120
print(iterative_factorial(50))
# Expected output: 30414093201713378043612608166064768844377641568960512000000000000

def recursive_factorial(number):
    """
    Computes factorial of 'number' using recursion.
    Base case: factorial(0) = 1
    Recursive case: factorial(n) = n × factorial(n - 1)

    NOTE:
      For very large 'number', this may cause a RecursionError if the recursion
      depth exceeds Python's default limit.
    """
    if number <= 1:
        return 1
    else:
        return number * recursive_factorial(number - 1)

# Test the recursive factorial function
print(recursive_factorial(0))   # Expected output: 1
print(recursive_factorial(5))   # Expected output: 120
print(recursive_factorial(50))
# Expected output: 30414093201713378043612608166064768844377641568960512000000000000

# Attempting recursive_factorial(1000) might cause a RecursionError in Python,
# because it exceeds the default recursion depth limit:
# print(recursive_factorial(1000))
