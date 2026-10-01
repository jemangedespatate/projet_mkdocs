"""
Fichier de logique pour le jeu Snake.
C'est ici que les élèves doivent implémenter les fonctions de manipulation de liste.
"""

def creer_serpent():
    """
    Crée la liste initiale représentant le serpent.
    
    Returns:
        list: Une liste de tuples (x, y) représentant les segments du serpent.
              Le premier élément est la tête.
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    # Exemple: Retourner une liste avec 3 segments au milieu de l'écran
    return [(10, 10), (10, 11), (10, 12)]


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
    tete = serpent[0]
    # 2. Calculer la nouvelle position
    return (tete[0] + direction[0], tete[1] + direction[1])

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
    serpent.insert(0, nouvelle_tete)

def supprimer_queue(serpent):
    """
    Supprime le dernier élément de la liste du serpent (la queue).
    
    Args:
        serpent (list): La liste représentant le serpent.
        
    Returns:
        None (la liste est modifiée sur place)
    """
    # À COMPLÉTER PAR LES ÉLÈVES
    serpent.pop()

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
    head = serpent[0]
    
    # 1. Collision avec les murs
    if (head[0] < 0 or head[0] >= largeur_grille or
        head[1] < 0 or head[1] >= hauteur_grille):
        return True
        
    # 2. Collision avec soi-même (le reste du corps)
    # Attention: serpent[0] est la tête, on vérifie si elle est dans serpent[1:]
    if head in serpent[1:]:
        return True
        
    return False

