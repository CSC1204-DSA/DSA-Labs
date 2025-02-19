# Import the time module to measure execution time
import time

# Create arrays of different sizes, filling each with the string 'CoCIS'
array_small = ['CoCIS' for i in range(10)]        # Array with 10 elements
array_medium = ['CoCIS' for i in range(100)]      # Array with 100 elements
array_large = ['CoCIS' for i in range(10000)]     # Array with 10,000 elements
array_large2 = ['CoCIS' for i in range(100000)]   # Array with 100,000 elements

def finding_nemo(array):
    """
    Iterates over each element in the given array and measures the
    total time taken to do so. Demonstrates O(n) time complexity
    since the loop runs 'n' times, where 'n' is the size of the array.
    """
    t0 = time.time()  # Record the start time
    for i in array:
        pass          # Placeholder for actual logic, does nothing here
    t1 = time.time()  # Record the end time
    print(f"Time taken = {t1 - t0}")

# Call the function with each array and observe that time taken grows with array size
finding_nemo(array_small)   # Expect minimal time for the small array
finding_nemo(array_medium)  # Expect more time for a larger array
finding_nemo(array_large)   # Expect even longer time
finding_nemo(array_large2)  # Expect the longest time

# Explanation:
# The time complexity is O(n) because we iterate through all elements
# of the array. As 'n' (the number of elements) increases,
# the total execution time increases linearly.
