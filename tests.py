import unittest
import math
import sympy as sp
from biseccion import biseccion
from newton_raphson import newton_raphson

max_iterations = 100

#tests for the biseccion function
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

class TestNewtonRaphson(unittest.TestCase):
    def test_constant_function(self):
        f = lambda x: 5
        start = 1
        min_error = 1e-6
        expected_output = "El algoritmo no converge en la funcion dada"
        self.assertEqual(newton_raphson(f, start, min_error, max_iterations), expected_output)

    def test_linear_function(self):
        f = lambda x: 2*x - 3
        start = 2
        min_error = 1e-6
        expected_root = 1.5
        self.assertAlmostEqual(newton_raphson(f, start, min_error, max_iterations), expected_root, places=4)

    def test_trigonometric_function(self):
        f = lambda x: sp.cos(x) - x
        start = 0.5
        min_error = 1e-6
        expected_root = 0.739085
        self.assertAlmostEqual(newton_raphson(f, start, min_error, max_iterations), expected_root, places=4)

    def test_multiple_roots_function(self):
        f = lambda x: x**2 - 2*x + 1
        start = 0.5
        min_error = 1e-6
        expected_roots = [1, 1]

        roots = []
        places = 4
        for i in range(2):
            root = round(newton_raphson(f, start, min_error, max_iterations),places)
            roots.append(root)
            start = root
        self.assertListEqual(roots, expected_roots)

    def test_discontinuous_function(self):
        f = lambda x: 1/x
        start = 0
        min_error = 1e-6
        expected_output = "No se puede hacer una division entre 0"
        self.assertEqual(newton_raphson(f, start, min_error, max_iterations), expected_output)

    def test_complex_function(self):
        f = lambda z: z**2 + 1
        start = 1
        min_error = 1e-6
        expected_output = "El algoritmo no converge en la funcion dada"
        self.assertEqual(newton_raphson(f, start, min_error, max_iterations), expected_output)


if __name__ == "__main__":
    unittest.main()
