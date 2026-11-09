# Sandbox de particules

Un bac à sable de physique en Python et Pygame. On dessine à la souris du **sable**, de l'**eau**
ou des **blocs solides**, et chaque grain s'anime selon ses propres règles : le sable tombe et
forme des tas, l'eau coule et s'étale, les blocs ne bougent pas.

> 🚧 **Projet en cours de finition.** Le simulateur fonctionne. Il reste quelques bugs à corriger
> avant la version finale.

## Lancer

```bash
pip install pygame
python "simulateur de particules.py"
```

## Commandes

- Clique sur un des boutons à gauche pour choisir un matériau :
  - jaune : sable
  - noir : bloc solide
  - bleu : eau
- Maintiens le clic gauche dans la zone grise pour dessiner.
- Échap pour quitter.

## Fonctionnement

La grille est un dictionnaire `{(x, y): particule}` : seules les cases occupées y sont stockées.
À chaque image, les particules sont mises à jour **du bas vers le haut**, pour que celles du
dessous libèrent la place avant que celles du dessus ne tombent.

| Matériau | Règle |
|----------|-------|
| `sable` | Tombe si la case du dessous est libre, sinon glisse en diagonale (bas-droite, puis bas-gauche) |
| `eau` | Comme le sable, et peut en plus se déplacer sur le côté pour s'étaler |
| `block` | Ne bouge jamais |

Chaque matériau est une classe qui hérite de `particule` et redéfinit `ChekVoisins`. Pour ajouter
un matériau, il suffit de créer une nouvelle classe et un bouton.

## Pistes pour finir le projet

Bugs et améliorations repérés en relisant le code :

- **L'eau ne s'étale pas au fond** : sur la dernière ligne, aucune condition ne lui permet d'aller
  sur le côté, donc elle forme des tas comme le sable.
- **Le sable ne coule pas dans l'eau** : il considère l'eau comme un obstacle, alors qu'il devrait
  échanger sa place avec elle et passer en dessous.
- **Pas de gomme** : on ne peut pas retirer un bloc ou une particule, alors que le commentaire
  de `block` le prévoit.
- **Bord droit** : la condition `self.x + 1 <= max_x` laisse une particule aller sur la colonne
  `max_x`, juste en dehors de la zone grise.
- **Dessiner écrase** : cliquer sur une case occupée remplace la particule qui s'y trouve.
- **Nettoyage** : `Dessiner` et `taille` ne sont pas utilisés (l'affichage passe par
  `afficher_grille` avec `TAILLE_CELL`), et la variable `object` masque une fonction de Python.
