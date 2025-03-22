class OurOwnRange():
    # Class variable 'current' defined here is not ideal for per-instance iteration,
    # so we'll use an instance variable instead.

    def __init__(self, first, last):
        # Initialize the range with a starting value ('first') and an ending value ('last').
        # The range will generate numbers from 'first' up to but not including 'last'.
        self.first = first
        self.last = last
        # Set the current value for the instance to the starting value.
        self.current = first

    def __iter__(self):
        # Return the iterator object itself.
        # This method makes OurOwnRange an iterator.
        return self

    def __next__(self):
        # Print a message each time __next__ is called (for demonstration purposes).
        print("hehehheh")
        # Check if the current value is less than the last value.
        if self.current < self.last:
            # Save the current value to return.
            num = self.current
            # Increment the current value for the next iteration.
            self.current += 1
            return num
        # Once current reaches or exceeds last, raise StopIteration to signal the end of iteration.
        raise StopIteration


# Create an instance of OurOwnRange that generates numbers from 0 to 9.
gen = OurOwnRange(0, 10)
# Print the generator object reference.
print(gen)

# Use a for loop to iterate over the custom iterator.
# The loop handles the StopIteration exception internally when the iteration ends.
for i in gen:
    print(i)

'''
Explanation:
- This custom iterator class mimics the behavior of Python's built-in range() function.
- The __iter__() method returns the iterator (self), allowing the object to be used in a for loop.
- The __next__() method returns the next number in the sequence until it reaches the defined limit,
  at which point it raises a StopIteration exception to terminate the loop.
- The print statements (e.g., "hehehheh") illustrate when __next__ is invoked.
'''
