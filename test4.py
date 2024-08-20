import unittest
from main4 import divide, modulo

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

class TestModulo(unittest.TestCase):
    def test_modulo_success(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        self.assertEqual(modulo(9, 2), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError) as context:
            modulo(10, 0)
        self.assertEqual(str(context.exception), "Невозможно найти остаток при делении на ноль")

if __name__ == '__main__':
    unittest.main()
