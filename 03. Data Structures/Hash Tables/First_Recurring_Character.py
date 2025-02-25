"""
Given an array, returns the first recurring character (the first character
that appears more than once while traversing from left to right).

Example:
--------
Input:  [2, 1, 4, 2, 6, 5, 1, 4]
Output: 2
"""

def simple_frc(array):
    """
    Simple approach using a dictionary (hash table):
    - Traverse the array once, keep track of elements in a dictionary.
    - If an element is already in the dictionary, return it immediately.
    - If we reach the end with no duplicates, return None.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    dictionary = {}
    for item in array:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True
    return None

array = [2, 1, 4, 1, 5, 2, 6]
print(simple_frc(array))  # Output: 1 (the first recurring character)


def naive_frc(array):
    """
    Naive approach using nested loops:
    - For each element i, compare it with subsequent elements j.
    - Once a match is found for i, record it and reduce the search space
      so we don't look beyond that position for further matches.
    - Continue until the first recurring character is identified.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    l = len(array)
    frc = None
    i = 0
    while i < l:
        j = i + 1
        while j < l:
            if array[i] == array[j]:
                # Found a recurring character for array[i]
                frc = array[j]
                # Narrow down the loop's range so we don't look beyond this position
                l = j
                break
            else:
                j += 1
        i += 1
    return frc

print(naive_frc(array))  # Output: 1 (the first recurring character)
