# Define a list of fruits.
fruits = ['apple', 'banana', 'cherry', 'grape']

# Use the enumerate() function to loop through the fruits list.
# The second argument (1) specifies that indexing should start at 1 instead of the default 0.
# 'index' will hold the current index (starting from 1) and 'fruit' will hold the fruit name.
for index, fruit in enumerate(fruits, 1):
    # Print the current index and fruit name.
    print(index, fruit)
