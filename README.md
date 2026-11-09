# Sandbox de particules

Un petit bac à sable de physique que j'ai codé en Python avec Pygame. On dessine à la souris du
**sable**, de l'**eau** ou des **blocs solides**, et chaque grain bouge selon ses propres règles :
le sable tombe et fait des tas, l'eau coule et s'étale, les blocs ne bougent pas.

> 🚧 **Pas encore tout à fait fini.** Le simulateur marche, mais il me reste quelques bugs à
> corriger avant la version finale.

## Lancer

```bash
pip install pygame
python "simulateur de particules.py"
```

## Commandes

- Clique sur un des boutons à gauche pour choisir le matériau : jaune pour le sable, noir pour
  les blocs, bleu pour l'eau.
- Garde le clic gauche enfoncé dans la zone grise pour dessiner.
- Échap pour quitter.

## Comment ça marche

La grille est un dictionnaire `{(x, y): particule}` : je ne stocke que les cases occupées. À
chaque image, je mets à jour les particules **du bas vers le haut**, pour que celles du dessous
libèrent la place avant que celles du dessus tombent.

- **Sable** : il tombe si la case du dessous est libre, sinon il glisse en diagonale (en bas à
  droite, puis en bas à gauche).
- **Eau** : pareil que le sable, mais elle peut aussi aller sur le côté pour s'étaler.
- **Bloc** : il ne bouge jamais.

Chaque matériau est une classe qui hérite de `particule` et a sa propre méthode `ChekVoisins`.
Pour ajouter un nouveau matériau, il suffit de créer une classe et un bouton.

## Ce qu'il me reste à faire

- Faire en sorte que l'eau s'étale aussi sur le fond : sur la dernière ligne, elle reste en tas
  comme le sable.
- Faire couler le sable dans l'eau : pour l'instant, il la prend pour un obstacle au lieu de passer
  en dessous.
- Ajouter une gomme pour pouvoir enlever des blocs et des particules.
- Corriger le bord droit : la condition `self.x + 1 <= max_x` laisse une particule sortir d'une
  colonne de la zone grise.
- Ne plus écraser une particule quand on dessine sur une case déjà occupée.
- Faire un peu de ménage : `Dessiner` et `taille` ne servent plus, et la variable `object` porte le
  même nom qu'une fonction de Python.
