# Define a function 'hello' that accepts another function 'func' as an argument.
# This demonstrates that functions in Python are first-class objects, meaning
# they can be passed around as variables and arguments.
def hello(func):
    # Call the function passed as an argument.
    func()

# Define a function 'greet' that prints "Hello!".
def greet():
    print("Hello!")

# Call the 'hello' function, passing the 'greet' function as an argument.
# Inside 'hello', 'greet' will be executed, printing "Hello!".
hello(greet)

# This example shows that functions can be used as variables and passed as arguments to other functions.
