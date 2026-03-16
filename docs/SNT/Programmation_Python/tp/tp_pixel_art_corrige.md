# 🔑 Correction du TP : Pixel Art & Remédiation

Ce document fournit les solutions complètes et des notes pédagogiques pour le TP de remédiation Pixel Art.

Rappel : Ce TP est conçu pour aider les élèves qui ont du mal avec les coordonnées `(x, y)` et les boucles, avant ou pendant le chapitre sur la photographie numérique.

---

## Fichiers
- **Code Élève** : `code_pixel_art.py` (à compléter)
- **Code Prof** : `code_pixel_art_corrige.py` (complet et fonctionnel)

---

## Activité 1 : Un simple Pixel

**Difficulté** : Très Facile  
**But** : Comprendre l'appel de fonction avec paramètres.

Beaucoup d'élèves oublient les parenthèses `()` ou ne savent pas où écrire le code. Insistez sur l'indentation (bien que non nécessaire pour un appel simple, c'est une bonne pratique).

```python
dessiner_pixel(0, 0, "red")       # Pixel de base
dessiner_pixel(30, 0, "blue")     # Défi : pixel décalé de 30px
```

*Note : Les coordonnées sont en pixels écran. Si on met `(1, 0)`, les pixels se chevaucheront car chaque carré fait 30px de côté.*

---

## Activité 2 : Une ligne de Pixels (La Boucle)

**Difficulté** : Moyenne  
**But** : Comprendre le lien entre l'indice de boucle `i` et la coordonnée `x`.

C'est le point de blocage fréquent. Les élèves écrivent souvent `x = i` au lieu de `x = i * 30`.  
Expliquez que `i` est le **numéro de la case** (0, 1, 2...) et `x` est la **position en pixels** (0, 30, 60...).

```python
for i in range(10):
    x = i * 30       # Le pas est de 30
    y = 0            # On reste sur la même ligne
    dessiner_pixel(x, y, "blue")
```

---

## Activité 3 : Le Carré (Boucles Imbriquées)

**Difficulté** : Difficile  
**But** : Introduire la double boucle nécessaire pour le traitement d'images.

Cette structure est identique à celle utilisée dans le TP Photo (parcours des pixels `width` x `height`).
L'erreur classique est d'inverser `x` et `y` ou d'oublier l'indentation de la deuxième boucle.

```python
for y_index in range(5):
    y = y_index * 30
    
    for x_index in range(5):
        x = x_index * 30
        
        # On peut varier la couleur si on veut s'amuser
        dessiner_pixel(x, y, "green")
```

---

## Activité 4 : Le Damier (Les Conditions)

**Difficulté** : Avancée  
**But** : Logique conditionnelle basée sur les mathématiques (Parité).

Le concept de damier repose sur le fait que la somme des coordonnées (indices de case) change de parité à chaque case adjacente.
- Case (0,0) -> 0 (pair) -> Noir
- Case (1,0) -> 1 (impair) -> Blanc
- Case (0,1) -> 1 (impair) -> Blanc
- Case (1,1) -> 2 (pair) -> Noir

```python
taille_grille = 8

for y_index in range(taille_grille):
    y = y_index * 30
    for x_index in range(taille_grille):
        x = x_index * 30
        
        # Test de parité sur la somme des indices
        if (x_index + y_index) % 2 == 0:
            couleur = "black"
        else:
            couleur = "white"
        
        dessiner_pixel(x, y, couleur)
```

## Prolongements possibles
Si des élèves finissent très vite :
1. **Drapeau Français** : Diviser la largeur par 3 et changer la couleur (Bleu, Blanc, Rouge) selon la valeur de `x_index`.
2. **Dégradé** : Utiliser la bibliothèque Turtle pour changer la couleur RGB en fonction de `i`.
