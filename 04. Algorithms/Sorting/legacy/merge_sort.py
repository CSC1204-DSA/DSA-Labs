def merge_sorted(arr1, arr2):
    """
    Merges two sorted lists (arr1, arr2) into one sorted list.

    Steps:
      1. Initialize pointers i, j to the start of each list.
      2. Compare arr1[i] and arr2[j], append the smaller to sorted_arr.
      3. Advance the pointer in the list from which the smaller element was chosen.
      4. If any elements remain in arr1 or arr2, append them to sorted_arr.
    """
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    # Merge elements while both sub-lists have items
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    # If there are remaining elements in arr2, append them
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    # If there are remaining elements in arr1, append them
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    return sorted_arr


def mergesort(arr):
    """
    Sorts a list 'arr' in ascending order using the Merge Sort algorithm.

    Steps:
      1. If the list is of length < 2, it's already sorted; return a copy.
      2. Otherwise, find the middle index.
      3. Recursively sort the left half and the right half.
      4. Merge the two sorted halves.
    """
    # Base case: A list of length < 2 is already sorted
    if len(arr) < 2:
        return arr[:]

    middle = len(arr) // 2
    # Recursively sort both halves
    l1 = mergesort(arr[:middle])
    l2 = mergesort(arr[middle:])
    # Merge the two sorted halves
    return merge_sorted(l1, l2)


# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l = [8, 6, 2, 5, 10, 13, 4, 55, 61, 23, 100]
print("Initial list:", l)
sorted_list = mergesort(l)
print("Sorted list: ", sorted_list)
