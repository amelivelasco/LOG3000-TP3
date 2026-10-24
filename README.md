# Calculatrice Flask

**TP3 du LOG3000**

**Groupe 5 : Ameli Velasco Duran et Mohammed Iich**

## Description

Application web de calculatrice simple construite avec Flask. L'utilisateur compose une
opération entre deux nombres à l'aide d'un clavier à l'écran ; le navigateur envoie
l'expression au serveur, qui la calcule et renvoie la page avec le résultat.

### Portée

- **Opérations prises en charge :** addition (`+`), soustraction (`-`), multiplication
  (`*`) et division (`/`).
- **Une seule opération à la fois**, entre deux nombres : `7-2` est accepté, `2+3*4` est
  refusé avec un message d'erreur.
- Les nombres peuvent être décimaux ou négatifs (`-3+2`, `3*-2`).
- Les erreurs (expression vide ou invalide, division par zéro) sont affichées dans
  l'écran de la calculatrice au lieu d'interrompre l'application.
- Hors portée : priorité des opérations, parenthèses, historique des calculs.

Les bogues connus et leur avancement sont suivis dans les
[issues GitHub](https://github.com/amelivelasco/LOG3000-TP3/issues).

## Structure du projet

| Élément | Rôle |
|---|---|
| `app.py` | Serveur Flask : route `/` et fonction `calculate()` qui analyse l'expression. |
| `operators.py` | Les quatre opérations arithmétiques appelées par `calculate()`. |
| [`templates/`](templates/README.md) | Page HTML de la calculatrice (`index.html`) et son JavaScript. |
| [`static/`](static/README.md) | Feuille de style `style.css`. |
| [`tests/`](tests/README.md) | Tests automatisés (`unittest`). |
| `requirements.txt` | Dépendances Python à installer. |

Chaque dossier contient son propre `README.md` qui détaille ses fichiers, ses
dépendances et ses hypothèses.

## Installation

### Prérequis

- Python 3.9 ou plus récent (`python --version` pour vérifier)
- pip
- Git

### Étapes

1. Cloner le dépôt et entrer dans le dossier :
   ```bash
   git clone https://github.com/amelivelasco/LOG3000-TP3.git
   cd LOG3000-TP3
   ```
2. Créer un environnement virtuel, pour isoler les dépendances du projet :
   ```bash
   python -m venv .venv
   ```
3. Activer l'environnement virtuel :
   ```bash
   source .venv/bin/activate      # Linux / macOS
   .venv\Scripts\activate         # Windows
   ```
4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Lancer l'application

Depuis la racine du projet, environnement virtuel activé :

```bash
python app.py
```

Ouvrir ensuite http://127.0.0.1:5000 dans un navigateur. Pour arrêter le serveur,
faire `Ctrl+C` dans le terminal.

### Utiliser la calculatrice

1. Cliquer sur les chiffres et sur un opérateur pour composer l'expression, par
   exemple `7`, `-`, `2`. Elle s'affiche dans l'écran en haut.
2. Cliquer sur `=` pour envoyer le calcul : le résultat remplace l'expression.
3. Cliquer sur `C` pour effacer l'écran avant un nouveau calcul.

| Saisie | Résultat affiché |
|---|---|
| `7-2` | `5.0` |
| `7/2` | `3.5` |
| `2+3*4` | `Error: only one operator is allowed` |
| `5/0` | Un message d'erreur de division par zéro |

Le résultat est toujours affiché comme un nombre décimal (`5.0` et non `5`).

## Tests

Les tests utilisent `unittest`, inclus dans Python : aucune installation supplémentaire
n'est nécessaire. Depuis la racine du projet :

```bash
python -m unittest discover -s tests -v
```

Pour lancer un seul fichier de tests :

```bash
python -m unittest discover -s tests -p "test_operators.py" -v
```

Les tests couvrent les opérations arithmétiques, l'analyse des expressions, les routes
Flask, les boutons de l'interface et le style du champ d'affichage. Le détail est dans
[`tests/README.md`](tests/README.md).

## Flux de contribution

1. **Issue :** tout bogue ou changement commence par une
   [issue](https://github.com/amelivelasco/LOG3000-TP3/issues) qui décrit le problème,
   les étapes de reproduction, le résultat attendu et le résultat obtenu. L'issue est
   assignée à un membre de l'équipe.
2. **Branche :** on ne travaille jamais directement sur `main`. On part d'un `main` à jour
   et on crée une branche par issue ou par tâche :
   ```bash
   git checkout main
   git pull
   git checkout -b fix/<n°-issue>-<description>    # ex. fix/8-multiply
   ```
   Préfixes utilisés : `fix/` pour un correctif, `docs/` pour la documentation,
   `tests/` pour les tests.
3. **Commits :** un commit par changement cohérent, avec un message qui explique ce qui
   change et pourquoi, par exemple `Fix #8: multiply utilise a * b au lieu de a ** b`.
4. **Tests :** avant d'ouvrir une PR, relancer la suite de tests et vérifier que le test
   lié à l'issue passe.
5. **Pull request :** ouvrir une PR vers `main`, avec `Closes #N` dans la description
   pour fermer l'issue automatiquement à la fusion.
6. **Revue et fusion :** l'autre membre de l'équipe relit la PR (commentaires,
   approbation), puis la fusionne avec « Create a merge commit » pour garder l'historique
   de chaque branche.
