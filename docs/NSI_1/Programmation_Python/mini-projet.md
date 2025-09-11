# <u>📝 Mini-projet : Jeu du Pendu en Python</u>

## <u>🎯 Objectif</u>

Nous allons programmer le célèbre **jeu du pendu** en Python.

Le principe est simple : un mot est choisi au hasard, et le joueur doit le deviner en proposant des lettres. À chaque erreur, on ajoute un élément du pendu. Le jeu s’arrête si le joueur trouve toutes les lettres ou s’il atteint le nombre maximum d’erreurs.

Dans ce TP, vous compléterez les fonctions manquantes dans le fichier Python donné, en respectant les consignes et en testant votre code.


## <u>Organisation des fichiers 📂</u>

Pour que votre projet fonctionne correctement, vous devez placer tous les fichiers dans **un même répertoire** (dossier).  

Les fichiers nécessaires sont :  
- [interface.py](../mini_projet/interface.py){:download="interface.py"} : contient les fonctions que vous devez compléter.  
- [pendu_dico.txt](../mini_projet/pendu_dico.txt){:download="pendu_dico.txt"} : dictionnaire de mots utilisés pour le pendu.  

👉 Arborescence attendue :  

```
mon_projet_pendu/
│
├── pendu.py
└── pendu_dico.txt
```

## <u>1. Choix d’un mot aléatoire</u>

La fonction suivante est déjà écrite :

```python
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
```

👉 **Dites, selon vous, ce que fait cette fonction en analysant rapidement son code.**

!!! info "informations"

    Écrivez vos réponses directement dans le fichier python, juste après `# réponse`.


## <u>2. Cacher le mot avec des underscores</u>

On veut afficher un mot inconnu sous forme de **tirets bas** `_`, un par lettre.

??? example "Exemple:"

    ```
    mot = "C H A T"
    → "_ _ _ _"
    ```

👉 **À vous d’écrire la fonction :**

```python
def cacher_mot(mot:str)->str:
    """
    fonction qui renvoie une chaine d'underscores de la même longueur que le paramètre mot
    
    Paramètre:  mot, de type chaine de caractère
    Retour:  mot_inconnu: chaine de caractère avec des "_"
```

??? success "🧪 **Teste avec doctest :**"

    ```python
    >>> cacher_mot("P E N D U")
    '_ _ _ _ _'
    >>> cacher_mot("C H A T")
    '_ _ _ _'
    ```

## <u>3. Vérifier si une lettre est présente</u>

On veut une fonction qui renvoie `True` si une lettre est dans le mot, et `False` sinon.

👉 Complètez la fonction :

```python
def verifier_lettre(mot:str, caractere:str)->str:
    """
    fonction qui renvoie True si caractere est présent dans mot
    
    Paramètres: caractere, de type chaine de caractère
               mot, de type chaine de caractère
    Retour:  Booléen, True si le caractere est dans le mot, False sinon
```

??? success "🧪 **Teste avec doctest :**"

    ```python
    >>> verifier_lettre("P E N D U", "E")
    True
    >>> verifier_lettre("P E N D U", "A")
    False
    ```


## <u>4. Révéler une lettre trouvée</u>

Quand le joueur propose une lettre correcte, il faut la remplacer à la bonne position dans le mot inconnu.

??? example "Exemple:"

    ```
    mot         = "P E N D U"
    mot_inconnu = "_ _ _ _ _"
    caractere   = "E"
    → mot_inconnu = "_ E _ _ _"
    ```

👉 Complètez la fonction :

```python
def lettre(mot:str, mot_inconnu:str,caractere:str)->str:
    """
    Fonction qui affiche la lettre trouvée à la place de l'unduscore de mot_inconnu
    
    Paramètre:  caractere, de type chaine de caractère
                mot_inconnu, de type chaine de caractère
                mot, de type chaine de caractère
    Retour:   mot_inconnu, de type chaine de caractère
    
```

??? success "🧪 **Teste avec doctest :**"

    ```python
    >>> lettre("P E N D U", "_ _ _ _ _", "E")
    '_ E _ _ _'
    >>> lettre("P E N D U", "_ _ _ _ _", "A")
    '_ _ _ _ _'
    ```

## <u>5. Compter les erreurs</u>

On a besoin d’une fonction qui incrémente le nombre d’erreurs du joueur.

👉 Complètez la fonction :

```python
def nb_erreur(erreur:int)->int:
    """
    fonction qui comptabilise le nombre d'erreurs
    
    Paramètre:     nb_erreur, de type int
    Retour:     nb_erreur, de type int
```

??? success "🧪 **Teste avec doctest :**"

    ```python
    >>> nb_erreur(5)
    6
    >>> nb_erreur(0)
    1
    ```

## <u>6. Utilisation de l’interface 🎮</u>

Pour jouer, vous allez maintenant intégrer le fichier [interface.py](../mini_projet/interface.py){:download="interface.py"} dans votre répertoire.

Voici à quoi doit ressembler votre répertoire après avoir ajouté le fichier :
```
mon_projet_pendu/
│
├── pendu.py
├── interface.py
└── pendu_dico.txt
```

Ce fichier contient une fonction principale qui gère l’affichage et la saisie.  

Pour démarrer le jeu, exécutez le fichier `interface.py`.

👉 **Question 3 :** Selon vous, à quoi sert l’interface dans ce projet ?  

👉 **Question 4 :** Quelles sont les informations qui doivent être envoyées par `pendu.py` vers `interface.py` ?  

## Pour aller plus loin

👉 Créez votre propre interface console dans le fichier `pendu.py`. L'affichage doit être mis à jour et affiché à chaque saisie de lettre.

??? example "Exemple:"

    ```
    Mot à trouver : _ _ _ _
    Nombre d’erreurs : 3
    Quelle est votre lettre ? ...
    ```

    Ici, `...` représente les lettres non trouvées et la zone après le `?` attend la lettre saisie par l'utilisateur.

??? example "Exemple:"

    ### Exemple quand le joueur perd (6 erreurs):

    ```
    Mot à trouver : _ _ _ _
    Nombre d’erreurs : 6
    Quelle est votre lettre ? x

    Dommage ! Vous avez perdu.
    Le mot était : CHAT
    ```

    ### Exemple quand le joueur **gagne** :

    ```
    Mot à trouver : C H A _
    Nombre d’erreurs : 2
    Quelle est votre lettre ? T

    Bravo ! Vous avez trouvé le mot : CHAT
    ```
