from turtle import *
import turtle

# ==========================================
# 🛠️ OUTILS (Ne pas modifier cette partie)
# ==========================================

def initialiser_tortue():
    speed(0) # Vitesse maximale
    hideturtle()
    title("TP Remédiation : Pixel Art (CORRECTION PROF)")
    bgcolor("#f0f0f0") # Gris très clair pour le fond

def aller_a(x, y):
    penup()
    goto(x, y)
    pendown()

def dessiner_pixel(x, y, couleur, taille=30):
    """
    Dessine un carré (pixel) à la position (x,y) de la couleur donnée.
    """
    aller_a(x, y)
    color("black", couleur) # Contour noir, remplissage 'couleur'
    begin_fill()
    for _ in range(4):
        forward(taille)
        left(90)
    end_fill()

# ==========================================
# 🚀 CORRECTION DES ACTIVITÉS
# ==========================================

def activite_1():
    print("--- Activité 1 : Un simple Pixel ---")
    # CORRECTION
    dessiner_pixel(0, 0, "red")       # Le premier pixel demandé
    dessiner_pixel(30, 0, "blue")     # Le défi supplémentaire

def activite_2():
    print("--- Activité 2 : Une ligne de Pixels ---")
    # CORRECTION
    for i in range(10):
        x = i * 30
        y = 0
        dessiner_pixel(x, y, "blue")

def activite_3():
    print("--- Activité 3 : Le Carré (Boucles Imbriquées) ---")
    # CORRECTION
    for y_index in range(5):
        # Pour descendre visuellement comme une image (le (0,0) est souvent en haut à gauche en info),
        # on peut utiliser -y_index. Ici on garde le positif pour simplifier l'axe Y mathématique.
        y = y_index * 30 
        
        for x_index in range(5):
            x = x_index * 30
            dessiner_pixel(x, y, "green")

def activite_4():
    print("--- Activité 4 : Le Damier (Conditions) ---")
    # CORRECTION
    taille_grille = 8
    
    for y_index in range(taille_grille):
        y = y_index * 30
        for x_index in range(taille_grille):
            x = x_index * 30
            
            # Somme des indices pour déterminer la parité
            if (x_index + y_index) % 2 == 0:
                couleur = "black"
            else:
                couleur = "white"
            
            dessiner_pixel(x, y, couleur)

# ==========================================
# 🎮 MENU PRINCIPAL
# ==========================================

def menu():
    while True:
        print("\n" + "="*30)
        print("   MENU TP PIXEL ART (CORRECTION)")
        print("="*30)
        print("1. Activité 1 : Un simple Pixel")
        print("2. Activité 2 : Une ligne (Boucle)")
        print("3. Activité 3 : Un carré (Double Boucle)")
        print("4. Activité 4 : Le Damier (Conditions)")
        print("0. Quitter")
        
        choix = input("\nVotre choix : ")
        
        reset() 
        initialiser_tortue()
        
        if choix == '1':
            activite_1()
        elif choix == '2':
            activite_2()
        elif choix == '3':
            activite_3()
        elif choix == '4':
            activite_4()
        elif choix == '0':
            print("Au revoir !")
            bye()
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    initialiser_tortue()
    menu()
