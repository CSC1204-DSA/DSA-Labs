"""
Demonstration of reversing a string by:
1. An iterative approach that constructs a new reversed string.
2. A second iterative approach that appends the characters in reverse to the original string,
   then slices the reversed portion.
3. A recursive approach that places the first character at the end by repeated calls.
"""

def iterative_reverse(string):
    """
    Iterative reversal of a string using an auxiliary string:
      - Traverse the original string from the last character to the first.
      - Concatenate each character to 'reversed_string'.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    reversed_string = ''
    for i in range(len(string)):
        reversed_string += string[len(string) - i - 1]
    return reversed_string

# Test the first iterative function
print(iterative_reverse("Zero To Mastery"))  # Expected: "yretsaM oT oreZ"


def second_iterative_reverse(string):
    """
    Iterative reversal by appending characters in reverse to the end of the
    original string, then slicing out the reversed part.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    original_length = len(string)
    # Append characters in reverse to the end of the string
    for i in range(original_length):
        string += string[original_length - i - 1]
    # Slice out the reversed portion
    string = string[original_length:]
    return string

# Test the second iterative function
print(second_iterative_reverse("Zero To Mastery"))  # Expected: "yretsaM oT oreZ"


def recursive_reverse(string):
    """
    Recursive approach to reverse a string:
      - Base Case: if the string is empty, return it.
      - Recursive Case: reverse the substring (excluding the first char), then append the first char.
    """
    print(string)  # Demonstration print to visualize the recursion steps
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]

# Test the recursive function
print(recursive_reverse("Zero To Mastery"))
# Expected: "yretsaM oT oreZ"
