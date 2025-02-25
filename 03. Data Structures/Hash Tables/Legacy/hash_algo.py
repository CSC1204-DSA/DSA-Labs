"""
Implements a simple hash table using a list of buckets (each bucket is a list).
Demonstrates storing (key, value) pairs, handling collisions by chaining.

Usage:
1) set_val(key, value) - Inserts or updates a key-value pair in the hash table.
2) get_val(key)        - Retrieves the value for the given key,
                         or returns a 'not found' message if absent.
"""


class AlgoHashTable:
    def __init__(self, size):
        """
        Initialize the hash table with a given number of buckets, 'size'.
        Each bucket is an empty list to handle collisions by chaining.
        """
        self.size = size
        self.hash_table = self.create_buckets()  # List of 'size' empty lists

    def create_buckets(self):
        """
        Helper function to create the initial list of empty buckets.
        """
        return [[] for _ in range(self.size)]

    def __str__(self):
        """
        Return a string representation of the hash table
        by concatenating the string forms of each bucket.
        """
        return "".join(str(item) for item in self.hash_table)

    def set_val(self, key, value):
        """
        Inserts or updates the (key, value) pair in the hash table.
        1) Compute hash of 'key' and reduce modulo the table size for the index.
        2) Check the bucket (list) at that index for an existing pair with the same key.
           If found, update it. Otherwise, append a new (key, value) pair.
        """
        # Determine the index by taking the built-in hash of the key
        hashed_key = hash(key) % self.size

        # Retrieve the bucket at the computed index
        bucket = self.hash_table[hashed_key]

        found_key = False
        # Search for the key in this bucket
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                # Key found; prepare to update
                found_key = True
                break

        if found_key:
            # Update existing (key, value)
            bucket[index] = (key, value)
        else:
            # Append a new (key, value) pair to the bucket
            bucket.append((key, value))

    def get_val(self, key):
        """
        Retrieves the value associated with 'key' from the hash table.
        1) Compute hash of 'key' and use modulo to find the index.
        2) Search the bucket at that index for a matching key.
        3) Return the value if found; otherwise report that the key isn't found.
        """
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        # Search the bucket for the key
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_value
        else:
            return f"{key} not found"


# Example Usage

# Create a hash table with 200 buckets
hash_table = AlgoHashTable(200)

# Reading data from a file named "data.txt"
# Each line is in the format: key:value
with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            key, value = line.split(":")
            hash_table.set_val(key, value)

# Print the structure of the hash table
print(hash_table)

print("-" * 100)

# Attempt to retrieve a specific key from the hash table
print(hash_table.get_val("ahlrdmukjn@yaexample.com"))
