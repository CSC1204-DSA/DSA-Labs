"""
Implements a stack using a Python list (dynamic array).
Methods:
--------
1) push(data)    : Inserts 'data' at the top of the stack (end of the list).
2) pop()         : Removes the topmost element.
3) peek()        : Returns the topmost element without removing it.
4) print_stack() : Prints the stack elements from top to bottom.

Time complexities:
------------------
- push : O(1) amortized
- pop  : O(1)
- peek : O(1)
- print_stack : O(n)
"""

class Stack:
    """
    A simple stack implementation backed by a Python list.
    The top of the stack corresponds to the end of the list.
    """
    def __init__(self):
        # Initialize an empty list (array)
        self.array = []

    def peek(self):
        """
        Returns the top element of the stack
        without removing it.
        Assumes the stack is not empty.
        """
        return self.array[-1]

    def push(self, data):
        """
        Push (insert) 'data' onto the top of the stack.
        Time Complexity: O(1) amortized (due to Python list append).
        """
        self.array.append(data)

    def pop(self):
        """
        Pop (remove) the top element from the stack.
        Time Complexity: O(1) (removing the last element of a list).
        If the stack is empty, prints a message and returns None.
        """
        if len(self.array) == 0:
            print("Stack Empty")
            return None
        return self.array.pop()

    def print_stack(self):
        """
        Prints all elements from top to bottom.
        The top of the stack is the end of the list, so we iterate backward.
        """
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])


# Demonstration
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("Azamuke's")
    my_stack.push("Courses")
    my_stack.push("Are")
    my_stack.push("Awesome")
    my_stack.print_stack()
    # Expected:
    # Awesome
    # Are
    # Courses
    # Azamuke's

    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()
    # Expected:
    # Courses
    # Azamuke's

    print(my_stack.peek())  
    # Expected: Courses

    print(my_stack.__dict__)
    # Example: {'array': ["Azamuke's", 'Courses']}

"""
Additional Pythonic ways to implement a stack:
1. 'deque' from collections:
   - push: deque.append(x)
   - pop : deque.pop()

2. 'LifoQueue' from queue:
   - push: LifoQueue.put(x)
   - pop : LifoQueue.get()
   Also provides additional features like maxsize, etc.
"""
