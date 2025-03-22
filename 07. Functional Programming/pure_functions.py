def multiply_by2(li):
    # Create a new, local list to store results.
    # Defining new_li inside the function ensures it is not affected by or affecting external variables.
    new_li = []
    # Iterate over each element in the input list.
    for item in li:
        # Append the current item to the new list.
        # NOTE: Despite the function's name suggesting multiplication, here we are simply copying the items.
        new_li.append(item)
    # Return the new list.
    return new_li

# Call the function with a sample list and print the result.
print(multiply_by2([5, 6, 8]))

'''
Explanation:
- The function 'multiply_by2' is designed as a pure function: it only works on its input and returns a new list.
- It does not modify any external state; 'new_li' is a local variable.
- There are no print statements or external side effects within the function.
- If we were to define 'new_li' outside of the function or include print statements inside it, the function would no longer be pure,
  as it would then rely on or alter external state.
'''
