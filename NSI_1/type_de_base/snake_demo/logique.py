def creer_serpent():
    """
    Crée la liste initiale représentant le serpent.
    
    Returns:
        list: Une liste de tuples (x, y) représentant les segments du serpent.
              Le premier élément est la tête.
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    # Exemple: Retourner une liste avec 3 segments au milieu de l'écran
    pass

def calculer_nouvelle_tete(serpent, direction):
    """
    Calcule la position de la nouvelle tête du serpent.
    
    Args:
        serpent (list): La liste représentant le serpent. Le premier élément est la tête actuelle.
        direction (tuple): La direction du mouvement (dx, dy).
        
    Returns:
        tuple: La nouvelle position (x, y).
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    # 1. Récupérer la tête actuelle (premier élément de la liste)
    # 2. Calculer la nouvelle position
    pass

def inserer_tete(serpent, nouvelle_tete):
    """
    Insère la nouvelle tête au début de la liste du serpent.
    
    Args:
        serpent (list): La liste représentant le serpent.
        nouvelle_tete (tuple): La position à ajouter.
        
    Returns:
        None (la liste est modifiée sur place)
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    pass

def supprimer_queue(serpent):
    """
    Supprime le dernier élément de la liste du serpent (la queue).
    
    Args:
        serpent (list): La liste représentant le serpent.
        
    Returns:
        None (la liste est modifiée sur place)
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    pass

def verifier_collision(serpent, largeur_grille, hauteur_grille):
    """
    Vérifie si la tête du serpent (serpent[0]) est en collision.
    
    Args:
        serpent (list): La liste représentant le serpent.
        largeur_grille (int): Largeur de la grille.
        hauteur_grille (int): Hauteur de la grille.
        
    Returns:
        bool: True si collision, False sinon.
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    
    # 1. Collision avec les murs
        
    # 2. Collision avec soi-même (le reste du corps)
    
    return False
