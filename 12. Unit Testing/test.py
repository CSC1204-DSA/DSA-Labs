import unittest
import script  # Import the module 'script' which contains the functions to be tested.

class TestMain(unittest.TestCase):
    """
    This class contains unit tests for functions defined in the 'script' module.
    It inherits from unittest.TestCase, allowing the use of various testing methods.
    """

    def setUp(self):
        """
        setUp is called before every test method.
        It is useful for initializing objects, variables, or configurations required for the tests.
        """
        print("Starting a method/test: ")

    def test_add(self):
        """
        Test the 'add' function with a valid integer input.
        Expected behavior: the function should add 5 to the input number.
        For example, passing 10 should return 15.
        """
        test_param = 10
        result = script.add(test_param)
        self.assertEqual(result, 15)

    def test_add2(self):
        """
        Test the 'add' function with an invalid string input.
        Expected behavior: the function should raise a ValueError (or return an error object)
        when the input cannot be converted to an integer.
        """
        test_param = 'random string'
        result = script.add(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def tearDown(self):
        """
        tearDown is called after every test method.
        It is typically used for cleaning up or resetting any changes made during the tests.
        """
        print("Cleaning up....")


# The following classes are defined to illustrate that code outside the test cases
# may also execute when the module is imported or run.

class A:
    # This print statement is executed when class A is defined.
    print("\nClass A")


# The main block ensures that the unit tests are run only when this script is executed directly,
# and not when it's imported as a module in another script.
if __name__ == '__main__':
    unittest.main()  # This will run all the tests in the file.


class B:
    # This print statement is executed when class B is defined.
    print("Class B")
