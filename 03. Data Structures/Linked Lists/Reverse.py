"""
Demonstrates how to reverse a singly linked list in-place.

1) We import a LinkedList implementation (from a hypothetical 'Implementation.py' file).
2) We create and populate a linked list.
3) We define a 'reverse' function that reverses the pointers of the nodes
   so the head becomes the tail and vice versa.
"""

from Implementation import LinkedList, Node

# Create and populate the linked list
my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
# Expected output: 2 3 4 5 6

def reverse(linked_list):
    """
    Reverses the given singly linked list in-place.

    Steps:
    1. If the list is empty or has only one element, no action needed.
    2. Maintain two pointers ('first' and 'second') which initially point
       to the head and head.next respectively.
    3. Iterate through the list until 'second' is None:
       - Temporarily store second.next.
       - Make second.next point to first (reversing the link).
       - Advance 'first' to 'second' and 'second' to the temp (stored next).
    4. After the loop, 'first' will be at the old tail (new head),
       and the old head must now become the new tail,
       so we set linked_list.head.next to None.
    5. Finally, update linked_list.head to 'first'.

    Time Complexity: O(n), where n is the length of the linked list.
    """
    if linked_list.length <= 1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        # The old head becomes the new tail
        linked_list.tail = linked_list.head
        # Reversing links until second becomes None
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        # The old head becomes the new tail, so nullify its .next
        linked_list.head.next = None
        # Update the list's head to what was originally the tail
        linked_list.head = first
        return linked_list

# Reverse the list and print the result
reversed_linked_list = reverse(my_linked_list)
reversed_linked_list.print_list()
# Expected output: 6 5 4 3 2
