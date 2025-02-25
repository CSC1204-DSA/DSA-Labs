"""
Implements a Stack using a singly linked list.

Key Properties (LIFO: Last In, First Out):
1) push(data)   : Insert an element at the top (O(1))
2) pop()        : Remove the element at the top (O(1))
3) peek()       : Return the top element without removing it (O(1))
4) print_stack(): Print all elements from top to bottom (O(n))
"""

class Node:
    """
    Represents a single node in the stack, holding 'data'
    and a pointer 'next' to the node below it.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """
    A stack implementation using a singly linked list, maintaining:
    - top    : Points to the node currently at the top of the stack
    - bottom : Points to the node at the bottom of the stack
    - length : Tracks how many nodes are in the stack
    """
    def __init__(self):
        # Initially, an empty stack
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        """
        Returns the data of the topmost node without removing it.
        If the stack is empty, returns None.
        """
        if self.top is None:
            return None
        return self.top.data

    def push(self, data):
        """
        Pushes a new node containing 'data' onto the top of the stack (O(1)).
        """
        new_node = Node(data)
        # If the stack is empty, both top and bottom reference the new node
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            # Link the new node above the current top
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        """
        Removes the topmost node from the stack and returns its data (O(1)).
        If the stack is empty, prints a message and returns None.
        """
        if self.top is None:
            print("Stack empty")
            return None
        # Move the top pointer down by one
        popped_data = self.top.data
        self.top = self.top.next
        self.length -= 1
        # If the stack becomes empty, reset bottom
        if self.length == 0:
            self.bottom = None
        return popped_data

    def print_stack(self):
        """
        Prints the stack from top to bottom (O(n)) by traversing the linked list.
        """
        if self.top is None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.data)
                current_pointer = current_pointer.next

# Demonstration
if __name__ == "__main__":
    my_stack = Stack()
    print(my_stack.peek())  # Expect None (stack is empty)

    my_stack.push('google')
    my_stack.push('udemy')
    my_stack.push('discord')
    my_stack.print_stack()
    # Expected:
    # discord
    # udemy
    # google

    print(my_stack.top.data)     # Expected: discord
    print(my_stack.bottom.data)  # Expected: google

    my_stack.pop()
    my_stack.print_stack()
    # Expected:
    # udemy
    # google

    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()
    # Expected: "Stack empty"
