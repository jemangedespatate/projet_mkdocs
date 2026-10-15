from tkinter import *


balle = None

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Space Invaders NSI")

# Création de la zone de dessin (largeur 800px, hauteur 600px)
canvas = Canvas(fenetre, width=800, height=600)
canvas.pack()

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


# Outil pour récupérer le centre (x, y) d'un objet
def centre(obj):
    c = canvas.coords(obj)
    if len(c) == 2: # c'est une image (x, y)
        return c[0], c[1]
    else:           # c'est un rectangle (x1, y1, x2, y2)
        return (c[0] + c[2]) / 2, (c[1] + c[3]) / 2

def clavier(event):
    """Gère les actions du joueur au clavier"""
    
    global balle
    
    # On récupère les coordonnées actuelles du vaisseau
    x, y = canvas.coords(joueur)
    
    # Si on appuie sur la flèche de gauche
    if event.keysym == "Left":
        canvas.move(joueur, -20, 0) # Déplace de -20 en x et 0 en y
        
    # Si on appuie sur la flèche de droite
    if event.keysym == "Right":
        canvas.move(joueur, 20, 0)
        
    if event.keysym == "space":
        if balle is None: # On s'assure qu'il n'y a qu'une balle à la fois
            x, y = centre(joueur)
            balle = canvas.create_rectangle(
                x - 3, y - 20,
                x + 3, y - 10,
                fill="yellow"
            )

# On associe l'appui d'une touche (<Key>) sur la fenêtre à notre fonction 'clavier'
fenetre.bind("<Key>", clavier)

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

# Lancement de l'interface (doit TOUJOURS être à la fin du fichier)
fenetre.mainloop()
