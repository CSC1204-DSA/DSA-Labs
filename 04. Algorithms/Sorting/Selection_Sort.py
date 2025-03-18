def selection_sort(array):
    """
    Sorts a list 'array' in ascending order using the Selection Sort algorithm.

    Selection Sort Overview:
      1. For each position 'i' in the list (except the last), find the minimum element
         from the unsorted sub-list array[i+1 ... end].
      2. If that minimum is smaller than the element at array[i], swap them.
      3. Move 'i' one step to the right and repeat.

    Time Complexity:
      - O(n^2) in all cases (worst, average, and best).
    """
    count = 0  # Tracks the number of comparisons

    # Outer loop to position the boundary between sorted and unsorted portions
    for i in range(len(array) - 1):  # '-1' since the last element will automatically be sorted
        print(array)  # Print the array to illustrate progress
        minimum = array[i]       # Assume current position 'i' holds the minimum value
        minimum_index = i        # Track the index of this assumed minimum

        # Inner loop to find the true minimum in the unsorted sub-list
        for j in range(i + 1, len(array)):
            count += 1  # Each comparison with the current minimum
            if array[j] < minimum:
                minimum = array[j]
                minimum_index = j

        # If a new minimum was found, swap it with the element at 'i'
        if minimum_index != i:
            array[minimum_index], array[i] = array[i], array[minimum_index]

    return f"{array} \nNumber of comparisons = {count}"


# Demonstration of selection_sort with different arrays

# 1. Partially unsorted array
array = [5, 9, 3, 10, 45, 2, 0]
print(selection_sort(array))
"""
Expected intermediate prints showing each pass.
Example Final Output:
[0, 2, 3, 5, 9, 10, 45]
Number of comparisons = 21
"""

# 2. Already sorted array
sorted_array = [5, 6, 7, 8, 9]
print(selection_sort(sorted_array))
"""
Expected minimal changes due to already being sorted.
Final Output:
[5, 6, 7, 8, 9]
Number of comparisons = 10
"""

# 3. Reverse sorted array
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5,
                        -6, -7, -8, -9, -10]
print(selection_sort(reverse_sorted_array))
"""
Expected to require many comparisons due to the reverse order.
Final Output:
[-10, -9, -8, -7, ..., 5, 6, 7, 8, 9]
Number of comparisons = 190
"""
