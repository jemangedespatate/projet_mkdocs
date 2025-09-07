# 🏗️ Mini-projet Turtle : Construis ta ville 🏙️

Bienvenue dans ton mini-projet Turtle ! 🐢💻

Aujourd’hui, **vous allez créer votre propre ville étape par étape**. Vous allez utiliser tout ce que vous avez appris sur **les boucles, les fonctions et les variables** pour construire une ville avec des maisons, une route et peut-être même des arbres ou un soleil.

---

## Étape 1 : Dessiner une maison 🏠

On commence par **une maison simple** : un carré pour les murs et un triangle pour le toit.

### Ce que vous devez faire :

1. Complétez la fonction `carre(cote)` pour dessiner un carré.
2. Complétez la fonction `triangle(cote)` pour dessiner un triangle équilatéral.
3. Créez ensuite une fonction `maison(cote)` qui combine le carré et le triangle pour former une maison.

💡 **Astuce :** utilisez les boucles `for` pour dessiner les côtés plus facilement.

---

## Étape 2 : Construire une route 🛣️

Maintenant, ajoutons **une route sous votre maison**.

### Ce que vous devez faire :

1. Complétez la fonction `rectangle(longueur, largeur)` pour dessiner un rectangle (la route).
2. Ajoutez des **bandes blanches** au milieu de la route en utilisant une boucle et les fonctions `penup()` et `pendown()`.

💡 **Astuce :** vous pouvez répéter plusieurs petits rectangles blancs pour faire les bandes.

---

## Étape 3 : Construire une ville 🏙️

Maintenant que vous savez dessiner des maisons et une route, vous allez créer **une vraie ville** !

### Ce que vous devez faire :

1. Complétez la fonction `ville(nb_maisons)` pour placer plusieurs maisons avec différentes tailles et couleurs.
2. Ajoutez **une route principale**.
3. (Optionnel) Ajoutez des détails comme des arbres 🌳, des immeubles 🏢 ou un soleil ☀️.

💡 **Astuce :** utilisez vos **fonctions** pour organiser votre code et des **boucles** pour répéter des maisons ou d’autres éléments.

---

## Votre squelette de code 📝

Voici le code de départ avec toutes les fonctions à compléter :

```python
from turtle import *

# -------------------------------
# Fonctions de base
# -------------------------------

def carre(cote):
    """
    Dessine un carré dont les côtés mesurent 'cote'.
    Complétez cette fonction !
    """
    pass  # À remplacer par votre code

def triangle(cote):
    """
    Dessine un triangle équilatéral dont les côtés mesurent 'cote'.
    Complétez cette fonction !
    """
    pass  # À remplacer par votre code

def rectangle(longueur, largeur):
    """
    Dessine un rectangle avec la longueur et la largeur données.
    Complétez cette fonction !
    """
    pass  # À remplacer par votre code

# -------------------------------
# Fonctions composées
# -------------------------------

def maison(cote):
    """
    Dessine une maison : un carré + un toit triangulaire.
    Utilisez les fonctions carre() et triangle().
    """
    pass  # À remplacer par votre code

def route(longueur, largeur, bandes):
    """
    Dessine une route avec 'bandes' blanches au milieu.
    Utilisez rectangle() et une boucle pour les bandes.
    """
    pass  # À remplacer par votre code

def ville(nb_maisons):
    """
    Dessine une ville avec 'nb_maisons' maisons et une route.
    Utilisez maison() et route().
    Ajoutez éventuellement des couleurs et des positions différentes.
    """
    pass  # À remplacer par votre code

# -------------------------------
# Testez vos fonctions !
# -------------------------------

reset()
# Exemples d'appel (à compléter) :
# maison(100)
# route(400, 50, 8)
# ville(5)
```