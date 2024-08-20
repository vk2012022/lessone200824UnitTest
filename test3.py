import unittest
from main3 import add, subtract, multiply, divide, modulo

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль невозможно")

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        with self.assertRaises(ValueError) as context:
            modulo(10, 0)
        self.assertEqual(str(context.exception), "Невозможно найти остаток при делении на ноль")

if __name__ == '__main__':
    unittest.main()
