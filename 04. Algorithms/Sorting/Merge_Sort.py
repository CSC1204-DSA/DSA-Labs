"""
Merge Sort Implementation

Merge Sort uses a divide-and-conquer strategy:
1. Recursively split the array into two halves until each sub-array contains only one element.
2. Merge the sub-arrays back together in sorted order.

Time Complexity: O(n log n)
Space Complexity: O(n)

The global variable 'count' tracks the total number of comparisons made during the merging step.
"""

count = 0  # Global variable to track the number of comparisons in merge function


def merge_sort(array):
    """
    Recursively divides the list 'array' into two halves, sorts each half,
    and merges them in sorted order.

    Args:
      array (list): The list of elements to be sorted.

    Returns:
      list: A new list that is sorted in ascending order.
    """
    # Base case: If the array length is 1, it's already sorted
    if len(array) == 1:
        return array

    # Find the middle index to split the array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    # Print statements to visualize how the array is being split
    print(f'Left : {left_array}')
    print(f'Right : {right_array}')

    # Recursively sort the left and right halves, then merge
    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(left, right):
    """
    Merges two sorted lists 'left' and 'right' into a single sorted list.

    During the merge process, elements from 'left' and 'right' are compared 
    and appended in ascending order.

    Args:
      left (list): Sorted list.
      right (list): Sorted list.

    Returns:
      list: A combined sorted list containing elements from both 'left' and 'right'.
    """
    global count
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0
    sorted_array = []

    # Merge the two lists while both have elements to compare
    while left_index < l and right_index < r:
        # Each comparison is counted
        count += 1
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Print the partially merged list for visualization
    print(sorted_array + left[left_index:] + right[right_index:])

    # Append any remaining elements from left or right sub-list
    return sorted_array + left[left_index:] + right[right_index:]


# -----------------------------------
# Demonstration with different arrays
# -----------------------------------

# 1. Example partially unsorted array
array = [5, 9, 3, 10, 45, 2, 0]
print("Final sorted:", merge_sort(array))
print(f'Number of comparisons = {count}\n')

# 2. Reset 'count' for a new example: already sorted array
count = 0
sorted_array = [5, 6, 7, 8, 9]
print("Final sorted:", merge_sort(sorted_array))
print(f'Number of comparisons = {count}\n')

# 3. Reverse sorted array
count = 0
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
print("Final sorted:", merge_sort(reverse_sorted_array))
print(f'Number of comparisons = {count}')
