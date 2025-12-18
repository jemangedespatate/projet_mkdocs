# Série d’exercices : Les dictionnaires en Python

---

## 🟢 **Niveau 1 — Bases et manipulation**

### **Exercice 1 : Mon premier dictionnaire**

1. Crée un dictionnaire `film` avec les clés suivantes :   
    * `"titre"` : "Inception"
    * `"realisateur"` : "Christopher Nolan"
    * `"annee"` : 2010

2. Affiche le réalisateur du film.
3. Modifie l'année pour `2011` (une erreur s'est glissée !).
4. Ajoute une clé `"genre"` avec la valeur `"Science-fiction"`.
5. Supprime la clé `"annee"`.

👉 *Objectif : syntaxe `{}`, accès `[]`, modification, ajout et suppression.*

---

### **Exercice 2 : Panier de courses**

Voici un dictionnaire représentant un panier de courses avec les prix des articles :

```python
panier = {"pain": 1.20, "lait": 0.90, "pommes": 2.50}
```

1. Ajoute "oeufs" à 3.10 €.
2. Le prix du "lait" a augmenté, passe-le à 1.00 €.
3. Affiche le prix total du panier (somme des valeurs).

👉 *Objectif : manipulation de valeurs numériques.*

---

## 🟡 **Niveau 2 — Parcours et logique**

### **Exercice 3 : L'inventaire**

On dispose d'un inventaire de magasin :

```python
stock = {"cahiers": 50, "stylos": 120, "gommes": 30, "règles": 15}
```

1. Affiche chaque article et sa quantité sous la forme : `Article : cahiers -> Quantité : 50`.
2. Calcule le nombre total d'objets dans le stock.
3. Affiche les articles dont le stock est inférieur à 40 (alerte stock bas !).

👉 *Objectif : utiliser une boucle `for` avec `.items()` et une condition.*

---

### **Exercice 4 : Compteur de lettres**

Écris une fonction `compte_lettres(texte)` qui prend une chaîne de caractères en paramètre et retourne un dictionnaire indiquant le nombre d'occurrences de chaque lettre.

Exemple :
```python
texte = "baba"
# Résultat attendu : {'b': 2, 'a': 2}
```

*Indice : Tu peux parcourir une chaîne de caractères directement avec une boucle `for`.*

👉 *Objectif : algorithme de comptage classique.*

---

## 🔵 **Niveau 3 — Structures imbriquées**

### **Exercice 5 : Base de données élèves**

On gère une classe d'élèves sous forme de liste de dictionnaires :

```python
classe = [
    {"nom": "Dupont", "note": 14},
    {"nom": "Durand", "note": 8},
    {"nom": "Martin", "note": 16}
]
```

1. Ajoute l'élève `{"nom": "Petit", "note": 12}` à la liste.
2. Écris un boucle qui affiche le nom des élèves ayant la moyenne (note >= 10).
3. Calcule la moyenne générale de la classe.

👉 *Objectif : manipuler une liste de dictionnaires.*

---

### **Exercice 6 : Système de traduction**

Crée un mini-traducteur anglais-français.
1. Crée un dictionnaire `lexique` : `{"hello": "bonjour", "cat": "chat", "dog": "chien", "red": "rouge"}`.
2. Écris une fonction `traduire(mot)` qui retourne la traduction française si le mot existe, ou "Mot inconnu" sinon (utilise `.get()`).

---

## 🔴 **Niveau 4 — Algorithmique avancée**

### **Exercice 7 : Inverser un dictionnaire**

Écris une fonction `inverse(d)` qui prend un dictionnaire et échange ses clés et ses valeurs.
Exemple : `{"a": 1, "b": 2}` devient `{1: "a", 2: "b"}`.

*Question bonus : Que se passe-t-il si deux clés avaient la même valeur ?*

---

### **Exercice 8 : Scrabble complet**

Voici les points au Scrabble :
```python
points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, 
    "J": 8, "K": 10, "L": 1, "M": 2, "N": 1, "O": 1, "P": 3, "Q": 8, "R": 1, 
    "S": 1, "T": 1, "U": 1, "V": 4, "W": 10, "X": 10, "Y": 10, "Z": 10
}
```

Écris une fonction `score(mot)` qui calcule le score d'un mot (en majuscules).
Exemple : `score("PYTHON")` doit renvoyer 20.

👉 *Objectif : parcours de chaîne, accès dictionnaire.*

---

## 🔥 **Niveau 5 - Challenge**

### **Exercice 9 : Anagrammes**

Deux mots sont des anagrammes s'ils contiennent les mêmes lettres avec les mêmes fréquences (ex: "CHIEN" et "NICHE").

Écris une fonction `sont_anagrammes(mot1, mot2)` qui utilise des dictionnaires pour vérifier si `mot1` et `mot2` sont des anagrammes.

*Indice : compte les lettres de chaque mot dans deux dictionnaires et compare-les.*
