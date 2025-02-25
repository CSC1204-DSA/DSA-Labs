"""
Demonstrates the usage of the built-in 'heapq' module in Python for implementing a Min-Heap
(which can also serve as a priority queue). The smallest element is always at the front (index 0).

Key heapq Functions:
--------------------
1) heapify(iterable): Converts the given iterable into a heap in-place (O(n)).
2) heappush(heap, item): Pushes a new item on the heap, maintaining heap order (O(log n)).
3) heappop(heap): Pops and returns the smallest item from the heap, maintaining heap order (O(log n)).
4) heappushpop(heap, item): Pushes the new item, then pops and returns the smallest item (efficient combined operation).
5) heapreplace(heap, item): Pops and returns the smallest item first, then pushes the new item (also an efficient combined operation).
"""

import heapq

# Initialize a list of integers
li = [5, 7, 9, 1, 3]

# Convert the list into a heap (in-place)
heapq.heapify(li)

# The heap is now reordered so the smallest element is at the front (index 0)
print("After heapify, the list becomes a heap:", li)
# Example output: [1, 3, 9, 7, 5]

# Push a new element onto the heap
heapq.heappush(li, 4)
print("After pushing 4 onto the heap:", li)
# Example output: [1, 3, 4, 7, 5, 9]

# Pop and return the smallest element from the heap
smallest = heapq.heappop(li)
print("After popping, the smallest element was:", smallest)
# Example output: 1

# Demonstrate the difference between heappushpop and heapreplace
li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]

# Convert both lists into heaps
heapq.heapify(li1)
heapq.heapify(li2)

# heappushpop: Pushes 2 onto the heap, then pops and returns the smallest item
popped_heappushpop = heapq.heappushpop(li1, 2)
print("Popped item using heappushpop() is:", popped_heappushpop)
# Here, the new item (2) can affect which item is actually popped.

# heapreplace: Pops and returns the smallest item first, then pushes 2 onto the heap
popped_heapreplace = heapq.heapreplace(li2, 2)
print("Popped item using heapreplace() is:", popped_heapreplace)
# The original smallest item is removed before inserting the new item (2).
