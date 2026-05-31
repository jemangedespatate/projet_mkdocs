# TP Projet : Créer un système d'alarme anti-intrusion (Antivol de sac)

## Objectif de la séance
L'objectif de ce TP est de programmer de A à Z un autre type d'objet connecté : **un système d'alarme anti-intrusion pour sac à dos**.   
Vous allez construire ce projet **étape par étape**. À la fin de la séance, votre carte Micro:bit sera capable de :

1. S'activer (s'armer) avec un compte à rebours pour vous laisser le temps de fermer votre sac.
2. Se désactiver (se désarmer) à l'aide d'un bouton.
3. Détecter si quelqu'un déplace ou secoue votre sac grâce à l'accéléromètre.
4. Déclencher un signal visuel clignotant (effet gyrophare) en cas d'intrusion.
5. Garder en mémoire et afficher le nombre de tentatives d'intrusion détectées.

---

## L'environnement de travail

Comme pour les séances précédentes, nous allons utiliser le simulateur intégré au navigateur.

1. Rendez-vous sur le site officiel : [https://python.microbit.org/v/3](https://python.microbit.org/v/3)
2. Effacez le code de démonstration présent dans l'éditeur.

---

## Étape 1 : Initialiser la mémoire de l'alarme

Pour savoir si notre alarme est en train de surveiller le sac ou non, elle doit retenir son état : "armée" ou "désarmée". Nous allons utiliser une **variable** booléenne (qui vaut soit `True` pour Vrai, soit `False` pour Faux).
Au démarrage, l'alarme doit être désarmée.

**Mission 1 :**

Au tout début de votre programme (lignes 1 et 2), importez la bibliothèque Micro:bit et créez une variable nommée `armee` initialisée à `False`.   
Affichez également un smiley endormi (`Image.ASLEEP`) pour indiquer que l'alarme est éteinte et ne surveille rien.

```python
from microbit import *

# On crée notre variable pour savoir si l'alarme surveille (True) ou non (False)
# À FAIRE : Créer la variable 'armee' et lui donner la valeur False
...

# Image au démarrage pour indiquer que l'alarme est désarmée
# À FAIRE : Afficher l'image Image.ASLEEP à l'écran
...
```

1. Copiez ce code et testez-le sur le simulateur.
2. L'image s'affiche-t-elle bien ? Le programme s'arrête-t-il tout de suite ? *(La réponse est oui, car nous n'avons pas encore créé notre boucle `while True:`).*

---

## Étape 2 : Activer et désactiver l'alarme (Boutons A et B)

Nous voulons pouvoir allumer l'alarme quand nous laissons notre sac, et l'éteindre à notre retour.

* Le **bouton A** servira à **armer** l'alarme.
* Le **bouton B** servira à **désarmer** l'alarme.

Pour laisser le temps de fermer le sac après avoir appuyé sur A, nous allons ajouter un petit compte à rebours visuel de 3 secondes avant d'armer l'alarme.

**Mission 2 :**

Complétez votre programme en ajoutant la boucle infinie `while True:` et les conditions associées aux boutons :

```python
from microbit import *

# (Rappel de l'étape 1)
armee = False
display.show(Image.ASLEEP)

while True:
    # Si on appuie sur le bouton A : on arme l'alarme
    if button_a.is_pressed():
        # Compte à rebours visuel
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(1000)
        display.show("1")
        sleep(1000)
        
        # À FAIRE 1 : Changer la variable 'armee' pour qu'elle devienne True
        ...
        
        # À FAIRE 2 : Afficher un cadenas fermé (Image.TARGET) ou une icône d'alerte (Image.SKULL) pour confirmer
        ...
        
    # Si on appuie sur le bouton B : on désactive l'alarme
    elif button_b.is_pressed():
        # À FAIRE 3 : Remettre la variable 'armee' à False
        ...
        
        # À FAIRE 4 : Afficher à nouveau l'image de sommeil Image.ASLEEP
        ...
```

*Testez votre code sur le simulateur :* Appuyez sur A, attendez le compte à rebours, vérifiez si l'image change. Appuyez sur B, l'écran doit revenir au mode sommeil.

---

## Étape 3 : Détecter l'intrusion (L'accéléromètre)

Maintenant que l'alarme peut être armée, elle doit surveiller les mouvements du sac. Si quelqu'un le déplace, l'accéléromètre va détecter une secousse (`shake`).
Mais attention ! On ne doit détecter le mouvement **que si l'alarme est armée**.

**Mission 3 :**

Dans votre boucle `while True:`, ajoutez une condition pour vérifier si l'alarme est armée **ET** si une secousse est détectée.
*Astuce : En Python, pour vérifier deux conditions en même temps, on utilise le mot-clé `and` (et).*

```python
while True:
    # (Rappel des boutons A et B de l'étape 2)
    if button_a.is_pressed():
        ...
    elif button_b.is_pressed():
        ...
        
    # À FAIRE : Si l'alarme est armée ET qu'on détecte une secousse ('shake')
    elif ... and ... :
        # Pour l'instant, on affiche une croix de danger pour signaler l'alerte
        display.show(Image.NO)
        sleep(2000)
        display.clear()
```

*Testez sur le simulateur :*

1. Armez l'alarme (bouton A) et attendez la fin du compte à rebours.
2. Secouez la carte (cliquez sur le bouton blanc "SHAKE" qui apparaît ou secouez votre souris sur la carte). La croix rouge `Image.NO` doit s'afficher !
3. Désarmez l'alarme (bouton B). Secouez à nouveau : la croix ne doit pas s'afficher, car l'alarme est désarmée.

