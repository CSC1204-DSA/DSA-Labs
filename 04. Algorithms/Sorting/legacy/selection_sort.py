def selection_sort(arr):
    """
    Sorts a list 'arr' in ascending order using the Selection Sort algorithm.

    Selection Sort Overview:
      1. We maintain a 'spot_marker' that indicates the position in the array
         we want to place the next smallest element.
      2. Starting from 'spot_marker', iterate through the rest of the array:
         - If we find an element smaller than the one at arr[spot_marker],
           swap them immediately.
      3. Increment 'spot_marker' to lock in that position as sorted, and
         continue until the entire list is sorted.

    Note: A more traditional selection sort implementation typically performs
    only one swap per outer loop. This version swaps immediately upon finding
    a smaller element, but the result is still a correctly sorted list.
    """
    spot_marker = 0  # Marks the position where the next smallest element should be placed
    while spot_marker < len(arr):
        # Compare the current spot_marker element with all elements to its right
        for num in range(spot_marker, len(arr)):
            # If we find an element smaller than arr[spot_marker], swap them
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        # Move the spot_marker forward to lock in that sorted element
        spot_marker += 1

# Example usage:
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)
print(l)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
