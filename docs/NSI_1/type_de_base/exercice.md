# Série d’exercices : Listes et tuples en Python



## 🟢 **Niveau 1 — Découverte et manipulation de base**

### **Exercice 1 : Création et affichage**

1. Crée une liste `fruits` contenant `"pomme"`, `"banane"`, `"cerise"`.
2. Affiche le premier et le dernier élément.
3. Ajoute `"kiwi"` à la fin.
4. Remplace `"banane"` par `"orange"`.
5. Supprime `"pomme"` de la liste.
6. Affiche la liste finale.

👉 *Objectif : maîtriser les opérations de base (`append`, `remove`, `index`, accès par indices)*



### **Exercice 2 : Moyenne de notes**

Écris un programme qui :

1. Crée une liste `notes = [14, 9, 12, 16, 10]`
2. Calcule la moyenne des notes (utilise `sum()` et `len()`).
3. Affiche la note maximale et minimale.

👉 *Objectif : manipuler des listes numériques et utiliser les fonctions intégrées.*



### **Exercice 3 : Parcours d’une liste**

Écris un programme qui affiche chaque élément d’une liste et son indice sous la forme :

```
Indice 0 → pomme
Indice 1 → orange
Indice 2 → kiwi
```

👉 *Objectif : utiliser une boucle `for` avec `range(len(liste))`.*



### **Exercice 4 : Saisie utilisateur**

Demande à l’utilisateur 3 prénoms et stocke-les dans une liste.
Affiche ensuite la liste complète.

👉 *Objectif : construire une liste dynamiquement avec `append()`.*



## 🟡 **Niveau 2 — Approfondissement et traitement**

### **Exercice 5 : Inversion et tri**

1. Crée une liste de nombres `[5, 1, 9, 3, 7]`.
2. Trie la liste dans l’ordre croissant et affiche-la.
4. Inverse la liste avec `reverse()`.

👉 *Objectif : comprendre `sort()` et `reverse()`.*



### **Exercice 6 : Filtrage**

Écris un programme qui, à partir de la liste :

```python
nombres = [5, 12, 7, 3, 18, 9, 2]
```

crée une nouvelle liste `pairs` contenant uniquement les nombres pairs.

👉 *Indice : utiliser une boucle et le test `n % 2 == 0`.*



### **Exercice 7 : Comptage**

Écris un programme qui compte le nombre de fois où `"e"` apparaît dans la liste :

```python
mots = ["elle", "est", "en", "été"]
```

👉 *Objectif : parcours + conditions + variable compteur.*



### **Exercice 8 : Liste de listes**

Crée une **matrice 3x3** :

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Affiche la somme de la deuxième ligne et l’élément au centre.

👉 *Objectif : travailler sur les listes imbriquées.*



## 🔵 **Niveau 3 — Tuples et données structurées**

### **Exercice 9 : Coordonnées**

1. Crée un tuple `point = (3, 5)`
2. Affecte ses valeurs à deux variables `x` et `y` (unpacking).
3. Affiche :

   ```
   Le point a pour coordonnées x=3 et y=5
   ```

👉 *Objectif : apprendre le déballage de tuples.*



### **Exercice 10 : Données d’élèves**

Crée une liste de tuples représentant des élèves et leurs notes :

```python
eleves = [("Alice", 15), ("Bob", 12), ("Clara", 17)]
```

Affiche chaque nom avec sa note sous la forme :

```
Alice a obtenu 15
Bob a obtenu 12
Clara a obtenu 17
```

👉 *Objectif : parcourir une liste de tuples et déballer les valeurs.*



### **Exercice 11 : Recherche d’un élément**

Écris une fonction :

```python
def cherche(liste, element):
    ...
```

qui renvoie `True` si `element` est dans la liste, sinon `False`.
Teste-la avec :

```python
cherche([1, 4, 9, 2], 9)  # → True
cherche([1, 4, 9, 2], 5)  # → False
```

👉 *Objectif : comprendre les recherches dans une séquence.*




### **Exercice 12 : Conversion**

Écris un programme qui :

1. Crée un tuple `t = (1, 2, 3, 4)`
2. Le convertit en liste.
3. Ajoute `5` à la liste.
4. Reconvertit le résultat en tuple.

👉 *Objectif : conversion entre types (`list()` / `tuple()`).*




## 🔴 **Niveau 4 — Raisonnement algorithmique**

### **Exercice 13 : Moyenne générale**

Écris un programme qui gère plusieurs élèves et leurs notes à l’aide d’une **liste de tuples** :

```python
notes_eleves = [("Alice", [15, 14, 13]), ("Bob", [10, 12, 11]), ("Clara", [18, 17, 19])]
```

Le programme doit afficher pour chaque élève :

```
Alice → moyenne : 14.0
Bob → moyenne : 11.0
Clara → moyenne : 18.0
```

👉 *Objectif : boucles imbriquées, calcul de moyenne, tuples + listes.*



### **Exercice 14 : Rotation de liste**

Écris une fonction `rotation(liste)` qui décale tous les éléments d’une liste vers la gauche.
Exemple :

```python
[1, 2, 3, 4]  →  [2, 3, 4, 1]
```

👉 *Objectif : travailler sur les indices et la logique algorithmique.*



### **Exercice 15 : Maximum d’une matrice**

Écris une fonction `max_matrice(m)` qui renvoie la plus grande valeur d’une **matrice** (liste de listes).

Exemple :

```python
m = [[4, 7, 2], [9, 3, 8], [1, 6, 5]]
max_matrice(m)  →  9
```

👉 *Objectif : parcours imbriqué et compréhension de listes 2D.*


## **Niveau 5 — challenge**

### 🔥 **Exercice 1 – Rotation de liste**

Écrire une fonction `rotation(liste, n)` qui **décale** la liste vers la droite de `n` positions.

Exemple :

```python
>>> rotation([1, 2, 3, 4, 5], 2)
[4, 5, 1, 2, 3]
```

⚠️ Contraintes :

* Ne pas utiliser `append()` ni `pop()` dans leur version avec indice négatif.
* L’algorithme doit fonctionner pour n'importe quelle taille de liste.



### 🔥 **Exercice 2 – Aplatir une liste imbriquée**

Écrire une fonction `aplatir(liste)` qui transforme une liste de listes en une **liste simple**.

Exemple :

```python
>>> aplatir([[1,2], [3,4], [5,6]])
[1, 2, 3, 4, 5, 6]
```

⚠️ Version difficile :
La liste peut contenir des sous-listes **de profondeur inconnue**, par exemple :

```python
[[1, [2, 3]], [4, [5, [6]]]]
```



### 🔥 **Exercice 3 – Matrice : diagonale principale**

On vous donne une **matrice carrée** sous forme de liste de listes.
Écrire une fonction qui retourne la **somme de la diagonale principale**.

Exemple :

```python
>>> diag([[1,2,3],
          [4,5,6],
          [7,8,9]])
15
```

⚠️ Extension possible :

* Vérifier que la matrice est bien carrée avant de calculer la somme (sinon afficher un message d’erreur).



### 🔥 **Exercice 4 – Détection de motif**

Écrire une fonction `contient_motif(liste, motif)` qui vérifie si **le motif apparaît tel quel dans la liste**.

Exemple :

```python
>>> contient_motif([1,2,3,4,5,3,4], [3,4])
True
>>> contient_motif([1,2,3,4], [4,3])
False
```

⚠️ Ce n’est pas juste "des mêmes éléments" : l’ordre compte.
(Comme la recherche d’un sous-mot dans une chaîne.)
