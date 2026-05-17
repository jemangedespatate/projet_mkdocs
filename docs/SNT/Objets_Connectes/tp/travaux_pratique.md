# TP : Introduction aux Objets Connectés avec la carte Micro:bit

## Objectifs de la séance
* Comprendre ce qu'est un objet connecté (capteur, traitement, actionneur).
* Découvrir l'interface de programmation en Python de la carte Micro:bit.
* Réactiver ses connaissances en Python (variables, boucles, conditions).
* Créer un programme interactif simulant un objet connecté.

---

## 1. Découverte de l'environnement

Pour ce TP, nous n'avons pas forcément besoin de la carte physique, nous allons utiliser un simulateur très puissant intégré au navigateur !

1. Rendez-vous sur le site officiel : [https://python.microbit.org/v/3](https://python.microbit.org/v/3)
2. Cliquez sur l'onglet **Reference** (ou Référence) en haut ou sur le côté de la page pour voir toutes les commandes possibles avec la carte. C'est votre "dictionnaire" !

La carte Micro:bit est équipée de :
* **Capteurs** (qui captent l'environnement) : Boutons A et B, capteur de lumière, de température, accéléromètre (détection de mouvement)...
* **Actionneurs** (qui agissent sur l'environnement) : Un écran de 25 LEDs (5x5).

### Mission 1 : Le "Hello World" des objets connectés

Sur l'interface, effacez tout le code présent dans l'éditeur et copiez ce code de base :

```python
from microbit import *

display.scroll('Bonjour !')
```

1. Cliquez sur le bouton **Play** (le triangle) sous la carte Micro:bit virtuelle à droite pour simuler le code.
2. Que se passe-t-il ? *(Rappelez-vous, `display` est l'écran, et `scroll` veut dire faire défiler).*

---

## 2. L'écran (Actionneur) et les Images

Faire défiler du texte, c'est bien, mais afficher des images, c'est mieux ! La carte possède plusieurs images pré-enregistrées.

### Mission 2 : Afficher des émotions

Testez le code suivant :

```python
from microbit import *

display.show(Image.HEART)
sleep(2000) # Fait une pause de 2000 millisecondes (2 secondes)
display.show(Image.SKULL)
```

**Travail à faire :**
Modifiez le code pour créer une animation : un cœur qui bat ! Pour cela, faites alterner `Image.HEART` et `Image.HEART_SMALL` avec des pauses courtes de 500ms entre chaque.
*Astuce : Vous aurez besoin de réutiliser la fonction `sleep()` plusieurs fois !*

---

## 3. Interagir avec l'utilisateur : Les Boutons (Capteurs)

Un objet connecté réagit à son environnement. Nous allons utiliser la boucle infinie `while True:` qui permet à la carte de vérifier en permanence ce qu'il se passe (sinon le programme s'arrête tout de suite).
*(Rappel Python : l'indentation, c'est-à-dire le décalage vers la droite, est obligatoire après le `while` et les `if` !)*

### Mission 3 : Les conditions (Si ... Sinon)

Copiez et simulez ce code :

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.clear() # Efface l'écran si on ne touche à rien
```

1. Testez en cliquant sur les boutons A et B sur le simulateur.
2. **Expliquez** avec vos propres mots sur votre compte-rendu ce que fait la ligne `elif button_b.is_pressed():`.

---

## 4. Mesurer l'environnement : La Température

La carte possède des capteurs intégrés. Lisons la température ambiante !

### Mission 4 : Un thermomètre intelligent

Voici comment lire la température avec la fonction `temperature()` :

```python
from microbit import *

while True:
    if button_a.is_pressed():
        temp = temperature() # On stocke la température dans la variable 'temp'
        display.scroll(temp)
```

*Indice : Sur le simulateur, une jauge de température (un petit thermomètre jaune) apparaît quand vous utilisez la fonction `temperature()`. Vous pouvez cliquer dessus et la faire glisser pour simuler le froid ou le chaud !*

**Défi :** 
Améliorez ce programme en utilisant la variable `temp` et les conditions (`if` / `else`) ! L'objectif est d'afficher sur l'écran :
* L'image d'un flocon de neige (ou un parapluie `Image.UMBRELLA`) **SI** la température est strictement inférieure à 15°C.
* L'image d'un soleil (`Image.HAPPY` ou dessinez un soleil) **SINON** (c'est-à-dire si elle est supérieure ou égale à 15°C).

---

## 5. Le Dé Électronique

Maintenant, à vous de jouer, presque sans aide !

**Objectif : Créer un dé de jeu électronique (de 1 à 6) qui se lance lorsqu'on secoue la carte.**

Pour cela, vous aurez besoin de deux nouveaux éléments :
1. Détecter la secousse du capteur (accéléromètre) : on utilise `accelerometer.was_gesture('shake')`.
2. Choisir un nombre au hasard. En Python, on importe la bibliothèque `random` tout en haut du programme et on utilise `random.randint(1, 6)`.

**Structure de code attendue :**
```python
from microbit import *
import random # Très important pour ajouter du hasard !

while True:
    if accelerometer.was_gesture('shake'):
        # 1. Choisir un nombre aléatoire entre 1 et 6 et le stocker dans une variable
        # 2. L'afficher à l'écran
        # 3. Mettre une petite pause pour avoir le temps de lire
    else:
        # Afficher une petite image d'attente 
```

*Test : Sur le simulateur, pour secouer la carte, passez votre souris rapidement de gauche à droite au-dessus de la carte Micro:bit virtuelle (un bouton "SHAKE" blanc peut aussi apparaître).*

---

## 6. Pour aller plus loin : Les Défis (Bonus)

Si vous avez terminé, voici des missions supplémentaires pour tester vos talents de programmeur !

### Défi Bonus 1 : La veilleuse automatique
La carte Micro:bit peut aussi mesurer la quantité de lumière qui frappe son écran (oui, les LEDs peuvent servir de capteurs de lumière !) : on utilise la fonction `display.read_light_level()`. Celle-ci renvoie un nombre entre `0` (nuit totale) et `255` (pleine lumière).

**Mission :** Créez un programme qui agit comme une veilleuse intelligente. 
* Si le niveau de lumière est inférieur à 100, la carte allume toutes ses LEDs (utilisez `Image.SQUARE` par exemple) pour éclairer la pièce. 
* Sinon, elle efface son écran.

### Défi Bonus 2 : Le jeu Pierre-Feuille-Ciseaux (Chifoumi)
Utilisez ce que vous avez appris avec le dé électronique (l'accéléromètre `shake` et l'aléatoire `random.randint`).
Au lieu d'afficher un nombre de 1 à 6 quand on secoue la carte, générez un nombre entre 1 et 3.
* Si le nombre est **1** : Affichez l'image `Image.SQUARE` (Feuille)
* Si le nombre est **2** : Affichez l'image `Image.SQUARE_SMALL` (Pierre)
* Si le nombre est **3** : Affichez l'image `Image.SCISSORS` (Ciseaux)

### Défi Bonus 3 : Le compteur manuel
Créez un programme qui sert de compteur ! 
1. Tout en haut de votre programme (mais **avant** le `while True:`), créez une variable `compteur = 0`.
2. Dans la boucle infinie, si on appuie sur le **bouton A**, on ajoute 1 à cette variable (`compteur = compteur + 1`) puis on l'affiche avec `display.scroll(compteur)`.
3. Si on appuie sur le **bouton B**, on remet le compteur à 0 et on affiche le nouveau score.
