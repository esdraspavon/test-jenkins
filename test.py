import unittest
from main import suma

class TestSumaMethods(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(3,5), 8)

    def test_suma_negative_numbers(self):
        self.assertEqual(suma(3,-5), -2)

if __name__ == '__main__':
    unittest.main()