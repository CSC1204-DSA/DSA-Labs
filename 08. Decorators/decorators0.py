# Define a decorator function that accepts a function 'func' as its argument.
def my_decorator(func):
    # Define an inner function 'wrap_func' that can accept any number of positional and keyword arguments.
    def wrap_func(*args, **kwargs):
        # Call the original function with all the passed arguments.
        func(*args, **kwargs)
    # Return the inner function, which now wraps the original function.
    return wrap_func

# Use the decorator '@my_decorator' to wrap the 'hello' function.
@my_decorator
def hello(name, age):
    # This function prints a greeting message that includes the provided name and age.
    print(f"Hello {name}, your age is {age}.")

# Use the decorator '@my_decorator' to wrap the 'logged_in' function.
@my_decorator
def logged_in(username):
    # This function prints a message indicating that the user with the given username is logged in.
    print(f"{username} is logged in.")

# Call the decorated 'hello' function.
# The decorator intercepts the call and routes it to 'wrap_func', which in turn calls 'hello' with the arguments.
hello("saurabh", 21)

# Call the decorated 'logged_in' function.
# Similarly, 'wrap_func' will call 'logged_in' with the provided username.
logged_in("saurabh")

# Note:
# Using the @my_decorator syntax is equivalent to manually wrapping the functions like so:
# hello = my_decorator(hello)
# logged_in = my_decorator(logged_in)
# and then calling them with:
# hello("saurabh", 21)
# logged_in("saurabh")