---

## Étape 4 : Déclencher la sirène (Alerte continue)

Actuellement, la croix de danger s'efface toute seule après 2 secondes. Une vraie alarme doit clignoter en continu jusqu'à ce que son propriétaire vienne la désactiver avec le bouton B !
Pour cela, nous allons ajouter une nouvelle variable : `alerte_declenchee = False`.

**Mission 4 :**

Modifiez votre programme pour intégrer cette variable et créer un effet gyrophare (clignotement).

```python
from microbit import *

armee = False
# À FAIRE 1 : Créer la variable 'alerte_declenchee' et l'initialiser à False
...

display.show(Image.ASLEEP)

while True:
    # Bouton A : Armer l'alarme
    if button_a.is_pressed():
        # (compte à rebours)
        ...
        armee = True
        # On réinitialise l'alerte au cas où elle tournait déjà
        alerte_declenchee = False 
        display.show(Image.SKULL)
        
    # Bouton B : Désarmer l'alarme ET arrêter la sirène
    elif button_b.is_pressed():
        armee = False
        # À FAIRE 2 : Remettre la variable 'alerte_declenchee' à False
        ...
        display.show(Image.ASLEEP)
        
    # Détection de secousse
    elif armee == True and accelerometer.was_gesture('shake'):
        # À FAIRE 3 : Passer la variable 'alerte_declenchee' à True
        ...
        
    # Effet gyrophare (sirène visuelle)
    # À FAIRE 4 : Si 'alerte_declenchee' est True, on fait clignoter l'écran
    if ... :
        display.show(Image.CHESSBOARD) # Motif 1
        sleep(200)
        display.clear() # Écran vide (Motif 2)
        sleep(200)
```

*Testez ce fonctionnement :* Une fois l'alarme armée et secouée, le clignotement doit continuer sans s'arrêter. Si vous appuyez sur B, tout doit s'arrêter et se désarmer.

---

## Étape 5 : Historique des intrusions (Compteur)

Lorsque vous revenez à votre sac, vous voulez savoir si quelqu'un a essayé d'y toucher pendant votre absence. Nous allons compter le nombre de fois où l'alarme s'est déclenchée.

**Mission 5 :**

1. Au tout début de votre programme, créez une variable `intrusions` initialisée à `0`.
2. À chaque fois qu'une secousse est détectée (Étape 3), ajoutez `1` à cette variable.
3. Pour lire ce compteur, ajoutez une condition : si l'utilisateur appuie **simultanément sur les boutons A et B**, la carte fait défiler le nombre de tentatives d'intrusion.

> [!WARNING]
> **Attention à l'ordre des conditions !**
> En Python, la carte lit les conditions `if` / `elif` dans l'ordre, du haut vers le bas. Si vous mettez le test `button_a.is_pressed() and button_b.is_pressed()` en dessous de `button_a.is_pressed()`, la carte s'arrêtera sur le premier bouton détecté et ne lira jamais l'appui double. 
> Pour éviter cela, placez la vérification des deux boutons tout en haut de votre boucle `while True:` !

```python
from microbit import *

# Variables de départ
armee = False
alerte_declenchee = False
# À FAIRE 1 : Créer la variable 'intrusions' à 0
...

display.show(Image.ASLEEP)

while True:
    # À FAIRE 2 : Si les boutons A ET B sont pressés ensemble (à mettre en premier !)
    if button_a.is_pressed() and button_b.is_pressed():
        # Affiche le nombre d'intrusions
        display.scroll("Alertes:")
        display.scroll(intrusions)
        sleep(1000)
        
    elif button_a.is_pressed():
        # (Armement)
        ...
        
    elif button_b.is_pressed():
        # (Désarmement)
        ...
        
    elif armee == True and accelerometer.was_gesture('shake'):
        alerte_declenchee = True
        # À FAIRE 3 : Augmenter 'intrusions' de 1 (ex: intrusions = intrusions + 1)
        ...
        
    # Effet gyrophare
    if alerte_declenchee == True:
        display.show(Image.CHESSBOARD)
        sleep(200)
        display.clear()
        sleep(200)
```

*Testez le programme complet :* Secouez plusieurs fois pendant que l'alarme est armée (arrêtez l'alerte avec B entre chaque test). Appuyez ensuite sur A et B en même temps pour lire le score !

---

## 🏆 Défis Bonus pour améliorer votre alarme

### Défi 1 : Alarme sensible à la lumière 💡

Si un voleur ouvre la fermeture éclair de votre sac, de la lumière va y entrer.
En utilisant le capteur de lumière `display.read_light_level()` (qui renvoie une valeur entre `0` (nuit totale) et `255` (pleine lumière)), faites en sorte que si l'alarme est armée et que la lumière dépasse `50`, l'alarme se déclenche également.

### Défi 2 : Code de désarmement secret 🔐

Actuellement, n'importe qui peut éteindre l'alarme en appuyant simplement sur le bouton B. C'est trop facile !
Modifiez le programme pour qu'après avoir appuyé sur B, l'utilisateur doive appuyer sur le bouton A dans les 2 secondes pour valider l'arrêt. Si ce n'est pas fait, l'alarme reste active !

### Défi 3 : Sirène sonore 🔊

Si votre carte Micro:bit possède un haut-parleur (comme sur la version V2), importez la bibliothèque `music` au début de votre code (`import music`).
Faites retentir un son strident (comme `music.SIREN` ou `music.BA_DING`) en même temps que le clignotement visuel.
