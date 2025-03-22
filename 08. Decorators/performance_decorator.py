from time import time  # Import the time function to measure execution time

# Define a decorator 'performance' that measures the time a function takes to execute.
def performance(fn):
    # The inner wrapper function that will replace the original function.
    # It accepts any positional and keyword arguments.
    def wrap_fn(*args, **kwargs):
        t1 = time()  # Record the start time before function execution.
        fn(*args, **kwargs)  # Execute the original function with its arguments.
        t2 = time()  # Record the end time after function execution.
        # Print the time difference, which is the execution duration of the function.
        print(f'It took {t2 - t1} sec')
    # Return the wrapper function, which now replaces the original function.
    return wrap_fn

# Apply the 'performance' decorator to 'long_fn'.
# This means that calling 'long_fn()' will now execute 'wrap_fn' instead.
@performance
def long_fn():
    # Loop 10 million times performing a simple operation.
    # The operation 'i * 5' is executed for each iteration.
    for i in range(10000000):
        i * 5  # Multiply i by 5; the result is not used.

# Execute the decorated function.
# This will run the loop and then print how long the function took to execute.
long_fn()
