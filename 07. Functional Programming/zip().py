# Define a list with three elements.
li1 = [1, 2, 3]

# Define a set with three elements.
# Note: Sets are unordered collections, so the pairing with other iterables may not follow a predictable order.
set1 = {4, 5, 6}

# Define a tuple with three elements.
tuple1 = (7, 8, 9)

# Use the zip() function to aggregate elements from the three iterables.
# zip() creates an iterator that pairs the first element from each iterable, then the second element, and so on.
print(zip(li1, set1, tuple1))  # Prints the zip object (an iterator), not the actual paired values.

# Convert the zip object to a list to display the sequence of tuples.
# Each tuple contains one element from li1, set1, and tuple1, in that order.
print(list(zip(li1, set1, tuple1)))  # Combines items sequence-wise into a sequence of tuples.

# Print the original iterables to show they remain unchanged after using zip().
print(li1, set1, tuple1)

'''
Note:
- The zip() function stops when the shortest iterable is exhausted.
- In this example, all iterables contain three elements.
- When using sets, remember that their inherent unordered nature may result in unpredictable pairings.
- Ensure that all iterables have the same number of elements to maintain consistent and expected output.
'''
