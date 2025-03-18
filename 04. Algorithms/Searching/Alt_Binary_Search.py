"""
Alternative Binary Search (Iterative)

This method uses a "jump and halve" strategy:
1. Start with an initial jump size i = n // 2.
2. As long as i >= 1:
   - Repeatedly move forward one step at a time by i (if doing so doesn't exceed array length
     and the element is still <= target).
   - When we can no longer move using the current jump size, halve i (i //= 2)
     to make smaller jumps.
3. Return the index if found, otherwise -1.

Time Complexity: O(log n)
"""

def bsearch_alt(target, arr):
    n = len(arr)
    k = 0               # 'k' holds the current index
    i = n // 2          # Start with a jump size of half the array length

    # While jump size is at least 1
    while i >= 1:
        # Move forward 'i' steps at a time if the element at (k + i) is <= target
        while (k + i < n) and (arr[k + i] <= target):
            k += 1
        # Halve the jump size for finer movement
        i //= 2

    # Check if the element at position 'k' matches the target
    return k if arr[k] == target else -1

# Example usage:
print(bsearch_alt(4, [1, 2, 3, 4, 5]))  # Expected output: 3
