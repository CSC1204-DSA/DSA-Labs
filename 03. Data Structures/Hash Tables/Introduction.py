"""
Demonstrates basic usage of Python dictionaries, which internally utilize 
a hash table for storing key-value pairs.

Key Points:
1) Lookup by key in O(1) average time.
2) Insertion/Deletion in O(1) average time.
3) Collisions may occur, but are handled internally with minimal performance impact.
"""

# Creating a dictionary (hash table) and initializing it with some key-value pairs
dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print(dictionary)  
# Example Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# Retrieving all keys
print(dictionary.keys())  
# dict_keys(['one', 'two', 'three', 'four', 'five'])

# Retrieving all values
print(dictionary.values())  
# dict_values([1, 2, 3, 4, 5])

# Retrieving all key-value pairs as tuples
print(dictionary.items())  
# dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)])

# Accessing a value using its key (O(1) average complexity)
print(dictionary['one'])  
# 1

# Adding a new key-value pair (O(1) average complexity)
dictionary['six'] = 6
print(dictionary)  
# Example Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
