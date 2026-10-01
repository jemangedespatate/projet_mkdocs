import random

def choix_mot(nom_fichier:str)->str:
    """
    Fonction qui renvoie un mot du fichier texte source
    
    Paramètre: nom_fichier : de type chaine de caractère
    Retour : str, un mot du fichier, de type chaine de caractère
    """
    with open(nom_fichier, "r") as myfile:
        les_mots = myfile.readlines()   # les_mots : liste deslignes du fichier
    longueur = len(les_mots)
    nb = random.randint(1, longueur)
    mot = les_mots[nb].strip()  # strip() pour supprimer le retour chariot
    mot = " ".join(mot)   # permet d'espacer les lettres
    return mot

def cacher_mot(mot:str)->str:
    """
    fonction qui renvoie une chaine d'underscores de la même longueur que le paramètre mot
    
    Paramètre:  mot, de type chaine de caractère
    Retour:  str, chaine de caractère avec des "_"
    
    exemple:
    
    >>> cacher_mot("P E N D U")
    '_ _ _ _ _'
    >>> cacher_mot("C H A T")
    '_ _ _ _'
    """
    rendu = ""
    for lettre in mot:
        if lettre == " ":
            rendu = rendu + " "
        else:
            rendu = rendu + "_"
    return rendu

def verifier_lettre(mot:str, caractere:str)->str:
    """
    fonction qui renvoie True si caractere est présent dans mot
    
    Paramètres: caractere, de type chaine de caractère
               mot, de type chaine de caractère
    Retour:  Booléen, True si le caractere est dans le mot, False sinon
    
    exemple:

    >>> verifier_lettre("P E N D U", "A")
    False
    >>> verifier_lettre("P E N D U", "E")
    True
    """
    for lettre in mot :
        if caractere == lettre:
            return True
    return False

def lettre(mot:str, mot_inconnu:str,caractere:str)->str:
    """
    Fonction qui affiche la lettre trouvée à la place de l'unduscore de mot_inconnu
    
    Paramètre:  caractere, de type chaine de caractère
                mot_inconnu, de type chaine de caractère
                mot, de type chaine de caractère
    Retour:   mot_inconnu, de type chaine de caractère
    
    exemple:

    >>> lettre("P E N D U", "_ _ _ _ _", "E")
    '_ E _ _ _'
    >>> lettre("P E N D U", "_ _ _ _ _", "A")
    '_ _ _ _ _'
    """
    if verifier_lettre(mot,caractere):
        nouveau_mot_inconnu = ""
        for i in range(len(mot)):
            if mot[i] == caractere:
                nouveau_mot_inconnu = nouveau_mot_inconnu + caractere
            else:
                nouveau_mot_inconnu = nouveau_mot_inconnu + mot_inconnu[i]
    else:
        nouveau_mot_inconnu = mot_inconnu
    return nouveau_mot_inconnu

def nb_erreur(erreur:int)->int:
    """
    fonction qui ajoute 1 aux nombre d'erreurs mise en paramètre    
    
    Paramètre:     nb_erreur, de type int
    Retour:     nb_erreur + 1, de type int

    exemple:

    >>> nb_erreur(5)
    6
    >>> nb_erreur(0)
    1
    """
    return erreur + 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# reponse