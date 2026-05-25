# TP Projet : Créer une montre connectée (Podomètre)

## Objectif de la séance
L'objectif de ce TP est de programmer de A à Z un véritable objet connecté : **une montre de sport intelligente (podomètre)**.   
Au lieu de faire des petits exercices séparés, vous allez construire ce projet **étape par étape**. À la fin de la séance, votre carte Micro:bit sera capable de :

1. Compter vos pas lorsque vous marchez (ou secouez la carte).
2. Afficher votre nombre de pas sur demande.
3. Se remettre à zéro.
4. Vous féliciter si vous atteignez votre objectif quotidien !

---

## L'environnement de travail

Comme pour notre découverte, nous allons utiliser le simulateur intégré au navigateur.

1. Rendez-vous sur le site officiel : [https://python.microbit.org/v/3](https://python.microbit.org/v/3)
2. Effacez le code de démonstration présent dans l'éditeur.

---

## Étape 1 : Initialiser la mémoire de la montre

Pour que notre montre puisse compter les pas, elle doit posséder une "mémoire" pour retenir ce nombre. En programmation, on utilise une **variable**.

**Mission 1 :**
Au tout début de votre programme (ligne 1 et 2), importez la bibliothèque Micro:bit et créez une variable nommée `pas` que vous initialiserez à 0.
Ajoutez ensuite un message de bienvenue pour indiquer que la montre est allumée.

```python
from microbit import *

# On crée notre variable pour stocker les pas
# À FAIRE : Créer la variable 'pas' et lui donner la valeur 0
...

# Message d'accueil au démarrage
# À FAIRE : Faire défiler le texte 'Montre ON' sur l'écran
...
```

1. Copiez ce code et testez-le sur le simulateur en appuyant sur le bouton de lecture (Play).
2. Que se passe-t-il à l'écran ? Le programme s'arrête-t-il après le message ? *(La réponse est oui, car nous n'avons pas encore mis de boucle infinie pour vérifier les capteurs en continu !)*

---

## Étape 2 : Détecter la marche (L'accéléromètre)

Un podomètre compte un pas à chaque fois qu'il détecte un choc ou un mouvement fort. Nous allons utiliser l'accéléromètre de la carte.
Pour que la montre surveille en permanence nos mouvements, nous devons placer notre code dans une **boucle infinie** `while True:`.

**Mission 2 :**
Complétez votre programme pour qu'il ressemble à ceci :

```python
from microbit import *

# (Rappel de l'étape 1 : création de la variable et message)
...

# Boucle infinie : la montre surveille les capteurs en permanence
while True:
    # Si on détecte une secousse (un pas)
    if accelerometer.was_gesture('shake'):
        
        # À FAIRE 1 : Ajouter 1 à la variable "pas" (ex: pas = pas + 1)
        ...
        
        # À FAIRE 2 : Afficher un "V" pour confirmer avec l'image Image.YES
        ...
        
        sleep(500) # Petite pause d'une demi-seconde
        display.clear() # On efface l'écran pour économiser la batterie
```

1. Sur le simulateur, passez votre souris rapidement sur la carte de gauche à droite (ou cliquez sur le bouton blanc "SHAKE" qui apparaît) pour simuler un pas.
2. Observez l'écran : le "V" (`Image.YES`) confirme que le pas a bien été compté.
3. *Problème :* Comment savoir combien de pas on a fait au total ? C'est l'étape suivante !

---

## Étape 3 : Afficher le compteur (Bouton A)

L'utilisateur de la montre veut pouvoir lire son nombre de pas quand il le décide. Nous allons utiliser le **bouton A** pour cela.

**Mission 3 :**

Dans la boucle infinie, ajoutez une nouvelle condition (avec `elif` pour "sinon si") pour vérifier si le bouton A est pressé. Si c'est le cas, on fait défiler le nombre de pas.

Modifiez votre boucle `while True:` *(attention à bien respecter l'indentation, c'est-à-dire le décalage des lignes vers la droite !)* :

```python
while True:
    if accelerometer.was_gesture('shake'):
        # (Votre code de l'étape 2)
        ...
        sleep(500)
        display.clear()
        
    # À FAIRE : Ajouter la condition "sinon si" le bouton A est pressé
    elif ... :
        # À FAIRE : Afficher la variable 'pas' sur l'écran
        ...
```

**Travail à faire :**

1. Secouez la carte virtuellement 3 ou 4 fois.
2. Appuyez sur le bouton A. La carte doit afficher votre score de pas !

---

## Étape 4 : Remettre à zéro (Bouton B)

À la fin de la journée, ou si l'on prête la montre à un ami, il faut pouvoir remettre le compteur de pas à zéro.

**Mission 4 :**

C'est à vous de jouer ! Sans que l'on vous donne le code exact, ajoutez une troisième condition dans votre boucle (un nouveau `elif`).

* **Condition :** Si le bouton B est pressé (`button_b.is_pressed()`).
* **Action :** Remettre la variable `pas` à 0.
* **Optionnel :** Afficher une croix (`Image.NO`) ou un petit message "RAZ" pour confirmer que tout a été effacé, suivi d'un `display.clear()`.

*Testez votre code : faites quelques pas (secouez), vérifiez le score avec A, appuyez sur B, puis vérifiez avec A que le score est bien revenu à 0 !*

---

## Étape 5 : L'objectif de santé (Félicitations)

Pour encourager l'utilisateur, notre montre connectée va afficher une petite récompense lorsqu'il atteint son objectif quotidien (par exemple, 10 pas dans notre simulation).

**Mission 5 :**

Il va falloir modifier ce qui se passe **quand on compte un pas** (donc à l'intérieur du `if accelerometer.was_gesture('shake'):`).
Juste après avoir fait `pas = pas + 1`, ajoutez une **condition** pour vérifier si `pas` est exactement égal à `10` *(rappel: en Python, pour vérifier une égalité on utilise un double signe égal `==`)*.

Voici la structure attendue pour cette partie :
```python
    if accelerometer.was_gesture('shake'):
        # On ajoute 1 au compteur de pas
        ...
        
        # À FAIRE : On vérifie si l'objectif de 10 pas est atteint (égalité)
        if ... :
            # À FAIRE : Afficher une récompense (ex: Image.HEART) et faire une pause de 2000 ms
            ...
            ...
        else:
            # À FAIRE : Afficher l'image habituelle (Image.YES) et faire une pause de 500 ms
            ...
            ...
            
        display.clear()
```

*Intégrez cette logique, et testez ! Secouez la carte 10 fois pour voir la récompense.*

---

## 🏆 Défis Bonus pour améliorer votre montre

Votre projet de base est terminé ! Si vous avez du temps, voici des idées pour rendre votre montre connectée encore plus "haut de gamme" :

### Défi 1 : Le mode Nuit Économique

Les montres modernes s'allument toutes seules quand il fait nuit pour qu'on puisse lire l'heure.   
En utilisant le capteur de lumière de l'écran (fonction `display.read_light_level()` qui renvoie un nombre de 0 à 255), faites en sorte que si la lumière est inférieure à 50 (nuit), l'écran affiche une petite veilleuse très faible (par exemple allumer juste la LED centrale). Attention à ne pas bloquer les autres capteurs !

### Défi 2 : Alerte de triche !

Les utilisateurs essaient parfois de tricher en secouant très fort la montre sans marcher. 
La Micro:bit peut détecter plusieurs types de gestes (regardez l'onglet Référence de l'éditeur !). Si la montre détecte le geste `'freefall'` (chute libre) ou `'8g'` (accélération extrême), affichez l'image `Image.ANGRY` et retirez 5 pas !

### Défi 3 : Ajout d'une jauge de progression

Au lieu d'afficher juste "YES" pour chaque pas, pourriez-vous allumer les LED de l'écran une par une à chaque pas, jusqu'à en allumer 10 ?

*(Indice : cherchez du côté de `display.set_pixel(x, y, intensité)`).*
