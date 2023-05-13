import unittest
from io import StringIO
from unittest.mock import patch
from math_ops import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        # Redirect stdout to a buffer
        with patch('sys.stdout', new=StringIO()) as buffer:
            # Call the add_numbers function with the arguments 2 and 3
            result = add_numbers(2, 3)
        
        # Assert that the result is equal to 5
        self.assertEqual(result, 5)
        
        # Assert that the function printed the expected message to stdout
        self.assertEqual(buffer.getvalue().strip(), "The sum of 2 and 3 is 5")

if __name__ == '__main__':
    unittest.main()
