def add(num):
    # Try to convert 'num' to an integer and add 5 to it.
    try:
        return int(num) + 5
    # If converting 'num' to an integer fails (e.g., if it's a non-numeric string),
    # catch the ValueError and return the error object.
    except ValueError as err:
        return err
