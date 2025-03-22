# Define a function for division that handles errors gracefully.
def division_fn(num1, num2):
    try:
        # Attempt to perform division of num1 by num2.
        return num1 / num2
    # Catch both ZeroDivisionError and TypeError exceptions.
    # ZeroDivisionError occurs when num2 is zero.
    # TypeError occurs if either num1 or num2 is of an unsupported type (e.g., string).
    except (ZeroDivisionError, TypeError) as err:
        # Print the error message that was captured.
        print(f'error: {err}')

# Call division_fn with arguments (1, '0').
# Here, '0' is a string, so a TypeError is expected.
print(division_fn(1, '0'))

# Call division_fn with arguments (1, 0).
# This will raise a ZeroDivisionError since division by zero is not allowed.
print(division_fn(1, 0))

# Call division_fn with arguments (1, 4).
# This is a valid division and should return 0.25.
print(division_fn(1, 4))
