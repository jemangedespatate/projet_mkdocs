# TP : Création du jeu Flappy Bird avec Tkinter

## Objectif
Dans ce TP, nous allons créer un jeu de **Flappy Bird** en Python avec la bibliothèque graphique `tkinter`. 

Pour commencer, nous n'utiliserons pas d'images externes. Nous allons dessiner nos éléments (l'oiseau, le sol, les tuyaux) directement à l'aide de **formes géométriques** (des rectangles et des cercles/ovales) programmées en Python !

À chaque étape, **copiez le code complet**, remplacez le contenu de votre fichier `flappy.py` et exécutez-le pour voir l'évolution.

---

## Étape 1 : La fenêtre de jeu et le ciel (Canvas)

Toute interface graphique a besoin d'une fenêtre principale. Nous allons y ajouter un `Canvas` (toile) avec une couleur de fond bleu ciel (`bg="sky blue"`).

**Copiez tout le code suivant dans votre fichier `flappy.py` et lancez-le :**

```python
from tkinter import *

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Flappy Bird SNT")

# Création de la zone de dessin (largeur 600px, hauteur 500px, fond bleu ciel)
canvas = Canvas(fenetre, width=600, height=500, bg="sky blue")
canvas.pack()

# Lancement de l'interface (doit toujours être à la fin du fichier)
fenetre.mainloop()
```

**Observation :** Une fenêtre avec un fond bleu ciel apparaît. C'est notre ciel !

---

## Étape 2 : Dessiner le sol et l'oiseau

Nous allons utiliser `create_rectangle` pour dessiner un rectangle vert représentant le sol, et `create_oval` pour dessiner un cercle jaune représentant notre oiseau.

**Remplacez tout le contenu de `flappy.py` par ce code et exécutez-le :**

```python
from tkinter import *

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Flappy Bird SNT")

# Zone de dessin
canvas = Canvas(fenetre, width=600, height=500, bg="sky blue")
canvas.pack()

# --- NOUVEAUTÉ ÉTAPE 2 ---
# Création du sol (un rectangle vert tout en bas)
sol = canvas.create_rectangle(0, 450, 600, 500, fill="forest green")

# Création de l'oiseau (un rond jaune : x1, y1, x2, y2)
oiseau = canvas.create_oval(100, 200, 130, 230, fill="yellow")
# -------------------------

# Lancement de l'interface
fenetre.mainloop()
```

**Observation :** Un sol vert apparaît en bas et un petit rond jaune (notre oiseau) s'affiche au milieu de l'écran.

---

## Étape 3 : Interaction au clavier (Faire sauter l'oiseau)

Pour que notre oiseau puisse voler, nous devons gérer sa vitesse verticale (`vitesse_y`). Lorsque l'on appuiera sur la barre **Espace**, on lui donnera une vitesse vers le haut (négative en Python, car le haut de l'écran correspond à $y = 0$).

**Remplacez tout le contenu de `flappy.py` par ce code et exécutez-le :**

```python
from tkinter import *

# Variables globales de jeu
vitesse_y = 0
jeu_actif = True

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Flappy Bird SNT")

# Zone de dessin
canvas = Canvas(fenetre, width=600, height=500, bg="sky blue")
canvas.pack()

# Création des éléments graphiques
sol = canvas.create_rectangle(0, 450, 600, 500, fill="forest green")
oiseau = canvas.create_oval(100, 200, 130, 230, fill="yellow")

# --- NOUVEAUTÉ ÉTAPE 3 ---
def clavier(event):
    global vitesse_y
    # Si on appuie sur la barre d'espace, on donne une impulsion vers le haut
    if event.keysym == "space" and jeu_actif:
        vitesse_y = -8  

# Associe l'appui de n'importe quelle touche à notre fonction 'clavier'
fenetre.bind("<Key>", clavier)
# -------------------------

# Lancement de l'interface
fenetre.mainloop()
```

**Observation :** Rien ne bouge encore ! C'est normal, il nous manque l'animation pour appliquer cette vitesse à chaque instant.

---

## Étape 4 : L'animation et la gravité

Nous allons créer une fonction `boucle()` qui s'exécutera toutes les 20 millisecondes (grâce à `.after()`). Cette fonction va simuler la gravité en augmentant la vitesse de chute de l'oiseau à chaque instant, puis déplacer l'oiseau. Elle vérifiera aussi s'il touche le sol ou le plafond.

**Remplacez tout le contenu de `flappy.py` par ce code et exécutez-le :**

