def insertion_sort(array):
    """
    Sorts a list 'array' in ascending order using the Insertion Sort algorithm.

    Insertion Sort Overview:
      1. Assume the first element is in its correct position (a "sorted" sub-list of size 1).
      2. Iterate over each remaining element, inserting it into the correct position
         within the already-sorted sub-list to the left.
      3. This "insertion" is performed by shifting larger elements to the right
         until the correct place for the current element is found.

    Time Complexity:
      - Worst/Average Case: O(n^2)
      - Best Case (almost sorted list): O(n)

    Args:
      array (list): The list of elements (numbers) to be sorted.

    Returns:
      str: A formatted string with the sorted list and the total number of comparisons.
    """

    count = 0  # Track the number of comparisons
    # Start from the second element, since the first is trivially "sorted"
    for i in range(1, len(array)):
        print(array)  # Print the array to show progress

        # Compare the current element with the last sorted element
        last_sorted = array[i - 1]
        count += 1

        # If the current element (array[i]) is smaller, insert it into correct position
        if array[i] < last_sorted:
            temp = array[i]  # Temporarily store the current element
            # Move backwards through the sorted portion to find correct insertion position
            for j in range(i - 1, -1, -1):
                count += 1  # Increment comparison count
                # Shift elements to the right if they are greater than 'temp'
                if temp < array[j]:
                    # If we've reached the start, place 'temp' at index 0
                    if j == 0:
                        array[j + 1] = array[j]
                        array[j] = temp
                    else:
                        array[j + 1] = array[j]
                else:
                    # Correct position found; insert 'temp' here
                    array[j + 1] = temp
                    break
    # Return final sorted array and the total comparisons
    return f'{array} \nNumber of comparisons = {count}'


# Demonstration with different types of lists

# 1. Partially unsorted array
array = [5, 9, 3, 10, 45, 2, 0]
print(insertion_sort(array))
"""
Expected process prints showing the sorting steps:
[5, 9, 3, 10, 45, 2, 0]
[5, 9, 3, 10, 45, 2, 0]
[3, 5, 9, 10, 45, 2, 0]
...
Final Output: [0, 2, 3, 5, 9, 10, 45]
Number of comparisons = <some count>
"""

# 2. Already sorted array
sorted_array = [5, 6, 7, 8, 9]
print(insertion_sort(sorted_array))
"""
Expected minimal comparisons:
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
...
Final Output: [5, 6, 7, 8, 9]
Number of comparisons = <small count>
"""

# 3. Reverse sorted array
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
print(insertion_sort(reverse_sorted_array))
"""
Expected to do maximum shifting and comparisons:
Final Output: [-10, -9, -8, ..., 7, 8, 9]
Number of comparisons = <large count>
"""
