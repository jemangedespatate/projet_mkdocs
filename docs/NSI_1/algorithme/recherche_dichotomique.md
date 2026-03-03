# 🔍 Cours : La Recherche Dichotomique

---

# 1. 📌 Problème de départ : chercher dans une liste

Imaginez que vous avez une liste de **1 000 prénoms** triés par ordre alphabétique, et on vous demande de retrouver le prénom `"Zoé"`. Comment procéderiez-vous ?

Deux stratégies s'opposent :

* **Stratégie 1** : Commencer depuis le début et lire chaque prénom un par un jusqu'à trouver `"Zoé"`.
* **Stratégie 2** : Ouvrir directement au milieu, voir si vous êtes avant ou après `"Zoé"`, puis réduire de moitié la zone de recherche.

L'informatique a formalisé ces deux idées sous la forme d'algorithmes de recherche.

---

# 2. 🔎 Recherche Séquentielle (ou Linéaire)

## Principe

La **recherche séquentielle** consiste à parcourir la liste **élément par élément**, du premier au dernier, jusqu'à trouver la valeur cherchée (ou arriver à la fin sans l'avoir trouvée).

??? Example "Illustration"
    On cherche `9` dans la liste `[4, 7, 2, 9, 1, 5]` :

    * On regarde `4` → non
    * On regarde `7` → non
    * On regarde `2` → non
    * On regarde `9` → **trouvé !** (à l'index 3)

## Implémentation Python

```python
def recherche_sequentielle(liste, valeur):
    """
    Recherche une valeur dans une liste de manière séquentielle.
    Retourne l'indice de la valeur si trouvée, -1 sinon.
    """
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i
    return -1
```

## Caractéristiques

* Fonctionne sur **toute liste**, qu'elle soit triée ou non.
* Simple à comprendre et à implémenter.

---

# 3. ⏱️ La Notion de Complexité

## Pourquoi s'intéresser à la complexité ?

Deux algorithmes qui résouslvent le même problème peuvent avoir des **performances très différentes** selon la taille des données.

En informatique, on mesure l'**efficacité** d'un algorithme grâce à sa **complexité temporelle** : on évalue le **nombre d'opérations** que l'algorithme doit effectuer en fonction de la taille **n** de la liste.

!!! info "Notion clé : la notation O()"
    On utilise la notation **O(...)** (lire « grand O ») pour décrire la complexité dans le **pire des cas** :

    * **O(1)** : complexité constante — le temps ne dépend pas de n
    * **O(n)** : complexité linéaire — le temps est proportionnel à n
    * **O(log n)** : complexité logarithmique — le temps croît très lentement
    * **O(n²)** : complexité quadratique — le temps croît très vite

## Complexité de la recherche séquentielle

Analysons le pire cas de la recherche séquentielle : la valeur cherchée **n'est pas dans la liste**.

Dans ce cas, on doit parcourir **tous les n éléments** de la liste.

👉 La **complexité de la recherche séquentielle est O(n)**.

## Illustration concrète

Voici combien d'opérations sont nécessaires selon la taille de la liste :

| Taille de la liste (n) | Recherche séquentielle (O(n)) |
|:-----------------------:|:------------------------------:|
| 10                     | 10 opérations                 |
| 100                    | 100 opérations                |
| 1 000                  | 1 000 opérations              |
| 1 000 000              | 1 000 000 opérations          |
| 1 000 000 000          | 1 000 000 000 opérations 😱   |

Sur une liste d'un milliard d'éléments, la recherche séquentielle peut prendre plusieurs secondes voire minutes !

---

# 4. 🎯 Recherche Dichotomique

## Pré-requis indispensable ⚠️

!!! warning "Attention"
    La recherche dichotomique ne fonctionne **que sur une liste triée** !

## Principe

La **recherche dichotomique** (du grec *dikha* = en deux parties) consiste à :

1. Regarder l'**élément au milieu** de la liste.
2. Si c'est la valeur cherchée → **trouvé !**
3. Si la valeur cherchée est **plus petite** → continuer la recherche dans la **moitié gauche**.
4. Si la valeur cherchée est **plus grande** → continuer la recherche dans la **moitié droite**.
5. Répéter jusqu'à trouver l'élément ou jusqu'à ce que la zone de recherche soit vide.

👉 À chaque étape, on **divise par 2** la zone de recherche.

---

## 🔍 Exemple détaillé

On cherche la valeur `37` dans la liste triée suivante (14 éléments) :

```
[2, 5, 8, 12, 16, 23, 37, 42, 56, 72, 84, 91, 95, 99]
  0  1  2   3   4   5   6   7   8   9  10  11  12  13
```

### ➤ Étape 1

```
gauche = 0       droite = 13
milieu = (0 + 13) // 2 = 6
liste[6] = 37
```

🎉 **Trouvé immédiatement à l'index 6 !**

---

Essayons maintenant de chercher `56` :

### ➤ Étape 1

```
gauche = 0       droite = 13
milieu = 6
liste[6] = 37
37 < 56 → on cherche dans la moitié DROITE
```

### ➤ Étape 2

```
gauche = 7       droite = 13
milieu = (7 + 13) // 2 = 10
liste[10] = 84
84 > 56 → on cherche dans la moitié GAUCHE
```

### ➤ Étape 3

```
gauche = 7       droite = 9
milieu = (7 + 9) // 2 = 8
liste[8] = 56
```

🎉 **Trouvé à l'index 8 en seulement 3 étapes !**

Avec une recherche séquentielle, on aurait parcouru 9 éléments (de l'index 0 à 8).

---

## 🧩 Schéma de la démarche

```
[2, 5, 8, 12, 16, 23, 37, 42, 56, 72, 84, 91, 95, 99]
 ←————————————————[milieu=37]————————————————→
                            56 > 37
                  ←——————→ [milieu=84] ←——————→
                    56 < 84
                  ←→[milieu=56]←→
                  ✅ Trouvé !
```

---

# 5. ⏱️ Complexité de la recherche dichotomique

## Analyse du pire cas

À chaque étape, on **divise la zone de recherche par 2**.

* Départ : **n** éléments
* Après 1 étape : **n/2** éléments
* Après 2 étapes : **n/4** éléments
* Après k étapes : **n/2ᵏ** éléments

On s'arrête quand il ne reste plus qu'1 élément : n/2ᵏ = 1, soit **k = log₂(n)**.

👉 La **complexité de la recherche dichotomique est O(log n)**.

## Comparaison des complexités

| Taille de la liste (n) | Recherche séquentielle O(n) | Recherche dichotomique O(log₂ n) |
|:-----------------------:|:---------------------------:|:---------------------------------:|
| 10                     | 10 opérations               | 4 opérations                     |
| 100                    | 100 opérations              | 7 opérations                     |
| 1 000                  | 1 000 opérations            | 10 opérations                    |
| 1 000 000              | 1 000 000 opérations        | 20 opérations                    |
| 1 000 000 000          | 1 000 000 000 opérations    | 30 opérations 🚀                 |

!!! tip "Bilan"
    Sur un milliard d'éléments, la recherche dichotomique ne nécessite que **30 comparaisons** ! Contre 1 milliard pour la recherche séquentielle.

    C'est la puissance du logarithme : **doubler la taille de la liste ne coûte qu'une seule étape de plus**.

---

# 6. 💻 Implémentation Python

## Version itérative

```python
def recherche_dichotomique(liste, valeur):
    """
    Recherche une valeur dans une liste TRIÉE par dichotomie.
    Retourne l'indice de la valeur si trouvée, -1 sinon.
    
    Précondition : la liste doit être triée par ordre croissant.
    """
    gauche = 0
    droite = len(liste) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2  # indice du milieu

        if liste[milieu] == valeur:
            return milieu          # valeur trouvée
        elif liste[milieu] < valeur:
            gauche = milieu + 1    # on cherche dans la moitié droite
        else:
            droite = milieu - 1    # on cherche dans la moitié gauche

    return -1  # valeur non trouvée
```

## Trace d'exécution

Pour `recherche_dichotomique([1, 3, 5, 7, 9, 11, 13], 7)` :

| Étape | gauche | droite | milieu | liste[milieu] | Action              |
|:-----:|:------:|:------:|:------:|:-------------:|:--------------------|
| 1     | 0      | 6      | 3      | 7             | **Trouvé !** → 3   |

Pour `recherche_dichotomique([1, 3, 5, 7, 9, 11, 13], 11)` :

| Étape | gauche | droite | milieu | liste[milieu] | Action                       |
|:-----:|:------:|:------:|:------:|:-------------:|:-----------------------------|
| 1     | 0      | 6      | 3      | 7             | 11 > 7 → gauche = 4         |
| 2     | 4      | 6      | 5      | 11            | **Trouvé !** → 5            |

---

# 7. ✅ Bilan et comparaison

## Tableau récapitulatif

| Critère                    | Recherche séquentielle | Recherche dichotomique |
|:---------------------------|:----------------------:|:-----------------------:|
| Liste doit être triée ?    | ❌ Non                | ✅ Oui                 |
| Complexité (pire cas)      | O(n)                   | O(log n)               |
| Efficacité sur grande liste| Lente                  | Très rapide            |
| Simplicité de code         | ⭐⭐⭐               | ⭐⭐                  |

## Quand utiliser quoi ?

* ✅ **Recherche séquentielle** : liste non triée, petite liste, cas simple.
* ✅ **Recherche dichotomique** : liste triée, grande liste, performance critique.

!!! success "À retenir"
    La recherche dichotomique est un exemple classique d'algorithme dit **« diviser pour régner »** (*divide and conquer*) : on résout un grand problème en le divisant en sous-problèmes plus petits.
    
    La notation **O(log n)** traduit une croissance extrêmement lente : c'est l'une des meilleures complexités qu'un algorithme de recherche puisse avoir.
