# Module templates

## Rôle

Le dossier `templates/` contient les modèles HTML utilisés par Flask pour afficher l'interface 
de la calculatrice.

## Fichiers

- `index.html` : définit l'interface de la calculatrice, ses boutons et les fonctions JavaScript 
permettant de modifier l'affichage.

## Fonctionnement

L'utilisateur construit une expression à l'aide des boutons. Le formulaire transmet cette expression
au serveur Flask avec une requête POST. Le résultat du calcul est ensuite affiché dans le champ
prévu à cet effet.

## Dépendances

- `app.py` : traite les requêtes et transmet le résultat au modèle HTML.
- `static/style.css` : définit l'apparence de la calculatrice.
- Flask: permet de générer la page HTML et d'y afficher la variable `result`.

## Hypothèses

- Flask recherche les modèles HTML dans le dossier `templates/`.
- Le serveur transmet une variable `result` au modèle.
- Le champ `display` contient l'expression à évaluer.
- Les opérations arithmétiques sont exécutées par le serveur.
