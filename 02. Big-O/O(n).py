# Importing the time module to measure the execution time
import time

# Creating arrays of different sizes filled with the string 'nemo'
array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(10000)]
array_large2 = ['nemo' for i in range(100000)]

# Define a function to iterate through an array and measure the time taken
def finding_nemo(array):
    t0 = time.time()  # Start time
    for i in array:
        pass  # Pass statement is a placeholder, does nothing but can be replaced with actual logic
    t1 = time.time()  # End time
    print(f'Time taken = {t1 - t0}')  # Print the time taken for the loop to execute

# Call the function with different arrays to observe time taken
finding_nemo(array_small)  # Expect short time for small array
finding_nemo(array_medium)  # Expect longer time for medium array
finding_nemo(array_large)  # Longer time for large array
finding_nemo(array_large2)  # Even longer time for largest array

# The function's time complexity is O(n), where n is the number of elements in the array.
# The time taken to execute the function increases with the size of the array.
# This demonstrates linear time complexity.
