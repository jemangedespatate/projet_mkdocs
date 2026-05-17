# ---------------------------------------------------------
# 🛠️ GESTIONNAIRE D'IMAGE (NE PAS MODIFIER CETTE PARTIE)
# ---------------------------------------------------------

_largeur = 0
_hauteur = 0
_pixels = []

def creer_image(largeur, hauteur):
    """Crée une nouvelle image toute blanche."""
    global _largeur, _hauteur, _pixels
    _largeur = largeur
    _hauteur = hauteur
    # On crée une liste simple pour stocker tous les points
    _pixels = [0] * (largeur * hauteur)
    print(f"✅ Image créée : {largeur}x{hauteur} pixels")

def colorier_pixel(x, y, couleur):
    """
    Change la couleur d'un pixel.
    x : colonne (de 0 à largeur-1)
    y : ligne (de 0 à hauteur-1)
    couleur : 0 (Blanc) ou 1 (Noir)
    """
    if 0 <= x < _largeur and 0 <= y < _hauteur:
        index = y * _largeur + x
        _pixels[index] = couleur
    else:
        print(f"⚠️ Attention : Le pixel ({x},{y}) est hors de l'image !")

def lire_pixel(x, y):
    """Renvoie la couleur du pixel (0 ou 1) aux coordonnées x, y."""
    if 0 <= x < _largeur and 0 <= y < _hauteur:
        index = y * _largeur + x
        return _pixels[index]
    return 0

def afficher_image():
    """Affiche l'image dans la console."""
    print("\n--- VOTRE IMAGE ---")
    print("-" * (_largeur * 2 + 2))
    for y in range(_hauteur):
        ligne = "|"
        for x in range(_largeur):
            val = lire_pixel(x, y)
            if val == 1:
                ligne += "██" # Noir
            else:
                ligne += "  " # Blanc
        ligne += "|"
        print(ligne)
    print("-" * (_largeur * 2 + 2))
    print("-------------------\n")

def sauvegarder_image(nom_fichier):
    """Sauvegarde l'image au format PBM."""
    if not nom_fichier.endswith(".pbm"):
        nom_fichier += ".pbm"
        
    with open(nom_fichier, 'w') as f:
        f.write("P1\n")
        f.write(f"{_largeur} {_hauteur}\n")
        # Écriture simple ligne par ligne
        for y in range(_hauteur):
            ligne_str = ""
            for x in range(_largeur):
                val = lire_pixel(x, y)
                ligne_str += str(val) + " "
            f.write(ligne_str + "\n")
    print(f"💾 Image sauvegardée dans le fichier '{nom_fichier}'")


# =========================================================
# ✍️ ZONE ÉLÈVE : C'EST ICI QUE VOUS ÉCRIVEZ VOTRE CODE
# =========================================================

# 1. Je crée une image de 5 pixels de large sur 5 de haut
creer_image(5, 5)

# 2. Je dessine des points noirs (1) aux positions voulues
# Rappel : (0,0) est en haut à gauche
colorier_pixel(2, 2, 1) # Un point au milieu
colorier_pixel(0, 0, 1) # Coin haut gauche
colorier_pixel(4, 4, 1) # Coin bas droite

# 3. J'affiche le résultat
afficher_image()

# 4. Je sauvegarde
sauvegarder_image("mon_dessin.pbm")


# --- EXERCICE : LE NÉGATIF ---
# Pour faire le négatif, on doit parcourir tous les pixels.
# Complétez le code ci-dessous :

# print("Calcul du négatif...")
#
# for y in range(5):          # Pour chaque ligne...
#     for x in range(5):      # Pour chaque colonne...
#         
#         couleur_actuelle = lire_pixel(x, y)
#         
#         # SI c'est blanc (0), on met noir (1)
#         # SINON, on met blanc (0)
#         
#         # ... À COMPLÉTER ICI ...
# 
# afficher_image() # On regarde le résultat
