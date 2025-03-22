import random  # Import the random module to generate random numbers


def run_guess(guess, answer):
    # Check if the guess is within the valid range (1 to 10).
    if 0 < guess < 11:
        # If the guess matches the randomly generated answer,
        # print a congratulatory message and return True.
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        # If the guess is outside the valid range,
        # inform the user with an error message and return False.
        print('hey bozo, I said 1~10')
        return False


# The following block ensures that the game runs only when this script is executed directly.
# This is helpful when testing, so the game logic doesn't run during unit tests.
if __name__ == '__main__':
    # Generate a random answer between 1 and 10.
    answer = random.randint(1, 10)

    # Enter an infinite loop to continuously prompt the user for guesses until the correct number is guessed.
    while True:
        try:
            # Prompt the user for a guess and convert the input to an integer.
            guess = int(input('guess a number 1~10:  '))
            # Call run_guess to check if the guess is correct.
            # If it returns True (i.e., the guess is correct), break out of the loop.
            if run_guess(guess, answer):
                break
        except ValueError:
            # If the input is not a valid integer, catch the ValueError and notify the user.
            print('please enter a number')
            # Continue prompting the user for input.
            continue

'''
Notes:
- This script is a simple number guessing game.
- It demonstrates the use of a helper function (run_guess) to check user input.
- Exception handling (try/except) is used to manage non-integer inputs.
- The '__main__' block prevents the game from starting when the module is imported,
  which is beneficial for unit testing individual components.
'''
