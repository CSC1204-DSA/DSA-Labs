"""
Implements a singly linked list data structure with various operations:
1) Node class: A single element of the list, holding data and a pointer to the next node.
2) LinkedList class:
   - append_val(x): Adds a new node (or existing Node) to the end (tail) of the list.
   - add_to_start(x): Adds a new node (or existing Node) at the beginning (head) of the list.
   - search_val(x): Searches for 'x' in the list and prints all indices where 'x' is found.
                    Prints a "not found" message if not present.
   - remove_val_by_index(key): Removes the first node whose data matches 'key'.
   - length(): Returns the total number of nodes in the list.
   - reverse_list_recur(current, previous): Recursively reverses the linked list in-place.
   - __str__(): Returns a string representation of the linked list, e.g., [1->2->3].

Below is an example usage that demonstrates these operations.
"""

class Node:
    """
    Represents a single node in a linked list, storing 'data'
    and a reference to the 'next' node.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        # Provides a string representation of the node's data.
        return f"{self.data}"

class LinkedList:
    """
    Implements basic linked list functionality, including:
    - Adding nodes to the end (append_val)
    - Adding nodes at the start (add_to_start)
    - Searching for values (search_val)
    - Removing by matching data (remove_val_by_index)
    - Checking length (length)
    - Reversing recursively (reverse_list_recur)
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """
        Provides a string representation of the entire list.
        Example format: [1->2->3]
        """
        to_print = ""
        curr = self.head

        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next

        if to_print:
            # Remove the trailing arrow, enclose in brackets
            return '[' + to_print[:-2] + ']'
        return '[]'

    def append_val(self, x):
        """
        Adds a new node with data 'x' (or 'x' itself if it's already a Node)
        at the end (tail) of the linked list.
        """
        # If x is not already a Node, create a new Node
        if not isinstance(x, Node):
            x = Node(x)

        # If the list is empty, set both head and tail to this new node
        if self.head is None:
            self.head = x
        else:
            # Otherwise, link the current tail to the new node
            self.tail.next = x

        # Update the tail reference to the new node
        self.tail = x

    def add_to_start(self, x):
        """
        Inserts a new node with data 'x' (or 'x' itself if it's already a Node)
        at the start (head) of the linked list.
        """
        # Ensure x is a Node object
        if not isinstance(x, Node):
            x = Node(x)

        # The new node's 'next' points to the current head
        x.next = self.head
        # Update head to the new node
        self.head = x
        # If the list was empty, the new node is also the tail
        if self.tail is None:
            self.tail = x

    def search_val(self, x):
        """
        Searches the linked list for value 'x'.
        Prints the index of each occurrence, or a "not found" message
        if 'x' is not present at all.
        """
        current = self.head
        i = 0
        found = False

        while current is not None:
            if current.data == x:
                print(f"{x} value found at index {i}")
                found = True
            current = current.next
            i += 1

        if not found:
            print(f"{x} value not found")

    def remove_val_by_index(self, key):
        """
        Removes the first node in the list whose data matches 'key'.
        """
        temp = self.head

        # If the list is empty, do nothing
        if temp is None:
            return

        # If the head node itself holds the key, remove it
        if temp.data == key:
            self.head = temp.next
            # If that was the only node, tail should also be reset
            if self.head is None:
                self.tail = None
            return

        # Otherwise, search for the node to remove
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key not found in the list, return
        if temp is None:
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        # If the removed node was the tail, update the tail
        if temp == self.tail:
            self.tail = prev

    def length(self):
        """
        Returns the number of nodes in the linked list.
        """
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse_list_recur(self, current, previous):
        """
        Recursively reverses the linked list in-place.
        Steps:
          - Base case: If list is empty or only one node, handle accordingly.
          - Otherwise, re-link each node to its predecessor, eventually 
            making the old tail become the new head.
        """
        # If the list is empty, nothing to reverse
        if self.head is None:
            return
        # If current is the last node, finalize the reversal
        elif current.next is None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            # Recur on the next node
            nxt = current.next
            current.next = previous
            self.reverse_list_recur(nxt, current)


# Example usage of the LinkedList and Node classes

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()

# Append Node objects
my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)

# Append a value (automatically converts to Node)
my_list.append_val(6)

# Add a value to start
my_list.add_to_start(9)

# Search for a particular value in the list
my_list.search_val(3)

# Print the current state of the list
print(my_list)  # Should show [9->1->2->3->4->5->6]
