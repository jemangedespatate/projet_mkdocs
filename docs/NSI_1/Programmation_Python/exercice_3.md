# Exercice 3

## Exercices sur les boucles et les fonctions

### 1. Affichage simple avec une boucle

Écris un programme qui affiche les nombres de 1 à 10 en utilisant une boucle `for`.

??? success "Réponse :"

    ```py
    for i in range(1,11):
        print(i)
    ```

---

### 2. Somme des entiers

Écris un programme qui calcule et affiche la somme des nombres de 1 à 100 en utilisant une boucle.

??? success "Réponse :"

    ```py
    resultat = 0
    for i in range(1,101):
        resultat = resultat + i
    print(resultat)
    ```

---

### 3. Compter les nombres pairs

Écris un programme qui affiche tous les nombres pairs entre 1 et 50 grâce à une boucle.

??? success "Réponse :"

    ```py
    for i in range(1,51):
        if i % 2 == 0:
            print(i)
    ```

---

### 4. Factorielle

Écris une fonction `factorielle(n)` qui calcule la factorielle de `n`.
Teste la fonction avec plusieurs valeurs.

??? example "Exemple :"


    `factorielle(5) = 120`


??? success "Réponse :"

    ```py
    def factorielle(n):
        resultat = 1
        for i in range(1,n+1):
            resultat = resultat + i
        return resultat
    ```

---

### 5. Table de multiplication

Écris une fonction `table(n)` qui affiche la table de multiplication de `n` (de 1 à 10).

??? example "Exemple :"

    `table(7)` doit afficher la table de 7.

??? success "Réponse :"

    ```py
    def table(n):
        for i in range(1,11):
            print(n," x ", i, " = ", n*i)
    ```

---

### 6. Compter les voyelles

Écris une fonction `compter_voyelles(mot)` qui retourne le nombre de voyelles contenues dans une chaîne de caractères.

??? example "Exemple :"


    `compter_voyelles("Bonjour") → 3`.

??? success "Réponse :"

    ```py
    def compter_voyelles(mot):
        resultat = 0
        for lettre in mot:
            if lettre in "aeiouy":
                resultat = resultat + 1
        return resultat
    ```

---

### 7. Somme des chiffres

Écris une fonction `somme_chiffres(n)` qui calcule la somme des chiffres d’un nombre entier.

??? example "Exemple :"

     `somme_chiffres(1234) → 10`.

??? success "Réponse :"

    ```py
    def somme_chiffres(n):
        mot_n = str(n)
        resultat = 0
        for chiffre in mot_n:
            resultat = resultat + int(chiffre)
        return resultat
    ```

---

### 8. Suite de Fibonacci (optionnel)

Écris une fonction `fibonacci(n)` qui affiche les `n` premiers termes de la suite de Fibonacci.

??? example "Exemple :"


     `fibonacci(7)` → `0 1 1 2 3 5 8`.

??? success "Réponse :"

    ```py
    def fibonacci(n):
        a = 0
        b = 1
        for i in range(n):
            print(a, end=" ")
            temp = a + b
            a = b
            b = temp
    ```

---

### 9. Nombre premier

Écris une fonction `est_premier(n)` qui renvoie `True` si `n` est un nombre premier, et `False` sinon.
Puis, écris un programme qui affiche tous les nombres premiers jusqu’à 100.

??? success "Réponse :"

    ```py
    def est_premier(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


    # Affichage des nombres premiers jusqu'à 100
    for nombre in range(2, 101):
        if est_premier(nombre):
            print(nombre, end=" ")
    ```

---

### 10. Dessin avec boucles

Écris un programme qui affiche un triangle de hauteur `n` en utilisant une boucle.

??? example "Exemple :"


    pour `n = 5` :

    ```
    *
    **
    ***
    ****
    *****
    ```

??? success "Réponse :"

    ```py
    def triangle(n):
        for i in range(1,n+1):
            ligne = "*" * i
            print(ligne)
    ```


## exercice complémentaire

### 11. Nombres parfaits

Un **nombre parfait** est un nombre égal à la somme de ses diviseurs propres (par exemple 6 = 1 + 2 + 3).

* Écris une fonction `est_parfait(n)` qui vérifie si `n` est un nombre parfait.
* Écris un programme qui affiche tous les nombres parfaits entre 1 et 1000.

??? success "Réponse :"

    ```py
    def est_parfait(n):
        somme = 0
        for i in range(1, n):
            if n % i == 0:
                somme += i
        return somme == n


    # Affichage des nombres parfaits entre 1 et 1000
    for nombre in range(1, 1001):
        if est_parfait(nombre):
            print(nombre, end=" ")
    ```


---

### 12. Dessin en losange

Écris une fonction `losange(n)` qui affiche un losange de hauteur `2n - 1` en utilisant des boucles.

??? example "Exemple :"


    pour `n = 4` :

    ```
    *
    ***
    *****
    *******
    *****
    ***
    *
    ```

??? success "Réponse :"

    ```py
    def losange(n):
        for i in range(1,n+1):
            ligne = "*" * i
            print(ligne)

        j = n - 1
        while j > 0:
            ligne = "*" * j
            print(ligne)
            j = j-1
    ```

---

### 13. Décomposition en facteurs premiers

Écris une fonction `facteurs_premiers(n)` qui décompose un entier en produit de nombres premiers et les affiches.

??? example "Exemple :"


    * `facteurs_premiers(84)` → `2, 2, 3, 7`
    * `facteurs_premiers(97)` → `97`

??? success "Réponse :"

    ```py

    def facteurs_premiers(n):
        facteur = 2
        while n > 1:
            if n % facteur == 0:
                print(facteur, end="")
                n //= facteur
                if n > 1:
                    print(", ", end="")
            else:
                facteur += 1
    ```

