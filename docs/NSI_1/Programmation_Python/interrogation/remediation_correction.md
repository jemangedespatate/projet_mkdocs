# Correction — Entraînement et Remédiation

Ce document fournit la correction détaillée des exercices d'entraînement proposés dans [remediation.md](./remediation.md).

---

## Exercice 1 — Analyse et compréhension de code

```python
def fct_A(n: int) -> int:
    total = 0
    while n != 0:
        total = total + 2
        n = n - 1
    return total

def fct_B(a: int, b: int) -> int:
    resultat = a
    while b != 0:
        resultat = resultat - 1
        b = b - 1
    return resultat

def fct_C(n: int) -> int:
    compteur = 0
    while n > 0:
        n = n // 10
        compteur = compteur + 1
    return compteur
```

### Réponses aux questions :

1. **Paramètres de `fct_B` :**  
   Les paramètres sont `a` et `b`. Ils sont tous les deux de type entier (`int`).

2. **Type de la valeur renvoyée :**  
   Chaque fonction renvoie un entier (`int`), comme indiqué par l'annotation `-> int`.

3. **Valeur de `total` avant la boucle dans `fct_A` :**  
   Avant d'entrer dans la boucle `while`, `total` vaut `0`.

4. **Condition d'arrêt pour `fct_C` :**  
   * La boucle continue tant que `n > 0`.  
   * Elle s'arrête dès que la condition devient fausse, c'est-à-dire dès que $n \le 0$ (dans les faits, dès que $n = 0$ pour un entier positif).

5. **Évolution de `resultat` dans `fct_B` :**  
   À chaque itération, la variable `resultat` diminue de 1 (`resultat = resultat - 1`).

6. **Tableau d'exécution :**

| Fonction | Paramètre(s) | Résultat renvoyé | Explication / Trace |
| :--- | :---: | :---: | :--- |
| `fct_A` | `n = 4` | **`8`** | On ajoute 2 quatre fois : $0 + 2 + 2 + 2 + 2 = 8$. |
| `fct_A` | `n = 0` | **`0`** | La condition `0 != 0` est fausse immédiatement, la boucle ne tourne pas. |
| `fct_B` | `a = 7, b = 3` | **`4`** | On part de 7 et on soustrait 1 trois fois : $7 - 1 - 1 - 1 = 4$. |
| `fct_B` | `a = 5, b = 0` | **`5`** | La condition `0 != 0` est fausse immédiatement, `resultat` reste égal à 5. |
| `fct_C` | `n = 354` | **`3`** | `354 // 10 = 35` (cpt=1), `35 // 10 = 3` (cpt=2), `3 // 10 = 0` (cpt=3). |
| `fct_C` | `n = 9` | **`1`** | `9 // 10 = 0` (cpt=1). Arrêt. |

7. **Rôle de chaque fonction :**  
   * `fct_A(n)` calcule le double de $n$, soit $2 \times n$.
   * `fct_B(a, b)` calcule la différence $a - b$ (soustraction).
   * `fct_C(n)` compte le **nombre de chiffres** de l'entier strictement positif $n$ en base 10.

---

## Exercice 2 — Boucles `for` et calculs cumulés

### Partie A : Produit des entiers (Factorielle)

```python
def produit_entiers(n: int) -> int:
    produit = 1
    for i in range(1, n + 1):
        produit = produit * i
    return produit
```

> **Point clé à expliquer aux élèves :**  
> On doit initialiser `produit` à `1` (élément neutre de la multiplication) et non à `0`, sinon le résultat resterait toujours `0`. De plus, `range(1, n + 1)` va bien jusqu'à `n` inclus.

### Partie B : Somme des entiers pairs

```python
def somme_pairs(n: int) -> int:
    somme = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            somme = somme + i
    return somme
```

*Variante possible en jouant sur le pas du `range` (intéressant à montrer aux élèves) :*
```python
def somme_pairs_variante(n: int) -> int:
    somme = 0
    for i in range(2, n + 1, 2):
        somme = somme + i
    return somme
```

---

## Exercice 3 — Arithmétique entière et division euclidienne

### Partie A : Rendu de monnaie

```python
def rendre_monnaie(montant: int):
    billets_20 = montant // 20
    reste = montant % 20
    pieces_2 = reste // 2
    pieces_1 = reste % 2
    
    print("Billets de 20€ :", billets_20, "| Pièces de 2€ :", pieces_2, "| Pièces de 1€ :", pieces_1)
```

> **Point clé à expliquer aux élèves :**  
> Après avoir retiré les billets de 20 €, le reste à rendre est `reste = montant % 20`. C'est **ce reste** que l'on divise ensuite par 2 pour trouver le nombre de pièces de 2 €, et non le montant initial.

### Partie B : Algorithme avec boucle `while` (soustractions successives)

```python
def nb_soustractions(n: int, p: int) -> int:
    compteur = 0
    while n >= p:
        n = n - p
        compteur = compteur + 1
    return compteur
```

> **Point clé à expliquer aux élèves :**  
> La condition est `n >= p` car tant que le nombre restant est supérieur ou égal au pas, on peut encore soustraire une fois.

---

## Exercice 4 — Conditions et programme interactif

### Partie 1 : Fonction de décision

```python
def categorie_sport(age: int) -> str:
    if age < 0 or age > 120:
        return "Erreur : âge invalide"
    elif age >= 18:
        return "Senior"
    elif age >= 14:
        return "Junior"
    elif age >= 10:
        return "Cadet"
    else:
        return "Poussin"
```

> **Point clé à expliquer aux élèves :**  
> Grâce à l'utilisation du `elif`, si la condition `age >= 18` est fausse, on sait déjà que `age < 18`. Il suffit donc d'écrire `elif age >= 14:` sans avoir besoin de répéter `and age < 18`.

### Partie 2 : Programme interactif complet

```python
prenom = input("Entrez votre prénom : ")
saisie_age = input("Entrez votre âge : ")
age = int(saisie_age)

categorie = categorie_sport(age)

print("Sportif", prenom, "(", age, "ans) : Catégorie", categorie)
```

Ou avec une f-string :
```python
print(f"Sportif {prenom} ({age} ans) : Catégorie {categorie}")
```

---

## 🌟 Exercice Bonus : Contrôle d'accès par mot de passe

```python
def verifier_mot_de_passe(bon_mdp: str):
    tentatives_restantes = 3
    
    while tentatives_restantes > 0:
        proposition = input("Entrez le mot de passe : ")
        if proposition == bon_mdp:
            print("Accès autorisé !")
            return  # Arrête immédiatement la fonction
        else:
            tentatives_restantes = tentatives_restantes - 1
            if tentatives_restantes > 0:
                print("Mot de passe incorrect ! (", tentatives_restantes, "essais restants)")
    
    # Si on sort de la boucle, c'est que les 3 essais ont échoué
    print("Compte verrouillé : trop de tentatives échouées.")
```
