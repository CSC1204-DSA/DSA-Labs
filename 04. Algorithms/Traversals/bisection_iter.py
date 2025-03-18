def bisection_iter(n, arr):
    """
    Performs an iterative binary search on a sorted list 'arr' to find 'n'.

    Parameters:
    n   : The number to search for in the list.
    arr : The sorted list in which to search for 'n'.

    Returns:
    A string indicating whether 'n' was found, and at which index, or if it was not found.
    """
    start = 0  # Starting index of the search range
    stop = len(arr) - 1  # Ending index of the search range

    # Continue searching while the start index is less than or equal to the stop index.
    while start <= stop:
        mid = (start + stop) // 2  # Find the middle index of the current range

        # If the middle element is the target, return the success message with its index.
        if n == arr[mid]:
            return f"{n} found at index {mid}"

        # If the target is greater than the middle element, search in the right half.
        elif n > arr[mid]:
            start = mid + 1

        # Otherwise, search in the left half.
        else:
            stop = mid - 1

    # If the loop exits without returning, the element wasn't found.
    return f"{n} not found in list"


def create_list(max_val):
    """
    Creates a list of integers from 1 up to 'max_val'.

    Parameters:
    max_val : The maximum integer to include in the list.

    Returns:
    A list of integers from 1 to 'max_val'.
    """
    arr = []
    for num in range(1, max_val + 1):
        arr.append(num)
    return arr


# Prompt the user for input
max_length = int(input("Enter the maximum length of the list : "))
num_to_search = int(input("Enter the number you want to search for : "))

# Create a list from 1 to max_length
l = create_list(max_length)

# Perform the binary search (bisection_iter) on the created list
print(bisection_iter(num_to_search, l))
