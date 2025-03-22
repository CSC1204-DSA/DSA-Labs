import unittest
import script  # Import the 'script' module that contains the 'add' function to be tested

class TestMain(unittest.TestCase):
    """
    This class contains unit tests for the 'add' function in the 'script' module.
    It inherits from unittest.TestCase, which provides a framework for writing tests.
    """

    def test_add(self):
        """
        Test that 'add' correctly adds 5 to an integer input.
        For example, when given 10, it should return 15.
        """
        test_param = 10                     # Input value for the test
        result = script.add(test_param)     # Call the function from the script module
        self.assertEqual(result, 15)        # Assert that the result is 15

    def test_add2(self):
        """
        Test that 'add' returns a ValueError when the input cannot be converted to an integer.
        For instance, passing a non-numeric string should cause the function to handle the error.
        """
        test_param = 'random string'        # Invalid input for integer conversion
        result = script.add(test_param)     # Call the function, expecting an error result
        self.assertTrue(isinstance(result, ValueError))  # Assert that the result is an instance of ValueError

if __name__ == '__main__':
    # This block ensures that the unit tests will only run when this script is executed directly,
    # and not when it is imported as a module.
    unittest.main()
