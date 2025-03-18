# ----------------------------------------------
# BFS (Breadth First Search) Implementation in a BST
# ----------------------------------------------

# A BFS or Breadth First Search is a traversal algorithm for a tree (or graph).
# We start from the root node (for a tree) and visit all the nodes level by level, from left to right.
# During this process, we store the children of each node in a queue, allowing us to visit them in the correct order.
#
# Time Complexity: O(n) because every node is visited exactly once.
# Space Complexity: Potentially O(n) in the worst case (e.g., a "wide" tree with many nodes at the same level).

# Below is an implementation of a Binary Search Tree (BST) along with BFS.


class Node:
    """
    Node Class for the BST.
    Contains:
    - data: The value/data stored in the node
    - left: Pointer to the left child (initially None)
    - right: Pointer to the right child (initially None)
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree (BST) class.
    Contains:
    - root: The root node of the BST (initially None)
    - number_of_nodes: Keep track of how many nodes exist in the tree
    """

    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):
        """
        Insert a new node with 'data' into the BST.
        Steps:
        1. If the tree is empty, make the new node the root.
        2. Otherwise, compare the new node's data with the current node:
            - If new node data > current node data, go to the right subtree.
            - If new node data < current node data, go to the left subtree.
        3. Insert the new node once the correct spot (None child) is found.

        Average Case Complexity: O(log n)
        Worst Case Complexity:   O(n) (for a skewed tree)
        """
        new_node = Node(data)

        # If tree has no root, set the root to the new node.
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            # Start from the root and find the correct position for insertion.
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    # If right child is None, attach new_node here, otherwise move right.
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    # If left child is None, attach new_node here, otherwise move left.
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left

            # Increment the count of nodes after successful insertion
            self.number_of_nodes += 1
            return

    def search(self, data):
        """
        Search for a node with the value 'data' in the BST.
        Steps:
        1. Start from the root.
        2. While the current node is not None:
            - If the current node's data matches 'data', return "Found".
            - If current_node.data > data, move to the left child.
            - Else move to the right child.
        3. If we reach a None node, it means the value doesn't exist in the tree.
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
        This operation is more complex as we need to handle multiple cases:
          1. The node to remove might not exist.
          2. The node to remove could have:
             - No children
             - Only left child
             - Only right child
             - Both left and right children

        We'll traverse the tree until we find the node or reach the end.
        After finding the node, we handle the above cases to restructure the tree accordingly.
        """
        if self.root is None:  # Tree is empty
            return "Tree Is Empty"

        current_node = self.root
        parent_node = None

        # First, find the node to remove and keep track of its parent
        while current_node is not None:
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Match found. Now handle the removal cases.

                # CASE 1: Node has only left child
                if current_node.right is None:
                    # If removing the root node itself:
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        # Replace parent's pointer according to BST property
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left
                        return

                # CASE 2: Node has only right child
                elif current_node.left is None:
                    # If removing the root node itself:
                    if parent_node is None:
                        self.root = current_node.right
                        return
                    else:
                        # Replace parent's pointer accordingly
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                        else:
                            parent_node.right = current_node.right
                        return

                # CASE 3: Node has no children (leaf node)
                elif current_node.left is None and current_node.right is None:
                    if parent_node is None:
                        # If it's the root node and it has no children
                        current_node = None
                        self.root = None
                        return
                    # If it is not the root, set the appropriate parent's child to None
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return

                # CASE 4: Node has both left and right children
                elif current_node.left is not None and current_node.right is not None:
                    # We'll find the leftmost node in the right subtree (successor)
                    del_node = current_node.right
                    del_node_parent = current_node.right

                    # Move all the way left
                    while del_node.left is not None:
                        del_node_parent = del_node
                        del_node = del_node.left

                    # Replace current_node's data with that of the found successor
                    current_node.data = del_node.data

                    # If del_node is actually the immediate right child
                    if del_node == del_node_parent:
                        current_node.right = del_node.right
                        return

                    # If the successor (del_node) has no right child
                    if del_node.right is None:
                        del_node_parent.left = None
                    else:
                        # If the successor has a right subtree,
                        # link it to the del_node's parent
                        del_node_parent.left = del_node.right
                    return

        return "Not Found"

    def BFS(self):
        """
        Perform BFS (Breadth First Search) traversal on the BST.
        Steps:
        1. Start with the root node.
        2. Maintain a queue to keep track of nodes at the current level.
        3. While the queue is not empty:
            a. Pop the first node from the queue (current node).
            b. Append the current node's data to the result list.
            c. If the current node has a left child, enqueue it.
            d. If the current node has a right child, enqueue it.
        4. Return the result list containing the BFS traversal.
        """
        current_node = self.root
        BFS_result = []
        queue = []

        if not current_node:
            return BFS_result  # If the tree is empty, return empty list

        # Enqueue the root node
        queue.append(current_node)

        # While there are nodes to process
        while len(queue) > 0:
            # Dequeue the front node and process it
            current_node = queue.pop(0)
            BFS_result.append(current_node.data)

            # Enqueue the left child if it exists
            if current_node.left:
                queue.append(current_node.left)
            # Enqueue the right child if it exists
            if current_node.right:
                queue.append(current_node.right)

        return BFS_result

    def Recursive_BFS(self, queue, BFS_list):
        """
        A recursive version of BFS.
        Arguments:
        - queue: a list that initially contains the root node.
        - BFS_list: an initially empty list to accumulate the data in BFS order.

        Steps:
        1. If the queue is empty, we are done. Return the BFS_list.
        2. Pop the first element from the queue, append its data to BFS_list.
        3. If that element has a left child, enqueue it; if it has a right child, enqueue it.
        4. Recursively call the function with the updated queue and BFS_list.
        """
        # Base case: if there's nothing in the queue, return the BFS list
        if len(queue) == 0:
            return BFS_list

        current_node = queue.pop(0)
        BFS_list.append(current_node.data)

        # Enqueue children if they exist
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        # Recursively call with the updated queue
        return self.Recursive_BFS(queue, BFS_list)


# ----------------------------------------------
# Testing the BST and BFS Implementations
# ----------------------------------------------

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
'''
            5
        3       7
    1               13
  0             10      65
'''

# The BFS Traversal for this tree should be : [5, 3, 7, 1, 13, 0, 10, 65]

# Iterative BFS
print(my_bst.BFS())
# Expected Output: [5, 3, 7, 1, 13, 0, 10, 65]

# Recursive BFS
print(my_bst.Recursive_BFS([my_bst.root], []))
# Expected Output: [5, 3, 7, 1, 13, 0, 10, 65]
