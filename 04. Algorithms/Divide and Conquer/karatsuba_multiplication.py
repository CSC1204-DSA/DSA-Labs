"""
Karatsuba Multiplication for Two n-Digit Integers (assuming n is even)

The multiplication formula:
  (a × c × 10^n) + (b × d) + ((b × c + a × d) × 10^(n/2))
where:
  a, b = the first and second halves of the first integer,
  c, d = the first and second halves of the second integer.

This is implemented recursively for a divide-and-conquer approach:
ac, bd, bc, ad are computed similarly by splitting each sub-problem.
"""


def k_multiply(x, y):
    """
    Recursively computes the product of two integer lists (each digit as an element)
    using the Karatsuba multiplication algorithm.
    """
    # Base case: if either list is of length 1, just multiply the single digits
    if len(x) == 1 and len(y) == 1:
        return x[0] * y[0]

    # Split each number into two halves: a, b and c, d
    mid_x = len(x) // 2
    mid_y = len(y) // 2
    a, b = x[:mid_x], x[mid_x:]
    c, d = y[:mid_y], y[mid_y:]

    # Recursively calculate sub-products
    ac = k_multiply(a, c)
    bd = k_multiply(b, d)
    bc = k_multiply(b, c)
    ad = k_multiply(a, d)

    # Compute the length and midpoint for shifting
    n = len(x)  # Assuming len(x) == len(y)
    n2 = n // 2

    # Karatsuba formula
    return (ac * 10**n) + bd + (bc + ad) * 10**n2

if __name__ == '__main__':
    try:
        first_integer = [int(ch) for ch in input('first integer: ')]
        second_integer = [int(ch) for ch in input('second integer: ')]

        # Validate input lengths
        if len(first_integer) != len(second_integer):
            raise ValueError

        product = k_multiply(first_integer, second_integer)
        print(product)
    except ValueError:
        print('Invalid Inputs')

"""
This code implements Karatsuba multiplication, a divide-and-conquer approach for multiplying two large integers. 
Each number is split into two halves (a, b) and (c, d), and four sub-products (ac, bd, bc, ad) are computed recursively.
These sub-results are then combined using the Karatsuba formula to produce the final product more efficiently than standard long multiplication.
"""