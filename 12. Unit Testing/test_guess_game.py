import unittest
import guess_game  # Import the module containing the 'run_guess' function for the guess game

class testGame(unittest.TestCase):
    """
    Unit tests for the 'run_guess' function in the guess_game module.
    These tests validate the behavior of the function for different inputs.
    """

    def test_game(self):
        """
        Test case where the guess is correct.
        When the guess equals the answer, run_guess should return True.
        """
        result = guess_game.run_guess(5, 5)
        self.assertTrue(result)

    def test_game2(self):
        """
        Test case where the guess is below the valid range.
        If the guess is not between 1 and 10, run_guess should return False.
        """
        result = guess_game.run_guess(0, 5)
        self.assertFalse(result)

    def test_game3(self):
        """
        Test case where the guess is above the valid range.
        If the guess is not between 1 and 10, run_guess should return False.
        """
        result = guess_game.run_guess(15, 4)
        self.assertFalse(result)

# This block ensures that the tests are executed only when this script is run directly.
if __name__ == '__main__':
    unittest.main()
