def insertion_sort(arr):
    """
    Sorts the list 'arr' in ascending order using the Insertion Sort algorithm.

    Insertion Sort Overview:
      - Treat the sub-array arr[0:key] as already sorted.
      - Take the element at position 'key', and shift it left until it's in the correct place.
      - Moves through the list from left to right, growing the "sorted" portion as it goes.

    Args:
      arr (list): The list of elements to be sorted (in place).

    Returns:
      None: The list is sorted in place, so no return value.
    """
    # Start from index 1, since arr[0] is trivially sorted by itself
    for key in range(1, len(arr)):

        # If the current element is less than the previous element,
        # then we need to place it in the correct sorted position
        if arr[key] < arr[key - 1]:
            j = key
            # Move the element left (swapping as needed) until it's no longer smaller
            while j > 0 and arr[j] < arr[j - 1]:
                # Swap the elements
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1


# Example usage:
l = [6, 1, 8, 4, 10]
insertion_sort(l)
print(l)  # Expected output: [1, 4, 6, 8, 10]
