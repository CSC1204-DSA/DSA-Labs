"""
Implements a Queue data structure (FIFO: First In, First Out) using linked nodes.

Key Operations:
1) enqueue(data) : Adds an item to the back of the queue (O(1)).
2) dequeue()     : Removes an item from the front of the queue (O(1)).
3) peek()        : Returns the front item without removing it (O(1)).
4) print_queue() : Prints the items in the queue from front to back.
"""

class Node:
    """
    Represents a single node in the queue, storing 'data'
    and a reference 'next' to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """
    A singly-linked Queue where:
    - 'first' points to the front (head) of the queue.
    - 'last' points to the rear (tail) of the queue.
    - 'length' tracks how many nodes are in the queue.
    """
    def __init__(self):
        # Initially, both first and last are None, indicating an empty queue.
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        """
        Returns the data of the front node (head) without removing it.
        Assumes queue is not empty.
        """
        return self.first.data

    def enqueue(self, data):
        """
        Adds a new node with 'data' to the tail of the queue.
        If the queue is empty, sets both first and last to the new node.
        Otherwise, links the current last node to the new node and updates last.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        # If the queue is empty
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            # Link the new node behind the current last
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """
        Removes the node at the front of the queue and returns its data.
        If the queue is empty, prints an appropriate message.
        If removing the only node, sets 'last' to None as well.
        Time Complexity: O(1)
        """
        if self.first is None:
            print("Queue Empty")
            return
        # If there's only one node in the queue
        if self.first == self.last:
            self.last = None
        # Move front pointer (first) to the next node
        removed_node = self.first
        self.first = self.first.next
        self.length -= 1
        return removed_node.data

    def print_queue(self):
        """
        Prints the queue from front to back in a visually indicative format.
        If empty, prints "Queue Empty".
        """
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while current_pointer is not None:
                if current_pointer.next is None:
                    # Last node, print data with a newline
                    print(current_pointer.data)
                else:
                    # Print data with a separator indicating the queue flow
                    print(f"{current_pointer.data}  <<--  ", end='')
                current_pointer = current_pointer.next

# Demonstration of the Queue in action
my_queue = Queue()

# Enqueue items
my_queue.enqueue("This")
my_queue.enqueue("is")
my_queue.enqueue("a")
my_queue.enqueue("Queue")
my_queue.print_queue()
# Expected output: "This  <<--  is  <<--  a  <<--  Queue"

# Peek at the front item
print(my_queue.peek())  # Expected output: "This"

# Dequeue two items
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
# Expected output: "a  <<--  Queue"

# Print internal state of the queue
print(my_queue.__dict__)
# Example: {'first': <__main__.Node object ...>, 'last': <__main__.Node object ...>, 'length': 2}

print(my_queue.first)        # Shows the node object at the front
print(my_queue.first.data)   # "a"

# Dequeue remaining items to empty the queue
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()       # Expected output: "Queue Empty"
