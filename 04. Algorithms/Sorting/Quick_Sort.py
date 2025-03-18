"""
Quick Sort Algorithm (using the last element as the pivot)

Overview:
1. Choose the last element in the current sub-array as the pivot.
2. Partition the sub-array around the pivot such that:
   - Elements smaller than the pivot move to its left.
   - Elements larger than the pivot move to its right.
3. Recursively apply the above steps to the sub-arrays on the pivot's left and right.

Time Complexity:
  - Best/Average Case: O(n log n)
  - Worst Case: O(n^2)
Space Complexity: O(log n) (due to recursion stack)

The global 'count' variable tracks the total number of comparisons made during the partitioning.
"""

count = 0  # Global variable to count comparisons


def partition(array, left, right):
    """
    Partitions the portion of 'array' between indices 'left' and 'right' around a pivot.

    Steps:
      1. Initialize 'smaller_index' to left-1.
      2. Choose the pivot as array[right].
      3. Iterate i from 'left' to 'right-1':
         - If array[i] < pivot, increment 'smaller_index' and swap array[i] with array[smaller_index].
      4. Finally, swap the pivot (array[right]) with array[smaller_index+1] so that
         the pivot is in its correct sorted position.

    Args:
      array (list): The list of elements to be partitioned.
      left (int): Starting index of the sub-array.
      right (int): Ending index of the sub-array.

    Returns:
      int: The partition index, where the pivot is placed in sorted order.
    """
    global count
    smaller_index = left - 1
    pivot = array[right]

    # Compare each element with the pivot
    for i in range(left, right):
        count += 1  # Increment comparison count
        if array[i] < pivot:
            smaller_index += 1
            # Swap the current element with the element at 'smaller_index'
            array[smaller_index], array[i] = array[i], array[smaller_index]

    # Place the pivot element in its correct position
    array[smaller_index + 1], array[right] = array[right], array[smaller_index + 1]

    # Print the array state for demonstration (optional)
    print(array)

    # Return the pivot's new position
    return smaller_index + 1


def quick_sort(array, left, right):
    """
    Recursively sorts the sub-array from 'left' to 'right' using the Quick Sort algorithm.

    Args:
      array (list): The list of elements to be sorted.
      left (int): Starting index of the sub-array.
      right (int): Ending index of the sub-array.

    Returns:
      None: The list is sorted in place.
    """
    if left < right:
        # Partition the array and get the pivot index
        partitioning_index = partition(array, left, right)

        # Print the partition index for demonstration (optional)
        print(partitioning_index)

        # Recursively apply quick sort to the left and right sub-arrays
        quick_sort(array, left, partitioning_index - 1)
        quick_sort(array, partitioning_index + 1, right)


# Demonstration of quick_sort with various inputs

# 1. Partially unsorted array
array = [5, 9, 3, 10, 45, 2, 0]
quick_sort(array, 0, len(array) - 1)
print("Sorted array:", array)
print(f'Number of comparisons = {count}\n')

# 2. Already sorted array
sorted_array = [5, 6, 7, 8, 9]
quick_sort(sorted_array, 0, len(sorted_array) - 1)
print("Sorted array:", sorted_array)
print(f'Number of comparisons = {count}\n')

# 3. Reverse sorted array
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0,
                        -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
quick_sort(reverse_sorted_array, 0, len(reverse_sorted_array) - 1)
print("Sorted array:", reverse_sorted_array)
print(f'Number of comparisons = {count}')
