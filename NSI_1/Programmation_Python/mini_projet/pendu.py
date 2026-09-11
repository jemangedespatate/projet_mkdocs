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
    pass

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
    pass

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
    pass

def nb_erreur(erreur:int)->int:
    """
    fonction qui comptabilise le nombre d'erreurs
    
    Paramètre:     nb_erreur, de type int
    Retour:     nb_erreur, de type int

    exemple:

    >>> nb_erreur(5)
    6
    >>> nb_erreur(0)
    1
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# reponse