"""
Given an array 'nums' and a non-negative integer 'k', this code rotates the array
to the right by 'k' steps.

Example:
--------
Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
"""


def naive_rotation(array, k):
    """
    Naive approach:
    1. Create a new list.
    2. Place the last 'k' elements of the original array into the beginning of the new list.
    3. Append the remaining elements after that.

    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    # Use modulo to handle k > len(array)
    k = k % len(array)

    new_array = []
    # Append the last 'k' elements
    for i in range(k):
        new_array.append(array[len(array) - k + i])
    # Append the first 'len(array) - k' elements
    for i in range(len(array) - k):
        new_array.append(array[i])

    return new_array


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 11
print(naive_rotation(array, k))  # Example output: [9, 1, 2, 3, 4, 5, 6, 7, 8]


def brute_force_rotation(array, k):
    """
    Brute force approach:
    1. Rotate the array by 1 step, k times.
    2. Each single rotation requires shifting elements, which is O(n).
    3. Doing this k times results in O(n*k) time complexity.

    Space Complexity: O(1) (modifying the array in place)
    """
    k = k % len(array)

    for _ in range(k):
        # Save the last element
        temp = array[-1]
        # Shift elements one position to the right
        for i in range(len(array) - 1, 0, -1):
            array[i] = array[i - 1]
        array[0] = temp

    return array


print(brute_force_rotation(array[:], k))  # Example output (using array[:] to avoid modifying original)


def reverse(nums, start, end):
    """
    Reverses the elements of 'nums' in-place from index 'start' to index 'end'.
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


def reverse_rotate(array, k):
    """
    Reversal algorithm for array rotation:
    1. Reverse the entire array.
    2. Reverse the first 'k' elements.
    3. Reverse the remaining 'n - k' elements.

    Time Complexity:  O(n)  (Three passes of O(n/3) each ≈ O(n))
    Space Complexity: O(1)

    This method modifies the array in place with no extra array of size n.
    """
    n = len(array)
    k = k % n  # Handle k > n

    # 1. Reverse the entire array
    reverse(array, 0, n - 1)

    # 2. Reverse the first 'k' elements
    reverse(array, 0, k - 1)

    # 3. Reverse the remaining 'n - k' elements
    reverse(array, k, n - 1)

    return array


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_rotate(a[:], k))  # Using a copy for demonstration
