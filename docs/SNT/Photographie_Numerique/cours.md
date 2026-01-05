# Photographie Numérique

## 🤔 Introduction

La photographie numérique a remplacé la photographie argentique (chimique) dans la quasi-totalité des usages courants. Mais qu'est-ce qu'une image pour un ordinateur ? Comment passe-t-on de la lumière réelle à une suite de 0 et de 1 ?

Dans ce cours, nous allons découvrir la structure d'une image matricielle, comment les couleurs sont codées et comment manipuler ces données.

## ⌛ Point historique

*   **1861** : Première photographie couleur réalisée par le physicien **James Clerk Maxwell**.
*   **1957** : Première image numérique produite par un ordinateur (un scan de bébé) par Russell Kirsch.
*   **1969** : Invention du capteur **CCD** par Willard Boyle et George Smith (Prix Nobel 2009).
*   **1991** : Premier appareil photo numérique commercial, le Kodak DCS-100 (1.3 mégapixels).

## Définitions

<span style="color: #FF0000">Définition : Pixel</span>

**Le pixel (contraction de *Picture Element*) est le plus petit élément constitutif d'une image numérique. Il représente un point de couleur ou de lumière.**

<span style="color: #FF0000">Définition : Image matricielle</span>

**Une image numérique est une grille (ou matrice) rectangulaire de pixels composée de L colonnes (Largeur) et H lignes (Hauteur).**

??? note "Définition vs Résolution"

    Il ne faut pas confondre deux termes souvent mal utilisés :
    
    *   **La définition** correspond au nombre total de pixels de l'image. Elle se calcule par le produit **Largeur × Hauteur**.
        *   *Exemple : Une image Full HD de **1920 × 1080** a une définition d'environ 2 mégapixels.*
    *   **La résolution** exprime la densité de pixels sur un support physique (écran ou papier). Elle se mesure en **ppp** (points par pouce) ou **dpi** (*dots per inch*).

## ⚫⚪ Images en Noir et Blanc et Niveaux de Gris

Pour qu'un ordinateur stocke une image, il doit transformer chaque pixel en nombre.

### Images binaires

C'est le format le plus simple. Chaque pixel ne peut prendre que deux états.

<span style="color: #FF0000">Définition : Image binaire</span>

**Une image où chaque pixel vaut soit 0 (Noir), soit 1 (Blanc). L'information est codée sur 1 bit.**

### Images en Niveaux de Gris

Pour obtenir plus de nuances, on code chaque pixel sur plusieurs bits. Le standard actuel utilise **1 octet (8 bits)** par pixel.

Cela permet d'avoir **2⁸ = 256** valeurs possibles :

*   **0** : Noir absolu
*   **255** : Blanc pur
*   **128** : Gris moyen

<span style="color: #26B260">Exemple : Codage d'une ligne</span>

Imaginez une ligne de 4 pixels : Noir, Gris foncé, Gris clair, Blanc.
En décimal, cela donnerait : `[0, 80, 200, 255]`.

## 🎨 Les Images en Couleur

### Le modèle RVB

L'œil humain perçoit les couleurs grâce à 3 types de cônes (Rouge, Vert, Bleu). Les écrans et capteurs utilisent le même principe de **synthèse additive**.

<span style="color: #FF0000">Définition : Modèle RVB</span>

**Chaque pixel couleur est composé de 3 sous-pixels (canaux) : Rouge, Vert et Bleu. Chacun est codé sur un octet (0 à 255).**

Un pixel couleur occupe donc 3 octets (**3 × 8 = 24** bits) en mémoire.

| Couleur | Rouge (R) | Vert (V) | Bleu (B) |
| :--- | :---: | :---: | :---: |
| **Noir** | 0 | 0 | 0 |
| **Blanc** | 255 | 255 | 255 |
| **Rouge** | 255 | 0 | 0 |
| **Vert** | 0 | 255 | 0 |
| **Bleu** | 0 | 0 | 255 |
| **Jaune** | 255 | 255 | 0 |
| **Magenta** | 255 | 0 | 255 |
| **Cyan** | 0 | 255 | 255 |

<span style="color: #26B260">Exemple de poids d'image</span>

Une image de **1000 × 1000** pixels en couleur pèse :

**1000 × 1000 × 3 octets = 3 millions d'octets ≈ 3 Mo**

## 🗂️ Formats et Métadonnées

### Formats de fichiers

Pour réduire la taille des fichiers (compression), on utilise différents formats :

*   **JPEG** : Compression **avec perte**. Idéal pour les photos. Supprime les détails invisibles à l'œil nu.
*   **PNG** : Compression **sans perte**. Gère la transparence. Idéal pour les graphismes.

### Métadonnées EXIF

<span style="color: #FF0000">Définition : Métadonnées</span>

**Ce sont des "données sur les données". Elles sont enregistrées dans le fichier image au moment de la prise de vue (souvent au format EXIF).**

Elles peuvent contenir :

*   La date et l'heure.
*   Les réglages de l'appareil (Flash, ISO, temps de pose).
*   Les coordonnées GPS (Latitude, Longitude).

??? warning "Vie privée et Géolocalisation"
    
    Partager une photo prise chez soi sur un réseau social ou un site web peut révéler votre adresse exacte si les métadonnées GPS ne sont pas supprimées. Soyez vigilants !

## 💻 Manipulation en Python (PIL)

Le langage Python permet de manipuler les images pixel par pixel grâce à la bibliothèque `Pillow`.

```python
from PIL import Image

# Ouvrir une image
img = Image.open("mon_image.jpg")

# Récupérer la taille
largeur, hauteur = img.size

# Récupérer la couleur du pixel (x=10, y=20)
r, v, b = img.getpixel((10, 20))

# Créer un négatif en modifiant les pixels
# (Exemple de principe, il faudrait une boucle pour tout l'image)
r_new = 255 - r
v_new = 255 - v
b_new = 255 - b
```