import unittest
from operaciones import sumar, restar, multiplicar, dividir, dividir_controlado

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
    
    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(8, 15), -7)
        self.assertEqual(restar(-1, -1), 0)
        
    def test_multiplicar(self):
        self.assertEqual(multiplicar(10, 10), 100)
        self.assertEqual(multiplicar(2, 0), 0)
        self.assertEqual(multiplicar(-6, 17), -102)
        
    def test_dividir(self):
        self.assertEqual(dividir_controlado(10,-5),-2)
        self.assertEqual(dividir_controlado(5,20),0.25)
        self.assertEqual(dividir_controlado(0,-6),0)
        self.assertEqual(dividir_controlado(33,0), "No se puede dividir por cero")
        with self.assertRaises(ZeroDivisionError):
            dividir(8,0)

if __name__ == '__main__':
    unittest.main()