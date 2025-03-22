# Initialize an empty list to store individual characters.
my_list = []

# Loop over each character in the string 'hello'
for item in 'hello':
    # Append the current character to my_list.
    my_list.append(item)

# Print the list of characters from the string 'hello'.
print(my_list)

# Use a list comprehension to create a list of characters from the string 'Saurabh'.
# This is a concise way to iterate over each character in the string.
my_list1 = [item for item in 'Saurabh']
print(my_list1)

# Create a list of squares for numbers 1 through 10 using a list comprehension.
# For each number in the range 1 to 10, calculate its square and include it in the list.
my_list2 = [num**2 for num in range(1, 11)]
print(my_list2)

# Create a set of even squares from numbers 1 through 10 using a set comprehension.
# The condition 'if num**2 % 2 == 0' filters the squares to include only even numbers.
my_set = {num**2 for num in range(1, 11) if num**2 % 2 == 0}
print(my_set)

# Note: Sets in Python automatically remove duplicate values.
