def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Bubble Sort Overview:
      - Repeatedly traverses the list, comparing adjacent items.
      - Swaps them if they are out of order.
      - Continues until no more swaps are needed, indicating the list is sorted.

    Args:
      arr (list): The list to be sorted in place.

    Returns:
      None: The list is sorted in place, so no return value.
    """
    swap_happened = True
    # Continue the loop as long as at least one swap happened in the previous pass
    while swap_happened:
        print('bubble sort status:', arr)
        swap_happened = False
        # Go through each pair of adjacent elements
        for i in range(len(arr) - 1):
            # If elements are out of order, swap them
            if arr[i] > arr[i + 1]:
                swap_happened = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Test the bubble_sort function with different cases
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]  # Original case
bubble_sort(l)
