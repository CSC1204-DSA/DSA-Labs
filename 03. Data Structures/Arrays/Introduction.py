"""
Demonstrates fundamental array (list) operations in Python (dynamic arrays), 
covering access, append (push), pop, insert, and delete, along with their 
typical time complexities.
"""

# Initialize the list (dynamic array) with some elements
array = [5, 8, 2, 9, 17, 43, 25, 10]

# ACCESS / LOOKUP
# Access an element by its index (O(1) time complexity in typical implementations).
first_element = array[0]   # Access the first element (5)
sixth_element = array[5]   # Access the sixth element (43)

# PUSH
# Append an element at the end of the list (amortized O(1) time complexity).
array.append(87)  # Adds 87 at the end of the list

# POP
# Remove the last element in O(1) time (amortized).
array.pop()  # Removes the last element (87)

print(array)  # Print the current state of the list

# INSERT
# Insert an element at a specified index (O(n) time complexity),
# because elements to the right need to shift one position.
array.insert(0, 50)  # Insert 50 at the beginning
array.insert(4, 0)   # Insert 0 at index 4

print(array)  # Print the list after the insert operations

# DELETE
# Remove an element by index (O(n) time), because elements to the right
# need to shift one position to the left.
array.pop(0)  # Remove the first element; everything shifts left
print(array)  # Print the list after popping index 0

# Remove an element by value (O(n) time), because it searches the list 
# until it finds a match.
array.remove(17)  # Remove the first occurrence of 17
print(array)

# Delete a slice (O(n) time) because elements are shifted.
del array[2:4]  # Remove elements from index 2 to 3 (inclusive)
print(array)

# Inserting a string at a far index will just place it at the end if the index is
# beyond the list length. Still O(n) because of shifting mechanics internally.
array.insert(11, 'shushrut')  
print(array)

print("-" * 100)  # Separator

# Another list to demonstrate lengths and insert
l = [5, 8, 2, 9, 17, 43, 25, 10]

# Printing 'len' directly shows that it's a built-in function (before reassigning it).
print(len)  

# Insert a new element at index 9 (which is effectively the end of the list in this case).
l.insert(9, "shushrut")

# Here, len is overridden as a variable name, storing the length of the list.
len = len(l)  
print(len)  # This now prints the integer length, not the built-in function

# Demonstrate Python's integer interning:
# a and b both reference the same small integer object (15), 
# so `a is b` is True. For larger integers like 300, 
# it may not always be the same object, depending on Python internals.
a = 15
b = 15
c = 300
d = 300
print(a is b, c is d)
