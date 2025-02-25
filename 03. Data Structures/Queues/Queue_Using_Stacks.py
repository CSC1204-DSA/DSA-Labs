"""
Implements a queue using two stacks (implemented as Python lists). 
Demonstrates the approach where the enqueue operation is expensive (O(n)) 
and the dequeue operation is O(1).

Method:
-------
1. s1: The main stack used to maintain the queue order, 
       where the front of the queue is at the top of s1.
2. s2: A temporary stack used during each enqueue to reverse the order 
       so the new element ends up at the bottom of s1.

Algorithm (Enqueue - O(n)):
1) Move all elements from s1 to s2 (popping from s1 and pushing onto s2).
2) Push the new element onto s1 (now s1 is empty, so this new element is at the bottom).
3) Move all elements back from s2 to s1.

Algorithm (Dequeue - O(1)):
1) Pop from s1 (the top of s1 is the oldest element in the queue).

Note: The second method (not implemented here) can make enqueue O(1) 
and make dequeue O(n) instead by reversing the direction of data movement.
"""

class Queue:
    """
    A Queue implementation using two stacks (lists in Python):
    s1 - primary stack
    s2 - temporary stack used during enqueue.
    """
    def __init__(self):
        """
        Initializes two empty stacks.
        """
        self.s1 = []
        self.s2 = []

    def peek(self):
        """
        Returns the front element of the queue (top of s1) without removing it.
        If queue is empty, prints a message and returns None.
        """
        if len(self.s1) == 0:
            print("Queue empty")
            return None
        return self.s1[-1]  # Top of s1 is the front of the queue

    def enqueue(self, data):
        """
        Adds 'data' to the queue in O(n) time.
        Steps:
        1) Pop all elements from s1 and push them onto s2.
        2) Push 'data' onto s1.
        3) Move all elements back from s2 to s1.
        """
        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Push the new item into s1
        self.s1.append(data)

        # Move everything back from s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        """
        Removes the front element of the queue (top of s1) in O(1) time.
        If the queue is empty, prints a message and returns None.
        """
        if len(self.s1) == 0:
            print("Queue Empty")
            return None
        return self.s1.pop()

    def print_queue(self):
        """
        Prints the queue from front to back, 
        with the front element on the left.
        If empty, prints "Queue Empty".
        """
        if not self.s1:
            print("Queue Empty")
            return
        # s1[-1] is the front, so print in reverse order
        for i in range(len(self.s1) - 1, 0, -1):
            print(f"{self.s1[i]} <<-- ", end='')
        print(self.s1[0])

# Example usage:
if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(2)
    my_queue.enqueue(5)
    my_queue.enqueue(0)
    my_queue.print_queue()
    # Expected: 2 <<-- 5 <<-- 0

    my_queue.dequeue()
    my_queue.print_queue()
    # Expected: 5 <<-- 0

    print(my_queue.peek())  
    # Expected: 5

    my_queue.enqueue(9)
    my_queue.print_queue()
    # Expected: 5 <<-- 0 <<-- 9

    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.print_queue()
    # Expected: Queue Empty

"""
Alternative method (not implemented here) reverses which operation is expensive:
- Enqueue: O(1)
- Dequeue: O(n)
   1) s1 always pushes new data directly (enqueue).
   2) For dequeue, pop all but one element from s1 onto s2, pop and return the last 
      element in s1, then move everything back from s2 to s1.
"""
