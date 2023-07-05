import unittest
import math
import sympy as sp
from integracion_numerica import sum_riemann
from integracion_numerica import trapezoid_method
from biseccion import biseccion
from newton_raphson import newton_raphson
from polinomio_taylor import taylor_polynomial_integrating, taylor_polynomial

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
        expected_output = "No se puede hacer una division entre 0"
        self.assertEqual(newton_raphson(f, start, min_error, max_iterations), expected_output)

    def test_linear_function(self):
        f = lambda x: 2*x - 3
        start = 2
        min_error = 1e-6
        expected_root = 1.5
        self.assertAlmostEqual(newton_raphson(f, start, min_error, max_iterations), expected_root, places=4)

    def test_trigonometric_function(self):
        f = lambda x: math.cos(x) - x
        start = 0.5
        min_error = 1e-6
        expected_root = 0.739085
        self.assertAlmostEqual(newton_raphson(f, start, min_error, max_iterations), expected_root, places=4)

    def test_multiple_roots_function(self):
        f = lambda x: x**2 - 2*x + 1
        start = 0.5
        min_error = 1e-5
        expected_roots = [1, 1]

        roots = []
        places = 3
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

# class TestTaylorPolynomialIntegrating(unittest.TestCase):
#
#     def test_polynomial_degree_1(self):
#         fx = lambda x: x**2
#         degree = 1
#         interval = [0, 1]
#         expected_result = 1/3
#         expected_error = 0
#         result, error = taylor_polynomial_integrating(fx, degree, interval)
#         self.assertAlmostEqual(result, expected_result)
#         self.assertAlmostEqual(error, expected_error)
#
#     def test_polynomial_degree_2(self):
#         fx = lambda x: x**3
#         degree = 2
#         interval = [-1, 1]
#         expected_result = 0
#         expected_error = 0
#         result, error = taylor_polynomial_integrating(fx, degree, interval)
#         self.assertAlmostEqual(result, expected_result)
#         self.assertAlmostEqual(error, expected_error)
#
#     def test_trigonometric_function(self):
#         fx = lambda x: sp.sin(x)
#         degree = 3
#         interval = [0, sp.pi/2]
#         expected_result = 0.9999
#         expected_error = 0.0001
#         result, error = taylor_polynomial_integrating(fx, degree, interval)
#         self.assertAlmostEqual(result, expected_result, places=2)
#         self.assertAlmostEqual(error, expected_error, places=2)
#
#     def test_exponential_function(self):
#         fx = lambda x: sp.exp(x)
#         degree = 5
#         interval = [0, 1]
#         expected_result = sp.exp(1) - sp.Rational(5,2)
#         expected_error = 0.0002
#         result, error = taylor_polynomial_integrating(fx, degree, interval)
#         self.assertAlmostEqual(result, expected_result, delta=0.5)
#         self.assertAlmostEqual(error, expected_error, delta=0.0005)
#
#     def test_different_interval_values(self):
#         fx = lambda x: sp.cos(x)
#         degree = 2
#         interval_1 = [0, sp.pi/2]
#         interval_2 = [sp.pi/2, sp.pi]
#         expected_result_1 = 0.707
#         expected_result_2 = -0.707
#         expected_error_1 = 0.016
#         expected_error_2 = 0.016
#         result_1, error_1 = taylor_polynomial_integrating(fx, degree, interval_1)
#         result_2, error_2 = taylor_polynomial_integrating(fx, degree, interval_2)
#         self.assertAlmostEqual(result_1, expected_result_1, places=3)
#         self.assertAlmostEqual(result_2, expected_result_2, places=3)
#         self.assertAlmostEqual(error_1, expected_error_1, places=3)
#         self.assertAlmostEqual(error_2, expected_error_2, places=3)

class TestSumRiemannAndTrapezoidMethod(unittest.TestCase):
    def test_1(self):
        f = lambda x: x**2
        self.assertAlmostEqual(sum_riemann(f, [0, 1], 10000), 0.333333, places=3)
        self.assertAlmostEqual(trapezoid_method(f, [0, 1], 10000), 0.333333, places=5)

    def test_2(self):
        f = lambda x: x**3
        self.assertAlmostEqual(sum_riemann(f, [0, 1], 10000), 0.25, places=3)
        self.assertAlmostEqual(trapezoid_method(f, [0, 1], 10000), 0.25, places=5)

    def _test_exponential(self):
        f = lambda x: math.exp(x)
        self.assertAlmostEqual(sum_riemann(f, [0, 1], 10000), 1.71828, places=3)
        self.assertAlmostEqual(trapezoid_method(f, [0, 1], 10000), 1.71828, places=5)

    def test_trigonometric(self):
        f = lambda x: math.cos(x ** 2)
        self.assertAlmostEqual(sum_riemann(f, [0,1], 10000), 0.90452, places = 3)
        self.assertAlmostEqual(trapezoid_method(f, [0, 1], 10000), 0.90452, places=5)


if __name__ == "__main__":
    unittest.main()
