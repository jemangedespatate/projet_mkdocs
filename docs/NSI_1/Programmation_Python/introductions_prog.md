# 🖥️ <u>Introduction à la programmation</u>

## <u>1. Qu’est-ce que programmer ?</u>

Programmer, c’est **donner des instructions précises à un ordinateur** pour qu’il exécute une tâche.
Un programme est comme une recette de cuisine :

* il faut des ingrédients (**les données**)
* suivre des étapes (**les instructions**)
* et obtenir un résultat (**la sortie du programme**).

En NSI, on utilise principalement **Python**, un langage simple et très répandu.

!!! note "thonny"

    Cette année, nous allons utiliser Thonny, un logiciel spécialement conçu pour apprendre à programmer en Python.
    C’est un environnement de développement (appelé IDE) qui facilite l’écriture, l’exécution et le test des programmes.

    Avec Thonny, on peut :

    - écrire du code Python dans une zone d’édition,

    - lancer le programme en cliquant sur ▶,

    - voir le résultat immédiatement dans la console,

    - utiliser des outils pratiques pour comprendre pas à pas le déroulement d’un programme (mode pas-à-pas, visualisation des variables).

## <u>2. Les bases de Python</u>

### <u>2.1. Les variables</u>

Une **variable** est comme une boîte qui permet de **stocker une information** pour pouvoir la réutiliser plus tard dans un programme.
Chaque variable a :

* un **nom** (choisi par le programmeur)
* une **valeur** (le contenu de la boîte)

!!! example "Exemple :"

    ```python
    age = 16
    nom = "Alice"
    pi = 3.14159
    ```

    Explication :

    * `age` contient un **nombre entier** (`int`) → 16
    * `nom` contient une **chaîne de caractères** (`str`) → "Alice"
    * `pi` contient un **nombre décimal** (`float`) → 3.14159

On peut afficher leur contenu grâce à la fonction `print` :

!!! example "Exemple :"

    ```python
    print("Bonjour", nom, "tu as", age, "ans.")
    ```

    Résultat affiché :

    ```
    Bonjour Alice tu as 16 ans.
    ```

### <u>2.2. Les types de données de base</u>

En Python, il existe différents types de données de base qui permettent de représenter des informations de nature différente

!!! example "Exemple :"

    * **int** → nombres entiers (`5`, `2025`)
    * **float** → nombres décimaux (`3.14`, `2.0`)
    * **str** → texte (`"Bonjour"`, `'NSI'`)
    * **bool** → vrai ou faux (`True`, `False`)

il est possible de visualiser ces type a l'aide de `type(...)`

!!! example "Exemple :"
    
    * `type(5)` -> `<class ‘int’>`
    * `type(3.14)` -> `<class ‘float’>`
    * `type("Bonjour")` -> `<class ‘str’>`
    * `type(True)` -> `<class ‘bool’>`

Il est également possible de changer le type de certaines variables à l’aide de `str()` ou `int()`, par exemple.

!!! example "Exemple :"
    
    * `int("5")` -> `5`
    * `str(5)` -> `"5"`


### <u>2.3. Les opérateurs</u>

Pour manipuler les nombres et effectuer des calculs en Python, on utilise des opérateurs arithmétiques.

!!! example "Exemple :"

    ```python
    a = 10
    b = 3
    print(a + b)  # addition -> 10 + 3 = 13
    print(a - b)  # soustraction -> 10 - 3 = 7
    print(a * b)  # multiplication -> 10 * 3 = 30
    print(a / b)  # division -> 10 / 3 = 3,33333... ⚠️ ici le resultat sera un float
    print(a // b) # division entière -> 10 // 3 = 3
    print(a % b)  # reste de la division (modulo) -> 10 // 3 = 1
    print(a ** b) # puissance -> 10 ** 3 = 1000
    ```

## <u>3. Contrôler le déroulement du programme</u>

### <u>3.1. Les conditions</u>

Une **condition** permet à un programme de **prendre une décision** en fonction d’une situation donnée.
L’ordinateur **teste une expression logique** (par exemple `âge >= 18`) et choisit ensuite quel bloc d’instructions exécuter.

En Python, on utilise les mots-clés :

* `if` → si la condition est vraie
* `else` → sinon (si la condition est fausse)
* `elif` → sinon si (autre condition à vérifier)

!!! example "Exemple :"

    ```python
    age = 16

    if age >= 18:
        print("Majeur")
    else:
        print("Mineur")
    ```

    Explication :

    * On définit `age = 16`.
    * Le programme vérifie la condition `age >= 18`.
    * Comme 16 n’est pas supérieur ou égal à 18, la condition est **fausse**.
    * L’ordinateur exécute donc le bloc qui suit `else`.

    Résultat affiché :

    ```
    Mineur
    ```

