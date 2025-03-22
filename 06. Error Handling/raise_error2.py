# -*- coding: utf-8 -*-
# This line specifies the file encoding as UTF-8, ensuring that the source code can include UTF-8 characters.

try:
    # Prompt the user to enter their age and convert the input to an integer.
    age = int(input("age: "))

    # Divide 10 by the user's age and assign the result back to 'age'.
    # This could raise a ZeroDivisionError if age is 0.
    age = 10 / age

    # Manually raise a ValueError with a custom message.
    # This is used here to intentionally trigger an exception and stop further execution.
    raise ValueError("Ending the program")

    # The following line is commented out.
    # If uncommented, it would raise a generic Exception with the message "quit".
    # raise Exception("quit")

# Catch any ValueError exceptions raised in the try block.
except ValueError:
    # Print a message to the console indicating an error occurred.
    print("Please enter a no.")
