# Higher Order Function (HOC): a function that accepts another function as an argument,
# or returns a function as its result.

# 'greet' is a higher order function that accepts a function 'func' as its parameter
# and then calls (executes) that function.
def greet(func):
    func()

# 'greet2' is intended to be a function that returns another function or its result.
# Here, it defines an inner function 'hello' that prints "hello!".
def greet2():
    # Define an inner function 'hello' that prints "hello!" when called.
    def hello():
        print("hello!")
    # Call the inner function 'hello' and return its result.
    # Note: Since 'hello' doesn't return any value (returns None by default),
    # 'greet2' will return None after printing "hello!".
    return hello()

# Call the higher order function 'greet' and pass 'greet2' as an argument.
# This will execute 'greet2()', which in turn calls 'hello()' and prints "hello!".
# Since 'greet2()' returns None, 'greet' also returns None.
print(greet(greet2))
