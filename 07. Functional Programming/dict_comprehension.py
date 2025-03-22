# Create a dictionary using dictionary comprehension.
# For every number in the range 1 to 10, set the key as the number and the value as its square.
my_dict = {num: num**2 for num in range(1, 11)}
# Output the resulting dictionary.
print(my_dict)

# Define a simple dictionary with character keys and integer values.
random_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

# Create a new dictionary using comprehension.
# Iterate over each key (k) and value (v) in 'random_dict'.
# For each pair, the new value is the square of the original value.
my_new_dict = {k: v**2 for k, v in random_dict.items()}
# Print the new dictionary with squared values.
print(my_new_dict)

# Create another dictionary with a filter condition.
# For each key-value pair in 'random_dict', check if the value is even (v % 2 == 0).
# Only include pairs that satisfy the condition, with the value squared.
my_new_dict2 = {k: v**2 for k, v in random_dict.items() if v % 2 == 0}
# Print the filtered and modified dictionary.
print(my_new_dict2)
