# Define a list of tuples where each tuple contains two numbers.
a = [(0, 2), (4, 4), (10, -1), (5, 3)]

# Sort the list 'a' in-place.
# The key parameter uses a lambda function to extract the second element (index 1) from each tuple.
# This means the list will be sorted based on the second value in each tuple.
# 'reverse=False' specifies that the sorting should be in ascending order.
a.sort(key=lambda x: x[1], reverse=False)

# Print the sorted list.
print(a)
