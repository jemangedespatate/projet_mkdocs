---
marp: true
theme: default
paginate: true
backgroundColor: #fff
footer: "NSI Premiere - Tris & Recherche"
---

# 📊 Diaporama : Tris, Complexité et Recherche Dichotomique

**Thème :** Algorithmique  
**Niveau :** Première NSI  
**Durée estimée :** 2 heures  

---

## 📅 Au programme aujourd'hui
1.  **Rappel sur les Tris** : Zoom sur le tri par insertion.
2.  **Introduction à la Complexité** : Pourquoi certains programmes sont-ils plus lents ?
3.  **La Recherche Dichotomique** : Comment être (très) efficace.
4.  **Analyse de performance** : Est-ce vraiment mieux ?

---

# 1. 🔍 Rappel : Le Tri par Insertion

> **Question de réflexion :**  
> Comment trieriez-vous naturellement un jeu de cartes dans votre main ?

---

## Principe du Tri par Insertion
L'idée : On parcourt la liste et on insère chaque élément à sa place dans la partie déjà triée.

---

## Principe du Tri par Insertion
**Décomposition de l'algorithme**
Pour transformer cette idée en code, nous allons séparer le tri en deux fonctions :
1.  Une fonction qui gère le **parcours** de la liste.
2.  Une fonction qui gère l'**insertion** d'un élément précis.

---

## 💻 À vous de jouer : La fonction principale

Complétez le parcours de la liste pour appeler l'insertion à chaque étape :

```python
def tri_insert(l: list[int], comp):
    """
    Parcourt la liste et insère chaque élément i 
    dans la tranche déjà triée l[0:i].
    """
    # parcourir chaque index i de la liste l
    for ... in range(...):
        # appeler la fonction d'insertion pour l'index i
        insert_tranche_triee(..., ..., ...)
```

---

## 💻 À vous de jouer : L'insertion (1/2)

Complétez le début de la fonction qui prépare l'insertion de l'élément `l[i]` :

```python
def insert_tranche_triee(l: list, i: int, comp):
    """
    Insère l[i] à sa place dans l[0:i]
    """
    # stocker la valeur à insérer (l[i]) dans une variable tmp
    tmp = ...
    # initialiser l'index de recherche j à i
    j = ...
```

---

## 💻 À vous de jouer : L'insertion (2/2)

Complétez la boucle de décalage vers la droite :

```python
    # Tant qu'on n'est pas au début ET que l'élément de gauche 
    # est plus "grand" que notre valeur
    while j > 0 and ... > ...:
        # décaler l'élément l[j-1] vers la position l[j]
        l[...] = l[...]
        # décrémenter j
        j = ...
        
    # placer la valeur tmp à sa position finale l[j]
    l[...] = ...
```

---

## 📝 Exercice Rapide
**Question :** Si on trie `[5, 8, 2, 4]`, quel sera l'état de la liste après l'appel de `insert_tranche_triee` pour `i = 2` ?

---

# 2. 🐢 Introduction à la Complexité

> **Question de réflexion :**  
> Si un programme met 1 seconde pour traiter 1000 noms, combien de temps mettra-t-il pour 1 million de noms ?  
> Est-ce forcément proportionnel ?

---

## Qu'est-ce que la complexité ?
C'est une mesure du **nombre d'opérations élémentaires** (comparaisons, affectations) que doit faire l'ordinateur.

On ne mesure pas en secondes (trop dépendant de la machine), mais en **évolution du nombre d'opérations** selon la taille $N$ des données.

---

## 📏 Ordre de grandeur : Le Tri
Dans nos tris (sélection, insertion), on a souvent :
1.  Une boucle (parcours de la liste).
2.  **DANS** cette boucle, une autre boucle (recherche du min ou décalage).

> **Question :** Si on a $N$ tours de boucle, et que chaque tour fait lui-même $N$ opérations, quel est le total ?

---

## 📏 La complexité quadratique ($N^2$)

- Environ $N \times N = N^2$ opérations.
- Doublez la taille $\rightarrow$ Temps $\times 4$.
- Décuplez la taille $\rightarrow$ Temps $\times 100$.

> **Question :** Pourquoi est-ce un problème pour des données géantes (Big Data) ?

---

# 3. 🎯 La Recherche Dichotomique

> **Question de réflexion :**  
> Comment trouvez-vous rapidement un mot dans un dictionnaire papier de 2000 pages ?  
> Est-ce que vous lisez chaque page une par une ?

---

## 🧠 Le principe de "Diviser pour Régner"
1.  Regarder l'élément au milieu.
2.  Si c'est la cible : Gagné !
3.  Si la cible est plus petite : On recommence sur la **moitié gauche**.
4.  Si la cible est plus grande : On recommence sur la **moitié droite**.

> **Question indispensable :** Quelle condition doit remplir la liste pour que cela fonctionne ?

---

## 💻 À vous de jouer : Recherche Dichotomique

Complétez l'implémentation de la recherche :

```python
def recherche_dicho(l: list, cible: int) -> int:
    debut = 0
    fin = len(l) - 1
    while debut <= fin:
        # calculer l'index du milieu de l'intervalle [debut, fin]
        milieu = (... + ...) // 2
        if l[milieu] == cible:
            return milieu
        elif l[milieu] < cible:
            # mettre à jour debut
            debut = ...
        else:
            # mettre à jour fin
            fin = ...
    return -1
```

---

# 4. ⚡ Analyse de Performance

> **Question de réflexion :**  
> Combien de fois peut-on couper une feuille de papier en deux avant qu'il ne reste qu'un tout petit morceau ?

---

## 📈 Le pouvoir de la division par 2
Imaginez une liste de **1 000 000** éléments.
- Étape 1 : 500 000 restants.
- Étape 2 : 250 000 restants.
- ...
- Étape 20 : **1** seul élément restant !

> **Question :** Pourquoi est-ce plus efficace que la recherche classique ?

---

## 📈 Séquentiel vs Dichotomique
| Taille (N) | Séquentiel | Dichotomique |
| :--- | :--- | :--- |
| 1 000 | 1 000 tests | ~10 tests |
| 1 000 000 | 1 000 000 tests | ~20 tests |
| 1 000 000 000 | 1 000 000 000 tests | ~30 tests |

> **Question :** Si on trie une fois pour faire des milliers de recherches ensuite, est-ce rentable ?

---

## 🚦 Conclusion
- **Trier est coûteux** ($N^2$).
- **Rechercher est ultra-rapide** ($\log N$).

---

# 🛠️ À vous de jouer !
Passez à la feuille d'exercices pour mettre cela en pratique.
