"""
Implements a Binary Search Tree (BST) where each node can have up to two children
(left_child and right_child).

Key operations:
1) insert(key)     : Inserts a new node with data 'key' into the BST.
2) in_order()      : Traverses and prints nodes in ascending (Left, Node, Right).
3) pre_order()     : Traverses and prints nodes (Node, Left, Right).
4) post_order()    : Traverses and prints nodes (Left, Right, Node).
5) find_val(key)   : Searches for 'key' in the BST, returning a message indicating presence.
6) delete_val(key) : Removes the node with 'key' from the BST if it exists.

Auxiliary Methods:
- _insert(curr, key)     : Recursively finds correct place for 'key'.
- _in_order(curr)        : Helper for in-order traversal.
- _pre_order(curr)       : Helper for pre-order traversal.
- _post_order(curr)      : Helper for post-order traversal.
- _find_val(curr, key)   : Recursively searches for 'key'.
- _delete_val(...)       : Recursively locates and deletes the node with 'key'.
- min_right_subtree(curr): Finds the minimum node in the right subtree (used during deletion).
"""

class Node:
    """
    Represents a single node of a BST:
    - data       : The value stored in the node.
    - left_child : Pointer to the left child.
    - right_child: Pointer to the right child.
    """
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    """
    A Binary Search Tree implementation with support for insertion, traversals,
    searching, and node deletion.
    """
    def __init__(self):
        # The root of the BST is initially None
        self.root = None

    def insert(self, key):
        """
        Inserts a new node (with data=key) into the BST. If the root is None,
        the new node becomes the root. Otherwise, the _insert helper is called.
        """
        if not isinstance(key, Node):
            key = Node(key)
        if self.root is None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        """
        Recursive helper for insert().
        Compares key.data with curr.data to decide whether to go left or right.
        If the appropriate child is None, inserts the new node there.
        Otherwise, continues recursion.
        """
        if key.data > curr.data:
            if curr.right_child is None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child is None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)
        # If key.data == curr.data, this implementation does not insert duplicates.

    def in_order(self):
        """
        Public method to perform an in-order traversal of the BST
        and print nodes' data. Order: Left, Node, Right.
        """
        self._in_order(self.root)
        print("")  # For a newline after traversal

    def _in_order(self, curr):
        """
        Helper method for in_order traversal (Left, Node, Right).
        """
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        """
        Public method for pre-order traversal: Node, Left, Right.
        """
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        """
        Helper for pre_order. Prints the node first,
        then recursively traverses the left and right subtrees.
        """
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        """
        Public method for post-order traversal: Left, Right, Node.
        """
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        """
        Helper for post_order. Recursively traverses left subtree,
        then right subtree, then prints the node.
        """
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data, end=" ")

    def find_val(self, key):
        """
        Public method to locate a value 'key' in the BST.
        Returns a string indicating whether the value is found or not.
        """
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        """
        Recursive search helper. At each node:
        - If curr.data == key, return "Value found in tree"
        - If key < curr.data, recurse left
        - If key > curr.data, recurse right
        - If curr is None, we've reached a leaf without finding 'key'
        """
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return "Value not found in tree"

    def min_right_subtree(self, curr):
        """
        Finds the minimum-value node in 'curr' subtree by moving left
        until it cannot go further. Used during node deletion
        for the case of two children.
        """
        if curr.left_child is None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        """
        Removes the node containing 'key' from the BST if it exists.
        Updates references within the tree so that BST properties are maintained.
        """
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        """
        Recursive helper that locates the node with 'key', then deletes it
        while preserving BST invariants:
        1) If the node has two children, replace its data with the minimum data
           of its right subtree, then remove that successor.
        2) If the node is a leaf, just remove it (set its parent's child link to None).
        3) If the node has one child, link the parent around the node being removed.
        """
        if curr:
            # If current node has the data to delete
            if key == curr.data:
                # Case 1: Node has two children
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child, curr, False, min_child.data)
                # Case 2: Node is a leaf
                elif curr.left_child is None and curr.right_child is None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        # We are deleting the root node in a single-node tree
                        self.root = None
                # Case 3a: Node has only right child
                elif curr.left_child is None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                # Case 3b: Node has only left child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            # If key is smaller, go left
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            # If key is greater, go right
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)
        else:
            # If we reach a None node, key is not in the tree
            print(f"{key} not found in Tree")


# Example Usage:
tree = BSTDemo()
# tree.insert("F")
# tree.insert("C")
# tree.insert("G")
# tree.in_order()
# tree.delete_val("C")
# tree.in_order()
print(tree.find_val("G"))
