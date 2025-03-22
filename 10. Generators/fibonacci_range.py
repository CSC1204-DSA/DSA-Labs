# Define a generator function 'fib' that yields Fibonacci numbers one at a time.
def fib(num):
    a = 0  # The first Fibonacci number.
    b = 1  # The second Fibonacci number.

    # Loop 'num' times to generate the Fibonacci sequence.
    for i in range(num):
        yield a  # Yield the current Fibonacci number.

        # Update the values for the next Fibonacci numbers:
        temp = a  # Temporarily store the current value of 'a'.
        a = b  # Set 'a' to the next Fibonacci number.
        b = temp + b  # Compute the new 'b' as the sum of the previous 'a' and 'b'.


# Prompt the user to input the number of Fibonacci numbers to generate,
# converting the input from a string to an integer.
num = int(input("Enter a number: "))

# Iterate over the generator 'fib(num)' and print each Fibonacci number.
for i in fib(num):
    print(i)
