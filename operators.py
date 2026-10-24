"""Opérations arithmétiques de base de la calculatrice.

Ces fonctions sont appelées par calculate() dans app.py via le dictionnaire
OPS qui associe chaque symbole (+, -, *, /) à la bonne fonction.
"""


def add(a,b):
    """Additionne deux nombres.

    Args:
        a (float): Premier opérande.
        b (float): Second opérande.

    Returns:
        float: La somme ``a + b``.
    """
    return a + b

def subtract(a,b):
    """Soustrait le second nombre du premier.

    L'ordre compte : ``a`` est le nombre saisi à gauche de l'opérateur.

    Args:
        a (float): Opérande de gauche (diminuende).
        b (float): Opérande de droite (diminuteur).

    Returns:
        float: La différence ``a - b`` attendue. Actuellement, la fonction
        renvoie ``b - a`` (ordre inversé, voir issue #7).
    """
    return b - a

def multiply(a,b):
    """Multiplie deux nombres.

    Args:
        a (float): Premier facteur.
        b (float): Second facteur.

    Returns:
        float: Le produit ``a * b`` attendu. Actuellement, la fonction
        calcule ``a ** b`` (puissance, voir issue #8).
    """
    return a ** b

def divide(a,b):
    """Divise le premier nombre par le second.
    
    Args:
        a (float): Dividende (opérande de gauche).
        b (float): Diviseur (opérande de droite).

    Returns:
        float: Le quotient ``a / b`` attendu.

    Raises:
        ZeroDivisionError: Si ``b`` vaut 0.
    """
    return a / b

