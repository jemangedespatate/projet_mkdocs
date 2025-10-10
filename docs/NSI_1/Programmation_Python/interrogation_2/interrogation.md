## <u>Premier exercice — Étude de code</u>

On donne trois fonctions nommées `mystere_a`, `mystere_b` et `mystere_c` :

```python
def mystere_a(n: int) -> int:
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i = i + 1
    return total

def mystere_b(n: int) -> int:
    resultat = 1
    i = 1
    while i <= n:
        resultat = resultat * i
        i = i + 1
    return resultat

def mystere_c(texte: str) -> str:
    resultat = ""
    i = 0
    while i < len(texte):
        if i % 2 == 0:
            resultat = resultat + texte[i]
        else:
            resultat = resultat + "-"
        i = i + 1
    return resultat
```

---

### Questions

* Comment s’appellent les trois fonctions ?
* Quels sont les **paramètres** de chacune d’elles ?
* De quel **type** sont ces paramètres ?
* De quel **type** sont les **valeurs renvoyées** ?
* Que contient la variable `total` ou `resultat` à la première ligne de chaque fonction ?
* Quelle est la **condition d’arrêt** des boucles `while` ?
* Comment évolue la variable `i` à chaque tour de boucle ?
* Compléter le tableau suivant pour comprendre le fonctionnement de chaque fonction :

| Entrée    | Fonction  | Résultat attendu |
| --------- | --------- | ---------------- |
| 5         | mystere_a | ?                |
| 4         | mystere_b | ?                |
| "bonjour" | mystere_c | ?                | 

* Décrire en une phrase le rôle de chaque fonction :

    * `mystere_a` : …
    * `mystere_b` : …
    * `mystere_c` : …


??? success "Réponse :"

    #### 1️⃣ Noms des fonctions

    Les trois fonctions s’appellent :

    * `mystere_a`
    * `mystere_b`
    * `mystere_c`

    ---

    #### 2️⃣ Paramètres de chaque fonction

    | Fonction    | Paramètre | Type du paramètre |
    | ----------- | --------- | ----------------- |
    | `mystere_a` | `n`       | `int`             |
    | `mystere_b` | `n`       | `int`             |
    | `mystere_c` | `texte`   | `str`             |

    ---

    #### 3️⃣ Type des valeurs renvoyées

    | Fonction    | Type de la valeur renvoyée |
    | ----------- | -------------------------- |
    | `mystere_a` | `int`                      |
    | `mystere_b` | `int`                      |
    | `mystere_c` | `str`                      |

    ---

    #### 4️⃣ Contenu initial de la variable `total` ou `resultat`

    | Fonction    | Variable utilisée | Valeur initiale    | Rôle                                |
    | ----------- | ----------------- | ------------------ | ----------------------------------- |
    | `mystere_a` | `total`           | `0`                | Sert à accumuler une somme          |
    | `mystere_b` | `resultat`        | `1`                | Sert à accumuler un produit         |
    | `mystere_c` | `resultat`        | `""` (chaîne vide) | Sert à construire un texte résultat |

    ---

    #### 5️⃣ Condition d’arrêt de la boucle `while`

    | Fonction    | Condition d’arrêt |
    | ----------- | ----------------- |
    | `mystere_a` | `i > n`           |
    | `mystere_b` | `i > n`           |
    | `mystere_c` | `i >= len(texte)` |

    Autrement dit, la boucle s’arrête quand `i` devient supérieur à la limite (`n` ou la longueur du texte).

    ---

    #### 6️⃣ Évolution de la variable `i`

    Dans les trois fonctions :

    ```python
    i = i + 1
    ```

    ➡️ donc `i` **augmente de 1 à chaque tour de boucle**.

    ---

    ### 🧮 7️⃣ Compléter le tableau

    | Entrée    | Fonction    | Résultat attendu | Explication                                                                       |
    | --------- | ----------- | ---------------- | --------------------------------------------------------------------------------- |
    | 5         | `mystere_a` | `15`             | car 1 + 2 + 3 + 4 + 5 = 15                                                        |
    | 4         | `mystere_b` | `24`             | car 1 × 2 × 3 × 4 = 24                                                            |
    | "bonjour" | `mystere_c` | `"b-n-j-u-"`     | on garde les lettres d’indice pair, on remplace celles d’indice impair par un `-` |

    ---

    ### ✏️ 8️⃣ Rôle de chaque fonction

    | Fonction    | Description                                                               |
    | ----------- | ------------------------------------------------------------------------- |
    | `mystere_a` | Calcule la **somme** des nombres de 1 à `n`.                              |
    | `mystere_b` | Calcule le **produit** des nombres de 1 à `n` (le **factoriel** de `n`).  |
    | `mystere_c` | Transforme une chaîne en remplaçant **une lettre sur deux par un tiret**. |

---

## <u>Deuxième exercice - Parcour d'une chaine de caractére</u>

Compléter la fonction suivante qui renvoie **le nombre de voyelles** contenues dans un mot donné.

⚠️ Contraintes :

* Vous ne devez **pas utiliser** `count()` ou `in`.
* Vous devez parcourir la chaîne **caractère par caractère** avec une **boucle `for`**.
* On considère comme voyelles : `a, e, i, o, u, y` (en minuscules uniquement).

