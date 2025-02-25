"""
Merges two sorted arrays (array1 and array2) into a single sorted array.
Example:
--------
If array1 = [1, 3, 5, 7] and array2 = [2, 4, 6, 8, 10, 12],
the result is [1, 2, 3, 4, 5, 6, 7, 8, 10, 12].
"""

def merge(array1, array2):
    """
    1. Initialize two pointers (indexes) for both arrays.
    2. Compare elements at these pointers.
    3. Append the smaller element to 'new_array' and move its pointer forward.
    4. Once one array is exhausted, append the remaining elements of the other array.
    """
    new_array = []  # Will store the merged sorted array
    flag = 0        # Will track which array got exhausted first
    first_array_index = 0
    second_array_index = 0

    # Loop until the end of one of the arrays is reached
    while not (first_array_index >= len(array1) or second_array_index >= len(array2)):
        # Compare elements at the current pointers
        if array1[first_array_index] <= array2[second_array_index]:
            new_array.append(array1[first_array_index])
            first_array_index += 1
        else:
            new_array.append(array2[second_array_index])
            second_array_index += 1

        # Check if the first array is exhausted
        if first_array_index == len(array1):
            flag = 1  # Indicate that array1 ended first

    # Append any leftover elements from array2 (if array1 ended first)
    if flag == 1:
        for item in array2[second_array_index:]:
            new_array.append(item)
    else:
        # Otherwise, append leftover elements from array1
        for item in array1[first_array_index:]:
            new_array.append(item)

    return new_array

# Example usage:
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8, 10, 12]
print(merge(array1, array2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
