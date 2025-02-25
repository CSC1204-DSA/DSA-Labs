"""
Given an array of integers, the task is to move all 0s to the end 
while maintaining the order of non-zero elements.

Example:
--------
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
"""


def naive_zero_mover(array):
    """
    1. Append zeros for every zero found in the original array length.
    2. Remove zeros (pop) from the first 'original_length' positions of the array.

    Time Complexity: O(n^2) in the worst case, since popping from the middle 
    or beginning of a list is O(n).
    """
    l = len(array)

    # Append zeros for each zero found in the original array
    for i in range(l):
        if array[i] == 0:
            array.append(0)

    # Remove zeros from the first 'l' positions
    j = 0
    c = 0
    while c < l:
        if array[j] != 0:
            j += 1
        else:
            array.pop(j)  # Popping from index j shifts the subsequent elements
        c += 1

    return array


array = [0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 12, 9, 7]
print(naive_zero_mover(array))  # Moves all zeros to the end, but inefficiently


def swap_move(array):
    """
    Optimized approach:
    - Use a pointer 'z' to track the position of the first zero.
    - For each non-zero element, swap it with the element at 'z' 
      and increment 'z'.

    Time Complexity: O(n), because each element is processed once, 
    and swapping is O(1).
    """
    z = 0  # Pointer to place the next non-zero element
    for i in range(len(array)):
        if array[i] != 0:
            # Swap the current non-zero element with 
            # the element at the 'z' pointer
            array[i], array[z] = array[z], array[i]
            z += 1
    return array


print(swap_move(array))  # An efficient linear-time approach


def one_liner_move(array):
    """
    One-liner using sort with key=bool:
    - Python treats 0 as False (0) and non-zero as True (1).
    - Sorting by bool moves zeros to one side, then 'reverse=True' 
      pushes zeros to the end.

    Time Complexity: O(n log n), due to sorting.
    """
    array.sort(key=bool, reverse=True)
    return array


print(one_liner_move(array))  # A concise single line solution but uses O(n log n) sorting
