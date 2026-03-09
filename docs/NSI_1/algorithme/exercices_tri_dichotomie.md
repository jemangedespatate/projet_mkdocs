# ✍️ Exercices : Tris, Complexité et Recherche Dichotomique

**Rappel :** Les exercices ci-dessous sont à réaliser en autonomie ou en binôme après avoir suivi la présentation.

---

## 🧩 Exercice 1 : Trace de l'algorithme de Tri par Insertion
Soit la liste suivante : `L = [5, 12, 8, 3, 10]`.  
On souhaite la trier en utilisant les fonctions `tri_insert` et `insert_tranche_triee` vues en cours.

1.  **Détailler l'état de la liste** après chaque appel à la fonction `insert_tranche_triee(l, i, comp)`.
    *   *i = 0* : 
    *   *i = 1* : 
    *   *i = 2* : 
    *   *i = 3* : 
    *   *i = 4* : 
2.  Dans `insert_tranche_triee`, pour `i = 3` (insertion du nombre 3), **combien de décalages** (l[j] = l[j-1]) sont effectués ?
3.  À quoi sert le `assert est_triee(l[:i], comp)` au début de la fonction ?

---

## 🐢 Exercice 2 : Analyse de Complexité (Tris)
Imaginez que trier une liste de **100** éléments avec le tri par sélection prend **0,01 seconde**.

1.  D'après la théorie du **N²** (complexité quadratique), combien de secondes faudra-t-il environ pour trier une liste de :
    *   **1 000** éléments ?
    *   **10 000** éléments ?
    *   **1 000 000** éléments ?
2.  Si la liste est **déjà triée**, quel algorithme est le plus efficace entre :
    *   Le tri par **sélection** ? (Vérifie toujours chaque élément).
    *   Le tri par **insertion** ? (Détecte immédiatement que l'élément est à sa place).
    *   *Expliquez pourquoi.*

---

## 🎯 Exercice 3 : Recherche Dichotomique "à la main"
On a la liste triée : `L = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`.
On cherche la valeur **56** par recherche dichotomique.

1.  Quelles seront les valeurs successives des variables `debut`, `fin` et `milieu` ?
    *   *Étape 1 :* debut = ..., fin = ..., milieu = ..., L[milieu] = ...
    *   *Étape 2 :* ...
    *   *Étape 3 :* ...
2.  Combien de comparaisons ont été nécessaires ?
3.  Combien en aurait-il fallu avec une recherche classique (séquentielle) ?

---

## 💻 Exercice 4 : Mission "Plus ou Moins" (Implémentation)
Le jeu du "Plus ou Moins" consiste à deviner un nombre entre 1 et 1 000.  
Si vous jouez de manière **optimale** (stratégie dichotomique) :

1.  Combien de coups au **maximum** vous faut-il pour gagner ?
2.  **Code de défi :** Écrivez une fonction Python `nombre_etapes_max(n: int) -> int` qui prend en paramètre la taille de la liste `n` et renvoie le nombre maximum d'étapes nécessaires pour trouver un élément par dichotomie.
    *   *Aide :* On divise par 2 à chaque fois jusqu'à arriver à 1.

---

## 🚀 Pour aller plus loin (Facultatif)
Modifiez la fonction `recherche_dicho` pour qu'elle renvoie l'**index de la première occurrence** si le nombre cherché apparaît plusieurs fois dans la liste triée (ex: `[1, 2, 2, 2, 3]`).
