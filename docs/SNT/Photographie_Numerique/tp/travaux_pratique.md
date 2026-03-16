# 💻 TP : Images Binaires (Noir et Blanc)

Ce TP a pour but de comprendre comment une image est stockée dans la mémoire de l'ordinateur en utilisant uniquement des **0** et des **1**, sans entrer dans la complexité de la programmation avancée.

## Introduction

Une image numérique est une grille de points appelés **pixels**.
Dans une image "binaire" (2 couleurs), chaque pixel est codé sur **1 bit** :
- **0** représente le **BLANC**.
- **1** représente le **NOIR**.

---

## Activité 1 : Créer une image à la main ✍️

Nous allons utiliser un format d'image ultra-simple appelé **PBM** (Portable Bitmap). C'est un simple fichier texte !

1. Ouvrez un éditeur de texte simple (Bloc-notes ou directement dans eduPython/Thonny).
2. Copiez-collez le texte suivant :
        
```text
P1
5 5
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
```

3. **Explications :**
    - `P1` : C'est le "code magique" qui dit "Je suis une image PBM".
    - `5 5` : Largeur et Hauteur de l'image (5 pixels sur 5).
    - La suite : Les pixels (0 pour blanc, 1 pour noir).
    
4. Enregistrez le fichier sous le nom `smiley.pbm` (Attention à l'extension `.pbm` !).
5. Ouvrez ce fichier avec un logiciel de visualisation d'image (ou glissez-le dans Thonny/eduPython).

**A vous de jouer :** Modifiez le fichier texte pour dessiner la première lettre de votre prénom. Sauvegardez et vérifiez le résultat.

---

## Activité 2 : Manipuler l'image avec Python 🐍

Dessiner pixel par pixel à la main, c'est long. Utilisons Python pour colorier les cases à notre place.

### 1. Préparation
Téléchargez le fichier de départ :
- [code_binaire.py](code_binaire.py){:download="code_binaire.py"}

Ouvrez-le dans **eduPython** (ou tout autre éditeur Python).

### 2. Comprendre les commandes
Dans ce fichier, nous avons préparé des commandes simples pour vous :

*   `creer_image(largeur, hauteur)` : Crée une image blanche.
*   `colorier_pixel(x, y, 1)` : Met le pixel en **NOIR** aux coordonnées (x, y).
*   `colorier_pixel(x, y, 0)` : Met le pixel en **BLANC**.
*   `afficher_image()` : Montre votre dessin dans la console.

_Rappel : En informatique, on commence à compter à partir de 0. Le point en haut à gauche est (0, 0)._

### 3. A vous de jouer
Dans la zone élève du fichier `code_binaire.py` :
1.  Lancez le code pour voir ce qu'il fait (il trace 3 points).
2.  Effacez les exemples et essayez de dessiner une **croix** ou un **carré** en utilisant les commandes `colorier_pixel`.

Exemple de croix à réaliser :
```text
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
```

---

## Activité 3 : Le Négatif (Inversion des couleurs) 🌗

Imaginez que vous deviez inverser une image de 1000 pixels. Vous n'allez pas écrire 1000 lignes de code !
Nous allons utiliser des **boucles** pour parcourir toute l'image.

Pour réaliser le négatif :
1.  On regarde chaque pixel un par un (avec deux boucles `for`, une pour les lignes `y`, une pour les colonnes `x`).
2.  On regarde sa couleur avec `lire_pixel(x, y)`.
3.  Si c'est **0**, on colorie en **1**. Sinon on colorie en **0**.

**Votre mission :**
Tout en bas du fichier `code_binaire.py`, décommentez la partie "EXERCICE : LE NÉGATIF" et complétez les lignes manquantes pour que le programme inverse les couleurs de votre dessin précédent.

---

## Activité 4 : L'image aléatoire (Neige TV) 🎲

Pour aller plus loin, essayons de remplir l'image au hasard.

1.  Ajoutez `from random import randint` tout en haut du fichier.
2.  Créez une nouvelle image plus grande : `creer_image(10, 10)`.
3.  Utilisez les boucles `for` (comme dans l'activité 3) pour parcourir toutes les cases.
4.  À l'intérieur de la boucle, au lieu de lire la couleur, choisissez une couleur au hasard :
    ```python
    couleur_hasard = randint(0, 1) # Choisit 0 ou 1 au hasard
    colorier_pixel(x, y, couleur_hasard)
    ```
5.  Affichez le résultat.

---
## Aller plus loin

Si vous avez fini ce TP, vous pouvez tenter le TP sur la photographie couleur :
👉 [TP 2 : Traitement d'Image (Pillow)](tp_pillow.md)
