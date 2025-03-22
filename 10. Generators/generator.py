# Define a generator function 'generator_fn' that works similarly to range().
# Generator functions yield one value at a time and maintain their state between yields.
def generator_fn(num):
    print("check")  # This prints once when the generator is first created.
    # Loop over a range of numbers from 0 to num-1.
    for i in range(num):
        print("****")  # Indicates that the loop iteration has started.
        yield i * 2   # Yield the value of i multiplied by 2.
        # After yielding, the function pauses here until the next value is requested.
        print("####")  # This line will execute after a yield when the generator resumes.

# Create a generator object by calling generator_fn with 3.
g = generator_fn(3)
print(g)  # Prints the generator object reference.

# Retrieve and print values from the generator using next().
# Each call to next(g) resumes the function until it hits the next yield.
print(next(g))  # First call: prints "check", "****", then yields 0 (0*2).
print(next(g))  # Second call: resumes, prints "####", then "****", then yields 2 (1*2).
print(next(g))  # Third call: resumes, prints "####", then "****", then yields 4 (2*2).

# Uncommenting the next line would raise a StopIteration error since the generator is exhausted.
# print(next(g))

print(g)  # Prints the generator object reference (still the same object, now exhausted).

# Using a for loop to iterate over the generator.
# Each iteration automatically calls next() until the generator is exhausted.
for item in generator_fn(5):
    print(item)

'''
Explanation:
- The 'yield' keyword makes this function a generator.
- When a generator function is called, it returns a generator object without executing the function.
- The function's execution is paused at each 'yield' statement, resuming on subsequent calls (e.g., via next()).
- This approach does not store all values in memory at once; it generates them on the fly.
- This is similar to how the built-in range() function works in terms of memory efficiency.
'''
