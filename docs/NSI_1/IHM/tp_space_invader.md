# TP : Découverte des Interfaces Graphiques avec Tkinter (Space Invader)

## Objectif
Dans ce TP, nous allons découvrir comment créer une Interface Homme-Machine (IHM) en Python à l'aide de la bibliothèque `tkinter`. Pour rendre cela plus concret, nous allons reconstruire étape par étape un jeu de *Space Invader*. 

À chaque étape, vous devrez exécuter le code pour observer l'évolution de la fenêtre graphique.

> **Préparation :**
> Créez un dossier `Space_Invader` sur votre ordinateur. 
> Récupérez les 3 images nécessaires ([background.png](background.png){:download="background.png"}, [player.png](player.png){:download="player.png"}, [enemy.png](enemy.png){:download="enemy.png"}) (que vous pouvez demander à votre professeur ou trouver dans les ressources) et placez-les dans ce dossier. Créez ensuite un fichier `jeu.py` dans le même dossier.
---

## Étape 1 : La Fenêtre et la zone de dessin (Canvas)

Toute interface graphique nécessite une fenêtre principale. Avec Tkinter, nous utilisons aussi un `Canvas` (toile), qui est une zone où l'on peut dessiner des formes ou afficher des images.

**Copiez et exécutez le code suivant dans `jeu.py` :**

```python
from tkinter import *

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Space Invaders NSI")

# Création de la zone de dessin (largeur 800px, hauteur 600px)
canvas = Canvas(fenetre, width=800, height=600)
canvas.pack()

# Lancement de l'interface (doit TOUJOURS être à la fin du fichier)
fenetre.mainloop()
```

**Observation :** Une fenêtre vide de 800x600 pixels apparaît. 

---

## Étape 2 : Ajouter des images (Fond et Joueur)

Maintenant, nous allons ajouter des images (les "sprites") dans notre zone de dessin. Dans Tkinter, on charge l'image avec `PhotoImage`, puis on l'affiche avec `create_image`.

**Modifiez votre code en ajoutant les éléments suivants (juste avant `fenetre.mainloop()`) :**

```python
# Chargement des images en mémoire
fond_img = PhotoImage(file="background.png")
player_img = PhotoImage(file="player.png")

# IMPORTANT : Il faut stocker les images dans une liste pour éviter qu'elles 
# ne soient effacées par le "ramasse-miette" (Garbage Collector) de Python
images = [fond_img, player_img]

# Affichage du fond au centre (x=400, y=300)
canvas.create_image(400, 300, image=fond_img)

# Affichage du joueur en bas au centre
joueur = canvas.create_image(400, 520, image=player_img)
```

**Observation :** Lancez le jeu. Vous devriez voir le fond d'écran et le vaisseau du joueur.

---

## Étape 3 : Interaction - Déplacement au clavier

Une interface doit réagir aux actions de l'utilisateur (événements). Nous allons lier les flèches du clavier au déplacement du vaisseau.

**Ajoutez la fonction de contrôle et la liaison (bind) :**

```python
def clavier(event):
    """Gère les actions du joueur au clavier"""
    
    # On récupère les coordonnées actuelles du vaisseau
    x, y = canvas.coords(joueur)
    
    # Si on appuie sur la flèche de gauche
    if event.keysym == "Left":
        canvas.move(joueur, -20, 0) # Déplace de -20 en x et 0 en y
        
    # Si on appuie sur la flèche de droite
    if event.keysym == "Right":
        canvas.move(joueur, 20, 0)

# On associe l'appui d'une touche (<Key>) sur la fenêtre à notre fonction 'clavier'
fenetre.bind("<Key>", clavier)
```

**Observation :** Lancez et testez. Le vaisseau doit se déplacer de gauche à droite lorsque vous appuyez sur les flèches.

---

## Étape 4 : Les ennemis et les formes géométriques

Nous allons générer plusieurs ennemis grâce à une double boucle `for`. Nous en profiterons pour ajouter le texte du score.

```python
# Chargement de l'image ennemie
enemy_img = PhotoImage(file="enemy.png")
images.append(enemy_img) # On la garde en mémoire dans notre liste

ennemis = []

# Création du texte pour le score en haut à gauche
texte_score = canvas.create_text(80, 30, text="Score : 0", fill="white", font=("Arial", 20))

# Création des ennemis (3 lignes de 8 ennemis)
for ligne in range(3):
    for colonne in range(8):
        x = 80 + colonne * 80
        y = 80 + ligne * 60
        # Affichage d'un ennemi
        ennemi = canvas.create_image(x, y, image=enemy_img)
        # On ajoute l'objet créé à notre liste pour s'en souvenir plus tard
        ennemis.append(ennemi) 
```

