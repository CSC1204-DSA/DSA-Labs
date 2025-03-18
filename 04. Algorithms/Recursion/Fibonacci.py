"""
Demonstration of two approaches to find the Fibonacci number at a given index:

Fibonacci Sequence:
  Index:  0  1  2  3  4  5   6   7   8   9   10  11  12  ...
  Value:  0  1  1  2  3  5   8  13  21  34   55  89  144 ...

Examples:
  fibonacci(0) -> 0
  fibonacci(1) -> 1
  fibonacci(5) -> 5
"""


def iterative_fibonacci(index):
    """
    Computes the Fibonacci number at a given index using an iterative approach.

    Algorithm:
      - Start with the first two Fibonacci numbers: 0 and 1.
      - If index is 0 or 1, return the corresponding number immediately.
      - Otherwise, iterate from 2 up to 'index', updating the sum of the last two numbers.
    """
    first_number = 0
    second_number = 1

    if index == 0:
        return first_number  # Fibonacci(0) = 0
    if index == 1:
        return second_number  # Fibonacci(1) = 1

    for _ in range(2, index + 1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number


# Test the iterative Fibonacci function
print(iterative_fibonacci(0))  # Expected output: 0
print(iterative_fibonacci(1))  # Expected output: 1
print(iterative_fibonacci(5))  # Expected output: 5
print(iterative_fibonacci(7))  # Expected output: 13
print(iterative_fibonacci(10))  # Expected output: 55
print(iterative_fibonacci(12))  # Expected output: 144


def recursive_fibonacci(index):
    """
    Computes the Fibonacci number at a given index using a recursive approach.

    Base cases:
      - Fibonacci(0) = 0
      - Fibonacci(1) = 1
    Recursive step:
      - Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    """
    if index == 0:
        return 0
    if index == 1:
        return 1
    return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)


# Test the recursive Fibonacci function
print(recursive_fibonacci(0))  # Expected output: 0
print(recursive_fibonacci(1))  # Expected output: 1
print(recursive_fibonacci(5))  # Expected output: 5
print(recursive_fibonacci(7))  # Expected output: 13
print(recursive_fibonacci(10))  # Expected output: 55
print(recursive_fibonacci(12))  # Expected output: 144