```python
from tkinter import *

# Variables globales de jeu
vitesse_y = 0
jeu_actif = True

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Flappy Bird SNT")

# Zone de dessin
canvas = Canvas(fenetre, width=600, height=500, bg="sky blue")
canvas.pack()

# Création des éléments graphiques
sol = canvas.create_rectangle(0, 450, 600, 500, fill="forest green")
oiseau = canvas.create_oval(100, 200, 130, 230, fill="yellow")

def clavier(event):
    global vitesse_y
    if event.keysym == "space" and jeu_actif:
        vitesse_y = -8  

fenetre.bind("<Key>", clavier)

# --- NOUVEAUTÉ ÉTAPE 4 ---
def boucle():
    global vitesse_y, jeu_actif
    
    if not jeu_actif:
        return

    # 1. Physique de l'oiseau (gravité)
    vitesse_y += 0.5  # La gravité tire l'oiseau vers le bas
    canvas.move(oiseau, 0, vitesse_y) # Déplacement vertical
    
    # On récupère la position actuelle de l'oiseau [x_gauche, y_haut, x_droite, y_bas]
    c_oiseau = canvas.coords(oiseau)
    
    # 2. Conditions de défaite (touche le sol ou sort par le haut)
    if c_oiseau[3] >= 450 or c_oiseau[1] <= 0:
        jeu_actif = False
        canvas.create_text(300, 250, text="GAME OVER", fill="red", font=("Arial", 30, "bold"))
        return
        
    # Relance de la boucle dans 20 millisecondes (50 FPS)
    fenetre.after(20, boucle)

# Lancement de la boucle d'animation
boucle()
# -------------------------

# Lancement de l'interface
fenetre.mainloop()
```

**Observation :** Testez le jeu ! L'oiseau tombe. Si vous appuyez sur **Espace**, il saute ! S'il touche le sol vert ou le haut de la fenêtre, le texte "GAME OVER" rouge s'affiche et le jeu s'arrête.

---

## Étape 5 : Ajouter les obstacles (les Tuyaux)

Un jeu Flappy Bird nécessite des obstacles à esquiver. Nous allons dessiner deux rectangles verts (un tuyau en haut, un tuyau en bas) qui vont avancer vers la gauche. Quand ils sortent de l'écran, ils réapparaissent à droite avec une hauteur aléatoire.

**Remplacez tout le contenu de `flappy.py` par ce code et exécutez-le :**

```python
from tkinter import *
# --- NOUVEAUTÉ ÉTAPE 5 ---
import random
# -------------------------

# Variables globales de jeu
vitesse_y = 0
jeu_actif = True

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Flappy Bird SNT")

# Zone de dessin
canvas = Canvas(fenetre, width=600, height=500, bg="sky blue")
canvas.pack()

# Création des éléments graphiques
sol = canvas.create_rectangle(0, 450, 600, 500, fill="forest green")
oiseau = canvas.create_oval(100, 200, 130, 230, fill="yellow")

# --- NOUVEAUTÉ ÉTAPE 5 ---
# Dimensions et position initiale des tuyaux
largeur_tuyau = 60
espace_tuyaux = 130
x_tuyau = 600
hauteur_haut = random.randint(50, 300)

# Création des deux rectangles pour le tuyau du haut et le tuyau du bas
tuyau_haut = canvas.create_rectangle(x_tuyau, 0, x_tuyau + largeur_tuyau, hauteur_haut, fill="green")
tuyau_bas = canvas.create_rectangle(x_tuyau, hauteur_haut + espace_tuyaux, x_tuyau + largeur_tuyau, 450, fill="green")
# -------------------------

def clavier(event):
    global vitesse_y
    if event.keysym == "space" and jeu_actif:
        vitesse_y = -8  

fenetre.bind("<Key>", clavier)

# --- NOUVEAUTÉ ÉTAPE 5 (Modification de la boucle) ---
def boucle():
    global vitesse_y, x_tuyau, hauteur_haut, jeu_actif
    
    if not jeu_actif:
        return

    # 1. Physique de l'oiseau (gravité)
    vitesse_y += 0.5
    canvas.move(oiseau, 0, vitesse_y)
    c_oiseau = canvas.coords(oiseau)
    
    # 2. Déplacement des tuyaux de 4 pixels vers la gauche
    canvas.move(tuyau_haut, -4, 0)
    canvas.move(tuyau_bas, -4, 0)
    
    # Si le tuyau sort complètement à gauche de la fenêtre
    coords_tuyau = canvas.coords(tuyau_haut)
    if coords_tuyau[2] < 0:
        # On le remet à droite
        x_tuyau = 600
        # On choisit une nouvelle hauteur de passage aléatoire
        hauteur_haut = random.randint(50, 300)
        # On met à jour les positions des tuyaux
        canvas.coords(tuyau_haut, x_tuyau, 0, x_tuyau + largeur_tuyau, hauteur_haut)
        canvas.coords(tuyau_bas, x_tuyau, hauteur_haut + espace_tuyaux, x_tuyau + largeur_tuyau, 450)
        
    # 3. Conditions de défaite (sol ou plafond)
    if c_oiseau[3] >= 450 or c_oiseau[1] <= 0:
        jeu_actif = False
        canvas.create_text(300, 250, text="GAME OVER", fill="red", font=("Arial", 30, "bold"))
        return
        
    fenetre.after(20, boucle)
# -----------------------------------------------------

# Lancement de la boucle d'animation
boucle()

# Lancement de l'interface
fenetre.mainloop()
```

