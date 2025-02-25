"""
Given an integer array `nums`, this code finds the contiguous subarray 
with the largest sum and returns its sum.

Example:
--------
Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] sums to 6, which is the maximum possible.
"""


def brute_force_max_subarray(array):
    """
    Brute force solution:
    - Checks every possible subarray by using two nested loops.
    - Calculates the running sum (cumulative) of subarrays starting from each index.
    - Updates a global maximum with the largest sum encountered.

    Time Complexity: O(n^2)
    """
    maximum = float('-inf')  # Use negative infinity to handle arrays with all negative numbers
    if len(array) == 0:
        return None

    for i in range(len(array)):
        cum_sum = 0
        # Build subarray sums starting at index 'i'
        for j in range(i, len(array)):
            cum_sum += array[j]
            # Update global maximum if necessary
            maximum = max(maximum, cum_sum)

    return maximum


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(brute_force_max_subarray(array))  # Output: 6


def kadane(array):
    """
    Kadane's algorithm (Optimal solution):
    - Maintains two variables:
      1) `maxarray` = maximum subarray sum ending at the current index
      2) `maximum` = global maximum subarray sum found so far
    - For each element, decide whether to:
      (a) add it to the previous subarray, or 
      (b) start a new subarray from this element.
    - Update the global maximum after each comparison.

    Time Complexity: O(n)
    """
    # Initialize with the first element
    maximum = maxarray = array[0]

    # Process the array starting from index 1
    for i in range(1, len(array)):
        # Decide if adding current element to the existing subarray is better
        # or starting a new subarray from the current element is better
        maxarray = max(array[i], maxarray + array[i])

        # Update the global maximum if needed
        maximum = max(maxarray, maximum)

    return maximum


print(kadane(array))  # Output: 6
