import unittest
from main import solving

class TestSolving(unittest.TestCase):

    def test_positive_discriminant(self):
        self.assertEqual(solving(1, -3, 2), (2, 1))
        self.assertEqual(solving(2, -5, -3), (3, -0.5))
        self.assertEqual(solving(1, 0, -9), (3, -3))

    def test_zero_discriminant(self):
        self.assertEqual(solving(1, 4, 4), -2)
        self.assertEqual(solving(1, -2, 1), 1)
        self.assertEqual(solving(1, 6, 9), -3)

    def test_negative_discriminant(self):
        self.assertEqual(solving(1, 2, 5), "Нет действительных корней")
        self.assertEqual(solving(1, 0, 1), "Нет действительных корней")

if __name__ == '__main__':
    unittest.main()