# 🌟 Cours : Les algorithmes de tri

# 1. 🔎 Qu’est-ce qu’un tri en informatique ?

En informatique, on manipule très souvent des **données** : des nombres, des mots, des objets, des dates, etc.
Lorsque ces données sont rangées dans un certain ordre, il est beaucoup plus facile et rapide :

* d’effectuer des recherches,
* de repérer des valeurs importantes (minimum, maximum…),
* de faire des statistiques,
* ou encore d’organiser des informations dans un tableau ou un programme.

👉 C’est pour cela qu’on utilise des **algorithmes de tri**.

??? Example "Exemples concrets où le tri est essentiel :"

    * ranger les messages sur un téléphone par date,
    * classer des photos par nom ou par année,
    * organiser un classement sportif du meilleur au moins bon,
    * trier des produits par prix croissant sur un site d’achat.


---

## 🎯 Définition

Un **tri** est une opération qui consiste à **réordonner les éléments d’une liste** selon un critère précis.

??? Example "Exemples de critères :"

* du plus petit au plus grand (croissant),
* du plus grand au plus petit (décroissant),
* ordre alphabétique (A → Z),
* ordre chronologique (du plus ancien au plus récent).

👉 Le mot *algorithme* signifie simplement une **suite d’instructions précises** que l’ordinateur peut exécuter pour obtenir un résultat.

---

## 📦 Les structures manipulées : les listes

Les algorithmes de tri s’appliquent à des **listes** ou **tableaux**.
Une liste est une suite ordonnée d’éléments, par exemple :

```
[12, 5, 9, 3, 14]
["Alice", "Brian", "Clara"]
```

Chaque élément de la liste a :

* une **valeur** (ex : 12),
* une **position** (ex : 12 est à la position 0).

Quand on applique un tri, on **modifie l’ordre des valeurs**, mais on garde les mêmes éléments.

---

## 🔍 Tri "manuel" vs tri algorithmique

Les humains trient instinctivement :

* un paquet de cartes,
* leurs fichiers dans un classeur,
* les vêtements dans une armoire.

Mais l’ordinateur, lui, ne peut pas "voir" ou "comprendre".
Il doit appliquer une méthode **claire**, **répétitive**, **automatisable**.

👉 D’où l’importance des **algorithmes de tri**.

## 🧩 Plusieurs familles de tris

Il existe beaucoup d’algorithmes de tri (tri rapide, tri à bulles, tri fusion, tri tas…).
Chacun a ses avantages et inconvénients (vitesse, simplicité, consommation mémoire…).

Pour les élèves de Première, on étudie surtout deux tris :

1. **le tri par sélection**,
2. **le tri par insertion**.


# 2. 🔷 Le tri par sélection

Le **tri par sélection** (en anglais *selection sort*) est un des algorithmes de tri les plus simples à comprendre.
Il est souvent étudié en premier parce qu’il illustre très bien les concepts de **parcours de liste**, de **comparaison**, et de **permutation**.

---

## 🎯 Idée générale

Le principe est le suivant :

1. **On recherche le plus petit élément de la liste.**
2. **On échange cet élément avec celui de la première position.**
3. On recommence sur la sous-liste restante (tous les éléments sauf le premier).
4. On répète jusqu’à ce que tous les éléments soient rangés.

Autrement dit, à chaque étape, on **sélectionne** (d’où le nom) l’élément le plus petit parmi ceux qui ne sont pas encore triés.

---

## 🧠 Pourquoi ce nom ?

L'algorithme *sélectionne* successivement les plus petits éléments pour les mettre au bon endroit.
Il ne construit pas une liste triée en avançant :
il place d’abord ce qui doit être au début, puis ce qui doit suivre, etc.

---

## 🔍 Exemple détaillé : trier la liste `[7, 3, 5, 2]`

On va suivre pas à pas ce que fait l’algorithme.

### ➤ Étape 1 : trouver le minimum de toute la liste

La liste est : `[7, 3, 5, 2]`
Le plus petit élément est **2**.

👉 On échange 2 avec le premier élément (7).

Nouvelle liste :
`[2, 3, 5, 7]`

### ➤ Étape 2 : trier la sous-liste à partir de la position 1

Sous-liste : `[3, 5, 7]`
Le plus petit élément est **3**, qui est déjà à sa place.

La liste ne change pas :
`[2, 3, 5, 7]`

### ➤ Étape 3 : trier la sous-liste à partir de la position 2

Sous-liste : `[5, 7]`
Le plus petit est **5**, déjà en position.

Rien ne change.

### ➤ Étape 4 : le dernier élément

Le dernier élément est forcément le plus grand restant.
Plus rien à faire.

👉 La liste est triée :
`[2, 3, 5, 7]`

---

## 🧩 Représentation schématisée

