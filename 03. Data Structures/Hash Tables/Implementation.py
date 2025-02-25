"""
Implements a simple hash table (dictionary) using an array of lists
to handle collisions (chaining).

Methods:
1) set(key, value)      : Insert a key-value pair.
2) get(key)             : Retrieve the value by key.
3) keys()               : Return all keys in the hash table.
4) values()             : Return all values in the hash table.

Collisions are handled by storing multiple (key, value) pairs in
a list at the hashed index.

Note: This is a simplistic hash table implementation to demonstrate
the core concepts of hashing and collision resolution via chaining.
"""

class hash_table:
    def __init__(self, size):
        """
        Initializes the hash table with a fixed 'size'. Creates an array
        (self.data) of length 'size' where each position is initially None.
        """
        self.size = size
        self.data = [None] * self.size  # Each slot can hold a list of [key, value] pairs

    def __str__(self):
        """
        Returns a string representation of the hash table's attributes:
        - number of buckets (self.size)
        - the array of buckets (self.data)
        """
        return str(self.__dict__)

    def _hash(self, key):
        """
        Custom hash function to convert 'key' into an index.
        It:
        1) Iterates over each character in the key.
        2) Converts it to its Unicode code point using 'ord'.
        3) Aggregates and takes the final sum modulo 'self.size'
           to ensure it's within array bounds.
        Returns an integer that serves as the index for that key.
        """
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.size
        return hash_value

    def get(self, key):
        """
        Retrieves the value for 'key' if it exists in the hash table.
        1) Hash the key to get the index.
        2) If the bucket (self.data[index]) is not None, search each
           [key, value] pair in that bucket.
        3) Return the matching value if found, otherwise return None.
        """
        hash_index = self._hash(key)
        if self.data[hash_index]:
            # Check each (key, value) pair in the bucket
            for i in range(len(self.data[hash_index])):
                if self.data[hash_index][i][0] == key:
                    return self.data[hash_index][i][1]
        return None

    def set(self, key, value):
        """
        Inserts a new (key, value) pair into the hash table.
        1) Hash the key to get the index.
        2) If the bucket at that index is empty, create a new list there.
        3) Otherwise, append the (key, value) pair to handle collision.
        """
        hash_index = self._hash(key)
        if not self.data[hash_index]:
            self.data[hash_index] = [[key, value]]
        else:
            self.data[hash_index].append([key, value])
        print(self.data)

    def keys(self):
        """
        Returns a list of all keys in the hash table.
        1) Iterate through each bucket.
        2) For every [key, value] pair in the bucket, append the key to keys_array.
        """
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                # Each bucket can have multiple [key, value] pairs
                for j in range(len(self.data[i])):
                    keys_array.append(self.data[i][j][0])
        return keys_array

    def values(self):
        """
        Returns a list of all values in the hash table.
        1) Iterate through each bucket.
        2) For every [key, value] pair in the bucket, append the value to values_array.
        """
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array


# Demonstration of hash_table usage
new_hash = hash_table(2)
print(new_hash)  # Shows initial structure: {'size': 2, 'data': [None, None]}

# Insert some key-value pairs
new_hash.set('one', 1)
new_hash.set('two', 2)
new_hash.set('three', 3)
new_hash.set('four', 4)
new_hash.set('five', 5)
print(new_hash)
# Example bucket structure:
# {'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

# Retrieve a value using a key
print(new_hash.get('one'))   # Output: 1

# Retrieve all keys
print(new_hash.keys())       # Example Output: ['one', 'five', 'two', 'three', 'four']

# Retrieve all values
print(new_hash.values())     # Example Output: [1, 5, 2, 3, 4]
