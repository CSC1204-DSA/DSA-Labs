"""
Implementation of a Max Heap using a list as the underlying data structure.

Key Operations and Their Complexities:
--------------------------------------
1) insert(element)   : Inserts a new element into the heap (O(log n)).
2) extract_max()     : Removes and returns the maximum element (root) (O(log n)).
3) max_heapify(pos)  : Ensures the heap property from a given 'pos' downwards (O(log n)).
4) print_heap()      : Prints the internal structure of the heap, showing parent-child relationships (O(n)).

Note:
- The heap is 1-indexed here for simplicity.
- The 0th index is filled with a very large integer (sys.maxsize)
  to simplify comparisons with parent nodes in insert operation.
"""

import sys


class MaxHeap:
    """
    A class to represent a Max Heap:
      - 'maxsize'   : The maximum number of elements the heap can hold.
      - 'size'      : The current number of elements in the heap.
      - 'Heap'      : A list to store the heap elements, 1-indexed in this implementation.
      - 'FRONT'     : A constant index (1) pointing to the root node in 'Heap'.
    """

    def __init__(self, maxsize):
        """
        Initializes the heap with a given 'maxsize'.
        Fills 'Heap' with zeros, except the 0th index with sys.maxsize.
        """
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize  # Sentinel for parent comparisons
        self.FRONT = 1

    def parent(self, pos):
        """
        Returns the index of the parent of the node at index 'pos'.
        """
        return pos // 2

    def left_child(self, pos):
        """
        Returns the index of the left child of the node at index 'pos'.
        """
        return (2 * pos) + 1

    def right_child(self, pos):
        """
        Returns the index of the right child of the node at index 'pos'.
        """
        return (2 * pos) + 2

    def is_leaf(self, pos):
        """
        Checks if the node at 'pos' is a leaf in the heap.
        Leaf nodes are located in the lower half of the array representation.
        """
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        """
        Swaps two elements in the heap list at indices 'fpos' and 'spos'.
        """
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def max_heapify(self, pos):
        """
        Ensures the subtree with root at index 'pos' satisfies the max heap property.
        If a violation is found (the node is smaller than either child), swap
        with the larger child and recurse.
        """
        # If 'pos' is not a leaf and is less than either of its children
        if not self.is_leaf(pos):
            left = self.left_child(pos)
            right = self.right_child(pos)

            if (self.Heap[pos] < self.Heap[left] or self.Heap[pos] < self.Heap[right]):
                # Swap with the larger of the two children
                if self.Heap[left] > self.Heap[right]:
                    self.swap(pos, left)
                    self.max_heapify(left)
                else:
                    self.swap(pos, right)
                    self.max_heapify(right)

    def insert(self, element):
        """
        Inserts a new element into the heap.
        - Places the element at the end (size+1).
        - Repeatedly swaps it with its parent if it violates the max heap property.
        """
        if self.size >= self.maxsize:
            return  # Heap is full, insertion not possible

        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        # Climb up the tree until the parent is larger or we reach the root
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print_heap(self):
        """
        Prints the heap by showing each parent node alongside its
        left and right children.
        """
        # Only need to iterate through the non-leaf nodes
        for i in range(1, (self.size // 2) + 1):
            left_val = self.Heap[2 * i + 1] if (2 * i + 1) <= self.size else None
            right_val = self.Heap[2 * i + 2] if (2 * i + 2) <= self.size else None

            print(
                f" PARENT : {self.Heap[i]} "
                f"LEFT CHILD : {left_val} "
                f"RIGHT CHILD : {right_val}"
            )

    def extract_max(self):
        """
        Removes and returns the maximum element (root) of the heap.
        Replaces the root with the last element and calls max_heapify
        to maintain the heap property.
        """
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)
        return popped


# Demonstration of MaxHeap usage
if __name__ == "__main__":
    my_heap = MaxHeap(15)
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(17)
    my_heap.insert(10)
    my_heap.insert(84)
    my_heap.insert(19)
    my_heap.insert(6)
    my_heap.insert(22)
    my_heap.insert(9)

    my_heap.print_heap()
    """
    Example output:
     PARENT : 84 LEFT CHILD : 22 RIGHT CHILD : 19
     PARENT : 22 LEFT CHILD : 17 RIGHT CHILD : 10
     PARENT : 19 LEFT CHILD : 5 RIGHT CHILD : 6
     PARENT : 17 LEFT CHILD : 3 RIGHT CHILD : 9
    """

    print("The Max val is " + str(my_heap.extract_max()))
    # Expected output: "The Max val is 84"

    my_heap.print_heap()
    """
    Updated heap structure.
    """

    my_heap.insert(100)
    my_heap.print_heap()
    """
    100 should now be the root if it's indeed the maximum.
    """

    print(my_heap.Heap[0])  # Should print sys.maxsize (used as a sentinel at index 0)
