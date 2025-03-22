# Define a function that checks if a given number is even.
def only_even(item):
    # Return True if the number is even (i.e., divisible by 2 with no remainder),
    # otherwise return False.
    return item % 2 == 0

# Define a list of integers.
my_list = [5, 8, 9, 2, 5, 6, 98, 56, 62]

# Apply the filter() function with only_even to my_list.
# The filter() function returns a filter object containing only the items for which only_even(item) is True.
# Printing the filter object directly will show its memory location, not the actual list of filtered items.
print(filter(only_even, my_list))

# Convert the filter object to a list to display the even numbers extracted from my_list.
# This will output a list of numbers from my_list that are even.
print(list(filter(only_even, my_list)))

# Apply the map() function with only_even to my_list.
# The map() function applies the only_even function to every element in my_list,
# resulting in a map object of boolean values (True for even, False for odd).
# Converting it to a list will show the boolean result for each element.
print(list(map(only_even, my_list)))

# Print the original list to show that it remains unchanged after using filter() and map().
print(my_list)
