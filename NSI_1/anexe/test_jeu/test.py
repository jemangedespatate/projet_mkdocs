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