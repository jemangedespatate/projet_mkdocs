# 🎨 TP de Remédiation : Pixel Art avec Python

Ce TP a pour but de consolider les bases de la programmation (variables, boucles, conditions) suite au chapitre sur la Photographie Numérique.

Nous allons recréer le principe d'une **image numérique** (une grille de pixels) mais en dessinant chaque pixel "à la main" avec la tortue Python.

## 0. Préparation

1. **Téléchargez** le fichier de départ : [code_pixel_art.py](code_pixel_art.py){:download="code_pixel_art.py"}
2. **Ouvrez-le** dans EduPython.
3. **Lancez le programme** : un menu s'affiche dans la console en bas.

---

## Activité 1 : Un simple Pixel
**🎯 Objectif : Appeler une fonction avec des paramètres.**

Dans ce TP, nous allons utiliser une fonction prête à l'emploi : `dessiner_pixel(x, y, couleur)`.
Elle dessine un carré (un "pixel") à l'endroit désiré.

1. Lancez le programme et choisissez l'option **1**. Une fenêtre s'ouvre et **un pixel rouge** apparaît au centre.
2. Fermez la fenêtre graphique pour revenir au menu ou à l'éditeur.
3. Dans le code, trouvez la fonction `activite_1()` (tout en haut du fichier). Une ligne de code est déjà écrite.
4. **Modifiez** cette ligne pour changer la couleur du pixel (par exemple "blue" ou "green").
5. **Ajoutez** une nouvelle ligne en dessous pour dessiner un deuxième pixel à côté, par exemple en `(30, 0)`.

---

## Activité 2 : Une ligne de Pixels (La Boucle)
**🎯 Objectif : Utiliser une boucle `for` pour répéter une action.**

Dessiner 100 pixels un par un serait trop long ! En informatique, on utilise des **boucles**.

1. Choisissez l'option **2**.
2. Dans `activite_2()`, on veut dessiner 10 pixels bleus alignés horizontalement (x change, y reste à 0).
3. Écrivez une boucle `for` pour réaliser cela.
4. N'oubliez pas que chaque pixel fait 30 de largeur.

---

## Activité 3 : Le Carré (Boucles Imbriquées)
**🎯 Objectif : Comprendre les images (Largeur x Hauteur).**

C'est ici que l'on rejoint le chapitre **Photo** ! Une image est une grille. Pour parcourir une grille, on a besoin de **deux boucles** :

- Une pour descendre les **lignes** (y).
- Une pour parcourir les **colonnes** (x) dans chaque ligne.

```python
for y in range(nombre_de_lignes):
    for x in range(nombre_de_colonnes):
        # Dessiner un pixel
```

1. Choisissez l'option **3**.
2. Dans `activite_3()`, écrivez deux boucles imbriquées pour dessiner un carré de 5x5 pixels verts.

!!! question "Observation"
    Combien de pixels sont dessinés au total ?

---

## Activité 4 : Le Damier (Les Conditions)
**🎯 Objectif : Changer la couleur selon la position.**

Nous voulons dessiner un damier (noir et blanc). Pour cela, il faut que la couleur change une case sur deux.
L'astuce mathématique est d'utiliser la **parité** de la somme des coordonnées.

Si `(x_index + y_index)` est un nombre **pair**, on met du noir. Sinon, du blanc.

1. Choisissez l'option **4**.
2. Dans `activite_4()`, utilisez une condition `if / else` avec l'opérateur modulo (`%`) pour alterner les couleurs.
3. Vous devez utiliser une boucle double comme dans l'activité 3.
