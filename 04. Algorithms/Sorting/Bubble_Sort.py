def bubble_sort(array):
    """
    Sorts a list 'array' in ascending order using Bubble Sort.
    In each pass, adjacent elements are compared and swapped if in the wrong order,
    which effectively bubbles up the largest element to the end of the list.

    Time Complexity:
      - Worst/Average Case: O(n^2)
      - Best Case (already sorted list): O(n)

    Args:
      array (list): The list of elements (numbers) to be sorted.

    Returns:
      str: A formatted string with the sorted array and the total number of comparisons.
    """

    # 'count' tracks the number of comparisons
    count = 0

    # Outer loop runs (n-1) times for an array of length n
    for i in range(len(array) - 1):
        # Print the current state of the array (for demonstration)
        print(array)

        # Inner loop goes up to the unsorted portion (len(array) - i - 1)
        for j in range(len(array) - i - 1):
            count += 1  # Increment comparison count

            # If the current element is bigger than the next, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    # Return a summary string with the final array and number of comparisons
    return (f'{array} \nNumber of comparisons = {count}')


def optimized_bubble_sort(array):
    """
    Optimized Bubble Sort that terminates early if the list becomes sorted
    before going through all passes.

    Similar to bubble_sort, but an additional 'swap' flag keeps track of whether
    any swap took place in the current pass. If no swaps occur, the list is 
    already sorted and we can exit early, saving time.

    Time Complexity:
      - Worst/Average Case: O(n^2)
      - Best Case (already sorted list): O(n)

    Args:
      array (list): The list of elements (numbers) to be sorted.

    Returns:
      str: A formatted string with the sorted array and the total number of comparisons.
    """

    count = 0

    # Outer loop runs (n-1) times unless the array gets sorted earlier
    for i in range(len(array) - 1):
        swap = False  # Tracks whether a swap occurred in the current pass
        print(array)  # Print the array state for demonstration

        for j in range(len(array) - i - 1):
            count += 1  # Increment comparison count

            # If current element is bigger than the next, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True

        # If no swaps occurred, the list is already sorted; break out early
        if not swap:
            return (f'{array} \nNumber of comparisons = {count}')

    return (f'{array} \nNumber of comparisons = {count}')


# Demonstration

# Standard Bubble Sort
unsorted_array = [5, 9, 3, 10, 45, 2, 0]
print("Standard Bubble Sort:")
print(bubble_sort(unsorted_array), "\n")

sorted_array = [5, 6, 7, 8, 9]
print("Standard Bubble Sort on an already sorted list:")
print(bubble_sort(sorted_array), "\n")

# Optimized Bubble Sort
unsorted_array1 = [5, 9, 3, 10, 45, 2, 0]
print("Optimized Bubble Sort:")
print(optimized_bubble_sort(unsorted_array1), "\n")

sorted_array1 = [5, 6, 7, 8, 9]
print("Optimized Bubble Sort on an already sorted list:")
print(optimized_bubble_sort(sorted_array1))
