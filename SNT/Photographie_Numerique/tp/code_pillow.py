"""
💻 Travaux Pratiques : Traitement d'Image avec Python
======================================================

Ce fichier contient les exercices du TP sur le traitement d'images.
Complétez les parties marquées par "???" ou "# A COMPLETER".

Assurez-vous que le fichier image_tp.jpg est dans le même dossier que ce script.
"""

from PIL import Image


# ============================================================================
# ACTIVITÉ 1 : Ouvrir et Analyser une image
# ============================================================================

def activite_1():
    """
    Ouvre une image et affiche ses informations de base.
    """
    print("\n" + "="*60)
    print("ACTIVITÉ 1 : Ouvrir et Analyser une image")
    print("="*60)
    
    # 1. Ouverture du fichier image
    img = Image.open("image_tp.jpg")
    
    # 2. Récupération des dimensions
    largeur, hauteur = img.size
    print(f"L'image fait {largeur} pixels de large et {hauteur} pixels de haut.")
    print(f"Définition totale : {largeur * hauteur} pixels.")
    
    # 3. Analyse du pixel central
    x = largeur // 2
    y = hauteur // 2
    r, v, b = img.getpixel((x, y))
    
    print(f"Couleur du pixel central ({x},{y}) : Rouge={r}, Vert={v}, Bleu={b}")
    
    # Question : Essayez de lire le pixel aux coordonnées (largeur, hauteur)
    # Décommentez la ligne suivante pour tester :
    # r, v, b = img.getpixel((largeur, hauteur))
    # Que se passe-t-il ? Pourquoi ?


# ============================================================================
# ACTIVITÉ 2 : Créer le Négatif d'une image
# ============================================================================

def activite_2():
    """
    Crée le négatif d'une image en inversant les couleurs.
    Pour chaque pixel : nouvelle_valeur = 255 - ancienne_valeur
    """
    print("\n" + "="*60)
    print("ACTIVITÉ 2 : Créer le Négatif d'une image")
    print("="*60)
    
    img = Image.open("image_tp.jpg")
    largeur, hauteur = img.size
    
    # On crée une nouvelle image vide de la même taille
    img_new = Image.new("RGB", (largeur, hauteur))
    
    # On parcourt tous les pixels de l'image (double boucle)
    for y in range(hauteur):
        for x in range(largeur):
            # On récupère les anciennes couleurs
            r, v, b = img.getpixel((x, y))
            
            # --- A VOUS DE JOUER ---
            # Calculez les nouvelles couleurs
            r_new = 255 - r
            v_new = None       # A compléter : inverser le vert
            b_new = None       # A compléter : inverser le bleu
            # -----------------------
            
            # On écrit le nouveau pixel dans la nouvelle image
            img_new.putpixel((x, y), (r_new, v_new, b_new))
    
    # On affiche le résultat
    print("Création du négatif terminée !")
    img_new.show()
    # On sauvegarde le résultat
    img_new.save("negatif.jpg")
    print("Image sauvegardée sous 'negatif.jpg'")


# ============================================================================
# ACTIVITÉ 3 : Passage en Noir et Blanc (Niveaux de gris)
# ============================================================================

def activite_3():
    """
    Transforme une image couleur en noir et blanc (niveaux de gris).
    Méthode : calculer la moyenne des trois composantes RGB.
    """
    print("\n" + "="*60)
    print("ACTIVITÉ 3 : Passage en Noir et Blanc")
    print("="*60)
    
    img = Image.open("image_tp.jpg")
    largeur, hauteur = img.size
    
    # On crée une nouvelle image vide de la même taille
    img_new = Image.new("RGB", (largeur, hauteur))
    
    # On parcourt tous les pixels de l'image
    for y in range(hauteur):
        for x in range(largeur):
            # On récupère les couleurs du pixel
            r, v, b = img.getpixel((x, y))
            
            # --- A VOUS DE JOUER ---
            # Calculez la moyenne des trois composantes
            # Attention : utilisez // pour avoir un entier !
            moyenne = None  # A compléter : (r + v + b) // 3
            
            # Affectez cette moyenne aux trois canaux pour obtenir du gris
            r_new = None  # A compléter
            v_new = None  # A compléter
            b_new = None  # A compléter
            # -----------------------
            
            # On écrit le nouveau pixel
            img_new.putpixel((x, y), (r_new, v_new, b_new))
    
    # On affiche et sauvegarde le résultat
    print("Conversion en noir et blanc terminée !")
    img_new.show()
    img_new.save("noir_et_blanc.jpg")
    print("Image sauvegardée sous 'noir_et_blanc.jpg'")


# ============================================================================
# ACTIVITÉ 4 : Effet "Filtre Rouge"
# ============================================================================

