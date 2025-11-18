# 🧮 Cours de NSI : Les listes et les tuples en Python

---

## 1. Introduction

En Python, les **structures de données séquentielles** (comme les **listes** et les **tuples**) permettent de **regrouper plusieurs valeurs dans une seule variable**.

Elles sont **ordonnées**, c’est-à-dire que les éléments sont rangés dans un ordre précis, et cet ordre est conservé.

---

## 2. Les listes (`list`)

### ➤ Définition

Une **liste** est une **structure de données modifiable (mutable)** contenant plusieurs éléments **ordonnés**.

```python
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "cerise"]
melange = ["texte", 42, True]
```

### ➤ Caractéristiques

* **Ordonnée** : les éléments ont un indice (index).
* **Mutable** : on peut **modifier** son contenu.
* **Hétérogène** : peut contenir différents types.

---

### 2.1 Accès aux éléments

On peut accéder aux éléments d’une liste en utilisant leur indice : les indices commencent à 0 en partant du début, et on peut aussi utiliser des indices négatifs pour accéder aux éléments depuis la fin.

```python
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])   # pomme
print(fruits[1])   # banane
print(fruits[-1])  # cerise (depuis la fin)
```

---

### 2.2 Modification

On peut modifier un élément d’une liste en utilisant son indice. Ici, l’élément à l’indice 1 ("banane") est remplacé par "orange".

```python
fruits[1] = "orange"      # Remplace "banane"
print(fruits)             # ["pomme", "orange", "cerise"]
```

---

### 2.3 Ajout et suppression

- Ajouter : append met un élément à la fin, insert à une position précise.

- Supprimer : remove supprime par valeur, del ou pop suppriment par position (indice).

```python
fruits.append("kiwi")     # ajoute à la fin
fruits.insert(1, "mangue")# insère à la position 1
fruits.remove("orange")   # supprime un élément par valeur
del fruits[0]             # supprime par indice
fruits.pop()              # retire le dernier
```

!!! note "explication"

    **Liste initiale :**

    ```
    ["pomme", "orange", "cerise"]
    Indices :  0        1        2
    ```

    **1️⃣ Ajouter avec `append("kiwi")` :**

    ```
    ["pomme", "orange", "cerise", "kiwi"]
    Indices :  0        1        2       3
    ```

    **2️⃣ Ajouter avec `insert(1, "mangue")` :**

    ```
    ["pomme", "mangue", "orange", "cerise", "kiwi"]
    Indices :  0       1        2        3       4
    ```

    **3️⃣ Supprimer par valeur `remove("orange")` :**

    ```
    ["pomme", "mangue", "cerise", "kiwi"]
    Indices :  0        1        2       3
    ```

    **4️⃣ Supprimer par indice `del fruits[0]` :**

    ```
    ["mangue", "cerise", "kiwi"]
    Indices :   0        1       2
    ```

    **5️⃣ Supprimer le dernier élément avec `pop()` :**

    ```
    ["mangue", "cerise"]
    Indices :   0       1
    ```
    
---

### 2.4 Parcours d’une liste

Parcourir une liste signifie **passer en revue tous ses éléments** pour les utiliser ou les afficher. On peut le faire de plusieurs façons.

#### a) Parcours direct avec `for`

```python
fruits = ["mangue", "cerise"]

for fruit in fruits:      # pour chaque élément de la liste
    print(fruit)          # on affiche l'élément
```

💡 **Explication :**
Ici, `fruit` prend **successivement la valeur de chaque élément** de la liste. C’est simple et lisible.

**Affichage :**

```
mangue
cerise
```

---

#### b) Parcours avec `range()` et indices

```python
fruits = ["mangue", "cerise"]

for i in range(len(fruits)):  # i parcourt les indices de 0 à len(fruits)-1
    print(i, fruits[i])       # on affiche l'indice et l'élément correspondant
```

💡 **Explication :**

* `len(fruits)` donne la **taille de la liste**.
* `range(len(fruits))` crée une **suite de nombres correspondant aux indices**.
* `fruits[i]` permet d’accéder à l’élément à l’indice `i`.

**Affichage :**

```
0 mangue
1 cerise
```

---

### 2.5 Fonctions utiles

| Fonction            | Rôle                           | Exemple                       |
| ------------------- | ------------------------------ | ----------------------------- |
| `len(l)`            | nombre d’éléments              | `len(fruits)` → `3`           |
| `sum(l)`            | somme des éléments numériques  | `sum([2, 3, 5])` → `10`       |
| `min(l)` / `max(l)` | plus petit / grand             | `max([4,7,2])` → `7`          |
| `sorted(l)`         | trie la liste (nouvelle liste) | `sorted([3,1,2])` → `[1,2,3]` |
| `l.sort()`          | trie sur place                 | `l.sort()`                    |
| `l.reverse()`       | inverse l’ordre                | `l.reverse()`                 |

