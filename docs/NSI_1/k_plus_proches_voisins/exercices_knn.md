# 📝 Exercices : k plus proches voisins

## Exercice 1 : Exécution manuelle

On a relevé le poids (en kg) et la taille au garrot (en cm) de plusieurs chiens pour essayer de distinguer avec un algorithme deux races : le *Carlin* et le *Lévrier*. On utilise la notation (Poids, Taille).

Voici nos données d'apprentissage étiquetées :

- **Carlins** : C1 (7, 30), C2 (8, 32), C3 (10, 31)
- **Lévriers** : L1 (25, 70), L2 (27, 72), L3 (30, 75)

L'algorithme rencontre une donnée d'un chien inconnu *Mystère*, avec comme caractéristiques (8.5, 33).

1. Représentez rapidement sur un graphique (à main levée sur papier brouillon) la disposition approximative de l'ensemble de ces points.
2. À l'œil, sans faire de calculs précis de distance, quelle sera logiquement la prédiction de l'algorithme des k-NN pour *Mystère* si l'on prend k=3 ? Argumentez.
3. Un autre chien, *Bizarre*, testé par l'algorithme a pour caractéristiques (15, 55). Si on analyse ses deux voisins les plus proches en forçant k=2, un problème algorithmique risque de survenir. Lequel ? Que fait-on pour habituellement parer cette éventualité ?

## Exercice 2 : Calculs formels et liste de distances

Dans ce cas d'étude, on étudie des personnages d'un jeu de rôle. Notre objectif est de les classer en "Guerrier" ou "Mage" selon deux attributs quantifiés sur 10 : l'Attaque Physique (X) et l'Attaque Magique (Y).

Nos données :

- P1 (8, 2) : Guerrier
- P2 (2, 9) : Mage
- P3 (6, 4) : Guerrier
- P4 (3, 7) : Mage
- P5 (5, 5) : Guerrier

Un nouveau PNJ N inconnu apparait avec les stats suivantes : attaque physique de 4 et magique de 6, donc (4, 6).

??? question "Astuce"
      d² = (X1 - X2)² + (Y1 - Y2)². Il n'y a pas besoin de calculer les racines carrées embêtantes pour juste comparer la grandeur relative des distances !

1. Calculez les distances (au carré) entre N et chaque personnage P1 à P5.
2. Classez les 5 personnages connus par distance croissante vis-à-vis de N.
3. Répertoriez les classes des k voisins de N les plus proches pour k = 1 et k = 3.
4. En respectant rigoureusement la logique des k-NN pour k=3, ce personnage N est-il un "Guerrier" ou un "Mage" ?

## Exercice 3 : Compréhension d'une implémentation Python

Voici un extrait de code Python qui correspond à la partie **tri et sélection** de l'algorithme k-NN. Lisez-le attentivement puis répondez aux questions.

```python
# On dispose d'une liste de (distance, classe) pour chaque voisin potentiel
distances_calculees = [
    (14.5, "Rouge"),
    (2.1,  "Bleu"),
    (8.0,  "Bleu"),
    (1.5,  "Rouge"),
    (3.2,  "Bleu")
]

# On trie la liste par distance croissante
distances_calculees.sort()

# On garde uniquement la classe des k voisins les plus proches
k = 3
voisins = []
for i in range(k):
    voisins.append(distances_calculees[i][1])
```

1. Donnez le contenu de la liste `distances_calculees` **après** l'appel à `.sort()`.
2. Que contient la liste `voisins` à la fin de la boucle `for` ?
3. D'après la liste `voisins`, quelle classe est majoritaire ? Comment écrire en Python un petit code qui compte les occurrences de chaque classe et renvoie celle qui apparaît le plus souvent ?
