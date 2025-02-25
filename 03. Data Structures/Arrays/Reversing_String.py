"""
Reverses a given string. Demonstrates multiple approaches:
1) Simple method of iterating from the end to the start.
2) Smarter in-place swap approach.
3) Using Python built-in functionalities.
"""


def simple_reverse(string):
    """
    Creates a new list, appending characters from the original
    string in reverse order, then joins them into a reversed string.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    new_string = []

    # Loop from the last index down to the first
    for i in range(len(string) - 1, -1, -1):
        new_string.append(string[i])

    # Join the list of reversed characters into a string
    return ''.join(new_string)


string = "Hello"
print(simple_reverse(string))  # Output: "olleH"


def swap(string, a, b):
    """
    Helper function to swap two characters at indices 'a' and 'b' in 'string'.
    Returns the new string with those characters swapped.
    """
    # Convert string to a list for mutability
    string_list = list(string)

    # Swap the elements at indices a and b
    temp = string_list[a]
    string_list[a] = string_list[b]
    string_list[b] = temp

    # Convert list back to string
    return ''.join(string_list)


def smarter_reverse(string):
    """
    Reverses the string by swapping characters in-place from the 
    two ends towards the center, avoiding creation of a separate array.

    Time Complexity: O(n)
    Space Complexity: O(1) (beyond the input string, though note that 
    Python strings are immutable, so effectively we're still creating 
    intermediate strings, but conceptually it's an in-place approach.)
    """
    # Perform swaps until the middle of the string is reached
    for i in range(len(string) // 2):
        string = swap(string, i, len(string) - i - 1)
    return string


print(smarter_reverse(string))  # Output: "olleH"

# Built-in methods to reverse a string

string1 = "abcde"

# Method 1: Using reversed()
string2 = reversed(string1)  # reversed() returns an iterator over the string in reverse
print(''.join(string2))  # Output: "edcba"

# Method 2: Using list reverse()
list1 = list(string1)  # Convert to list
list1.reverse()  # Reverse the list in-place
print(''.join(list1))  # Output: "edcba"
