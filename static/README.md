# static/

## Raison d'être

Ce dossier contient les fichiers servis tels quels au navigateur, sans passer par
Python. Ici, il s'agit uniquement du style visuel de la calculatrice.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `style.css` | Mise en page et apparence de la calculatrice : centrage de la page, écran d'affichage, grille de boutons 4 × 4, couleurs des chiffres et des opérateurs, effets de survol et de clic. |

## Dépendances et hypothèses

- **Flask** sert automatiquement ce dossier à l'URL `/static/`. Le template
  `templates/index.html` charge la feuille avec
  `{{ url_for('static', filename='style.css') }}` : si le fichier est renommé ou
  déplacé, il faut aussi mettre à jour cette ligne.
- **Le CSS dépend de la structure HTML** de `templates/index.html`. Les sélecteurs
  `.calculator`, `#display`, `.buttons`, `.btn` et `.operator` doivent
  correspondre aux classes et à l'identifiant utilisés dans le template. Renommer
  l'un d'eux d'un côté impose de le renommer de l'autre.
- La grille suppose **4 boutons par ligne** dans le template.
- Aucune bibliothèque externe ni préprocesseur (Sass, Tailwind…) : le CSS est
  écrit à la main et chargé directement.
- Le JavaScript de la calculatrice n'est pas dans ce dossier : il est intégré
  dans `templates/index.html`.
