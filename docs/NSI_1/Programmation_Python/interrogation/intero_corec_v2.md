# ✅ Correction du nouveau sujet d’évaluation (2h)

## Exercice 1 — Analyse et compréhension de code (5 points)

??? note "1. Comment s’appellent les différentes fonctions déclarées ici ?"
    Elles s’appellent : `mystere_1`, `mystere_2` et `mystere_3`.

??? note "2. Quels sont les paramètres de ces fonctions ?"
    Chaque fonction possède deux paramètres : `a` et `b`.

??? note "3. De quel type sont ces paramètres ?"
    Les deux paramètres sont de type entier (`int`).

??? note "4. De quel type seront les résultats renvoyés par ces fonctions ?"
    Toutes les fonctions renvoient un résultat de type entier (`int`).

??? note "5. Ce qui est stocké dans la variable `resultat` avant l'entrée dans la boucle `while` :"
    * Pour `mystere_1` : `resultat = a`
    * Pour `mystere_2` : `resultat = 0`
    * Pour `mystere_3` : `resultat = a`

??? note "6. Condition pour que la boucle `while` s’arrête :"
    Pour les trois fonctions, la boucle s’arrête dès que `b == 0` (car la boucle continue tant que `b != 0`).

??? note "7. Évolution de la variable `resultat` à chaque itération :"
    * Dans `mystere_1` : on ajoute 1 (`resultat = resultat + 1`).
    * Dans `mystere_2` : on ajoute `a` (`resultat = resultat + a`).
    * Dans `mystere_3` : on multiplie par `a` (`resultat = resultat * a`).

??? note "8. Tableau complété :"
    | a | b | Fonction | Résultat attendu | Explication |
    | :-: | :-: | :--- | :--- | :--- |
    | 2 | 3 | `mystere_1` | **5** | $2 + 1 + 1 + 1 = 5$ |
    | 2 | 3 | `mystere_2` | **6** | $0 + 2 + 2 + 2 = 6$ |
    | 2 | 3 | `mystere_3` | **16** | $2 \times 2 \times 2 \times 2 = 16$ |
    | 5 | 0 | `mystere_1` | **5** | la boucle ne s'exécute pas |
    | 5 | 0 | `mystere_2` | **0** | la boucle ne s'exécute pas |
    | 5 | 0 | `mystere_3` | **5** | la boucle ne s'exécute pas |

??? note "9. Rôle mathématique de chaque fonction :"
    * `mystere_1(a, b)` calcule l'addition $a + b$ (par incrémentations successives de 1).
    * `mystere_2(a, b)` calcule la multiplication $a \times b$ (par additions successives de $a$).
    * `mystere_3(a, b)` calcule $a^{b+1}$ (puissance).

---

## Exercice 2 — Boucles `for` et calculs cumulés (5 points)

### Partie A : Somme des entiers

```python
def somme_entiers(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
```

### Partie B : Compter les multiples d'un nombre

```python
def compter_multiples(n: int, k: int) -> int:
    compteur = 0
    for i in range(1, n + 1):
        if i % k == 0:
            compteur = compteur + 1
    return compteur
```

---

## Exercice 3 — Arithmétique entière et division euclidienne (5 points)

### Partie A : Décomposition horaire

```python
def conversion_temps(total_secondes: int):
    heures = total_secondes // 3600
    reste_heures = total_secondes % 3600
    minutes = reste_heures // 60
    secondes = reste_heures % 60
    
    print(heures, "h", minutes, "min", secondes, "s")
```

### Partie B : Algorithme avec boucle `while`

```python
def nb_divisions_par_deux(n: int) -> int:
    compteur = 0
    while n > 0:
        n = n // 2
        compteur = compteur + 1
    return compteur
```

---

## Exercice 4 — Conditions et programme complet (5 points)

### Partie 1 : Fonction de décision

```python
def appreciation(note: float) -> str:
    if note < 0 or note > 20:
        return "Erreur : note invalide"
    elif note >= 16:
        return "Très bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"
```

### Partie 2 : Programme interactif complet

```python
prenom = input("Entrez votre prénom : ")
note_saisie = float(input("Entrez votre note : "))

resultat = appreciation(note_saisie)
print("Élève", prenom, ": note", note_saisie, "/20 ->", resultat)
```

---

## 🌟 Exercice Bonus : Le jeu du nombre mystère

```python
def jeu_devinette(secret: int):
    proposition = int(input("Entrez un nombre : "))
    nb_essais = 1
    
    while proposition != secret:
        if proposition > secret:
            print("Trop grand !")
        else:
            print("Trop petit !")
        proposition = int(input("Entrez un nombre : "))
        nb_essais = nb_essais + 1
        
    print("Bravo ! Vous avez trouvé en", nb_essais, "essais.")
```
