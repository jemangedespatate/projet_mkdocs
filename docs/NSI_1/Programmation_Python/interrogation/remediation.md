# Entraînement et Remédiation — Programmation Python

Ce document propose des exercices d'entraînement parallèles à l'évaluation pour consolider les notions clés vues pendant la correction.

---

## Exercice 1 — Analyse et compréhension de code

On considère les trois fonctions suivantes :

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

1. Quels sont les paramètres de la fonction `fct_B` ainsi que leurs types ?
2. Quel est le type de la valeur renvoyée par chacune de ces trois fonctions ?
3. Pour la fonction `fct_A`, quelle est la valeur de la variable `total` avant d'entrer dans la boucle `while` ?
4. Pour la fonction `fct_C`, quelle est la condition pour que la boucle `while` continue à tourner ? Quelle condition provoque l'arrêt ?
5. Pour la fonction `fct_B`, comment évolue la variable `resultat` à chaque itération (tour de boucle) ?
6. Compléter le tableau d'exécution suivant :

| Fonction | Paramètre(s) | Résultat renvoyé |
| :--- | :---: | :---: |
| `fct_A` | `n = 4` | |
| `fct_A` | `n = 0` | |
| `fct_B` | `a = 7, b = 3` | |
| `fct_B` | `a = 5, b = 0` | |
| `fct_C` | `n = 354` | |
| `fct_C` | `n = 9` | |

7. Quel est le rôle mathématique ou algorithmique de chacune de ces trois fonctions ?

---

## Exercice 2 — Boucles `for` et calculs cumulés

### Partie A : Produit des entiers (Factorielle)

Écrire une fonction `produit_entiers(n: int) -> int` qui prend en paramètre un nombre entier strictement positif `n` et renvoie le produit de tous les entiers de `1` à `n` inclus :
$$1 \times 2 \times 3 \times \dots \times n$$

⚠️ **Contraintes :**

* Utiliser une boucle `for` avec la fonction `range()`.
* Utiliser une variable accumulatrice bien initialisée.

```python
def produit_entiers(n: int) -> int:
    # À compléter
```

Exemples attendus :
```python
print(produit_entiers(3))  # Affiche 6 (car 1 * 2 * 3 = 6)
print(produit_entiers(5))  # Affiche 120 (car 1 * 2 * 3 * 4 * 5 = 120)
print(produit_entiers(1))  # Affiche 1
```

### Partie B : Somme des entiers pairs

Écrire une fonction `somme_pairs(n: int) -> int` qui prend en paramètre un nombre entier positif `n` et renvoie la somme de tous les entiers **pairs** compris entre `1` et `n` inclus.

⚠️ **Contraintes et rappel :**

* Utiliser une boucle `for` avec `range()`.
* Tester si chaque entier est pair à l'aide de l'opérateur modulo `% 2 == 0` et d'une condition `if`.
* Accumuler la somme des nombres vérifiant la condition.

```python
def somme_pairs(n: int) -> int:
    # À compléter
```

Exemples attendus :
```python
print(somme_pairs(6))   # Affiche 12 (car 2 + 4 + 6 = 12)
print(somme_pairs(7))   # Affiche 12 (car 2 + 4 + 6 = 12)
print(somme_pairs(10))  # Affiche 30 (car 2 + 4 + 6 + 8 + 10 = 30)
```

---

## Exercice 3 — Arithmétique entière et division euclidienne

### Partie A : Rendu de monnaie

Un distributeur automatique doit rendre un montant entier en euros en utilisant le moins de pièces et billets possible. Il dispose de :

* Billets de 20 €
* Pièces de 2 €
* Pièces de 1 €

Compléter la fonction `rendre_monnaie(montant: int)` :

```python
def rendre_monnaie(montant: int):
    billets_20 = montant // 20
    reste = montant % 20
    pieces_2 = ...      # À compléter
    pieces_1 = ...      # À compléter
    
    print("Billets de 20€ :", billets_20, "| Pièces de 2€ :", pieces_2, "| Pièces de 1€ :", pieces_1)
```

Exemples attendus :
```python
rendre_monnaie(47)  # Affiche : Billets de 20€ : 2 | Pièces de 2€ : 3 | Pièces de 1€ : 1
rendre_monnaie(15)  # Affiche : Billets de 20€ : 0 | Pièces de 2€ : 7 | Pièces de 1€ : 1
```

### Partie B : Algorithme avec boucle `while` (soustractions successives)

On souhaite savoir combien de fois on peut soustraire un pas `p > 0` à un nombre `n >= 0` tant que `n >= p`. Cela correspond à la division entière de `n` par `p` réalisée à l'aide d'une boucle `while`.

Écrire une fonction `nb_soustractions(n: int, p: int) -> int` :

```python
def nb_soustractions(n: int, p: int) -> int:
    compteur = 0
    while ... :
        # À compléter
    return compteur
```

Exemple : pour `n = 14` et `p = 3` :

* `14 - 3 = 11` (1ère soustraction)
* `11 - 3 = 8` (2ème soustraction)
* `8 - 3 = 5` (3ème soustraction)
* `5 - 3 = 2` (4ème soustraction)
* `2 < 3` $\rightarrow$ arrêt.
* Le résultat renvoyé est `4`.

---

## Exercice 4 — Conditions et programme interactif

### Partie 1 : Fonction de décision

Écrire une fonction `categorie_sport(age: int) -> str` qui prend en paramètre l'âge d'un adhérent et renvoie :

* `"Erreur : âge invalide"` si `age < 0` ou `age > 120`.
* `"Senior"` si `age >= 18`.
* `"Junior"` si `14 <= age < 18`.
* `"Cadet"` si `10 <= age < 14`.
* `"Poussin"` si `0 <= age < 10`.

```python
def categorie_sport(age: int) -> str:
    # À compléter
```

### Partie 2 : Programme interactif complet

Écrire un programme Python complet qui :

1. Demande le prénom du sportif à l'utilisateur (`input()`).
2. Demande son âge à l'utilisateur (`input()`).
3. Convertit l'âge saisi en nombre entier (`int(...)`).
4. Appelle la fonction `categorie_sport` pour déterminer sa catégorie.
5. Affiche le récapitulatif sous la forme :  
   `"Sportif <prenom> (<age> ans) : Catégorie <categorie>"`

---

## 🌟 Exercice Bonus : Contrôle d'accès par mot de passe

Écrire une fonction `verifier_mot_de_passe(bon_mdp: str)` qui demande à un utilisateur de saisir un mot de passe avec les règles suivantes :

1. L'utilisateur a au maximum **3 tentatives**.
2. Tant que la saisie est incorrecte et qu'il reste des tentatives :
   * Afficher `"Mot de passe incorrect !"`
   * Indiquer le nombre d'essais restants.
3. Si le mot de passe saisi correspond à `bon_mdp`, la boucle s'arrête immédiatement et le programme affiche :  
   `"Accès autorisé !"`
4. Si les 3 tentatives sont épuisées sans succès, afficher :  
   `"Compte verrouillé : trop de tentatives échouées."`

```python
def verifier_mot_de_passe(bon_mdp: str):
    # À compléter
```

Exemple d'exécution :
```text
>>> verifier_mot_de_passe("secret123")
Entrez le mot de passe : test
Mot de passe incorrect ! (2 essais restants)
Entrez le mot de passe : secret123
Accès autorisé !
```
