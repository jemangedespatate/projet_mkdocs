# 💻 Travaux Pratiques : Traitement d'Image avec Python

L'objectif de ce TP est d'apprendre à manipuler des images numériques pixel par pixel à l'aide du langage Python et de la bibliothèque **Pillow** (PIL).

## 0. Préparation

Vous devez disposer d'une image nommée `image_tp.jpg` dans le même dossier que votre script Python. Vous pouvez télécharger une image simple (par exemple un paysage ou un fruit) pour faire les tests.

Pour utiliser la bibliothèque, on commence toujours par :
```python
from PIL import Image
```

## Activité 1 : Ouvrir et Analyser une image

Copiez et exécutez le code suivant :

```python
from PIL import Image

# 1. Ouverture du fichier image
img = Image.open("image_tp.jpg")

# 2. Récupération des dimensions
largeur, hauteur = img.size
print(f"L'image fait {largeur} pixels de large et {hauteur} pixels de haut.")
print(f"Définition totale : {largeur * hauteur} pixels.")

# 3. Analyse du pixel central
x = largeur // 2
y = hauteur // 2
r, v, b = img.getpixel((x, y))

print(f"Couleur du pixel central ({x},{y}) : Rouge={r}, Vert={v}, Bleu={b}")
```

**Question :** Que se passe-t-il si vous essayez de lire le pixel aux coordonnées `(largeur, hauteur)` ? Pourquoi ? (Essayez !)

---

## Activité 2 : Créer le Négatif d'une image

Pour créer le négatif d'une image, il faut inverser les couleurs :
*   Le 0 devient 255
*   Le 255 devient 0
*   La valeur `v` devient `255 - v`

Complétez le programme suivant :

```python
from PIL import Image

img = Image.open("image_tp.jpg")
largeur, hauteur = img.size

# On crée une nouvelle image vide de la même taille
img_new = Image.new("RGB", (largeur, hauteur))

# On parcourt tous les pixels de l'image (double boucle)
for y in range(hauteur):
    for x in range(largeur):
        # On récupère les anciennes couleurs
        r, v, b = img.getpixel((x, y))
        
        # --- A VOUS DE JOUER ---
        # Calculez les nouvelles couleurs
        r_new = 255 - r
        v_new = ???       # A compléter
        b_new = ???       # A compléter
        # -----------------------
        
        # On écrit le nouveau pixel dans la nouvelle image
        img_new.putpixel((x, y), (r_new, v_new, b_new))

# On affiche le résultat
img_new.show()
# On sauvegarde le résultat
img_new.save("negatif.jpg")
```

---

## Activité 3 : Passage en Noir et Blanc (Niveaux de gris)

Une méthode simple pour transformer une image couleur en noir et blanc est de faire la **moyenne** des trois composantes pour chaque pixel.

$$Gris = \frac{Rouge + Vert + Bleu}{3}$$

1.  Reprenez le squelette du code de l'Activité 2.
2.  Modifiez le calcul à l'intérieur de la boucle pour calculer la moyenne.
3.  Affectez cette valeur moyenne aux trois canaux (`r_new`, `v_new`, `b_new`) pour obtenir du gris.

*Attention : La division doit donner un nombre entier ! Utilisez `// 3` ou `int((r+v+b)/3)`.*

??? tip "Indice pour le code"
    ```python
    moyenne = (r + v + b) // 3
    img_new.putpixel((x, y), (moyenne, moyenne, moyenne))
    ```

---

## Activité 4 : Effet "Filtre Rouge"

On souhaite ne garder que la composante **Rouge** de l'image.

*   Le Rouge reste inchangé.
*   Le Vert devient 0.
*   Le Bleu devient 0.

Écrivez le script qui réalise cet effet et sauvegardez l'image sous `filtre_rouge.jpg`.

---

## Activité 5 : Le Mystère de l'Image Cachée (Steganographie) 🕵️‍♂️

*Niveau avancé*

On soupçonne qu'un message secret est caché dans les composantes **bleues** d'une image apparemment noire.
Si le pixel est totalement noir (0,0,0), il n'y a rien. Mais si le bleu vaut 1 (0,0,1), c'est un pixel du message !

**Objectif :** Révéler le message caché.
**Méthode :** Multiplier la composante bleue par 255.
*   Si Bleu était 0 -> $0 \times 255 = 0$ (Noir)
*   Si Bleu était 1 -> $1 \times 255 = 255$ (Bleu vif)

Essayez d'écrire un script qui transforme les micros-variations de bleu en bleu vif pour faire apparaître une forme.

```python
# Squelette
r_new = 0
v_new = 0
b_new = b * 255 # On amplifie le signal bleu

# Note : Cela ne fonctionne que si vous avez une image préparée pour cet exercice !
# Vous pouvez en créer une vous-même en dessinant des pixels (0,0,1) sur un fond (0,0,0).
```