
"""Tests de la structure et des boutons de l'interface HTML."""

import unittest
from html.parser import HTMLParser
from app import app


class CalculatorParser(HTMLParser):
    """Extrait les boutons, les champs et les formulaires HTML."""

    def __init__(self):
        """Initialise les collections utilisées pour l'analyse HTML."""
        super().__init__()
        self.buttons = []
        self.inputs = []
        self.forms = []
        self.current_button = None

    def handle_starttag(self, tag, attrs):
        """Enregistre les éléments HTML utiles aux tests."""
        attributes = dict(attrs)
        if tag == "button":
            self.current_button = {"attrs": attributes, "text": ""}
        elif tag == "input":
            self.inputs.append(attributes)
        elif tag == "form":
            self.forms.append(attributes)

    def handle_data(self, data):
        """Récupère le libellé du bouton en cours."""
        if self.current_button is not None:
            self.current_button["text"] += data

    def handle_endtag(self, tag):
        """Enregistre un bouton lorsque sa balise se termine."""
        if tag == "button" and self.current_button is not None:
            self.buttons.append(self.current_button)
            self.current_button = None


class TestTemplate(unittest.TestCase):
    """Vérifie les éléments de l'interface de la calculatrice."""

    @classmethod
    def setUpClass(cls):
        """Charge la page Flask et analyse son contenu HTML."""
        response = app.test_client().get("/")
        cls.parser = CalculatorParser()
        cls.parser.feed(response.get_data(as_text=True))

    def button_for(self, value):
        """Retourne le bouton associé au caractère demandé."""
        action = f"appendToDisplay('{value}')"
        return next(
            (button for button in self.parser.buttons
             if button["attrs"].get("onclick") == action),
            None
        )

    def test_digit_labels(self):
        """Vérifie que les boutons numériques ont les bons libellés."""
        for digit in "0123456789":
            with self.subTest(digit=digit):
                button = self.button_for(digit)
                self.assertIsNotNone(button)
                self.assertEqual(button["text"].strip(), digit)

    def test_operator_labels(self):
        """Vérifie que les opérateurs possèdent un libellé visible."""
        for operator in "+-*/":
            with self.subTest(operator=operator):
                button = self.button_for(operator)
                self.assertIsNotNone(button)
                self.assertEqual(button["text"].strip(), operator)

    def test_decimal_button(self):
        """Vérifie la présence d'un bouton pour les nombres décimaux."""
        button = self.button_for(".")
        self.assertIsNotNone(button)
        self.assertEqual(button["text"].strip(), ".")

    def test_clear_button(self):
        """Vérifie la présence du bouton de réinitialisation."""
        self.assertTrue(any(
            button["attrs"].get("onclick") == "clearDisplay()"
            for button in self.parser.buttons
        ))

    def test_equal_button(self):
        """Vérifie que le bouton égal soumet le formulaire."""
        self.assertTrue(any(
            button["attrs"].get("type") == "submit"
            and button["text"].strip() == "="
            for button in self.parser.buttons
        ))

    def test_form_method(self):
        """Vérifie que les expressions sont envoyées par POST."""
        self.assertTrue(any(
            form.get("method", "").upper() == "POST"
            for form in self.parser.forms
        ))

    def test_display_input(self):
        """Vérifie que le champ d'affichage est présent et protégé."""
        self.assertTrue(any(
            field.get("name") == "display"
            and "readonly" in field
            for field in self.parser.inputs
        ))


if __name__ == "__main__":
    unittest.main()
