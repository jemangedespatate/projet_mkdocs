# <u>Exercice 3</u>

## <u>Exercices sur les boucles et les fonctions</u>

### <u>1. Affichage simple avec une boucle</u>

Écris un programme qui affiche les nombres de 1 à 10 en utilisant une boucle `for`.

---

### <u>2. Somme des entiers</u>

Écris un programme qui calcule et affiche la somme des nombres de 1 à 100 en utilisant une boucle.

---

### <u>3. Compter les nombres pairs</u>

Écris un programme qui affiche tous les nombres pairs entre 1 et 50 grâce à une boucle.

---

### <u>4. Factorielle</u>

Écris une fonction `factorielle(n)` qui calcule la factorielle de `n`.
Teste la fonction avec plusieurs valeurs.

??? example "Exemple :"


    `factorielle(5) = 120`

---

### <u>5. Table de multiplication</u>

Écris une fonction `table(n)` qui affiche la table de multiplication de `n` (de 1 à 10).

??? example "Exemple :"


    `table(7)` doit afficher la table de 7.

---

### <u>6. Compter les voyelles</u>

Écris une fonction `compter_voyelles(mot)` qui retourne le nombre de voyelles contenues dans une chaîne de caractères.

??? example "Exemple :"


    `compter_voyelles("Bonjour") → 3`.

---

### <u>7. Somme des chiffres</u>

Écris une fonction `somme_chiffres(n)` qui calcule la somme des chiffres d’un nombre entier.

??? example "Exemple :"


     `somme_chiffres(1234) → 10`.

---

### <u>8. Suite de Fibonacci</u>

Écris une fonction `fibonacci(n)` qui affiche les `n` premiers termes de la suite de Fibonacci.

??? example "Exemple :"


     `fibonacci(7)` → `0 1 1 2 3 5 8`.

---

### <u>9. Nombre premier</u>

Écris une fonction `est_premier(n)` qui renvoie `True` si `n` est un nombre premier, et `False` sinon.
Puis, écris un programme qui affiche tous les nombres premiers jusqu’à 100.

---

### <u>10. Dessin avec boucles</u>

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

## <u>exercice complémentaire</u>

### <u>11. Nombres parfaits</u>

Un **nombre parfait** est un nombre égal à la somme de ses diviseurs propres (par exemple 6 = 1 + 2 + 3).

* Écris une fonction `est_parfait(n)` qui vérifie si `n` est un nombre parfait.
* Écris un programme qui affiche tous les nombres parfaits entre 1 et 1000.

---

### <u>12. Dessin en losange</u>

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

### <u>13. Décomposition en facteurs premiers</u>

Écris une fonction `facteurs_premiers(n)` qui décompose un entier en produit de nombres premiers.

??? example "Exemple :"


    * `facteurs_premiers(84)` → `[2, 2, 3, 7]`
    * `facteurs_premiers(97)` → `[97]`