!!! example "Exemple :"

    ```python
    example = 14

    if example >= 16:
        print("Très bien")
    elif example >= 12:
        print("Assez bien")
    elif example >= 10:
        print("Passable")
    else:
        print("Insuffisant")
    ```

    Explication :

    * Le programme teste d’abord si la example est `>= 16`. Ici `14 >= 16` est faux.
    * Ensuite il teste `example >= 12`. Comme c’est vrai, il affiche `"Assez bien"`.
    * Les autres conditions ne sont pas vérifiées car une condition vraie a déjà été trouvée.

    Résultat affiché :

    ```
    Assez bien
    ```

### <u>3.2. Les boucles</u>

Une boucle permet de répéter automatiquement une série d’instructions sans avoir à les réécrire plusieurs fois. Elle est très utile lorsque l’on veut effectuer une même action plusieurs fois (par exemple afficher les nombres de 1 à 10 ou répéter un calcul).

**Deux types de boucles sont disponibles en Python : la boucle `while` et la boucle `for`.**

#### <u>3.2.1. Boucle **while** (tant que)</u>

La boucle **while** permet de répéter une suite d’instructions **tant qu’une condition est vraie**.
Autrement dit, l’ordinateur vérifie la condition au début de chaque tour de boucle :

* si la condition est vraie → il exécute les instructions,
* si la condition devient fausse → la boucle s’arrête.

!!! example "Exemple :"

    ```python
    i = 1
    while i <= 5:
        print("Compteur :", i)
        i = i + 1
    ```

    Explication :

    * On commence avec `i = 1`.
    * La boucle s’exécute tant que `i <= 5`.
    * À chaque tour, le programme affiche la valeur de `i` puis ajoute 1 (`i = i + 1`).
    * Quand `i` atteint 6, la condition `i <= 5` devient fausse et la boucle s’arrête.

    Résultat affiché :

    ```
    Compteur : 1
    Compteur : 2
    Compteur : 3
    Compteur : 4
    Compteur : 5
    ```

#### <u>3.2.2. Boucle **for** (pour)</u>

La boucle **for** est utilisée lorsqu’on veut répéter une suite d’instructions **un nombre de fois connu à l’avance** ou lorsqu’on veut parcourir les éléments d’une liste.

En Python, on utilise souvent la fonction `range()` pour générer une séquence de nombres.

!!! example "Exemple :"

    ```python
    for i in range(5):
        print("Compteur :", i)
    ```

    Explication :

    * `range(5)` crée une séquence de nombres allant de **0 à 4** (le 5 n’est pas inclus).
    * La boucle `for` va donc exécuter le bloc d’instructions 5 fois.
    * À chaque tour, la variable `i` prend successivement les valeurs `0, 1, 2, 3, 4`.
    * Le programme affiche donc la valeur de `i` à chaque passage.

    Résultat affiché :

    ```
    Compteur : 0
    Compteur : 1
    Compteur : 2
    Compteur : 3
    Compteur : 4
    ```
!!! example "Exemple :"

    Si on veut commencer à 1 et aller jusqu’à 5 inclus, on peut écrire :

    ```python
    for i in range(1, 6):
        print("Compteur :", i)
    ```

    Résultat :

    ```
    Compteur : 1
    Compteur : 2
    Compteur : 3
    Compteur : 4
    Compteur : 5
    ```

## <u>4. Les fonctions</u>

Une **fonction** est un bloc de code qui réalise une tâche précise et que l’on peut **réutiliser plusieurs fois** dans un programme, sans avoir à réécrire les mêmes instructions.

On peut comparer une fonction à une **machine** :

* on lui donne une **entrée** (des données, appelées *paramètres*),
* elle effectue un **traitement** (les instructions de la fonction),
* et elle renvoie une **sortie** (le résultat, grâce au mot-clé `return`).

!!! example "Exemple :"

    ```python
    def carre(x):
        return x * x

    print(carre(5))  # Affiche 25
    ```

    Explication :

    * On définit une fonction appelée `carre` avec le mot-clé `def`.
    * Elle prend une **entrée** : `x`.
    * Elle renvoie le résultat de `x * x`.
    * Lorsque l’on appelle `carre(5)`, la fonction calcule `5 * 5` et retourne `25`.

    Résultat affiché :

    ```
    25
    ```

#### Avantages des fonctions :

* Éviter de répéter du code identique.
* Rendre un programme plus **lisible** et **organisé**.
* Faciliter la **réutilisation** et la **modification**.