---

### 14. Nombre mystère

Écris une fonction `deviner(n)` qui fait deviner un nombre entre 1 et `n`.

* L’ordinateur choisit un nombre au hasard.
* L’utilisateur doit proposer des valeurs (saisies au clavier).
* Le programme indique *trop grand* ou *trop petit*.
* Quand le nombre est trouvé, afficher le nombre d’essais.

??? success "Réponse :"

    ```py

    import random

    def deviner(n):
        secret = random.randint(1, n)
        essais = 0
        trouve = False

        print(f"J'ai choisi un nombre entre 1 et {n}. Essaie de le deviner !")

        while trouve != True:
            proposition = int(input("Ta proposition : "))
            essais += 1

            if proposition < secret:
                print("Trop petit !")
            elif proposition > secret:
                print("Trop grand !")
            else:
                print(f"Bravo ! Tu as trouvé en {essais} essai(s).")
                trouve = True
    ```

---

### 15. Somme des chiffres pairs

Écris une fonction `somme_pairs(nombre)` qui renvoie la somme des chiffres **pairs** d’un entier.

??? example "Exemple :"


    * `somme_pairs(48215)` → `14`  (car 4 + 8 + 2 = 14)  

??? success "Réponse :"

    ```py
    def somme_pairs(n):
        mot_n = str(n)
        resultat = 0
        for chiffre in mot_n:
            if int(chiffre) % 2 == 0: 
                resultat = resultat + int(chiffre)
        return resultat
        
    ```

---

### 16. Triangle inversé

Écris une fonction `triangle_inverse(n)` qui affiche un triangle de `n` lignes avec des `*` décroissants.

??? example "Exemple :"

    * `triangle_inverse(5)`  
    ```
    *****
    ****
    ***
    **
    *
    ```  

??? success "Réponse :"

    ```py
    def losange(n):
        j = n - 1
        while j > 0:
            ligne = "*" * j
            print(ligne)
            j = j-1
    ```

---


### 17. Anagrammes

Écris une fonction `est_anagramme(mot1, mot2)` qui retourne `True` si les deux mots sont des anagrammes (mêmes lettres en nombre identique, ordre différent).

??? example "Exemple :"

    * `est_anagramme("chien", "niche")` → `True`  
    * `est_anagramme("python", "typhon")` → `True`  
    * `est_anagramme("test", "tseta")` → `False`  

??? success "Réponse :"

    ```py
    def est_anagramme(mot1, mot2):
        # On met les mots en minuscules pour éviter les différences entre majuscules/minuscules
        mot1 = mot1.lower()
        mot2 = mot2.lower()

        # Si les mots n'ont pas la même longueur, ils ne peuvent pas être des anagrammes
        if len(mot1) != len(mot2):
            return False

        # Pour chaque lettre du premier mot
        for lettre in mot1:
            # On cherche cette lettre dans le deuxième mot
            position = -1
            for i in range(len(mot2)):
                if mot2[i] == lettre:
                    position = i  # on note où elle se trouve
                    break

            # Si la lettre n'est pas trouvée → ce n’est pas une anagramme
            if position == -1:
                return False

            # On enlève la lettre trouvée dans mot2 en collant la partie gauche a la lettre a sa partie a droite
            mot2 = mot2[:position] + mot2[position+1:]

        # Si à la fin, mot2 est vide, toutes les lettres ont été utilisées → c’est une anagramme
        return len(mot2) == 0


    # --- Programme principal ---
    motA = input("Entrez le premier mot : ")
    motB = input("Entrez le deuxième mot : ")

    if est_anagramme(motA, motB):
        print("Les deux mots sont des anagrammes ✅")
    else:
        print("Les deux mots ne sont pas des anagrammes ❌")
    ```

---

### 18. Mots en escalier

Écris une fonction `escalier_mot(mot)` qui affiche un mot en escalier.

??? example "Exemple :"

    * `escalier_mot("PYTHON")`  
    ```
    P
    PY
    PYT
    PYTH
    PYTHO
    PYTHON
    ```  

??? success "Réponse :"

    ```py
    def escalier_mot(mot):
        ligne = ""
        for lettre in mot:
            ligne = ligne + lettre
            print(ligne)
    ```
---

### 19. Symétrie verticale

Écris une fonction `symetrie(mot)` qui crée un effet miroir en concaténant le mot avec son inverse.

??? example "Exemple :"

    * `symetrie("code")` → `"codeedoc"`  

??? success "Réponse :"

    ```py
    def symetrie(mot):
        mot_copie = mot[:] # ici, on effectue une copie à l'aide de [:] pour eviter d'ecraser le mot mis en parametre

        i = len(mot) -1
        while i >= 0:
            mot_copie = mot_copie + mot[i]
            i = i -1
        return mot_copie
    ```

---

### 20. Caractère le plus fréquent

Écris une fonction `plus_frequent(texte)` qui retourne le caractère le plus fréquent dans une chaîne (en ignorant les espaces).

??? example "Exemple :"

    * `plus_frequent("abracadabra")` → `'a'`  

??? success "Réponse :"

    ```py
    def plus_frequent(texte):

        caractere_max = ""   # le caractère le plus fréquent
        frequence_max = 0    # combien de fois il apparaît

        # On parcourt chaque caractère du texte
        for caractere in texte:
            if caractere != " ":  # on ignore les espaces
                # Compter combien de fois ce caractère apparaît
                compteur = 0
                for c in texte:
                    if c == caractere:
                        compteur += 1

                # Si ce caractère est plus fréquent que le précédent, on le garde
                if compteur > frequence_max:
                    frequence_max = compteur
                    caractere_max = caractere

        return caractere_max

    ```
