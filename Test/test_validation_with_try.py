import unittest
#from input_validation import validation_with_try as val_with_try


class MyTestCase(unittest.TestCase):

    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)