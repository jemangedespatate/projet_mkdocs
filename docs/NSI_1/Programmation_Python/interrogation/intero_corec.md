# ✅ Correction de l’évaluation

## Premier exercice

??? note "1. Comment s’appellent les différentes fonctions déclarées ici ?"

    Elles s’appellent : `mystere_1`, `mystere_2`, `mystere_3`.

??? note "2. Quels sont les paramètres de ces fonctions ?"

    Chaque fonction a deux paramètres : `a` et `b`.

??? note "3. De quel type sont ces paramètres ?"

    Les deux paramètres `a` et `b` sont de type `int` (entier).

??? note "4. De quel type seront les résultats de ces fonctions ?"

    Toutes les fonctions renvoient un entier (`int`).

??? note "5. Pour chaque fonction, indiquer ce qui est stocké dans la variable `resultat` à la première ligne."

    * `mystere_1` : `resultat = a`
    * `mystere_2` : `resultat = 0`
    * `mystere_3` : `resultat = a`

??? note "6. Pour chaque fonction, quelle est la condition pour que la boucle `while` s’arrête ?"

    La boucle `while` s’arrête lorsque `b == 0`.

??? note "7. Pour chaque fonction, comment évolue la variable `resultat` à chaque itération ?"

    * `mystere_1` : on ajoute **1** à `resultat` à chaque tour.
    * `mystere_2` : on ajoute **a** à `resultat` à chaque tour.
    * `mystere_3` : on multiplie `resultat` par **a** à chaque tour.

??? note "8. Compléter le tableau"

    | a | b | Fonction   | Résultat attendu |
    | - | - | ---------- | ---------------- |
    | 2 | 3 | mystere\_1 | 5 (car 2+3)      |
    | 2 | 3 | mystere\_2 | 6 (car 2×3)      |
    | 2 | 3 | mystere\_3 | 16 (car 2^4)       |
    | 5 | 0 | mystere\_1 | 5                |
    | 5 | 0 | mystere\_2 | 0                |
    | 5 | 0 | mystere\_3 | 5                |

??? note "9. Finalement, que font ces fonctions ?"

    * `mystere_1(a,b)` → calcule **a + b**
    * `mystere_2(a,b)` → calcule **a × b**
    * `mystere_3(a,b)` → calcule **a puissance (b+1)**, c’est-à-dire **a^(b+1)**

---

## Deuxième exercice

```python
def recherche(texte: str, caractere: str) -> int | bool:
    i = 0
    while i < len(texte):
        if texte[i] == caractere:
            return i
        i += 1
    return False
```

✅ Vérification :

```python
print(recherche("bonjour", "b"))  # 0
print(recherche("bonjour", "o"))  # 1
print(recherche("bonjour", "i"))  # False
```

---

## Troisième exercice

```python
def inverse(mot: str) -> str:
    resultat = ""
    for lettre in mot:
        resultat = lettre + resultat  # on ajoute la lettre au début
    return resultat

# Tests
print(inverse("NSI"))     # "ISN"
print(inverse("kayak"))   # "kayak"
```

---

## Quatrième exercice

```python
def moyenne():
    note = float(input("Entrez une note entre 0 et 20 : "))
    
    if note < 0 or note > 20:
        return("Erreur : la note doit être comprise entre 0 et 20.")
    elif note >= 16:
        return("Très bien")
    elif note >= 12:
        return("Assez bien")
    elif note >= 10:
        return("Passable")
    else:
        return("Insuffisant")
```
