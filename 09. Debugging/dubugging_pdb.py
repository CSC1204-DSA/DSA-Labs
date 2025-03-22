import pdb  # Import the Python debugger module

# Define a function 'add' that takes two parameters and returns their sum.
def add(n1, n2):
    return n1 + n2

# Set a breakpoint here. When the code execution reaches this line,
# the debugger will pause and allow interactive debugging.
pdb.set_trace()

# Call the function 'add' with 4 (an integer) and 'five' (a string).
# This will cause a TypeError since Python cannot add an integer and a string.
add(4, 'five')

'''
Useful commands for pdb (Python Debugger):
a      : Print the argument list of the current function.
step   : Execute the current line and stop at the first possible occasion.
help   : List all available commands.
help <command> : Show details about a specific command.
continue: Continue program execution until the next breakpoint or error occurs.
w      : Display a stack trace with the previous, current, and next lines of code.
next   : Continue execution until the next line in the current function is reached or it returns.

Additional tips:
- You can inspect and change variable values in the debugger console.
- Simply type the variable name to see its current value.
'''
