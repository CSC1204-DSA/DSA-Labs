# Define a dictionary representing a user with a name and a 'valid' flag.
user1 = {
    'name': 'Sorna',  # User's name
    'valid': True     # Indicates whether the user is authenticated (True means authenticated)
}

# Define a decorator that checks if the user is authenticated before allowing the function to run.
def authenticated(fn):
    # The wrapper function accepts any number of positional and keyword arguments.
    def wrapper(*args, **kwargs):
        # Check if the first argument (expected to be a user dictionary) has 'valid' set to True.
        if args[0]['valid']:
            # If the user is valid, call the original function with the provided arguments.
            return fn(*args, **kwargs)
        # Optionally, you might add an else clause to handle the case where the user is not valid.
    # Return the inner wrapper function as the decorated version of the original function.
    return wrapper

# Use the @authenticated decorator to restrict access to the function.
@authenticated
def message_friends(user):
    # Function that sends a message (simulated here by printing a message).
    print('message has been sent')

# Call the decorated function with user1.
# Since user1['valid'] is True, the function will execute and print the message.
message_friends(user1)