**Observation :** Les aliens apparaissent alignés en haut de l'écran. Le score est visible.

---

## Étape 5 : Le tir (Action spatiale)

Lorsque l'on appuie sur *Espace*, un tir doit se créer. Contrairement aux images, le tir sera un simple rectangle dessiné avec `create_rectangle`.

**Modifiez votre fonction `clavier` (de l'étape 3) et ajoutez cette fonction utile :**

```python
# Ajoutez cette variable globale tout en haut de votre code (sous les imports)
balle = None 

# Outil pour récupérer le centre (x, y) d'un objet
def centre(obj):
    c = canvas.coords(obj)
    if len(c) == 2: # c'est une image (x, y)
        return c[0], c[1]
    else:           # c'est un rectangle (x1, y1, x2, y2)
        return (c[0] + c[2]) / 2, (c[1] + c[3]) / 2

# ... Modifiez la fonction clavier(event) existante pour y inclure le tir ...
def clavier(event):
    global balle
    
    # ... (le code du déplacement reste ici) ...
    
    if event.keysym == "space":
        if balle is None: # On s'assure qu'il n'y a qu'une balle à la fois
            x, y = centre(joueur)
            balle = canvas.create_rectangle(
                x - 3, y - 20,
                x + 3, y - 10,
                fill="yellow"
            )
```

**Observation :** En appuyant sur Espace, un petit rectangle jaune apparaît juste au-dessus du vaisseau. Mais elle ne bouge pas encore car il n'y a pas d'animation !

---

## Étape 6 : L'Animation et la boucle de jeu

Pour qu'un jeu "vive", il faut qu'il s'actualise régulièrement. En Tkinter, on utilise la méthode `after(delai_ms, fonction)` pour créer une boucle qui s'exécute en continu.

**Ajoutez la gestion de collision et la boucle d'animation :**

```python
score = 0

def collision(obj1, obj2):
    """Vérifie si deux objets se touchent (approximation mathématique basique)"""
    x1, y1 = centre(obj1)
    x2, y2 = centre(obj2)
    return abs(x1 - x2) < 30 and abs(y1 - y2) < 30

def boucle():
    """Fonction principale d'animation (Game Loop)"""
    global balle, score
    
    # ----- 1. Déplacement et gestion de la balle -----
    if balle is not None:
        canvas.move(balle, 0, -15) # Déplace la balle de 15px vers le haut
        
        # On récupère la position du rectangle (x1, y1, x2, y2)
        x1, y1, x2, y2 = canvas.coords(balle)
        
        # Si la balle sort de l'écran par le haut
        if y2 < 0:
            canvas.delete(balle) # On la supprime visuellement
            balle = None         # On l'enlève de la variable
            
        else:
            # ----- 2. Gestion des collisions avec chaque ennemi -----
            for ennemi in ennemis:
                if collision(balle, ennemi):
                    canvas.delete(ennemi)   # Efface l'image de l'ennemi
                    ennemis.remove(ennemi)  # Le retire de notre liste
                    
                    canvas.delete(balle)    # Efface la balle
                    balle = None
                    
                    # Augmente le score et met à jour l'affichage
                    score += 10
                    canvas.itemconfig(texte_score, text="Score : " + str(score))
                    break # On arrête la boucle for car la balle est détruite
    
    # ----- 3. Condition de victoire -----
    if len(ennemis) == 0:
        canvas.create_text(400, 300, text="VICTOIRE", fill="white", font=("Arial", 40))
        return # Arrête la boucle d'animation (ne fait pas de after)

    # ----- 4. Relance de la boucle -----
    # On rappelle la fonction boucle() dans 20 millisecondes
    fenetre.after(20, boucle)

# On lance la boucle une première fois juste AVANT 'fenetre.mainloop()'
boucle()
```

**Félicitations !** Vous venez de reconstituer votre propre jeu Space Invader.
Lancez le jeu, déplacez-vous avec les flèches, tirez avec espace et détruisez tous les extra-terrestres !
