import unittest

# i want test called as numbers

class TestMyNumber(unittest.TestCase):
    pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        