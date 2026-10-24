"""Gère l'application Flask et le calcul des expressions arithmétiques."""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Évalue une expression arithmétique.

    Les opérandes peuvent être négatifs : un « - » en début d'expression ou
    juste après un opérateur est lu comme un signe (ex. ``-3+2``, ``3*-2``).

    Args:
        expr (str): Expression contenant deux nombres et un opérateur.

    Returns:
        float: Résultat du calcul.

    Raises:
        ValueError: Si l'expression est vide, contient plusieurs opérateurs,
            n'a pas le format « nombre opérateur nombre » ou si un opérande
            n'est pas un nombre.
        ZeroDivisionError: Si l'expression divise par zéro.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        # Un "-" en tête ou juste après un opérateur est le signe d'un nombre
        # négatif, pas une soustraction : il reste dans l'opérande.
        if ch == '-' and (i == 0 or s[i - 1] in OPS):
            continue
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et traite les expressions soumises.

    Args:
        Aucun. Les données proviennent de la requête Flask.

    Returns:
        str: Page HTML contenant le résultat ou un message d'erreur.
    """
    
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except ZeroDivisionError:
            # Pour éviter d'afficher le message technique de Python à l'utilisateur.
            result = "Error: Division by zero"
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)