from functools import reduce  # Import reduce from the functools module

def accumulator(acc, item):
    # Print the current accumulator value and the current item for debugging purposes.
    print(f'acc: {acc}, item: {item}')
    # Return the sum of the accumulator and the current item.
    return acc + item

# Define a list of numbers.
my_list = [1, 2, 3, 4, 5]

# Use reduce() with the accumulator function on my_list.
# Since no initial value is provided, reduce() uses the first element as the initial accumulator.
# It effectively computes (((1+2)+3)+4)+5.
print(reduce(accumulator, my_list))

# Use reduce() with an initial value of 10.
# Here, the initial accumulator starts at 10 and then adds each element of my_list in sequence.
print(reduce(accumulator, my_list, 10))

# Print the original list to show that it remains unchanged after reduce().
print(my_list)

'''
Explanation:
- The accumulator function prints the accumulator (acc) and the current item at each step,
  which helps in understanding the intermediate values during the reduction process.
- The first call to reduce() starts with the first element of my_list as the accumulator.
- The second call to reduce() provides an initial accumulator value of 10.
- The original list (my_list) is not modified by the reduce() function.
- In this context, "acc" represents the cumulative result returned by the accumulator function from the previous iteration.
'''
