def bisection_recur(n, arr, start, stop):
    """
    Performs a recursive binary search on a sorted list 'arr' to find 'n'.

    Parameters:
    n     : The number to search for in the list.
    arr   : The sorted list in which to search for 'n'.
    start : The starting index of the portion of the list currently being searched.
    stop  : The ending index of the portion of the list currently being searched.

    Returns:
    A string indicating whether 'n' was found (and its index) or if it was not found.
    """
    # Base case: if start index goes beyond stop index, 'n' is not in the list
    if start > stop:
        return f"{n} not found in list"

    else:
        # Calculate the midpoint between start and stop
        mid = (start + stop) // 2

        # If the element at mid matches 'n', we've found it
        if n == arr[mid]:
            return f"{n} is found at index {mid}"

        # If 'n' is greater than the midpoint element, search the right half
        elif n > arr[mid]:
            start = mid + 1
            return bisection_recur(n, arr, start, stop)

        # Otherwise, search the left half
        else:
            stop = mid - 1
            return bisection_recur(n, arr, start, stop)


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

# Print the generated list (optional, for verification)
print(l)

# Perform the recursive binary search.
# Note: We pass start=1 and stop=len(l)-1 here.
# For a typical 0-based indexing search, you might do start=0.
print(bisection_recur(num_to_search, l, 1, len(l) - 1))
