# Exercice 3

## Exercices sur les boucles et les fonctions

### 1. Affichage simple avec une boucle

Écris un programme qui affiche les nombres de 1 à 10 en utilisant une boucle `for`.

---

### 2. Somme des entiers

Écris un programme qui calcule et affiche la somme des nombres de 1 à 100 en utilisant une boucle.

---

### 3. Compter les nombres pairs

Écris un programme qui affiche tous les nombres pairs entre 1 et 50 grâce à une boucle.

---

### 4. Factorielle

Écris une fonction `factorielle(n)` qui calcule la factorielle de `n`.
Teste la fonction avec plusieurs valeurs.

??? example "Exemple :"


    `factorielle(5) = 120`

---

### 5. Table de multiplication

Écris une fonction `table(n)` qui affiche la table de multiplication de `n` (de 1 à 10).

??? example "Exemple :"


    `table(7)` doit afficher la table de 7.

---

### 6. Compter les voyelles

Écris une fonction `compter_voyelles(mot)` qui retourne le nombre de voyelles contenues dans une chaîne de caractères.

??? example "Exemple :"


    `compter_voyelles("Bonjour") → 3`.

---

### 7. Somme des chiffres

Écris une fonction `somme_chiffres(n)` qui calcule la somme des chiffres d’un nombre entier.

??? example "Exemple :"


     `somme_chiffres(1234) → 10`.

---

### 8. Suite de Fibonacci

Écris une fonction `fibonacci(n)` qui affiche les `n` premiers termes de la suite de Fibonacci.

??? example "Exemple :"


     `fibonacci(7)` → `0 1 1 2 3 5 8`.

---

### 9. Nombre premier

Écris une fonction `est_premier(n)` qui renvoie `True` si `n` est un nombre premier, et `False` sinon.
Puis, écris un programme qui affiche tous les nombres premiers jusqu’à 100.

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

## exercice complémentaire

### 11. Nombres parfaits

Un **nombre parfait** est un nombre égal à la somme de ses diviseurs propres (par exemple 6 = 1 + 2 + 3).

* Écris une fonction `est_parfait(n)` qui vérifie si `n` est un nombre parfait.
* Écris un programme qui affiche tous les nombres parfaits entre 1 et 1000.

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

---

### 13. Décomposition en facteurs premiers

Écris une fonction `facteurs_premiers(n)` qui décompose un entier en produit de nombres premiers.

??? example "Exemple :"


    * `facteurs_premiers(84)` → `[2, 2, 3, 7]`
    * `facteurs_premiers(97)` → `[97]`
