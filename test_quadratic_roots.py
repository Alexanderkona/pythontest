import unittest
from main import quadratic_roots

class TestQuadraticRoots(unittest.TestCase):

    def test_zero_coefficient_a(self):
        with self.assertRaises(ValueError) as context:
            quadratic_roots(0, 2, 1)
        self.assertEqual(str(context.exception), "Коэффициент 'a' не должен быть равен 0 для квадратного уравнения.")

    def test_two_different_roots(self):
        result = quadratic_roots(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))

    def test_one_root(self):
        result = quadratic_roots(1, 2, 1)
        self.assertEqual(result, (-1.0,))

    def test_complex_roots(self):
        result = quadratic_roots(1, 2, 5)
        self.assertEqual(result, (-1.0 + 2.0j, -1.0 - 2.0j))

    def test_large_coefficients(self):
        result = quadratic_roots(1e6, -3e6, 2e6)
        self.assertEqual(result, (2.0, 1.0))

    def test_zero_coefficients_b_and_c(self):
        result = quadratic_roots(1, 0, 0)
        self.assertEqual(result, (0.0,))

    def test_invalid_string_coefficients (self):
        with self.assertRaises(ValueError):
            quadratic_roots("a", "b", "c")

if __name__ == '__main__':
    unittest.main()
