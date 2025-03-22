# Start an infinite loop to repeatedly prompt the user for input until a valid age is provided.
while True:
    try:
        # Prompt the user to enter their age and convert the input to an integer.
        age = int(input("Enter your age: "))
        # Calculate a derived value (for example, converting to "dog years")
        # Here, it arbitrarily divides 10 by the entered age.
        age_in_dogs_year = 10 / age

    # This block catches the case where the entered age is zero,
    # which would cause a division by zero error.
    except ZeroDivisionError:
        # Inform the user that the age must be greater than 0.
        print("enter age greater than 0")
        # Use 'continue' to restart the loop and ask for input again.
        continue

    # This block catches errors where the input cannot be converted to an integer.
    except ValueError:
        # Inform the user that the input is not a valid number.
        print("Please enter a no.")
        # Break out of the loop after printing the message.
        break

    # NOTE: This except block for ValueError is redundant because the previous
    # except ValueError already handles that exception. This block will never be reached.
    except ValueError:
        print("!!!!")

    # The 'else' block executes only if no exceptions were raised in the try block.
    else:
        # Thank the user and confirm the entered age.
        print(f"thank you, and your age is {age}")
        # Break out of the loop since a valid age has been provided.
        break

    # The 'finally' block always executes, regardless of whether an exception occurred.
    finally:
        print("I will always get printed no matter what :)")

    # NOTE: This print statement is unreachable because every path in the try/except/else blocks
    # either breaks or continues the loop before this line is reached.
    print("can you hear me??????")
