# 📚 Cours de NSI : Les dictionnaires en Python

---

## 1. Introduction

Les **dictionnaires** (ou **tableaux associatifs**) sont des structures de données permettant de stocker des couples **clé : valeur**.
Contrairement aux listes qui sont indexées par des entiers (0, 1, 2...), les dictionnaires sont indexés par des **clés** (qui peuvent être des chaînes de caractères, des nombres, etc.).

C'est une structure essentielle qui fonctionne comme un vrai dictionnaire papier : on cherche un mot (**la clé**) pour obtenir sa définition (**la valeur**).

---

## 2. Création d'un dictionnaire

### ➤ Syntaxe

Un dictionnaire se définit avec des accolades `{}`. Chaque élément est une paire `clé : valeur`, séparée par une virgule.

```python
# Dictionnaire vide
vide = {}

# Dictionnaire représenant une personne
perso = {
    "nom": "Bond",
    "prenom": "James",
    "agent": 7
}

# Dictionnaire avec des types variés
notes = {
    "maths": 15,
    "anglais": 18,
    "sport": 12
}
```

### ➤ Clés et Valeurs

*   **Les clés** doivent être **uniques** et de type **immuable** (str, int, float, tuple...).
*   **Les valeurs** peuvent être de **n'importe quel type** (str, int, liste, autre dictionnaire...).

---

## 3. Accès aux valeurs

On accède à une valeur en utilisant sa **clé** entre crochets `[]`.

```python
print(perso["nom"])    # Affiche "Bond"
print(notes["maths"])  # Affiche 15
```

⚠️ **Attention :** Si la clé n'existe pas, Python renvoie une erreur `KeyError`.
Pour éviter cela, on peut utiliser la méthode `.get()` :

```python
print(perso.get("age"))        # Affiche None (pas d'erreur)
print(perso.get("age", 18))    # Affiche 18 (valeur par défaut)
```

---

## 4. Modification et ajout

Les dictionnaires sont **mutables** (modifiables). On peut changer la valeur associée à une clé existante ou créer une nouvelle paire.

```python
# Modification d'une valeur existante
perso["agent"] = "007" 

# Ajout d'une nouvelle clé
perso["ville"] = "Londres"
perso["actif"] = True

print(perso)
# {'nom': 'Bond', 'prenom': 'James', 'agent': '007', 'ville': 'Londres', 'actif': True}
```

---

## 5. Suppression

Il existe plusieurs façons de retirer des éléments :

```python
# del : supprime une paire par sa clé
del perso["actif"]

# pop() : supprime la clé et renvoie la valeur supprimée
ville = perso.pop("ville") 
# ville vaut "Londres", et la clé "ville" n'est plus dans le dictionnaire
```

---

## 6. Parcours d'un dictionnaire

Comme les listes, on peut parcourir un dictionnaire avec une boucle `for`.

### ➤ Parcourir les clés (comportement par défaut)

```python
for matiere in notes:
    print(matiere)
# Affiche : maths, anglais, sport
```

### ➤ Parcourir les valeurs avec `.values()`

```python
for note in notes.values():
    print(note)
# Affiche : 15, 18, 12
```

### ➤ Parcourir les couples (clé, valeur) avec `.items()`

C'est souvent la méthode la plus utile.

```python
for matiere, note in notes.items():
    print(f"En {matiere}, la note est {note}")
```

---

## 7. Appartenance (in)

Pour vérifier si une **clé** est présente dans le dictionnaire :

```python
if "maths" in notes:
    print("La note de maths est présente")
```

---

## 8. Méthodes utiles

| Méthode | Rôle | Exemple |
| :--- | :--- | :--- |
| `len(d)` | Nombre de paires | `len(notes) → 3` |
| `d.keys()` | Liste des clés | `notes.keys()` |
| `d.values()` | Liste des valeurs | `notes.values()` |
| `d.items()` | Liste des couples | `notes.items()` |
| `d.clear()` | Vide le dictionnaire | `d.clear()` |

---

## 9. Comparaison Liste vs Dictionnaire

| Caractéristique | Liste (`list`) | Dictionnaire (`dict`) |
| :--- | :--- | :--- |
| **Syntaxe** | `[val1, val2]` | `{cle1: val1, cle2: val2}` |
| **Accès** | Par indice `L[0]` | Par clé `D["nom"]` |
| **Ordre** | Ordonné | Ordonné (depuis Python 3.7) |
| **Recherche** | Lente (parcours complet) | Très rapide (immédiat) |
| **Usage** | Collections d'éléments | Association de données |
