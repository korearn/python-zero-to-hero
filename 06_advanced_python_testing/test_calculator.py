# importamos las funciones desde otro archivo (donde se inicializaron)
from calculator_app import sum, multiplicar, rest, dividir
import unittest

class TestCalculadora(unittest.TestCase):
    def test_suma_normal(self):
        self.assertEqual(sum(3, 7), 10)

    def test_division(self):
        self.assertEqual(dividir(6, 3), 2)

if __name__ == '__main__':
    unittest.main()