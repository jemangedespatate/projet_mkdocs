"""
🐍 FICHIER LOGIQUE À COMPLÉTER
-------------------------------
Ce fichier contient les fonctions de gestion de l'inventaire.
C'est ici que tu dois écrire ton code !

L'inventaire est représenté par un dictionnaire Python.
- Les CLÉS sont les noms des objets (str)
- Les VALEURS sont les quantités (int)

Exemple : {"Potion": 3, "Épée": 1, "Torche": 10}
"""

def creer_inventaire():
    """
    Initialise l'inventaire de départ.
    :return: Un dictionnaire contenant quelques objets de base.
    """
    # Tu peux modifier le contenu pour tester
    return {"Potion": 5, "Épée": 1, "Pain": 10}

def ajouter_objet(inventaire, nom, quantite):
    """
    Ajoute une quantité d'un objet à l'inventaire.
    - Si l'objet existe déjà, augmenter sa quantité.
    - Si l'objet n'existe pas, le créer avec cette quantité.
    
    :param inventaire: dict représentant le sac à dos
    :param nom: str, le nom de l'objet
    :param quantite: int, nombre d'objets à ajouter
    :return: Rien (modification en place)
    """
    # À TOI DE JOUER
    pass

def retirer_objet(inventaire, nom, quantite):
    """
    Retire des objets de l'inventaire.
    - Décrémenter la quantité.
    - Si la quantité tombe à 0 ou moins, supprime complètement la clé du dictionnaire.
    - Si l'objet n'existe pas, ne rien faire (on peut afficher un message d'erreur dans la console si on veut).
    
    :param inventaire: dict
    :param nom: str
    :param quantite: int
    :return: True si retrait réussi, False si objet absent
    """
    # À TOI DE JOUER
    pass

def obtenir_quantite(inventaire, nom):
    """
    Retourne la quantité d'un objet donné.
    Si l'objet n'est pas dans l'inventaire, retourner 0.
    
    :param inventaire: dict
    :param nom: str
    :return: int
    """
    # À TOI DE JOUER
    pass

def lister_objets(inventaire):
    """
    Dresse la liste des objets pour l'affichage.
    Doit retourner une LISTE de chaînes de caractères.
    Format attendu pour chaque chaîne : "Nom : Quantité"
    
    Exemple: ["Potion : 5", "Épée : 1"]
    
    :param inventaire: dict
    :return: list[str]
    """
    # À TOI DE JOUER
    pass

# --- ZONE DE TEST ---
# Tu peux tester tes fonctions ici sans lancer l'interface graphique.
if __name__ == "__main__":
    sac = creer_inventaire()
    print("Inventaire initial :", sac)
    
    ajouter_objet(sac, "Or", 100)
    print("Après ajout d'or :", sac)
    # Ajoute d'autres tests...