def activite_4():
    """
    Ne garde que la composante rouge de l'image.
    Le vert et le bleu sont mis à 0.
    """
    print("\n" + "="*60)
    print("ACTIVITÉ 4 : Effet Filtre Rouge")
    print("="*60)
    
    img = Image.open("image_tp.jpg")
    largeur, hauteur = img.size
    
    # On crée une nouvelle image vide de la même taille
    img_new = Image.new("RGB", (largeur, hauteur))
    
    # --- A VOUS DE JOUER ---
    # Parcourez tous les pixels et ne gardez que le rouge
    # Le vert et le bleu doivent être mis à 0
    
    # A COMPLETER : double boucle for
    # for y in range(...):
    #     for x in range(...):
    #         r, v, b = ...
    #         r_new = ...
    #         v_new = ...
    #         b_new = ...
    #         img_new.putpixel(...)
    # -----------------------
    
    # On affiche et sauvegarde le résultat
    print("Filtre rouge appliqué !")
    img_new.show()
    img_new.save("filtre_rouge.jpg")
    print("Image sauvegardée sous 'filtre_rouge.jpg'")


# ============================================================================
# ACTIVITÉ 5 : Le Mystère de l'Image Cachée (Steganographie)
# ============================================================================

def activite_5():
    """
    Révèle un message caché dans les composantes bleues d'une image.
    Méthode : multiplier la composante bleue par 255.
    
    Note : Cette activité nécessite une image spéciale avec des pixels (0,0,1).
    """
    print("\n" + "="*60)
    print("ACTIVITÉ 5 : Steganographie - Message Caché")
    print("="*60)
    
    # Cette activité nécessite une image préparée spécialement
    # Vous pouvez créer votre propre image avec des pixels (0,0,1)
    
    try:
        img = Image.open("image_cachee.jpg")
        largeur, hauteur = img.size
        
        # On crée une nouvelle image vide
        img_new = Image.new("RGB", (largeur, hauteur))
        
        # On parcourt tous les pixels
        for y in range(hauteur):
            for x in range(largeur):
                r, v, b = img.getpixel((x, y))
                
                # --- A VOUS DE JOUER ---
                # Amplifiez le signal bleu
                r_new = 0
                v_new = 0
                b_new = None  # A compléter : b * 255 (attention au maximum 255!)
                
                # Assurez-vous que b_new ne dépasse pas 255
                if b_new > 255:
                    b_new = 255
                # -----------------------
                
                img_new.putpixel((x, y), (r_new, v_new, b_new))
        
        print("Message révélé !")
        img_new.show()
        img_new.save("message_revele.jpg")
        print("Image sauvegardée sous 'message_revele.jpg'")
        
    except FileNotFoundError:
        print("⚠️  Fichier 'image_cachee.jpg' non trouvé.")
        print("Cette activité nécessite une image spéciale préparée pour la steganographie.")


# ============================================================================
# MENU PRINCIPAL
# ============================================================================

def menu():
    """
    Affiche le menu et permet de choisir l'activité à exécuter.
    """
    while True:
        print("\n" + "="*60)
        print("   TRAVAUX PRATIQUES - TRAITEMENT D'IMAGE AVEC PYTHON")
        print("="*60)
        print("\nChoisissez une activité :")
        print("  1. Activité 1 : Ouvrir et Analyser une image")
        print("  2. Activité 2 : Créer le Négatif")
        print("  3. Activité 3 : Passage en Noir et Blanc")
        print("  4. Activité 4 : Effet Filtre Rouge")
        print("  5. Activité 5 : Steganographie (avancé)")
        print("  0. Quitter")
        print("="*60)
        
        choix = input("\nVotre choix (0-5) : ")
        
        if choix == "1":
            activite_1()
        elif choix == "2":
            activite_2()
        elif choix == "3":
            activite_3()
        elif choix == "4":
            activite_4()
        elif choix == "5":
            activite_5()
        elif choix == "0":
            print("\n👋 Au revoir !")
            break
        else:
            print("\n❌ Choix invalide. Veuillez choisir un nombre entre 0 et 5.")
        
        input("\nAppuyez sur Entrée pour continuer...")


# ============================================================================
# POINT D'ENTRÉE DU PROGRAMME
# ============================================================================

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║   💻 TP PHOTOGRAPHIE NUMÉRIQUE - TRAITEMENT D'IMAGES      ║
    ║                                                            ║
    ║   📚 Objectif : Apprendre à manipuler des images          ║
    ║      pixel par pixel avec Python et Pillow                ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    # Vérification que l'image de test existe
    try:
        test_img = Image.open("image_tp.jpg")
        test_img.close()
        print("✅ Fichier 'image_tp.jpg' trouvé !\n")
    except FileNotFoundError:
        print("❌ ERREUR : Le fichier 'image_tp.jpg' n'a pas été trouvé.")
        print("   Téléchargez-le depuis le site et placez-le dans le même dossier que ce script.\n")
        exit(1)
    
    # Lancement du menu
    menu()
