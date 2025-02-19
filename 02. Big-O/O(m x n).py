import time  # Imported for timing if needed (not specifically used in this example)

# array1 (length m = 5 in this example)
array1 = ['a', 'b', 'c', 'd', 'e']

# array2 (length n = 5 in this example)
array2 = [1, 2, 3, 4, 5]


def pairs(array1, array2):
    """
    Prints every combination of elements between array1 and array2.

    Time Complexity:
    - We use a nested loop:
        - Outer loop runs m times (m = len(array1))
        - Inner loop runs n times (n = len(array2))
    - Total operations: m * n
    - Hence, the overall time complexity is O(m * n).
    """

    # Outer loop: iterates over all elements in array1
    for i in range(len(array1)):  # Runs m times
        # Inner loop: iterates over all elements in array2 for each element in array1
        for j in range(len(array2)):  # Runs n times
            # Print the pair (current element from array1 and current element from array2)
            print(array1[i], array2[j])  # m * n prints in total


# Call the function to print all pairs
pairs(array1, array2)

# Final Time Complexity = O(m * n)
