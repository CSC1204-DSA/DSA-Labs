"""
Implements a queue data structure using linked nodes.
Each node holds 'data' and a pointer to the next node in the queue.

Operations:
1. add(x)   : Enqueue operation; inserts 'x' at the tail of the queue.
2. remove() : Dequeue operation; removes the node at the head of the queue and returns its value.
3. peek()   : Returns the value at the head without removing it.
4. is_empty(): Checks if the queue is empty.
5. __str__() : Provides a visual/string representation of the queue contents.
"""

import time


class Node:
    """
    Represents a single node in the queue with 'data'
    and a pointer 'next' to the next node.
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    """
    A Queue implementation using Node objects,
    which maintains references to 'head' and 'tail'.
    """

    def __init__(self):
        """
        Initialize the queue with both head and tail set to None.
        """
        print("Queue created")
        self.head = None
        self.tail = None

    def add(self, x):
        """
        Enqueue:
        - Adds an element 'x' (or a Node containing 'x') to the tail of the queue.
        - If the queue is empty, both head and tail become the new node.
        - If not, link the current tail to the new node and update the tail pointer.
        """
        if not isinstance(x, Node):
            x = Node(x)
        print(f"Appending {x.data} to the tail of the Queue")

        if self.is_empty():
            self.head = x
        else:
            self.tail.next = x

        self.tail = x

    def remove(self):
        """
        Dequeue:
        - Removes and returns the data of the node at the head of the queue.
        - If the queue is empty, returns a message indicating that.
        """
        if not self.is_empty():
            print(f"Removing node at head of the Queue")
            curr = self.head
            self.head = self.head.next
            curr.next = None

            # If head is now None, the queue became empty, so tail should also be None
            if self.head is None:
                self.tail = None

            return curr.data
        else:
            return "Queue is empty"

    def is_empty(self):
        """
        Checks if the queue has no elements by verifying if head is None.
        Returns True if empty, else False.
        """
        return self.head is None

    def peek(self):
        """
        Returns the data at the head of the queue without removing it.
        """
        if not self.is_empty():
            return self.head.data

    def __str__(self):
        """
        Visualizes the queue from head to tail.
        The string format shows "Head -> ... -> Tail" representation.

        Example: [1->2->3]
        """
        print("Printing Queue state...")
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next

        if to_print:
            if len(to_print) > 4:
                print("Head", " " * (len(to_print) - 9), "Tail")
                print(" |", " " * (len(to_print) - 6), "|")
                print(" V", " " * (len(to_print) - 6), "V")
                return "[" + to_print[:-2] + "]"
            else:
                # Only one or two elements scenario
                print("Head & Tail")
                print(" |")
                print(" V")
                return "[" + to_print[:-2] + "]"
        return "[]"


# Demonstration
my_queue = Queue()
print("Checking if Queue is empty:", my_queue.is_empty())
time.sleep(2)

my_queue.add(1)
print(my_queue)
time.sleep(2)

my_queue.add(2)
my_queue.add(3)
print(my_queue)
time.sleep(2)

my_queue.add(4)
my_queue.add(5)
time.sleep(2)

print("Checking node at head of Queue:", my_queue.peek())
time.sleep(2)

my_queue.add(6)
print(my_queue)
time.sleep(2)

print(my_queue.remove())  # Should remove the node with data=1
time.sleep(2)

print(my_queue.remove())  # Should remove the node with data=2
time.sleep(2)

print(my_queue)
time.sleep(2)

my_queue.add(4)
time.sleep(2)

print(my_queue)
