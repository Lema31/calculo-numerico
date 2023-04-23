import unittest
import math
from biseccion import biseccion

max_iterations = 50


class TestBiseccion(unittest.TestCase):
    def test_potencia(self):
        f = lambda x: x**3 - 2 * x - 5
        interval = [2, 3]
        tol = 0.0009
        resultado_esperado = 2.0947265625
        resultado_obtenido = biseccion(f, interval, tol, max_iterations)
        self.assertAlmostEqual(resultado_esperado, resultado_obtenido, places=7)

    def test_sin_x(self):
        f = lambda x: math.sin(x) - math.e**-x
        interval = [0, 1]
        tol = 0.053
        resultado_esperado = 0.59375
        resultado_obtenido = biseccion(f, interval, tol, max_iterations)
        self.assertAlmostEqual(resultado_esperado, resultado_obtenido, places=5)

    def test_funcion_no_cumple_bolzano(self):
        f = lambda x: x**2 + 1
        interval = [0, 1]
        tol = 1e-5
        with self.assertRaises(AssertionError):
            biseccion(f, interval, tol, max_iterations)


if __name__ == "__main__":
    unittest.main()
