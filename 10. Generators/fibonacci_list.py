# Define a function to generate and print the Fibonacci sequence up to 'num' elements.
def fib(num):
    # Initialize the first two Fibonacci numbers.
    a = 0  # First Fibonacci number.
    b = 1  # Second Fibonacci number.

    # Initialize an empty list to store the Fibonacci sequence.
    li = []

    # Loop 'num' times to generate the sequence.
    for i in range(num):
        # Append the current Fibonacci number to the list.
        li.append(a)

        # Update the values for the next iteration:
        # - 'a' becomes the current 'b'
        # - 'b' becomes the sum of the old 'a' and 'b'
        temp = a  # Store the current value of 'a'.
        a = b  # Update 'a' to the next number in the sequence.
        b = temp + b  # Calculate the new 'b' as the sum of the old 'a' and 'b'.

    # Print the complete Fibonacci sequence stored in the list.
    print(li)


# Prompt the user to enter a number, convert the input to an integer,
# and store it in the variable 'num'.
num = int(input("Enter a number: "))

# Call the 'fib' function with the user-provided number to display the Fibonacci sequence.
fib(num)