**Observation :** Les tuyaux défilent de droite à gauche et changent de taille à chaque passage. Mais pour le moment, l'oiseau passe au travers sans perdre !

---

## Étape 6 : Gérer les collisions avec les tuyaux et afficher le score

Pour finaliser notre jeu, nous allons implémenter :
1. Une fonction `collision(obj1, obj2)` qui détecte si le rectangle imaginaire entourant l'oiseau chevauche l'un des tuyaux.
2. Un affichage du score au centre de l'écran qui augmente de 1 à chaque fois qu'un tuyau est esquivé avec succès.

Voici le **code final complet** du jeu !

**Remplacez tout le contenu de `flappy.py` par ce code et jouez :**

```python
from tkinter import *
import random

# Variables globales de jeu
score = 0
vitesse_y = 0
jeu_actif = True

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Flappy Bird SNT")

# Création de la zone de dessin (largeur 600px, hauteur 500px, fond bleu ciel)
canvas = Canvas(fenetre, width=600, height=500, bg="sky blue")
canvas.pack()

# Création du sol (un rectangle vert tout en bas)
sol = canvas.create_rectangle(0, 450, 600, 500, fill="forest green")

# Création de l'oiseau (un rond jaune)
oiseau = canvas.create_oval(100, 200, 130, 230, fill="yellow")

# Dimensions des tuyaux
largeur_tuyau = 60
espace_tuyaux = 130
x_tuyau = 600
hauteur_haut = random.randint(50, 300)

# Création des deux rectangles pour le tuyau du haut et du bas
tuyau_haut = canvas.create_rectangle(x_tuyau, 0, x_tuyau + largeur_tuyau, hauteur_haut, fill="green")
tuyau_bas = canvas.create_rectangle(x_tuyau, hauteur_haut + espace_tuyaux, x_tuyau + largeur_tuyau, 450, fill="green")

# Affichage du score
texte_score = canvas.create_text(300, 50, text="Score : 0", fill="white", font=("Arial", 24, "bold"))

def clavier(event):
    global vitesse_y
    # Si on appuie sur la barre d'espace
    if event.keysym == "space" and jeu_actif:
        vitesse_y = -8  # Impulsion vers le haut

# Liaison du clavier à la fenêtre
fenetre.bind("<Key>", clavier)

# --- NOUVEAUTÉ ÉTAPE 6 ---
def collision(obj1, obj2):
    """Détecte si deux objets se touchent sur le Canvas"""
    c1 = canvas.coords(obj1)
    c2 = canvas.coords(obj2)
    if not c1 or not c2:
        return False
    # Renvoie True si les deux rectangles de collision se superposent
    return not (c1[2] < c2[0] or c1[0] > c2[2] or c1[3] < c2[1] or c1[1] > c2[3])
# -------------------------

def boucle():
    global vitesse_y, x_tuyau, hauteur_haut, score, jeu_actif
    
    if not jeu_actif:
        return

    # 1. Physique de l'oiseau (gravité)
    vitesse_y += 0.5
    canvas.move(oiseau, 0, vitesse_y)
    c_oiseau = canvas.coords(oiseau)
    
    # 2. Déplacement des tuyaux
    canvas.move(tuyau_haut, -4, 0)
    canvas.move(tuyau_bas, -4, 0)
    
    coords_tuyau = canvas.coords(tuyau_haut)
    if coords_tuyau[2] < 0:
        x_tuyau = 600
        hauteur_haut = random.randint(50, 300)
        canvas.coords(tuyau_haut, x_tuyau, 0, x_tuyau + largeur_tuyau, hauteur_haut)
        canvas.coords(tuyau_bas, x_tuyau, hauteur_haut + espace_tuyaux, x_tuyau + largeur_tuyau, 450)
        
        # --- NOUVEAUTÉ ÉTAPE 6 ---
        # +1 point quand le tuyau est passé
        score += 1
        canvas.itemconfig(texte_score, text="Score : " + str(score))
        # -------------------------

    # 3. Vérification des collisions (sol, plafond, ou l'un des tuyaux)
    # --- NOUVEAUTÉ ÉTAPE 6 (Ajout des collisions tuyaux) ---
    if c_oiseau[3] >= 450 or c_oiseau[1] <= 0 or collision(oiseau, tuyau_haut) or collision(oiseau, tuyau_bas):
        jeu_actif = False
        canvas.create_text(300, 250, text="GAME OVER", fill="red", font=("Arial", 30, "bold"))
        return
    # --------------------------------------------------------
        
    fenetre.after(20, boucle)

# Lancement de la boucle d'animation
boucle()

# Lancement de l'interface
fenetre.mainloop()
```

**Félicitations !** Vous avez créé votre premier jeu graphique en Python. 
Prenez les commandes de votre oiseau jaune et tentez de réaliser le meilleur score possible !
