# Define a custom function that mimics a for loop using an iterator.
def my_own_forloop(iterable):
    # Convert the input iterable (e.g., a list) into an iterator.
    iterator = iter(iterable)

    # Loop indefinitely until the iterator is exhausted.
    while True:
        try:
            # Print the current iterator object (for demonstration purposes).
            print(iterator)
            # Retrieve and print the next element from the iterator.
            # If no elements remain, this will raise a StopIteration exception.
            print(next(iterator))
        except StopIteration:
            # When the iterator is exhausted, a StopIteration exception is caught,
            # and the loop is terminated.
            break


# Call the custom for loop function with a list of numbers.
my_own_forloop([1, 2, 3, 4, 5])
