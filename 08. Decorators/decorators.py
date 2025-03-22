# Define a decorator function 'my_decorator' that takes a function 'func' as an argument.
def my_decorator(func):
    # Define an inner function 'wrap_func' that will wrap around the original function.
    def wrap_func():
        # Print a decorative line before calling the original function.
        print("***********")
        # Call the original function passed to the decorator.
        func()
        # Print another decorative line after the original function is executed.
        print("***********")
    # Return the inner function, effectively replacing the original function with 'wrap_func'.
    return wrap_func

# Use the decorator '@my_decorator' to wrap the 'hello' function.
@my_decorator
def hello():
    # The original functionality of 'hello' is to print "Hello!".
    print("Hello!")

# When calling 'hello()', the decorator intercepts the call and executes 'wrap_func' instead.
hello()

# Note:
# The decorator syntax '@my_decorator' is equivalent to explicitly reassigning the function as follows:
# hello = my_decorator(hello)
# Therefore, calling hello() is the same as calling my_decorator(hello)().
