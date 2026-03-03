# 🔄 Cours : Introduction à la Récursivité

---

# 1. 🪞 Qu'est-ce que la récursivité ?

Une fonction est dite **récursive** lorsqu'elle **s'appelle elle-même** dans sa propre définition.

C'est une technique puissante qui permet de résoudre des problèmes en les **décomposant en sous-problèmes** de même nature, mais plus petits.

??? Example "Analogie du quotidien"
    Imaginez que vous voulez savoir combien de personnes sont devant vous dans une file d'attente.
    
    * Si la file est vide → il y a **0** personne devant vous.
    * Sinon → il y a **1 personne** + le nombre de personnes devant *elle*.
    
    Vous venez de raisonner de façon récursive !

---

# 2. 🏗️ La structure d'une fonction récursive

Toute fonction récursive bien écrite doit contenir **deux éléments obligatoires** :

| Élément | Rôle |
|:--------|:-----|
| **Cas de base** | La condition d'arrêt — répond directement sans rappeler la fonction |
| **Appel récursif** | La fonction se rappelle elle-même sur un problème **plus petit** |

!!! warning "Danger : la récurrence infinie"
    Si une fonction récursive n'a pas de cas de base, elle s'appellera **indéfiniment**,
    ce qui provoquera une erreur Python : `RecursionError: maximum recursion depth exceeded`.
    
    C'est l'équivalent informatique d'une boucle infinie !

---

# 3. 🔢 Exemple 1 — Compte à rebours

## Version itérative (avec une boucle)

```python
def compte_a_rebours_iteratif(n):
    while n >= 0:
        print(n)
        n -= 1
```

## Version récursive

```python
def compte_a_rebours(n):
    if n < 0:          # ← Cas de base : on arrête
        return
    print(n)
    compte_a_rebours(n - 1)  # ← Appel récursif sur n-1
```

Appel : `compte_a_rebours(3)`

```
Appel compte_a_rebours(3) → affiche 3
  Appel compte_a_rebours(2) → affiche 2
    Appel compte_a_rebours(1) → affiche 1
      Appel compte_a_rebours(0) → affiche 0
        Appel compte_a_rebours(-1) → cas de base, on s'arrête
```

---

# 4. 🔢 Exemple 2 — La factorielle

La **factorielle** de n (notée n!) est définie ainsi :

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

Avec **0! = 1** par convention.

Par exemple : **4! = 4 × 3 × 2 × 1 = 24**

## Vision récursive

On peut remarquer que :

```
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1 × 0!
0! = 1   ← cas de base
```

La factorielle de n, c'est donc : **n × factorielle(n-1)** !

## Implémentation Python

```python
def factorielle(n):
    if n == 0:              # ← Cas de base
        return 1
    return n * factorielle(n - 1)  # ← Appel récursif
```

## Trace d'exécution de `factorielle(4)`

```
factorielle(4)
  = 4 × factorielle(3)
        = 3 × factorielle(2)
              = 2 × factorielle(1)
                    = 1 × factorielle(0)
                                = 1    ← cas de base
                    = 1 × 1 = 1
              = 2 × 1 = 2
        = 3 × 2 = 6
  = 4 × 6 = 24
```

👉 Les appels s'**empilent** jusqu'au cas de base, puis les résultats **remontent** en chaîne.

---

# 5. 📐 Schéma mental : la pile d'appels

Chaque appel récursif est mis en attente dans ce qu'on appelle la **pile d'appels** (*call stack*).

```
┌────────────────────────┐  ← dernier appel (cas de base)
│ factorielle(0) → 1     │
├────────────────────────┤
│ factorielle(1) → 1×1   │
├────────────────────────┤
│ factorielle(2) → 2×1   │
├────────────────────────┤
│ factorielle(3) → 3×2   │
├────────────────────────┤
│ factorielle(4) → 4×6   │  ← premier appel
└────────────────────────┘
```

Les fonctions s'accumulent jusqu'au cas de base, puis les résultats remontent de bas en haut.

---

# 6. ✅ Récursivité vs Itération

Les deux approches permettent de résoudre le même problème :

| | Itératif | Récursif |
|:--|:--------:|:--------:|
| Utilise | une boucle `for`/`while` | un appel à soi-même |
| Lisibilité | Souvent plus directe | Plus élégante pour certains problèmes |
| Risque | Boucle infinie | Récurrence infinie |
| Exemple naturel | Parcourir une liste | Diviser pour régner |

!!! tip "Quand préférer la récursivité ?"
    La récursivité est particulièrement adaptée lorsque le problème se **décompose naturellement** en sous-problèmes identiques mais plus petits, comme :

    * La recherche dichotomique (diviser la liste en deux)
    * Le parcours d'arbres
    * Les algorithmes de type « diviser pour régner »

---

# 7. 📝 À retenir

!!! success "Les 3 règles d'une récursion correcte"
    1. **Un cas de base** qui arrête les appels récursifs
    2. **Un appel récursif** qui progresse vers le cas de base
    3. **Le problème se réduit** à chaque appel (n-1, n//2, etc.)

Dans le TP qui suit, vous allez utiliser la récursivité pour réécrire la recherche dichotomique :
à chaque appel, on divise par deux la zone de recherche jusqu'à trouver la valeur (cas de base).
