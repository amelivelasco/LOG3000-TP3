
"""Tests de l'évaluation des expressions et des routes Flask."""

import unittest
from app import app, calculate


class TestCalculate(unittest.TestCase):
    """Vérifie le calcul et la validation des expressions."""

    def test_add_expression(self):
        """Vérifie une expression d'addition valide."""
        self.assertEqual(calculate("2+3"), 5)

    def test_subtract_expression(self):
        """Vérifie une expression de soustraction valide."""
        self.assertEqual(calculate("7-2"), 5)

    def test_multiply_expression(self):
        """Vérifie une expression de multiplication valide."""
        self.assertEqual(calculate("3*4"), 12)

    def test_divide_expression(self):
        """Vérifie une expression de division valide."""
        self.assertEqual(calculate("7/2"), 3.5)

    def test_spaces(self):
        """Vérifie que les espaces sont ignorés."""
        self.assertEqual(calculate(" 2 + 3 "), 5)

    def test_decimal_numbers(self):
        """Vérifie le calcul avec des opérandes décimaux."""
        self.assertEqual(calculate("2.5+1.5"), 4)

    def test_negative_first_operand(self):
        """Vérifie une expression avec un premier opérande négatif."""
        self.assertEqual(calculate("-3+2"), -1)

    def test_negative_second_operand(self):
        """Vérifie une expression avec un deuxième opérande négatif."""
        self.assertEqual(calculate("3*-2"), -6)

    def test_empty_expression(self):
        """Vérifie qu'une expression vide est rejetée."""
        with self.assertRaises(ValueError):
            calculate("")

    def test_invalid_operand(self):
        """Vérifie qu'un opérande non numérique est rejeté."""
        with self.assertRaises(ValueError):
            calculate("abc+2")

    def test_multiple_operators(self):
        """Vérifie le rejet de plusieurs opérations successives."""
        with self.assertRaises(ValueError):
            calculate("2+3*4")

    def test_missing_operand(self):
        """Vérifie le rejet d'une expression incomplète."""
        with self.assertRaises(ValueError):
            calculate("2+")

    def test_no_operator(self):
        """Vérifie le rejet d'une expression sans opérateur."""
        with self.assertRaises(ValueError):
            calculate("123")

    def test_none_expression(self):
        """Vérifie le rejet d'une valeur absente."""
        with self.assertRaises(ValueError):
            calculate(None)


class TestFlaskRoutes(unittest.TestCase):
    """Vérifie le traitement des requêtes HTTP."""

    def setUp(self):
        """Initialise un client de test Flask."""
        self.client = app.test_client()

    def test_get_index(self):
        """Vérifie que la page principale est accessible."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask Calculator", response.data)

    def test_post_valid_expression(self):
        """Vérifie l'affichage du résultat d'un calcul."""
        response = self.client.post("/", data={"display": "2+3"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'5.0', response.data)

    def test_post_invalid_expression(self):
        """Vérifie l'affichage d'une erreur de saisie."""
        response = self.client.post("/", data={"display": "abc+2"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error:", response.data)

    def test_division_by_zero_message(self):
        """Vérifie qu'une division par zéro affiche un message clair."""
        response = self.client.post("/", data={"display": "5/0"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error: Division by zero", response.data)


if __name__ == "__main__":
    unittest.main()
