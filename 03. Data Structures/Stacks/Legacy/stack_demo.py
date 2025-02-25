"""
Demonstrates a Stack implementation in Python using a singly linked list.
Each element of the stack is represented by a Node that holds some data and
a pointer to the node beneath it in the stack.
"""

import time

class Node:
    """
    Represents a single node in the stack with:
      - data: The value held by this node
      - next: Pointer to the node below it in the stack
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    """
    A LIFO (Last In, First Out) stack where:
      - stack_pointer points to the topmost node in the stack.
    """
    def __init__(self):
        print("Stack created")
        self.stack_pointer = None  # Initially empty

    def push(self, x):
        """
        Adds 'x' (or Node with data 'x') to the top of the stack in O(1) time.
        """
        if not isinstance(x, Node):
            x = Node(x)
        print(f"Adding {x.data} to the top of stack")

        # Make the new node's next point to the current top
        x.next = self.stack_pointer
        # Update the top to be the new node
        self.stack_pointer = x

    def pop(self):
        """
        Removes and returns the node on top of the stack in O(1) time.
        If the stack is empty, returns a message indicating so.
        """
        if not self.is_empty():
            print(f"Removing node on top of stack")
            # Save the top node
            curr = self.stack_pointer
            # Reassign the top to the next node
            self.stack_pointer = self.stack_pointer.next
            # Detach the popped node
            curr.next = None
            return curr.data
        else:
            return "Stack is empty"

    def is_empty(self):
        """
        Returns True if the stack is empty, otherwise False.
        """
        return self.stack_pointer is None

    def peek(self):
        """
        Returns the data at the top of the stack without removing it.
        """
        if not self.is_empty():
            return self.stack_pointer.data

    def __str__(self):
        """
        Prints the contents of the stack from top to bottom.
        Example format: [top->next->...->bottom]
        """
        print("Printing Stack state...")
        to_print = ""
        curr = self.stack_pointer
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            print("Stack Pointer")
            print(" |")
            print(" V")
            return "[" + to_print[:-2] + "]"
        return "[]"

# Demonstration of Stack usage
my_stack = Stack()
print("Checking if stack is empty:", my_stack.is_empty())

# Push elements
my_stack.push(1)
time.sleep(2)
my_stack.push(2)
print(my_stack)
time.sleep(2)
my_stack.push(3)
time.sleep(2)
my_stack.push(4)
time.sleep(2)

# Peek at the top element
print("Checking item on top of stack:", my_stack.peek())
time.sleep(2)

# Push another element
my_stack.push(5)
print(my_stack)
time.sleep(2)

# Pop from the stack
print(my_stack.pop())   # Removes the node with data=5
time.sleep(2)
print(my_stack.pop())   # Removes the node with data=4
print(my_stack)
time.sleep(2)

# Push an element again
my_stack.push(4)
print(my_stack)
time.sleep(2)
