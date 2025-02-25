"""
Implements a Trie (prefix tree) data structure to store strings, enabling
fast prefix-based searches. Each node in the Trie can have up to 26 children
(for the 26 letters of the English alphabet), and an end_of_word marker to
indicate the termination of a word.

Time Complexity:
- insert(string): O(m), where m is the length of the string
- search(string): O(m)
"""

class TrieNode:
    """
    Represents a node in the Trie, holding:
    - an array 'children' of size 26, each entry potentially a TrieNode
    - a boolean 'is_end_of_word' marking if this node corresponds
      to the last letter of a valid word in the trie.
    """
    def __init__(self):
        self.children = [None] * 26  # 26 letters: a-z or A-Z
        self.is_end_of_word = False  # Tracks if this node marks the end of a word

class Trie:
    """
    A Trie (prefix tree) class with:
    - A 'root' node (TrieNode)
    - insert(string): Inserts a string into the Trie
    - search(string): Checks if a string exists in the Trie
    """

    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def _character_index(self, char):
        """
        Converts a character into a zero-based index (0-25).
        Handles both uppercase and lowercase letters by aligning them to 'a' or 'A'.
        """
        if char.isupper():
            return ord(char) - ord('A')
        else:
            return ord(char) - ord('a')

    def insert(self, string):
        """
        Inserts 'string' into the Trie in O(m) time, where m is the string length.
        For each character:
         1) Convert character to a zero-based index.
         2) If the corresponding child doesn't exist, create it.
         3) Move the pointer to that child.
        After the last character, mark is_end_of_word=True.
        """
        pointer = self.root
        for char in string:
            index = self._character_index(char)
            if pointer.children[index] is None:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True

    def search(self, string):
        """
        Searches for 'string' in the Trie. Returns True if the word exists, else False.
        Similar traversal as insert, but if a required child doesn't exist, returns False.
        The final node must have is_end_of_word=True.
        Time Complexity: O(m)
        """
        pointer = self.root
        for char in string:
            index = self._character_index(char)
            if pointer.children[index] is None:
                return False
            pointer = pointer.children[index]
        return pointer is not None and pointer.is_end_of_word


# Demonstration
if __name__ == "__main__":
    my_trie = Trie()
    my_trie.insert('Data')
    my_trie.insert("Structures")
    my_trie.insert("and")
    my_trie.insert("Algorithms")

    print(my_trie.search("and"))         # Expected: True
    print(my_trie.search("Data"))        # Expected: True
    print(my_trie.search("woohoo"))      # Expected: False
    print(my_trie.search("STructures"))  # Expected: True
