# 📝 Série d’exercices Python

Dans cette série d’exercices, vous allez vous entraîner à manipuler les variables, les boucles, les conditions et à écrire vos propres fonctions en Python.

👉 **Consigne générale :**
Écrivez vos réponses directement dans le fichier `.py`, à la suite de `# réponse`.

---

## ⚡ Exercices

!!! note "Exercice 1 : Échanger deux variables"

    Complétez le code suivant pour échanger les valeurs des variables `a` et `b`.

    ```python
    from random import *

    a = randint(0, 10)
    b = randint(0, 10)

    print("avant ", a, b)

    # réponse

    print("après ", a, b)
    ```

!!! note "Exercice 2 : Compter de a à b"

    Complétez la fonction suivante qui doit :

    * compter de `a` jusqu’à `b` inclus,
    * afficher chaque étape,
    * renvoyer le nombre d’étapes effectuées.

    ```python
    def compte(a, b):
        # réponse
        pass

    compte(0, 10)
    ```

!!! note "Exercice 3 : Division euclidienne"

    Écrivez une fonction qui renvoie le reste de la division euclidienne de deux entiers `a` et `b`, d’abord **en utilisant** l’opérateur Python (`%`), puis **sans l’utiliser**.


!!! note "Exercice 4 : Vérifier la majorité"

    Écrivez une fonction qui demande l’âge de l’utilisateur (avec `input`) et renvoie un booléen indiquant s’il est majeur.

!!! note "Exercice 5 : Plus grand de trois nombres"

    Complétez la fonction suivante qui renvoie le plus grand des 3 nombres mis en parametre:

    ```python
    def plus_grand(x, y, z):
        # réponse
        pass

    # quelques tests
    print(plus_grand(1, 2, 3))
    print(plus_grand(-1, 0.2, 4))
    print(plus_grand("a", "b", "A"))
    ```

!!! note "Exercice 6 : Inverser un mot"

    Écrivez une fonction qui renvoie le mot inversé sans modifier l’original.

    ```python
    def inverse(mot):
        # réponse
        pass

    # quelques tests
    print(inverse("NSI"))
    print(inverse("kayak"))
    ```


!!! note "Exercice 7 : Nombre d’apparitions d’une lettre"

    Écrivez une fonction qui compte le nombre d’apparitions d’une lettre dans une phrase.

    ```python
    def apparition(phrase, lettre):
        # réponse
        pass

    texte_somptueux = "J'adore la NSI. Vraiment l'informatique c'est super top."
    print(apparition(texte_somptueux, "i"))
    print(apparition(texte_somptueux, "."))
    ```


!!! note "Exercice 8 : Inverser des bits"

    Écrivez une fonction qui inverse tous les bits d’un nombre binaire donné sous forme de chaîne de caractères.

    ```python
    def inversion(binaire):
        # réponse
        pass

    print(inversion("01000001"))
    ```

!!! note "Exercice 9 : Moyenne des notes"

    Écrivez une fonction qui demande **5 notes** à l’utilisateur et lui renvoie sa moyenne.


!!! note "Exercice 10 : Table de multiplication"

    Affichez les 20 premiers termes de la table de multiplication par 7.
    👉 Les multiples de 3 doivent être signalés par un `*`.

    Exemple :

    ```
    7 14 21* 28 35 42* 49 ...
    ```


!!! note "Exercice 11 : Deux dés consécutifs"

    Écrivez une fonction qui simule des lancers de dés et renvoie le nombre d’essais nécessaires pour obtenir **deux 6 consécutifs**.

!!! note "Exercice 12 : Mot de passe"

    Écrivez une fonction qui demande un mot de passe à l’utilisateur.
    👉 L’utilisateur a droit à **4 essais maximum**.
    👉 La fonction s’arrête si le code est correct.

    ```python
    mdp = "NSI4ever"
    ```

!!! note "Exercice 13 : Jeu des dés"

    Un joueur lance deux dés et additionne les résultats.
    👉 Il continue tant que la somme n’est **pas comprise entre 7 et 12 inclus**.
    👉 Écrivez un programme qui automatise cette partie.

!!! note "Exercice 14 : Pourcentage de 6"

    Écrivez une fonction `jeu(n)` qui simule **1000 tirages** aléatoires de nombres entre 1 et 6, et renvoie le pourcentage de `6` obtenus.

    👉 Indice : utilisez `randint` du module `random`.
