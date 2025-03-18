# ------------------------------------------------------
# Depth-First Search (DFS) Implementation in a BST
# ------------------------------------------------------
#
# DFS is a tree (or graph) traversal algorithm where we explore as far along each branch as possible
# before backtracking.
#
# There are three common types of DFS traversals in a binary tree:
# 1. Inorder   (Left, Root, Right)
# 2. Preorder  (Root, Left, Right)
# 3. Postorder (Left, Right, Root)
#
# Below is an implementation of a Binary Search Tree (BST) and the three DFS traversals.

class Node:
    """
    Node class for the BST.
    Attributes:
    - data : The value stored in the node.
    - left : Pointer to the left child (initially None).
    - right: Pointer to the right child (initially None).
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree (BST) class.

    Attributes:
    - root             : The root node of the BST (initially None).
    - number_of_nodes  : Tracks the number of nodes inserted in the BST.
    """

    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):
        """
        Insert a new node with 'data' into the BST.

        Steps:
        1. If the tree is empty, the new node becomes the root.
        2. Otherwise, compare 'data' with the current node:
           - If data is greater, move to the right child.
           - If data is smaller, move to the left child.
        3. Insert when the correct spot is found (where child is None).

        Average-case Time Complexity: O(log n)
        Worst-case Time Complexity  : O(n)
        """
        new_node = Node(data)
        # If there is no root, make new_node the root.
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            # Start from the root and traverse down.
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    # If the right child does not exist, insert here; otherwise, move right.
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    # If the left child does not exist, insert here; otherwise, move left.
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1
            return

    def search(self, data):
        """
        Search for a node with value 'data' in the BST.

        Returns "Found" if the node is present, otherwise "Not Found".
        If the tree is empty, returns "Tree Is Empty".

        Steps:
        1. Start at the root.
        2. If root is None, the tree is empty.
        3. Compare 'data' with current node's data:
           - If equal, return "Found".
           - If smaller, move to the left subtree.
           - If larger, move to the right subtree.
        4. If we reach a None node, it means 'data' is not in the tree.
        """
        if self.root is None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right

    def remove(self, data):
        """
        Remove a node with the value 'data' from the BST.

        This involves multiple cases:
          1. The node might not exist in the tree.
          2. The node could have:
             - No children (leaf node)
             - One child (left or right)
             - Two children (left and right)

        Strategy:
        - Traverse the tree to find the node (and keep track of its parent).
        - Once found, handle the removal based on the number of children.
        """
        if self.root is None:  # If the tree is empty
            return "Tree Is Empty"

        current_node = self.root
        parent_node = None

        # Search for the node to remove
        while current_node is not None:
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Match found. Let's handle the four cases:

                # CASE 1: Node has left child only
                if current_node.right is None:
                    if parent_node is None:
                        # If the node to delete is the root
                        self.root = current_node.left
                        return
                    else:
                        # Link the parent's left/right to current_node's left child
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left
                        return

                # CASE 2: Node has right child only
                elif current_node.left is None:
                    if parent_node is None:
                        # If the node to delete is the root
                        self.root = current_node.right
                        return
                    else:
                        # Link the parent's left/right to current_node's right child
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                        else:
                            parent_node.right = current_node.left
                        return

                # CASE 3: Node has no children (leaf node)
                elif current_node.left is None and current_node.right is None:
                    # If it is the root node
                    if parent_node is None:
                        current_node = None
                        self.root = None
                        return
                    # Otherwise, remove the leaf
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return

                # CASE 4: Node has both left and right children
                elif (current_node.left is not None) and (current_node.right is not None):
                    # Find the leftmost node in the right subtree (successor)
                    del_node = current_node.right
                    del_node_parent = current_node.right

                    # Traverse left
                    while del_node.left is not None:
                        del_node_parent = del_node
                        del_node = del_node.left

                    # Copy the successor's value into current_node
                    current_node.data = del_node.data

                    # If del_node is the immediate right child
                    if del_node == del_node_parent:
                        current_node.right = del_node.right
                        return

                    # If the successor has no right child
                    if del_node.right is None:
                        del_node_parent.left = None
                    else:
                        # Link the successor's right child to del_node_parent
                        del_node_parent.left = del_node.right
                    return

        return "Not Found"  # If we exit the loop, node wasn't found in the BST

    # ------------------------------------------------------
    # DFS Traversal Methods
    # ------------------------------------------------------
    def DFS_Inorder(self):
        """
        Returns a list of node values using Inorder DFS (Left, Root, Right).
        """
        return inorder_traversal(self.root, [])

    def DFS_Preorder(self):
        """
        Returns a list of node values using Preorder DFS (Root, Left, Right).
        """
        return preorder_traversal(self.root, [])

    def DFS_Postorder(self):
        """
        Returns a list of node values using Postorder DFS (Left, Right, Root).
        """
        return postorder_traversal(self.root, [])


# ------------------
# Helper Functions for DFS
# ------------------

def inorder_traversal(node, DFS_list):
    """
    Inorder DFS:
    1. Traverse left subtree
    2. Visit the node (append to DFS_list)
    3. Traverse right subtree
    """
    if node.left:
        inorder_traversal(node.left, DFS_list)
    DFS_list.append(node.data)
    if node.right:
        inorder_traversal(node.right, DFS_list)
    return DFS_list


def preorder_traversal(node, DFS_list):
    """
    Preorder DFS:
    1. Visit the node (append to DFS_list)
    2. Traverse left subtree
    3. Traverse right subtree
    """
    DFS_list.append(node.data)
    if node.left:
        preorder_traversal(node.left, DFS_list)
    if node.right:
        preorder_traversal(node.right, DFS_list)
    return DFS_list


def postorder_traversal(node, DFS_list):
    """
    Postorder DFS:
    1. Traverse left subtree
    2. Traverse right subtree
    3. Visit the node (append to DFS_list)
    """
    if node.left:
        postorder_traversal(node.left, DFS_list)
    if node.right:
        postorder_traversal(node.right, DFS_list)
    DFS_list.append(node.data)
    return DFS_list


# ------------------
# Testing the BST and DFS Implementations
# ------------------

my_bst = BST()

# Insert nodes into the BST
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
        3       7
    1               13
  0              10     65
"""

# Expected DFS traversals:
# Inorder   : [0, 1, 3, 5, 7, 10, 13, 65]
# Preorder  : [5, 3, 1, 0, 7, 13, 10, 65]
# Postorder : [0, 1, 3, 10, 65, 13, 7, 5]

# Perform and print DFS traversals
print(my_bst.DFS_Inorder())  # [0, 1, 3, 5, 7, 10, 13, 65]
print(my_bst.DFS_Preorder())  # [5, 3, 1, 0, 7, 13, 10, 65]
print(my_bst.DFS_Postorder())  # [0, 1, 3, 10, 65, 13, 7, 5]
