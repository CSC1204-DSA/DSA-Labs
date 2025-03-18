def quicksort(arr):
    """
    Sorts a list 'arr' in ascending order using the Quick Sort algorithm
    with the last element as the pivot.

    Quick Sort Overview:
      1. If the array has fewer than 2 elements, it is already sorted.
      2. Choose the last element of 'arr' as the pivot.
      3. Partition the array into three lists:
         - 'smaller': elements less than the pivot,
         - 'equal': elements equal to the pivot,
         - 'larger': elements greater than the pivot.
      4. Recursively apply quicksort to 'smaller' and 'larger'.
      5. Concatenate the sorted smaller list, the equal list,
         and the sorted larger list.

    Time Complexity:
      - Average Case: O(n log n)
      - Worst Case: O(n^2)
    """

    # Base case: an array of length less than 2 is already sorted
    if len(arr) < 2:
        return arr
    else:
        # Choose the last element as the pivot
        pivot = arr[-1]

        # Partition into three sub-lists
        smaller, equal, larger = [], [], []

        # Compare each element to the pivot
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        # Recursively sort smaller and larger, then combine with 'equal'
        return quicksort(smaller) + equal + quicksort(larger)

# Example usage
l = [6, 8, 1, 4, 10, 7, 8.9, 3, 2, 5]
print("Original list:", l)
sorted_list = quicksort(l)
print("Sorted list:  ", sorted_list)
