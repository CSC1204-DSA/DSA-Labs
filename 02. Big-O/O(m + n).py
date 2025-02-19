import time  # Import the time module for measuring execution times

# Create two lists of 100,000 elements each, where every element is the string "CoCIS".
large1 = ['CoCIS' for i in range(100000)]  # List of size m = 100,000
large2 = ['CoCIS' for i in range(100000)]  # List of size n = 100,000


def find_nemo(array1, array2):
    """
    This function searches through two arrays (array1 and array2) for the string "CoCIS".
    It measures and prints how long each search takes, and prints a message each time
    "CoCIS" is found in the lists.
    """

    # Record the start time before searching array1
    t0 = time.time()

    # Iterate over every element in array1
    for i in range(len(array1)):
        # If the element matches "CoCIS", print a confirmation message
        if array1[i] == 'CoCIS':
            print("Found CoCIS!!")

    # Record the end time after searching array1
    t1 = time.time()
    # Print the time taken to complete the search in array1
    print(f'The search for array1 took {t1 - t0} seconds.')

    # Record the start time before searching array2
    t0 = time.time()

    # Iterate over every element in array2
    for i in range(len(array2)):
        # If the element matches "CoCIS", print a confirmation message
        if array2[i] == 'CoCIS':
            print("Found CoCIS!!")

    # Record the end time after searching array2
    t1 = time.time()
    # Print the time taken to complete the search in array2
    print(f'The search for array2 took {t1 - t0} seconds.')


# Call the function with the two lists as arguments
find_nemo(large1, large2)
