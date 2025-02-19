# Import the time module to measure execution time
import time

# Create arrays of different sizes, filling each with the string 'CoCIS'
array_small = ['CoCIS' for i in range(10)]        # An array with 10 elements
array_medium = ['CoCIS' for i in range(100)]      # An array with 100 elements
array_large = ['CoCIS' for i in range(10000)]     # An array with 10,000 elements
array_large2 = ['CoCIS' for i in range(100000)]   # An array with 100,000 elements

def finding_nemo(array):
    """
    Checks the first element of the given array to see if it is 'CoCIS', and measures
    the time it takes to do this. Demonstrates O(1) time complexity since only one
    comparison is made regardless of array size.
    """
    t0 = time.time()       # Record the start time
    if array[0] == 'CoCIS':
        pass               # 'pass' is a placeholder for any desired operation
    t1 = time.time()       # Record the end time
    print(f"Time taken = {t1 - t0}")

# Call the function with each array to show that the time taken is constant, O(1)
finding_nemo(array_small)
finding_nemo(array_medium)
finding_nemo(array_large)
finding_nemo(array_large2)

# Explanation:
# The time complexity is O(1) because the function only checks the first element of the array,
# performing a single comparison regardless of the array size.
