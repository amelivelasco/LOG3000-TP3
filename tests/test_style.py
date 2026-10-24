
"""Tests de la configuration CSS de l'affichage."""

import re
import unittest
from pathlib import Path


class TestStyle(unittest.TestCase):
    """Vérifie les propriétés CSS nécessaires à l'affichage."""

    @classmethod
    def setUpClass(cls):
        """Charge la feuille de style depuis le dossier static."""
        root = Path(__file__).resolve().parent.parent
        cls.css = (root / "static" / "style.css").read_text(
            encoding="utf-8"
        )

    def test_display_box_sizing(self):
        """Vérifie que la largeur de l'affichage inclut son padding."""
        # Les commentaires CSS sont retirés : sinon ils restent collés au
        # sélecteur suivant et "#display" n'est pas reconnu.
        css = re.sub(r"/\*.*?\*/", "", self.css, flags=re.S)
        # Un style global ou spécifique peut définir cette propriété.
        rules = re.findall(r"([^{}]+)\{([^{}]*)\}", css)
        valid = any(
            ("#display" in selectors or "*" in selectors)
            and re.search(
                r"box-sizing\s*:\s*border-box\s*;",
                declarations
            )
            for selector_group, declarations in rules
            for selectors in [
                [s.strip() for s in selector_group.split(",")]
            ]
        )
        self.assertTrue(valid, "Le champ doit utiliser box-sizing: border-box.")


if __name__ == "__main__":
    unittest.main()
