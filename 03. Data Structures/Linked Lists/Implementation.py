"""
Demonstrates a Singly Linked List implementation in Python.

Key Operations:
---------------
1) Node class:
   - A container for data and a pointer `next` to the next node in the list.

2) LinkedList class:
   - append(data)           : Add a node with 'data' to the end (tail) of the list.
   - prepend(data)          : Add a node with 'data' to the start (head) of the list.
   - print_list()           : Print all node values from head to tail.
   - insert(position, data) : Insert a node with 'data' at a given 'position' (0-indexed).
   - delete_by_value(data)  : Remove the first node encountered that holds 'data'.
   - delete_by_position(pos): Remove the node at index 'pos'.

Time Complexities:
------------------
- Lookup/Search    : O(n)
- Insert/Remove    : O(n)
- Append/Prepend   : O(1) amortized (if tail/head references are maintained)
"""


class Node:
    """
    Represents a single node in a linked list, holding 'data'
    and a pointer 'next' referencing the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None  # By default, a new node doesn't point to anything


class LinkedList:
    """
    Implements a Singly Linked List with the following features:
      - head: Points to the first node
      - tail: Points to the last node
      - length: Tracks the number of nodes in the list
    """

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        """
        Adds a new node containing 'data' at the end of the list.
        If the list is empty, sets both head and tail to the new node.
        Otherwise, links the current tail to the new node and updates the tail.
        """
        new_node = Node(data)
        # If list is empty, new node becomes both head and tail
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            # Link new node at the tail and update tail reference
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        """
        Inserts a new node containing 'data' at the start of the list.
        If the list is empty, new node becomes both head and tail.
        Otherwise, link the new node as the head and update the head reference.
        """
        new_node = Node(data)
        # If list is empty
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            # Link new node in front and update head
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        """
        Prints the data of all nodes from head to tail.
        If the list is empty, prints "Empty".
        """
        if self.head is None:
            print("Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()  # Newline for clarity

    def insert(self, position, data):
        """
        Inserts a node with 'data' at the specified 'position' (0-indexed).
        - If position >= length, appends at the end.
        - If position == 0, prepends at the start.
        - Otherwise, finds the (position-1)th node and links the new node in place.
        """
        if position >= self.length:
            if position > self.length:
                print("This position is not available. Inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            # Traverse up to node just before the position
            for _ in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def delete_by_value(self, data):
        """
        Deletes the first node in the list that contains 'data'.
        If the list is empty, prints a message and returns.
        If the head node contains 'data', reassign the head.
        Otherwise, traverse until the next node matches 'data',
        then bypass the node to be deleted.
        If 'data' is not found, prints a message.
        """
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        # If the head node is the one to delete
        if current_node.data == data:
            self.head = self.head.next
            # If list has become empty or has a single node left
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return

        # Traverse until we find a node whose next has 'data'
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next

        # If the node to delete is found
        if current_node.next is not None:
            current_node.next = current_node.next.next
            # If the deleted node was the tail, update tail
            if current_node.next is None:
                self.tail = current_node
            self.length -= 1
        else:
            print("Given value not found.")

    def delete_by_position(self, position):
        """
        Deletes the node at the given 'position' (0-indexed).
        If the list is empty, prints a message and returns.
        If position=0, deletes the head.
        If position >= length, deletes the tail node.
        Otherwise, bypasses the node at 'position' by linking the previous
        node to the next of the node being deleted.
        """
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        # If we are removing the head
        if position == 0:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return

        # If the position is out of range, remove the tail
        if position >= self.length:
            position = self.length - 1

        current_node = self.head
        # Traverse to the node just before the target position
        for _ in range(position - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next
        self.length -= 1
        # If we removed the last node, update tail
        if current_node.next is None:
            self.tail = current_node


# Usage demonstration (runs only if this file is the main program)
if __name__ == '__main__':
    my_linked_list = LinkedList()
    my_linked_list.print_list()  # Empty

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()  # 5 2 9

    my_linked_list.prepend(4)
    my_linked_list.print_list()  # 4 5 2 9

    my_linked_list.insert(2, 7)
    my_linked_list.print_list()  # 4 5 7 2 9

    my_linked_list.insert(0, 0)
    my_linked_list.insert(6, 0)
    my_linked_list.insert(9, 3)  # Tries position 9, prints a message, inserts at end
    my_linked_list.print_list()  # 0 4 5 7 2 9 0 3

    my_linked_list.delete_by_value(3)
    my_linked_list.print_list()  # 0 4 5 7 2 9 0

    my_linked_list.delete_by_value(0)
    my_linked_list.print_list()  # 4 5 7 2 9 0

    my_linked_list.delete_by_position(3)
    my_linked_list.print_list()  # 4 5 7 9 0

    my_linked_list.delete_by_position(0)
    my_linked_list.print_list()  # 5 7 9 0

    my_linked_list.delete_by_position(8)
    my_linked_list.print_list()  # 5 7 9

    print(my_linked_list.length)  # 3