```
[7, 3, 5, 2]
   ↓
(minimum = 2)
↳ échange avec 7
[2, 3, 5, 7]
   ↓
(minimum = 3)
[pas d’échange]
[2, 3, 5, 7]
   ↓
(minimum = 5)
[pas d’échange]
[2, 3, 5, 7]
```

---

## 🔄 Comment fonctionne l’algorithme à chaque tour ?

Pour chaque position **i** dans la liste :

1. on suppose que la plus petite valeur se trouve en position **i** ;
2. on parcourt les positions qui suivent (i+1, i+2, …) pour vérifier si un élément plus petit existe ;
3. si on le trouve, on retient sa position ;
4. à la fin du parcours, on échange l’élément trouvé avec celui de la position **i**.

👉 C’est un algorithme qui nécessite **deux boucles** :

* une boucle extérieure qui fixe la position où doit aller le prochain plus petit,
* une boucle intérieure qui cherche le minimum.

---

## 📦 Avantages et inconvénients

### ✔️ Avantages

* Très simple à comprendre et à implémenter.
* Réalise très peu d’échanges (au maximum n échanges pour n éléments).

### ❌ Inconvénients

* Il faut **parcourir toute la liste** pour chaque position → lent si la liste est longue.
* Ne s’adapte pas bien aux listes déjà presque triées : il fera quand même les mêmes comparaisons.


# 3. 🔶 Le tri par insertion (Version développée)

Le **tri par insertion** (en anglais *insertion sort*) est un algorithme de tri très intuitif, souvent expliqué en comparant son fonctionnement avec la manière dont on trie des **cartes à jouer dans sa main**.

---

## 🎯 Idée générale

On considère qu’une partie de la liste (au début, juste le premier élément) est déjà **triée**.

Ensuite, pour chaque nouvel élément de la liste :

1. On le compare avec les éléments déjà triés ;
2. On le déplace vers la gauche jusqu’à trouver sa **juste place** ;
3. On l’insère là où il doit aller.

👉 De cette manière, la partie gauche de la liste est toujours triée, et elle **grandit** à chaque étape.

---

## 🃏 Exemple concret : comme trier des cartes

Quand on reçoit des cartes dans un jeu :

1. On commence avec une carte → c’est trié.
2. On prend la seconde → on la met avant ou après selon sa valeur.
3. On prend la troisième → on la glisse au bon endroit, même s’il faut bouger les autres cartes.
4. Et ainsi de suite.

Le tri par insertion fait exactement la même chose, mais avec des nombres dans une liste.

---

## 🔍 Exemple détaillé : trier la liste `[7, 3, 5, 2]`

On va construire progressivement une partie triée à gauche.

---

### ➤ Étape 0 : point de départ

On considère que `[7]` est déjà trié.

---

### ➤ Étape 1 : insérer 3

On compare 3 avec les éléments de la partie triée (`[7]`) :

* 3 < 7 → on déplace 7 vers la droite
* On place 3 à sa place

Résultat :
`[3, 7, 5, 2]`

---

### ➤ Étape 2 : insérer 5

On compare 5 à 7 puis à 3 :

* 5 < 7 → on décale 7 à droite
* 5 > 3 → sa place est ici

Résultat :
`[3, 5, 7, 2]`

---

### ➤ Étape 3 : insérer 2

On compare 2 à 7 → déplacer 7
On compare 2 à 5 → déplacer 5
On compare 2 à 3 → déplacer 3
Puis on place 2 au début.

Résultat final :
`[2, 3, 5, 7]`

---

## 🧩 Schéma illustré

```
[7 | 3, 5, 2] → 3 s'insère → [3, 7 | 5, 2]
[3, 7 | 5, 2] → 5 s'insère → [3, 5, 7 | 2]
[3, 5, 7 | 2] → 2 s'insère → [2, 3, 5, 7]
```

La partie à gauche de la barre (`|`) est toujours triée.

---

## 🔄 Le fonctionnement détaillé

Pour chaque position **i** de la liste :

1. On retient la valeur à insérer : `valeur = liste[i]`
2. On parcourt les éléments à gauche de `i` en partant de `i-1`
3. Tant que la valeur est **plus petite**, on décale les éléments vers la droite
4. On place la valeur au bon endroit.

👉 Cet algorithme nécessite aussi deux boucles :

* une boucle extérieure pour parcourir la liste,
* une boucle intérieure pour déplacer les éléments.

---

## 📦 Avantages et inconvénients

### ✔️ Avantages

* Très efficace quand la liste est déjà **presque triée**.
* Simple à comprendre et très naturel.
* Fonctionne "en ligne" : à chaque élément ajouté, la liste reste triée.

### ❌ Inconvénients

* Peut être lent si la liste est très désordonnée.
* Nécessite parfois beaucoup de **déplacements** d’éléments.
