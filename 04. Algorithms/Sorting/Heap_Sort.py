"""
Heap Sort Implementation (Max-Heap)

Algorithm Overview:
1. Build a max-heap from the given array.
2. Repeatedly swap the first (largest) element in the max-heap with the last 
   element of the heap and reduce the heap size by one.
3. Call max_heapify on the root to restore the max-heap property in the reduced heap.
4. Continue until the entire array is sorted in ascending order.

Time Complexity: 
  - O(n log n) in all cases (building the heap is O(n), 
    and each removal + heapify step is O(log n) repeated n times).

Space Complexity:
  - O(1) auxiliary space (sorting happens in-place).

Note: 
- The variable 'count' globally tracks the number of comparisons in the max_heapify function 
  to demonstrate how many comparisons occur during the sort process.
"""

count = 0  # Global counter for comparisons

def max_heapify(array, heap_size, i):
    """
    Ensures the subtree with root at index 'i' is a valid max-heap,
    assuming the subtrees below 'i' are already valid max-heaps.

    Args:
      array (list): The list representing the heap.
      heap_size (int): The current size of the heap we are considering.
      i (int): Index of the current root for which we need to maintain the max-heap property.
    """
    global count

    # Calculate indices of left and right children in the heap
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i  # Assume the current root 'i' is the largest

    # Compare left child
    if left < heap_size:
        count += 1  # Increment comparison count
        if array[left] > array[largest]:
            largest = left

    # Compare right child
    if right < heap_size:
        count += 1  # Increment comparison count
        if array[right] > array[largest]:
            largest = right

    # If the largest element is not the current root, swap and recurse
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)


def build_heap(array):
    """
    Builds a max-heap from an arbitrary list 'array' by calling max_heapify 
    starting from the lowest non-leaf node down to the root.

    Args:
      array (list): The list to be converted into a max-heap.
    """
    heap_size = len(array)
    # Start from the last non-leaf node and move upward
    for i in range(heap_size // 2, -1, -1):
        max_heapify(array, heap_size, i)


def heap_sort(array):
    """
    Sorts the list 'array' in ascending order using the Heap Sort algorithm.

    Steps:
      1. Build a max-heap from the entire array.
      2. Swap the largest element (array[0]) with the last element in the heap, 
         reduce the heap size by 1, and call max_heapify to restore the heap.
      3. Repeat until the heap size is reduced to 1.

    Args:
      array (list): The list of elements to be sorted (in place).
    """
    # Build the initial max-heap
    build_heap(array)
    print(f'Heap : {array}')  # For demonstration

    heap_size = len(array)
    # Repeatedly move the largest element to the end and reduce the heap
    for i in range(heap_size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]  # Swap largest to the end
        heap_size -= 1
        # Restore max-heap property for the reduced heap
        max_heapify(array, heap_size, 0)


# Demonstration of heap_sort with different arrays

# 1. Unsorted array
array = [5, 9, 3, 10, 45, 2, 0]
heap_sort(array)
print(array)
print(f'Number of comparisons = {count}\n')

# 2. Already sorted array
sorted_array = [5, 6, 7, 8, 9]
# Reset comparison count for a new test
count = 0
heap_sort(sorted_array)
print(sorted_array)
print(f'Number of comparisons = {count}\n')

# 3. Reverse sorted array
reverse_sorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5,
                        -6, -7, -8, -9, -10]
# Reset comparison count for a new test
count = 0
heap_sort(reverse_sorted_array)
print(reverse_sorted_array)
print(f'Number of comparisons = {count}')
