# Module de tests

## Rôle

Le dossier `tests/` contient les tests de la calculatrice Flask.
Ils permettent de vérifier les fonctionnalités attendues et
d'identifier les bogues présents dans l'application.

## Fichiers

- `test_operators.py` : teste les opérations arithmétiques et la division par zéro.
- `test_app.py` : teste les expressions, les erreurs et les routes Flask.
- `test_template.py` : vérifie les boutons et les éléments de l'interface HTML.
- `test_style.py` : vérifie la configuration CSS du champ d'affichage.

## Exécution

Depuis la racine du projet, avec l'environnement virtuel activé :

```bash
python -m unittest discover -s tests -v
```

Pour exécuter un seul fichier :

```bash
python -m unittest discover -s tests -p "test_operators.py" -v
```

## Couverture

Les tests vérifient :

- Les quatre opérations arithmétiques.
- Les expressions contenant des nombres négatifs ou décimaux.
- La validation des expressions invalides.
- La gestion de la division par zéro.
- Les requêtes GET et POST.
- Les libellés des boutons numériques et des opérateurs.
- La présence des boutons décimal, égal et effacer.
- La configuration du formulaire HTML.
- La propriété CSS utilisée pour éviter le débordement du champ.

Le débordement visuel doit également être vérifié dans un navigateur.

## Dépendances

- `unittest` : bibliothèque standard de tests Python.
- Flask : fournit le client de test HTTP.
- `app.py` : contient les routes et l'évaluation des expressions.
- `operators.py` : contient les fonctions arithmétiques.
- `templates/index.html` : définit l'interface.
- `static/style.css` : définit les styles de l'interface.

## Suivi des problèmes

Chaque bogue confirmé doit faire l'objet d'une Issue GitHub
documentant le résultat attendu, le résultat obtenu et les
étapes de reproduction.

Les corrections sont réalisées dans des branches distinctes.
Les tests concernés sont ensuite réexécutés pour vérifier les correctifs.
```
