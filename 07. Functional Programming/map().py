# Define a function that multiplies a given item by 2.
def multiply_by2(item):
    # Return the result of the multiplication.
    return item * 2

# Create a list of numbers.
my_list = [5, 8, 9]

# Apply the 'multiply_by2' function to each element in 'my_list' using the map() function.
# Note: map() returns a map object, which is an iterator that produces the results on demand.
print(map(multiply_by2, my_list))  # This will print the map object (e.g., <map object at 0x...>).

# Convert the map object to a list to see the actual results of the function application.
# The list() function consumes the iterator and returns a new list containing the mapped values.
print(list(map(multiply_by2, my_list)))  # Outputs the list [10, 16, 18].

# Print the original list to show that it remains unchanged.
print(my_list)

'''
Explanation:
- The function 'multiply_by2' takes an input 'item' and returns the value multiplied by 2.
- The map() function applies 'multiply_by2' to every element in 'my_list' and creates a new iterator.
- Converting the map object to a list with list() displays the transformed values.
- Note that the original list 'my_list' is not modified; map() creates a new collection.
- This demonstrates a core idea in functional programming: functions are applied to data without side effects.
- The function is "pure" since it returns a new value without modifying the input data.
'''
