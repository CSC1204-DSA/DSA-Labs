# Importing the time module to measure the execution time
import time

# Creating arrays of different sizes filled with the string 'nemo'
array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(10000)]
array_large2 = ['nemo' for i in range(100000)]

# Define a function to check only the first element of the array and measure the time taken
def finding_nemo(array):
    t0 = time.time()  # Start time
    if array[0] == 'nemo':  # Check only the first element
        pass  # Pass statement does nothing but indicates where logic could be implemented
    t1 = time.time()  # End time
    print(f'Time taken = {t1 - t0}')  # Print the time taken for the operation

# Call the function with different arrays to observe that time taken remains constant
finding_nemo(array_small)  # Time taken should be minimal and constant
finding_nemo(array_medium)  # Time remains constant despite larger array size
finding_nemo(array_large)  # Constant time despite even larger array
finding_nemo(array_large2)  # Constant time for the largest array

# This function demonstrates O(1) - Constant Time Complexity.
# The time complexity is O(1) because it always performs a fixed number of operations (one check).
