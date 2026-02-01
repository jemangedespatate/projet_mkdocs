from turtle import *
import turtle

# ==========================================
# 🛠️ OUTILS (Ne pas modifier cette partie)
# ==========================================

def initialiser_tortue():
    speed(0) # Vitesse maximale
    hideturtle()
    title("TP Remédiation : Pixel Art")
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
# 🚀 ACTIVITÉS À COMPLÉTER
# ==========================================

def activite_1():
    print("--- Activité 1 : Un simple Pixel ---")
    # Objectif : Dessiner un pixel rouge aux coordonnées (0, 0)
    # Aide : Utilise la fonction dessiner_pixel(x, y, couleur)
    # Exemple : dessiner_pixel(12, 24, "blue")
    
    # 👇 A COMPLÉTER CI-DESSOUS 👇
    
    pass 

def activite_2():
    print("--- Activité 2 : Une ligne de Pixels ---")
    # Objectif : Dessiner une ligne de 10 pixels bleus.
    # Les coordonnées seront : (0,0), (30,0), (60,0)...
    # Aide : Utilise une boucle 'for i in range(...):'
    
    # 👇 A COMPLÉTER CI-DESSOUS 👇

    pass 

def activite_3():
    print("--- Activité 3 : Le Carré (Boucles Imbriquées) ---")
    # Objectif : Dessiner un carré de 5x5 pixels verts.
    # C'est comme une image ! Il y a des lignes et des colonnes.
    
    # 👇 A COMPLÉTER CI-DESSOUS 👇
    
    pass

def activite_4():
    print("--- Activité 4 : Le Damier (Conditions) ---")
    # Objectif : Dessiner un damier 8x8.
    # Si la somme (x_index + y_index) est paire -> Noir, sinon -> Blanc
    
    taille_grille = 8
    
    # 👇 A COMPLÉTER CI-DESSOUS 👇
    
    pass

# ==========================================
# 🎮 MENU PRINCIPAL
# ==========================================

def menu():
    while True:
        print("\n" + "="*30)
        print("   MENU TP PIXEL ART")
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
