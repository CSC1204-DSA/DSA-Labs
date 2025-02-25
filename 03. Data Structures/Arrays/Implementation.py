# This class implements a simple array-like data structure using a dictionary for storage.
# It provides methods to get, push, pop, insert, and delete elements, simulating typical array operations.

class my_array():
    def __init__(self):
        self.length = 0  # Tracks the current number of elements in the array
        self.data = {}   # Dictionary to store elements with key as index and value as item

    def __str__(self):
        """
        Modifies how the class instance is printed.
        By default, it would show an object reference,
        but here we display the dictionary of attributes for clarity.
        """
        print(self.data.values())
        return str(self.__dict__)

    def get(self, index):
        """
        Retrieves the element at the given index in O(1) time.
        """
        return self.data[index]

    def push(self, item):
        """
        Adds a new item at the end of the array and increments the length.
        """
        self.length += 1
        self.data[self.length - 1] = item

    def pop(self):
        """
        Removes the last item from the array and decrements the length.
        Returns the removed item in O(1) time.
        """
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def insert(self, index, item):
        """
        Inserts an item at the given index, shifting subsequent elements to the right.
        This is an O(n) operation.
        """
        self.length += 1
        # Shift elements one step to the right, starting from the end
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item

    def delete(self, index):
        """
        Deletes the element at the given index, shifting elements after it to the left.
        This is also an O(n) operation.
        """
        # Shift elements one step to the left from the deletion point
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        # Remove the now-duplicate last element
        del self.data[self.length - 1]
        self.length -= 1

# Example usage:

arr = my_array()
print(arr)
print("-" * 100)

arr.push(6)   # Adds 6 at index 0
arr.push(2)   # Adds 2 at index 1
arr.push(9)   # Adds 9 at index 2
arr.pop()     # Removes the last element (9)
arr.push(45)
arr.push(12)
arr.push(67)
arr.insert(3, 10)  # Inserts 10 at index 3
arr.delete(4)      # Deletes the element at index 4
print(arr.get(1))  # Outputs the element at index 1 (should be 2)
print(arr)         # Prints the current state of the array
