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

```python
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])   # pomme
print(fruits[1])   # banane
print(fruits[-1])  # cerise (depuis la fin)
```

---

### 2.2 Modification

```python
fruits[1] = "orange"      # Remplace "banane"
print(fruits)             # ["pomme", "orange", "cerise"]
```

---

### 2.3 Ajout et suppression

```python
fruits.append("kiwi")     # ajoute à la fin
fruits.insert(1, "mangue")# insère à la position 1
fruits.remove("orange")   # supprime un élément par valeur
del fruits[0]             # supprime par indice
fruits.pop()              # retire le dernier
```

---

### 2.4 Parcours d’une liste

#### a) Avec `for`

```python
for fruit in fruits:
    print(fruit)
```

#### b) Avec `range()`

```python
for i in range(len(fruits)):
    print(i, fruits[i])
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

⚠️ Attention : deux variables peuvent **pointer vers la même liste** !

```python
a = [1, 2, 3]
b = a        # b est un alias de a
b[0] = 99
print(a)     # affiche [99, 2, 3]
```

Pour copier sans lien :

```python
b = a.copy()
```

---

### 2.7 Les listes imbriquées

```python
matrice = [[1,2,3], [4,5,6], [7,8,9]]
print(matrice[1][2])  # 6
```

---

## 3. Les tuples (`tuple`)

### ➤ Définition

Un **tuple** est une **structure de données ordonnée mais non modifiable (immuable)**.

```python
coordonnees = (10, 20)
jour = ("lundi", "mardi", "mercredi")
```

### ➤ Caractéristiques

* **Ordonné** (indices comme les listes)
* **Immuable** : on **ne peut pas modifier, ajouter ou supprimer** d’éléments
* **Hétérogène**

---

### 3.1 Création

```python
t = (1, 2, 3)
t2 = 1, 2, 3       # les parenthèses sont facultatives
t3 = (5,)          # un seul élément → la virgule est obligatoire
```

---

### 3.2 Accès aux éléments

```python
coord = (12.4, 5.7)
print(coord[0])  # 12.4
print(coord[1])  # 5.7
```

---

### 3.3 Immuabilité

```python
t = (1, 2, 3)
# t[0] = 10  ❌ provoque une erreur : tuple immuable
```

---

### 3.4 Déballage (unpacking)

Très utile en NSI pour affecter plusieurs variables à la fois :

```python
x, y = (3, 4)
print(x)  # 3
print(y)  # 4
```

Ou encore :

```python
nom, age, ville = ("Alice", 17, "Paris")
```

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

