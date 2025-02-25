"""
Implements a Doubly Linked List where each node has pointers to both
the next and the previous nodes. Includes methods to append, prepend, insert,
and delete by value or position, as well as a method to print the list.

Although the time complexities remain O(n) for most operations (similar to
a singly linked list), having a 'previous' pointer can simplify certain operations.
"""

class Node:
    """
    Represents a single node in a Doubly Linked List with:
      - data:       The value stored in the node
      - next:       Pointer to the next node
      - previous:   Pointer to the previous node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    """
    Doubly Linked List providing the following operations:
      - print_list():         Print all elements in the list
      - append(data):         Add a node at the end of the list
      - prepend(data):        Add a node at the start of the list
      - insert(position, data): Insert a node at a specified position
      - delete_by_value(data):  Remove the first node containing 'data'
      - delete_by_position(pos):Remove the node at a given position
      - length:               Keep track of the number of nodes in the list
    """
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        """
        Prints the data of each node from head to tail.
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

    def append(self, data):
        """
        Adds a node with 'data' at the end (tail) of the list.
        If the list is empty, this new node becomes both head and tail.
        Otherwise, links the new node to the current tail and updates the tail.
        """
        new_node = Node(data)
        # If empty list, new node is head and tail
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            # Connect the new node to the current tail
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        """
        Inserts a new node with 'data' at the beginning (head) of the list.
        If the list is empty, new node becomes head and tail.
        Otherwise, links the new node to the current head and updates the head.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def insert(self, position, data):
        """
        Inserts a new node at the given 'position' (0-indexed).
        If position=0, it behaves like prepend.
        If position >= length, it behaves like append.
        Otherwise, traverses to the correct spot and inserts the new node there.
        """
        if position == 0:
            self.prepend(data)
            return
        if position >= self.length:
            self.append(data)
            return

        new_node = Node(data)
        current_node = self.head
        # Move to the node just before the insertion point
        for _ in range(position - 1):
            current_node = current_node.next

        # Insert new_node between current_node and current_node.next
        new_node.previous = current_node
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.next.previous = new_node
        self.length += 1

    def delete_by_value(self, data):
        """
        Removes the first node in the list whose data equals 'data'.
        If the value is not found, prints "Given value not found.".
        """
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head

        # If the head node is the one to delete
        if current_node.data == data:
            self.head = self.head.next
            # If list becomes empty or only one node remains
            if self.head is None or self.head.next is None:
                self.tail = self.head
            if self.head is not None:
                self.head.previous = None
            self.length -= 1
            return

        # Otherwise, search for the node to delete
        try:
            while current_node is not None and current_node.next.data != data:
                current_node = current_node.next

            # If current_node is not None, we found the node to delete
            if current_node is not None:
                # current_node.next is the node to remove
                node_to_remove = current_node.next
                current_node.next = node_to_remove.next
                if current_node.next is not None:
                    current_node.next.previous = current_node
                else:
                    # If the removed node was the last node, update tail
                    self.tail = current_node
                self.length -= 1
            else:
                # If we never found 'data' in the list
                print("Given value not found.")
        except AttributeError:
            print("Given value not found.")

    def delete_by_position(self, position):
        """
        Removes the node at the specified 'position' (0-indexed).
        If the list is empty, does nothing.
        If position=0, delete the head.
        If position >= length, deletes the last node.
        Otherwise, traverses to the node and removes it by adjusting pointers.
        """
        if self.head is None:
            print("Linked List is empty. Nothing to delete.")
            return

        # If the head node is to be removed
        if position == 0:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            if self.head is not None:
                self.head.previous = None
            self.length -= 1
            return

        # If position is beyond current length, treat it as last node
        if position >= self.length:
            position = self.length - 1

        current_node = self.head
        # Move to the node just before the one we want to delete
        for _ in range(position - 1):
            current_node = current_node.next

        # current_node.next is the node to delete
        node_to_remove = current_node.next
        current_node.next = node_to_remove.next
        if current_node.next is not None:
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1


# Example usage of the DoublyLinkedList

my_linked_list = DoublyLinkedList()
my_linked_list.print_list()               # Empty

my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.print_list()               # 5 2 9

my_linked_list.prepend(4)
my_linked_list.print_list()               # 4 5 2 9

my_linked_list.insert(2, 7)
my_linked_list.print_list()               # 4 5 7 2 9

my_linked_list.insert(0, 0)
my_linked_list.insert(6, 0)
my_linked_list.insert(9, 3)
my_linked_list.print_list()               # 0 4 5 7 2 9 0 3

my_linked_list.delete_by_value(3)
my_linked_list.print_list()               # 0 4 5 7 2 9 0

my_linked_list.delete_by_value(0)
my_linked_list.print_list()               # 4 5 7 2 9 0

my_linked_list.delete_by_position(3)
my_linked_list.print_list()               # 4 5 7 9 0

my_linked_list.delete_by_position(0)
my_linked_list.print_list()               # 5 7 9 0

my_linked_list.delete_by_position(8)
my_linked_list.print_list()               # 5 7 9

my_linked_list.delete_by_value(3)         # "Given value not found."
my_linked_list.print_list()               # 5 7 9

print(my_linked_list.length)              # 3
