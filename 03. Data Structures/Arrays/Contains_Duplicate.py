# Given an array of integers, find if the array contains any duplicates.
# Return True if any value appears at least twice; otherwise return False.

# Example 1:
# Input: [1,2,3,1]
# Output: True

# Example 2:
# Input: [1,2,3,4]
# Output: False


def brute_force_duplicate_search(array):
    """
    Naive approach:
    This function checks every possible pair in the array (nested loops).
    If any two elements match, it returns True immediately.
    If no duplicates are found, it returns False.
    Time Complexity: O(n^2)
    """
    # Outer loop: iterate through elements from 0 to second last
    for i in range(len(array) - 1):
        # Inner loop: compare element at i with elements from i+1 to end
        for j in range(i + 1, len(array)):
            # If any pair matches, return True
            if array[i] == array[j]:
                return True

    # If no matching pair found, return False
    return False


array = [1, 2, 46, 32, 98, 61, 34, 46]
print(brute_force_duplicate_search(array))  # Expected output: True (46 is duplicated)


def better_duplicate_search(array):
    """
    Slightly better approach:
    1. Sort the array (O(n log n))
    2. Traverse the sorted array once (O(n))
       Check if any consecutive elements are the same.
    Overall Time Complexity: O(n log n)
    """
    # Sort the array in-place
    array.sort()
    # Check each element with its next neighbor
    for i in range(len(array) - 1):
        # If any consecutive pair matches, return True
        if array[i] == array[i + 1]:
            return True

    # If no consecutive matches, return False
    return False


print(better_duplicate_search(array))  # Expected output: True (46 is duplicated)


def smart_duplicate_search(array):
    """
    Optimal approach using a dictionary (hash map):
    1. Create an empty dictionary to track seen elements.
    2. Iterate through the array, check if current element is in dictionary.
       - If yes, return True immediately (duplicate found).
       - If no, add this element to the dictionary.
    Time Complexity: O(n) on average (thanks to O(1) dictionary lookups)
    """
    dictionary = dict()

    # If array has fewer than 2 elements, it can't have duplicates
    if len(array) < 2:
        return False
    else:
        # Iterate over each element
        for i in range(len(array)):
            # Check if the element is already in the dictionary
            if array[i] in dictionary:
                return True
            else:
                # Add the new element to the dictionary
                dictionary[array[i]] = True
    # If no duplicates found, return False
    return False


print(smart_duplicate_search(array))  # Expected output: True (46 is duplicated)