---

### 2.6 Copies et alias

⚠️ **Attention : deux variables peuvent pointer vers la même liste !**

```python
a = [1, 2, 3]
b = a        # b devient un alias de a
b[0] = 99
print(a)     # affiche [99, 2, 3]
```

💡 **Explication :**

* Ici, `b` ne crée pas une nouvelle liste, mais **référence exactement la même liste que `a`**.
* Donc, toute modification via `b` se voit aussi dans `a`.

---

#### Copier une liste pour éviter ce lien

```python
a = [1, 2, 3]
b = a.copy()  # crée une **nouvelle liste indépendante**
b[0] = 99
print(a)      # affiche [1, 2, 3]
print(b)      # affiche [99, 2, 3]
```

💡 **Explication :**

* `copy()` crée une **copie indépendante** de la liste.
* Les modifications sur `b` **n’affectent pas `a`**.

---

### 2.7 Les listes imbriquées

Une **liste peut contenir d’autres listes**. On parle alors de **liste imbriquée**, utile pour représenter des tableaux ou des matrices.

```python
# Définition d'une matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accéder à un élément : ligne 1, colonne 2
print(matrice[1][2])  # affiche 6
```

💡 **Explication :**

* `matrice[1]` sélectionne la **deuxième ligne** : `[4, 5, 6]`.
* `matrice[1][2]` sélectionne le **troisième élément** de cette ligne : `6`.

---

## 3. Les tuples (`tuple`)

### ➤ Définition

Un **tuple** est une **liste spéciale** :

* les éléments sont **ordonnés** (comme dans une liste)
* mais **on ne peut pas les modifier** une fois créés (immuable).

```python
coordonnees = (10, 20)                # tuple de deux nombres
jours = ("lundi", "mardi", "mercredi")  # tuple de chaînes de caractères
```

💡 **Explication :**

* Les tuples ressemblent aux listes, mais **ils sont figés** : on ne peut pas changer leurs valeurs, ajouter ou supprimer un élément.

---

### ➤ Caractéristiques principales

* **Ordonné** : chaque élément a un **indice** (0, 1, 2, …).
* **Immuable** : impossible de modifier, ajouter ou supprimer un élément.
* **Hétérogène** : peut contenir différents types de données (nombres, chaînes, booléens…).

---

### 3.1 Création d’un tuple

```python
t = (1, 2, 3)       # tuple avec parenthèses
t2 = 1, 2, 3        # parenthèses facultatives
t3 = (5,)           # un seul élément → **la virgule est obligatoire**
```

💡 **Explication :**

* Les tuples peuvent être **créés avec ou sans parenthèses**, sauf pour un élément unique : `(5,)` est nécessaire pour que Python comprenne que c’est un tuple.

---

### 3.2 Accès aux éléments

```python
coord = (12.4, 5.7)
print(coord[0])  # 12.4
print(coord[1])  # 5.7
```

💡 **Explication :**

* Les tuples sont **ordonnés** : chaque élément a un indice.
* L’accès se fait comme dans une liste, avec `[]`.

---

### 3.3 Immuabilité

```python
t = (1, 2, 3)
# t[0] = 10  ❌ provoque une erreur : tuple immuable
```

💡 **Explication :**

* Les tuples sont **immuables**, donc on **ne peut pas modifier leurs éléments** après création.

---

### 3.4 Déballage (unpacking)

Le **déballage** permet d’affecter facilement plusieurs variables à partir d’un tuple :

```python
x, y = (3, 4)
print(x)  # 3
print(y)  # 4
```

On peut aussi l’utiliser pour des tuples plus grands :

```python
nom, age, ville = ("Alice", 17, "Paris")
print(nom)   # Alice
print(age)   # 17
print(ville) # Paris
```

💡 **Astuce visuelle :**

* Pensez au tuple comme un **ensemble de cases alignées**.
* Le déballage **copie chaque valeur dans la variable correspondante**.

---

## 4. Comparaison liste / tuple

| Caractéristique     | Liste (`list`)     | Tuple (`tuple`)                          |
| ------------------- | ------------------ | ---------------------------------------- |
| Ordonnée            | ✅                  | ✅                                        |
| Modifiable          | ✅                  | ❌                                        |
| Taille variable     | ✅                  | ❌                                        |
| Syntaxe             | `[]`               | `()`                                     |
| Rapidité            | plus lente         | plus rapide (lecture seule)              |
| Utilisation typique | données à modifier | données fixes (coordonnées, constantes…) |

---

## 5. Conversion entre types

```python
t = (1, 2, 3)
l = list(t)     # tuple → liste
print(l)

l2 = [4, 5, 6]
t2 = tuple(l2)  # liste → tuple
print(t2)
```

