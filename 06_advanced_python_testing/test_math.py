import unittest
# función a probar (se importa desde otro archivo)
def sumar(a, b):
    return a + b

class TestOperaciones(unittest.TestCase):

    def test_suma_correcta(self):
        # afirmamos el resultado de la suma
        self.assertEqual(sumar(3, 7), 10)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, -1), -2)

# Esto ejecuta los tests al correr el archivo
if __name__ == '__main__':
    unittest.main()