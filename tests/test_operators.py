"""Tests unitaires des opérations arithmétiques."""

import unittest
from operators import add, subtract, multiply, divide


class TestOperators(unittest.TestCase):
    """Vérifie les résultats des opérations arithmétiques."""

    def test_add(self):
        """Vérifie que l'addition retourne la somme attendue."""
        self.assertEqual(add(5, 3), 8)

    def test_add_negative(self):
        """Vérifie l'addition avec un nombre négatif."""
        self.assertEqual(add(-5, 3), -2)

    def test_subtract(self):
        """Vérifie que la soustraction respecte l'ordre des opérandes."""
        self.assertEqual(subtract(7, 2), 5)

    def test_multiply(self):
        """Vérifie que la multiplication retourne le produit attendu."""
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        """Vérifie qu'un produit par zéro donne zéro."""
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        """Vérifie que la division conserve les décimales."""
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_exact(self):
        """Vérifie une division sans reste."""
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self):
        """Vérifie qu'une division par zéro génère une exception."""
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
