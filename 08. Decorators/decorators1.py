# Define a function 'hello' that prints "hello!" when called.
def hello():
    print("hello!")

# Assign the 'hello' function to a new variable 'greet'.
# Both 'hello' and 'greet' now reference the same function object.
greet = hello

# Delete the name 'hello' from the current namespace.
# Note: The function object is still available via 'greet'.
del hello

# The following would raise an error because 'hello' is no longer defined:
# hello()

# Print the function object that 'greet' refers to.
# This displays information about the function, such as its memory address.
print(greet)

# Call the function using the 'greet' reference.
# This will output: hello!
greet()
