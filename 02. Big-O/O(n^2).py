import time  # Imported, though not strictly used in these demonstrations

# Example array of strings
array = ['a', 'b', 'c', 'd', 'e']


def log_all_pairs(array):
    """
    Prints all possible pairs of elements from the 'array'.

    Time Complexity:
    - We have two nested loops, each iterating over the entire array (size n).
    - Hence, the total operations are ~n * n = n^2.
    - Overall complexity: O(n^2).
    """

    # Outer loop: runs from 0 to n-1 (where n = len(array))
    for i in range(len(array)):  # O(n)
        # Inner loop: for each element of the outer loop, run again from 0 to n-1
        for j in range(len(array)):  # O(n)
            # Print the pair formed by the elements at indices i and j
            print(array[i], array[j])  # O(1) each time; total n * n = n^2 prints


# Call the function to demonstrate pair printing
log_all_pairs(array)

# Explanation of Time Complexity for log_all_pairs:
# - Outer loop: O(n)
# - Inner loop: O(n) for each iteration of the outer loop => O(n * n) = O(n^2)
# - No additional loops or major operations => overall O(n^2)

# Another array to demonstrate a slightly different function
new_array = [1, 2, 3, 4, 5]


def print_numbers_then_pairs(array):
    """
    First prints each element in 'array', then prints all possible pairs.

    Time Complexity:
    - Printing all elements with a single loop: O(n).
    - Printing all pairs with nested loops: O(n^2).
    - Total: O(n) + O(n^2) = O(n^2) (dominant term is n^2).
    """

    # Print a header message (constant time)
    print("The numbers are : ")  # O(1)

    # Single loop to print each number in the array
    for i in range(len(array)):  # O(n)
        print(array[i])  # O(1) each time; total O(n)

    # Print another header message (constant time)
    print("The pairs are :")  # O(1)

    # Outer loop to go through each element in the array
    for i in range(len(array)):  # O(n)
        # Inner loop to again go through each element
        for j in range(len(array)):  # O(n)
            # Print the pair of elements at indices i and j
            print(array[i], array[j])  # O(1) each time; total n * n = n^2 prints


# Call the function to demonstrate printing numbers, then pairs
print_numbers_then_pairs(new_array)

# Explanation of Time Complexity for print_numbers_then_pairs:
# - A single loop to print numbers: O(n)
# - Nested loops to print pairs: O(n * n) = O(n^2)
# - Combined => O(n + n^2) = O(n^2)
