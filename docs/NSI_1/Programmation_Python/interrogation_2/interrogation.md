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
    1
    """
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

### 🌟 **Bonus : amélioration du programme**

Améliorer la fonction `meteo_message` pour la rendre **plus complète et interactive** :

1. **Demander la température à l’utilisateur** avec `input`.
2. **Accepter les valeurs décimales** (exemple : `12.5`).
