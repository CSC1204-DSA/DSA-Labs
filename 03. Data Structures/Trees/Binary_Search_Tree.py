"""
Implementation of an unbalanced Binary Search Tree (BST) with basic operations:
1) Insert a node
2) Search for a value
3) Remove a node
Average time complexity for BST operations: O(log n)
Worst-case time complexity (highly unbalanced tree): O(n)
"""

class Node:
    """
    Represents a node in the BST, storing 'data' and
    references to 'left' and 'right' child nodes.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    An unbalanced Binary Search Tree implementation, supporting:
      - Insertion of nodes
      - Searching for a value
      - Removal of nodes
    """
    def __init__(self):
        # Initialize an empty BST with no root and zero nodes
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):
        """
        Inserts a new node with 'data' into the BST.
        Steps:
        1) If the tree is empty, this node becomes the root.
        2) Otherwise, compare 'data' with the current node.
           a) If data > current node's data, go to the right child.
           b) If data < current node's data, go to the left child.
        3) Repeat until the correct position is found, then insert.
        Time Complexity: O(log n) on average; O(n) in the worst case (unbalanced).
        """
        new_node = Node(data)
        # If tree is empty, new node is root
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            # Traverse to find correct position
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    # Go right
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    # Go left
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1

    def search(self, data):
        """
        Searches for 'data' in the BST.
        Returns 'Found' if present, otherwise 'Not Found'.
        Time Complexity: O(log n) average, O(n) worst case.
        """
        # If tree is empty
        if self.root is None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            # Traverse until you find the data or reach a leaf
            while True:
                if current_node is None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                else:  # current_node.data < data
                    current_node = current_node.right

    def remove(self, data):
        """
        Removes the node containing 'data' from the BST, if it exists.
        Cases handled:
          1) Node with only left child
          2) Node with only right child
          3) Node with no children (leaf)
          4) Node with both children (use the minimum value in right subtree).
        Time Complexity: O(log n) average, O(n) worst case.
        """
        # If tree is empty
        if self.root is None:
            return "Tree Is Empty"

        current_node = self.root
        parent_node = None

        # Search for the node to delete
        while current_node is not None:
            if current_node.data > data:
                # Go left
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                # Go right
                parent_node = current_node
                current_node = current_node.right
            else:
                # Node to delete is found (current_node.data == data)

                # Case 1: Node has only left child
                if current_node.right is None:
                    if parent_node is None:
                        # Deleting the root node
                        self.root = current_node.left
                        return
                    else:
                        # Link parent around current_node
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left
                        return

                # Case 2: Node has only right child
                elif current_node.left is None:
                    if parent_node is None:
                        # Deleting the root node
                        self.root = current_node.right
                        return
                    else:
                        # Link parent around current_node
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                        else:
                            parent_node.right = current_node.right
                        return

                # Case 3: Node has no children (leaf)
                elif current_node.left is None and current_node.right is None:
                    # If deleting root node
                    if parent_node is None:
                        self.root = None
                        return
                    # Link parent's child pointer to None
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return

                # Case 4: Node has both left and right children
                else:
                    del_node = current_node.right
                    del_node_parent = current_node.right

                    # Find the leftmost node of right subtree
                    while del_node.left is not None:
                        del_node_parent = del_node
                        del_node = del_node.left

                    # Replace current node's value with that of del_node
                    current_node.data = del_node.data

                    # If the node to be removed is the immediate right child
                    if del_node == del_node_parent:
                        current_node.right = del_node.right
                        return

                    # If the leftmost node has no right subtree
                    if del_node.right is None:
                        del_node_parent.left = None
                    else:
                        # Link the parent's left pointer to del_node's right subtree
                        del_node_parent.left = del_node.right
                    return
        # If we finished while loop without returning, data not found
        return "Not Found"


# Example usage and testing
if __name__ == "__main__":
    my_bst = BST()
    my_bst.insert(5)
    my_bst.insert(3)
    my_bst.insert(7)
    my_bst.insert(1)
    my_bst.insert(13)
    my_bst.insert(65)
    my_bst.insert(0)
    my_bst.insert(10)
    """
                5
             3     7
          1           13
        0         10     65
    """

    my_bst.remove(13)
    """
                5
             3     7
          1           65
        0         10
    """
    my_bst.remove(5)
    """
                7
             3     65
          1        10
        0
    """
    my_bst.remove(3)
    """
                7
             1     65
          0        10
    """
    my_bst.remove(7)
    """
               10
             1     65
          0
    """
    my_bst.remove(1)
    """
              10
             0   65
    """
    my_bst.remove(0)
    """
              10
                 65
    """
    my_bst.remove(10)
    """
              65
    """
    my_bst.remove(65)
    """ 
        (empty tree)
    """

    my_bst.insert(10)
    """
           10
    """
    print(my_bst.root.data)  # Expected output: 10
