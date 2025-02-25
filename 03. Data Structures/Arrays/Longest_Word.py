"""
Finds the longest word in a given string by considering only alphanumeric characters.
Demonstrates multiple approaches:
1) Simple approach returning length only.
2) Naive approach to store and return the actual word.
3) Using regular expressions (regex) to simplify parsing and returning the longest word.
"""


def easy_longest_word(string):
    """
    Returns the length of the longest alphanumeric word in the given string.
    Iterates through each character:
    - If the character is alphanumeric, increase the counter.
    - If not, compare the counter with the current maximum and reset it to 0.
    Finally returns the maximum counter encountered.
    """
    count = 0
    maximum = 0

    for char in string:
        if char.isalnum():
            count += 1
        else:
            maximum = max(maximum, count)
            count = 0

    # Compare one last time after the loop finishes (in case the string ends with an alphanumeric character)
    maximum = max(maximum, count)
    return maximum


string = 'fun!@#$# times'
print(easy_longest_word(string))  # Prints the numeric length of the longest word


def naive_longest_word(string):
    """
    Returns the actual longest alphanumeric word from the given string.
    Logic:
    - Create a list `words` to store all unique words.
    - Create a temporary list `word` to collect characters of the current alphanumeric segment.
    - For each character:
      * If alphanumeric, add it to `word` and increment count.
      * If not, convert `word` to a string (if not empty or already in `words`) and add it to `words`.
        Then reset `word` to empty.
    - After the loop, handle any leftover word similarly.
    - Track the maximum length encountered during iteration, and finally return the first word that matches this maximum length.
    """
    count = 0
    maximum = 0
    words = []
    word = []

    for char in string:
        if char.isalnum():
            count += 1
            word.append(char)
        else:
            if word not in words and word:
                words.append(''.join(word))
                word = []
            maximum = max(maximum, count)
            count = 0

    # Handle any last word after the loop
    maximum = max(maximum, count)
    if word not in words and word:
        words.append(''.join(word))

    # Return the first word that matches the maximum length
    for item in words:
        if len(item) == maximum:
            return item


print(naive_longest_word(string))  # Prints the longest word among all alphanumeric segments

# Using Regular Expressions (Regex)
import re


def regex(string):
    """
    Returns the longest word from the string using regular expressions.
    1) Splits the string by one or more word characters (\w+) into a list.
    2) Finds the maximum length of these extracted words.
    3) Returns the first word that matches this maximum length.
    """
    # Find all alphanumeric segments in the string
    string = re.findall(r'\w+', string)
    # Compute the maximum length among all words
    maximum = max([len(item) for item in string])
    # Return the first word that matches the max length
    for item in string:
        if len(item) == maximum:
            return item


sss = "Hello there how are you"
print(regex(sss))  # Prints the longest word among "Hello", "there", "how", "are", "you"
