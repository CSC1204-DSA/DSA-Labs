import functools  # Import the functools module for the reduce function

# Define a list of integers.
my_list = [1, 2, 3, 4, 5]

# Use map() with a lambda function to multiply each element by 2.
# The lambda function takes a parameter 'item' and returns item * 2.
# map() applies this function to every element in my_list.
# We convert the result to a list and print it.
print(list(map(lambda item: item * 2, my_list)))

# Use filter() with a lambda function to select only odd numbers from my_list.
# The lambda function checks if an item is odd (item % 2 != 0).
# filter() returns only those elements for which the lambda returns True.
# We convert the filtered result to a list and print it.
print(list(filter(lambda item: item % 2 != 0, my_list)))

# Use functools.reduce() with a lambda function to sum all the elements in my_list.
# The lambda function takes two parameters: acc (accumulator) and item.
# It returns the sum of the accumulator and the current item.
# reduce() applies this function cumulatively, resulting in the total sum.
print(functools.reduce(lambda acc, item: item + acc, my_list))

# The following multi-line string explains the lambda syntax:
'''
syntax:
lambda param: action(param)
It automatically returns the result of the action,
has no name (is anonymous), and doesn't get stored in memory.
Therefore, it is typically used only once,
behaving exactly like a regular function.
'''
