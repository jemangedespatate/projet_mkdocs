from tkinter import *

# =========================
# FENÊTRE
# =========================

fenetre = Tk()
fenetre.title("Space Invaders NSI")

canvas = Canvas(fenetre, width=800, height=600)
canvas.pack()

# =========================
# SPRITES
# =========================

fond_img = PhotoImage(file="background.png")
player_img = PhotoImage(file="player.png")
enemy_img = PhotoImage(file="enemy.png")

# IMPORTANT : garder les images
images = [fond_img, player_img, enemy_img]

# =========================
# FOND
# =========================

canvas.create_image(400, 300, image=fond_img)

# =========================
# JOUEUR
# =========================

joueur = canvas.create_image(400, 520, image=player_img)

# =========================
# VARIABLES
# =========================

balle = None
score = 0
ennemis = []

# =========================
# SCORE
# =========================

texte_score = canvas.create_text(
    80, 30,
    text="Score : 0",
    fill="white",
    font=("Arial", 20)
)

# =========================
# ENNEMIS
# =========================

for ligne in range(3):
    for colonne in range(8):

        x = 80 + colonne * 80
        y = 80 + ligne * 60

        ennemi = canvas.create_image(x, y, image=enemy_img)
        ennemis.append(ennemi)

# =========================
# OUTIL : CENTRE D'UN OBJET
# =========================

def centre(obj):
    """
    Retourne le centre d’un objet canvas
    - image → (x, y)
    - rectangle → calcule le centre
    """

    c = canvas.coords(obj)

    if len(c) == 2:
        return c[0], c[1]
    else:
        return (c[0] + c[2]) / 2, (c[1] + c[3]) / 2

# =========================
# COLLISION SIMPLE
# =========================

def collision(obj1, obj2):
    """
    Collision basée sur la distance entre centres
    """

    x1, y1 = centre(obj1)
    x2, y2 = centre(obj2)

    return abs(x1 - x2) < 30 and abs(y1 - y2) < 30

# =========================
# CLAVIER
# =========================

def clavier(event):
    """
    Déplacement joueur + tir
    """

    global balle

    x, y = centre(joueur)

    if event.keysym == "Left":
        canvas.move(joueur, -20, 0)

    if event.keysym == "Right":
        canvas.move(joueur, 20, 0)

    if event.keysym == "space":

        if balle is None:

            balle = canvas.create_rectangle(
                x - 3, y - 20,
                x + 3, y - 10,
                fill="yellow"
            )

# =========================
# BOUCLE DE JEU
# =========================

def boucle():
    """
    Mise à jour du jeu
    """

    global balle, score

    # ---------------- balle ----------------
    if balle is not None:

        canvas.move(balle, 0, -15)

        x1, y1, x2, y2 = canvas.coords(balle)

        # sortie écran
        if y2 < 0:
            canvas.delete(balle)
            balle = None

        else:
            # collision ennemis
            for ennemi in ennemis:

                if collision(balle, ennemi):

                    canvas.delete(ennemi)
                    ennemis.remove(ennemi)

                    canvas.delete(balle)
                    balle = None

                    score += 10

                    canvas.itemconfig(
                        texte_score,
                        text="Score : " + str(score)
                    )

                    break

    # ---------------- victoire ----------------
    if len(ennemis) == 0:

        canvas.create_text(
            400, 300,
            text="VICTOIRE",
            fill="white",
            font=("Arial", 40)
        )
        return

    fenetre.after(20, boucle)

# =========================
# CONTROLES + LANCEMENT
# =========================

fenetre.bind("<Key>", clavier)

boucle()
fenetre.mainloop()