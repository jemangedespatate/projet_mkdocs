import logique
import random
import os

# Paramètres de la grille
LARGEUR = 10
HAUTEUR = 10

def effacer_ecran():
    """Efface l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_grille(serpent, pomme, largeur, hauteur):
    """
    Affiche la grille du jeu dans la console.
    
    Le serpent est représenté par 'O' (tête) et 'o' (corps).
    La pomme est représentée par 'X'.
    Le vide est représenté par '.'.
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    
    # Indice: Utilisez deux boucles imbriquées (pour y, puis pour x)
    # Pour chaque case (x, y), vérifiez si c'est le serpent, la pomme ou rien.
    pass

def demander_direction():
    """
    Demande à l'utilisateur d'entrer une direction (z/q/s/d) et retourne le vecteur (dx, dy).
    """
    choix = input("Direction (z=haut, q=gauche, s=bas, d=droite) : ").lower()
    
    # À COMPLÉTER : Retourner le bon tuple (dx, dy) selon la touche
    if choix == 'z':
        return (0, -1)
    # ... suite des conditions
    
    return None # Si touche invalide

def main():
    serpent = [(5, 5), (5, 6), (5, 7)]
    direction = (0, -1) # Haut par défaut
    pomme = (2, 2)
    
    while True:
        effacer_ecran()
        afficher_grille(serpent, pomme, LARGEUR, HAUTEUR)
        
        # Demander la prochaine direction (bloquant)
        nouvelle_dir = demander_direction()
        if nouvelle_dir:
            direction = nouvelle_dir
            
        # Logique (la même que pour la version graphique !)
        nouvelle_tete = logique.calculer_nouvelle_tete(serpent, direction)
        
        # TODO: Vérifier collisions (Exercice)
        
        # TODO: Gérer manger pomme (Exercice)
        
        # Avancer
        logique.inserer_tete(serpent, nouvelle_tete)
        logique.supprimer_queue(serpent)

if __name__ == "__main__":
    main()
