# This program demonstrates how to manually raise exceptions to stop program execution.

# Print a greeting message to the console.
print("Hello!!!!")

# The following line is commented out.
# If uncommented, it would raise a TypeError with the message "yo".
# raise TypeError("yo")

# Raise a generic Exception with a custom message.
# This stops the program immediately; any code after this line will not run.
raise Exception("Any message ")

# This line will never be executed because the exception above terminates the program.
print("bye")
