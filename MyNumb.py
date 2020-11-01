import unittest

from MyNumber import MyNumber

class TestMyNumber(unittest.TestCase):
    def test_checkforeven(self):
        my_number = MyNumber()  # Arrange
        result = my_number.is_even(10)  # Action
        self.assertEqual(result, True)  # Assert

    def test_is_even_negative(self):
        my_number = MyNumber()
        result = my_number.is_even(11)
        self.assertEqual(result, False)





"""    This method is used to test to even or odd functionality   """