```python
def compter_voyelles(mot: str) -> int:
    """
    Renvoie le nombre de voyelles contenues dans le mot.

    Paramètres :
        mot : str, une chaîne de caractères

    Résultat :
        int : le nombre de voyelles présentes dans le mot

    Exemples :
    >>> compter_voyelles("bonjour")
    3
    >>> compter_voyelles("informatique")
    6
    >>> compter_voyelles("rhythme")
    2
    """
```

??? success "Réponse :"

    ```python
    def compter_voyelles(mot: str) -> int:
        """
        Renvoie le nombre de voyelles contenues dans le mot.

        Paramètres :
            mot : str, une chaîne de caractères

        Résultat :
            int : le nombre de voyelles présentes dans le mot
        """
        compteur = 0
        for caractere in mot:
            # on teste si le caractère est une voyelle sans utiliser 'in'
            if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u" or caractere == "y":
                compteur = compteur + 1
        return compteur
    ```

---

## <u>Troisième exercice - Parcour d'une chaine de caractére</u>

Écrire une fonction qui renvoie une chaîne où chaque caractère du mot donné est répété deux fois de suite, sans utiliser de compréhension de liste ni de fonction Python avancée.

```python
def double_caracteres(mot: str) -> str:
    """
    Renvoie une nouvelle chaîne où chaque caractère du mot est répété deux fois.

    Paramètres :
        mot : str, une chaîne de caractères

    Résultat :
        str : une nouvelle chaîne contenant chaque caractère du mot répété deux fois

    Exemples :
    >>> double_caracteres("NSI")
    'NNSSII'
    >>> double_caracteres("test")
    'tteesstt'
    >>> double_caracteres("abc")
    'aabbcc'
    """
    
```

??? success "Réponse :"

    ```python
    def double_caracteres(mot: str) -> str:
        """
        Renvoie une nouvelle chaîne où chaque caractère du mot est répété deux fois.

        Paramètres :
            mot : str, une chaîne de caractères

        Résultat :
            str : une nouvelle chaîne contenant chaque caractère du mot répété deux fois

        Exemples :
        >>> double_caracteres("NSI")
        'NNSSII'
        >>> double_caracteres("test")
        'tteesstt'
        >>> double_caracteres("abc")
        'aabbcc'
        """
        resultat = ""
        for caractere in mot:
            resultat = resultat + caractere + caractere
        return resultat
    ```   

---

## <u>Quatrième exercice - Conditions</u>

Compléter la fonction suivante qui renvoie un **message** en fonction de la **température** donnée (en degrés Celsius).

⚠️ Contraintes et précisions :

* La température est un **nombre** (entier ou décimal).
* Utilisez uniquement des **structures conditionnelles** (`if`, `elif`, `else`).

```python
def meteo_message(temp: int) -> str:
    """
    Renvoie un message en fonction de la température.

    Paramètres :
        temp : int, la température en degrés Celsius

    Résultat :
        str : un message correspondant à la température

    Règles :
        - temp < 0      → "Il gèle !"
        - 0 ≤ temp < 10 → "Il fait froid."
        - 10 ≤ temp < 25 → "Température agréable."
        - temp ≥ 25     → "Il fait chaud !"

    Exemples :
    >>> meteo_message(-3)
    "Il gèle !"
    >>> meteo_message(8)
    "Il fait froid."
    >>> meteo_message(18)
    "Température agréable."
    >>> meteo_message(30)
    "Il fait chaud !"
    """
```


??? success "Réponse :"

    ``` python
    def meteo_message(temp:int) -> str:
        """
        Renvoie un message en fonction de la température.

        Paramètres :
            temp : int, la température en degrés Celsius

        Résultat :
            str : un message correspondant à la température

        Règles :
            - temp < 0      → "Il gèle !"
            - 0 ≤ temp < 10 → "Il fait froid."
            - 10 ≤ temp < 25 → "Température agréable."
            - temp ≥ 25     → "Il fait chaud !"

        Exemples :
        >>> meteo_message(-3)
        "Il gèle !"
        >>> meteo_message(8)
        "Il fait froid."
        >>> meteo_message(18)
        "Température agréable."
        >>> meteo_message(30)
        "Il fait chaud !"
        """

        if temp < 0:
            message = "Il gèle !"
        elif temp < 10:
            message = "Il fait froid."
        elif temp < 25:
            message = "Température agréable."
        else:
            message = "Il fait chaud !"

        return message
    ```

### 🌟 **Bonus : amélioration du programme**

Améliorer la fonction `meteo_message` pour la rendre **plus complète et interactive** :

1. **Demander la température à l’utilisateur** avec `input`.
2. **Accepter les valeurs décimales** (exemple : `12.5`).


??? success "Réponse :"

    ``` python
    def meteo_message() -> str:
        """
        Renvoie un message en fonction de la température.

        Résultat :
            str : un message correspondant à la température

        Règles :
            - temp < 0      → "Il gèle !"
            - 0 ≤ temp < 10 → "Il fait froid."
            - 10 ≤ temp < 25 → "Température agréable."
            - temp ≥ 25     → "Il fait chaud !"

        Exemples :
        >>> meteo_message(-3)
        "Il gèle !"
        >>> meteo_message(8)
        "Il fait froid."
        >>> meteo_message(18)
        "Température agréable."
        >>> meteo_message(30)
        "Il fait chaud !"
        """
        temp = float(input("Entrez la température en °C : "))

        if temp < 0:
            message = "Il gèle !"
        elif temp < 10:
            message = "Il fait froid."
        elif temp < 25:
            message = "Température agréable."
        else:
            message = "Il fait chaud !"

        return message
    ```