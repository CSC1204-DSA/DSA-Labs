import re  # Import the regular expression module

# Define a sample string to perform regex operations on.
string = "this is a really cool string really!"

# Use re.search() to find the first occurrence of the substring 'really' in the string.
# re.search() scans through the string and returns a match object if found.
a = re.search('really', string)
print(a)  # Prints the match object (e.g., <re.Match object; span=(10, 16), match='really'>)

# The following methods are called on the match object 'a':
# - a.span() returns a tuple with the start and end positions of the match.
# - a.start() returns the starting index of the match.
# - a.end() returns the ending index of the match.
# - a.group() returns the matched substring.
# Note: If 'really' was not found, these methods would raise an error since 'a' would be None.
print(a.span())
print(a.start())
print(a.end())
print(a.group())

# Compile a regular expression pattern for the substring 'really'.
# Compiling a pattern can improve performance when the same pattern is used multiple times.
pattern = re.compile('really')

# Use the compiled pattern to search the string.
# This will return a match object for the first occurrence of 'really' in the string.
b = pattern.search(string)

# Use findall() to return a list of all non-overlapping occurrences of the pattern in the string.
c = pattern.findall(string)

# Compile a pattern for an exact match of the entire string.
pattern = re.compile('this is a really cool string really!')

# fullmatch() checks if the entire string exactly matches the pattern.
# 'd' will contain a match object because the string exactly matches.
d = pattern.fullmatch('this is a really cool string really!')

# 'e' will be None because the string does not exactly match the pattern.
e = pattern.fullmatch('hello this is a really cool string really!')  # Exact match required

# Re-compile the pattern for 'really' for use with match().
pattern = re.compile('really')

# match() checks if the pattern matches at the beginning of the string.
# 'f' will contain a match object because the string starts with 'really'.
f = pattern.match('really cool feature')  # The string starts with 'really'

# 'g' will be None because the string does not start with 'really'.
g = pattern.match('yo really')  # The string starts with 'yo', not 'really'

# Print the results of the various regex operations.
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")
