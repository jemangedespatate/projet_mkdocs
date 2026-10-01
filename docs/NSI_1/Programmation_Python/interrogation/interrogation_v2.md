
<script>
  const password = "mdp1nsi2026"; // mot de passe
  const userInput = prompt("Entrez le mot de passe pour accéder à cette page :");

  if (userInput !== password) {
    alert("Mot de passe incorrect !");
    window.location.href = "/";
  }
</script>


# Évaluation de Programmation Python (2 heures)

## Exercice 1 — Analyse et compréhension de code

On donne trois fonctions appelées ici `mystere_1`, `mystere_2` et `mystere_3` :

```python
def mystere_1(a: int, b: int) -> int:
    resultat = a
    while b != 0:
        resultat = resultat + 1
        b = b - 1
    return resultat

def mystere_2(a: int, b: int) -> int:
    resultat = 0
    while b != 0:
        resultat = resultat + a
        b = b - 1
    return resultat

def mystere_3(a: int, b: int) -> int:
    resultat = a
    while b != 0:
        resultat = resultat * a
        b = b - 1
    return resultat
```

1. Comment s’appellent les différentes fonctions déclarées ici ?
2. Quels sont les paramètres de ces fonctions ?
3. De quel type sont ces paramètres ?
4. De quel type seront les résultats renvoyés par ces fonctions ?
5. Pour chaque fonction, indiquer ce qui est stocké dans la variable `resultat` avant l'entrée dans la boucle `while`.
6. Pour chaque fonction, quelle est la condition pour que la boucle `while` s’arrête ?
7. Pour chaque fonction, comment évolue la variable `resultat` à chaque itération (tour) de la boucle ?
8. Compléter le tableau suivant pour chaque fonction avec les valeurs proposées :

| a | b | Fonction | Résultat attendu |
| :-: | :-: | :--- | :--- |
| 2 | 3 | `mystere_1` | |
| 2 | 3 | `mystere_2` | |
| 2 | 3 | `mystere_3` | |
| 5 | 0 | `mystere_1` | |
| 5 | 0 | `mystere_2` | |
| 5 | 0 | `mystere_3` | |

9. Quel est le rôle mathématique de chacune de ces trois fonctions ?

---

## Exercice 2 — Boucles `for` et calculs cumulés

### Partie A : Somme des entiers

Écrire une fonction `somme_entiers(n: int) -> int` qui prend en paramètre un nombre entier positif `n` et renvoie la somme de tous les entiers de `1` à `n` inclus :
$$1 + 2 + 3 + \dots + n$$

⚠️ **Contraintes :**

* Utiliser une boucle `for` avec la fonction `range()`.
* Utiliser une variable pour accumuler la somme.

```python
def somme_entiers(n: int) -> int:
    # À compléter
```

Exemples attendus :
```python
print(somme_entiers(5))   # Affiche 15 (car 1 + 2 + 3 + 4 + 5 = 15)
print(somme_entiers(10))  # Affiche 55
print(somme_entiers(1))   # Affiche 1
```

### Partie B : Compter les multiples d'un nombre

Écrire une fonction `compter_multiples(n: int, k: int) -> int` qui prend en paramètres deux entiers strictement positifs `n` et `k`, et renvoie le nombre d'entiers entre `1` et `n` (inclus) qui sont des **multiples de `k`** (c'est-à-dire divisibles par `k`).

⚠️ **Contraintes et rappel :**

* Utiliser une boucle `for` avec la fonction `range()`.
* Tester si chaque entier est un multiple de `k` à l'aide de l'opérateur modulo `%` et d'une condition `if`.
* Utiliser un compteur pour comptabiliser les multiples trouvés.

```python
def compter_multiples(n: int, k: int) -> int:
    # À compléter
```

Exemples attendus :
```python
print(compter_multiples(10, 3))  # Affiche 3 (les multiples sont 3, 6, 9)
print(compter_multiples(20, 5))  # Affiche 4 (les multiples sont 5, 10, 15, 20)
print(compter_multiples(7, 10))  # Affiche 0 (aucun multiple de 10 entre 1 et 7)
```

---

## Exercice 3 — Arithmétique entière et division euclidienne

### Partie A : Décomposition horaire

On rappelle que dans une heure il y a 3600 secondes, et dans une minute il y a 60 secondes.  
Les opérateurs de division entière `//` et de reste modulo `%` permettent de décomposer un nombre entier.

Compléter la fonction `conversion_temps(total_secondes: int)` qui prend un nombre entier de secondes et calcule le nombre d'heures, de minutes et de secondes restantes :

```python
def conversion_temps(total_secondes: int):
    heures = total_secondes // 3600
    reste_heures = total_secondes % 3600
    minutes = ...          # À compléter
    reste_minutes = ...    # À compléter
    secondes = ...         # À compléter
    
    print(heures, "h", minutes, "min", secondes, "s")
```

Exemples attendus :
```python
conversion_temps(3665)  # Affiche : 1 h 1 min 5 s
conversion_temps(7320)  # Affiche : 2 h 2 min 0 s
```

### Partie B : Algorithme avec boucle `while`

On cherche à savoir combien de fois on peut diviser un nombre entier `n > 0` par 2 (division entière) avant qu'il n'atteigne 0.

Écrire une fonction `nb_divisions_par_deux(n: int) -> int` qui utilise une boucle `while` pour compter et renvoyer ce nombre de divisions :

```python
def nb_divisions_par_deux(n: int) -> int:
    compteur = 0
    while ... :
        # À compléter
    return compteur
```

Exemple : pour `n = 10` :

* `10 // 2 = 5` (1ère division)
* `5 // 2 = 2` (2ème division)
* `2 // 2 = 1` (3ème division)
* `1 // 2 = 0` (4ème division -> arrêt)
* Le résultat renvoyé est `4`.

---

## Exercice 4 — Conditions et programme complet

### Partie 1 : Fonction de décision

Écrire une fonction `appreciation(note: float) -> str` qui prend en paramètre une note sur 20 (pouvant comporter des décimales) et renvoie :

* `"Erreur : note invalide"` si la note est strictement inférieure à 0 ou strictement supérieure à 20.
* `"Très bien"` si la note `> 16`.
* `"Assez bien"` si `12 <= note < 16`.
* `"Passable"` si `10 <= note < 12`.
* `"Insuffisant"` si `0 <= note < 10`.

```python
def appreciation(note: float) -> str:
    # À compléter
```

### Partie 2 : Programme interactif complet

Écrire un programme Python complet qui :

1. Demande son prénom à l'utilisateur (`input()`)
2. Demande à l'utilisateur sa note obtenue à un devoir (`input()`).
3. Convertit cette note en type décimal (`float(nb_a_convertir)`).
4. Fait appel à la fonction `appreciation` pour obtenir l'appréciation correspondante.
5. Affiche un message récapitulatif sous la forme :
   `"Élève <prenom> : note <note>/20 -> <appreciation>"`

---

## 🌟 Exercice Bonus : Le jeu du nombre mystère

On souhaite créer un petit jeu dans lequel le joueur doit deviner un **nombre secret** (fixé au départ, par exemple `secret = 42`).

Écrire une fonction `jeu_devinette(secret: int)` qui :

1. Demande au joueur de proposer un nombre entier (avec `input`).
2. Indique au joueur :
   * `"Trop grand !"` si sa proposition est strictement supérieure au nombre secret.
   * `"Trop petit !"` si sa proposition est strictement inférieure au nombre secret.
3. Répète la saisie **tant que** le joueur n'a pas trouvé le nombre secret.
4. Compte le **nombre d'essais** nécessaires.
5. Dès que le joueur a trouvé, affiche :  
   `"Bravo ! Vous avez trouvé en <nb_essais> essais."`

⚠️ **Contraintes :**

* Veiller à bien convertir la saisie de l'utilisateur avec `int()`.
* La boucle doit s'arrêter dès que la bonne réponse est donnée.

```python
def jeu_devinette(secret: int):
    # À compléter
```

Exemple d'exécution :
```text
>>> jeu_devinette(42)
Entrez un nombre : 50
Trop grand !
Entrez un nombre : 20
Trop petit !
Entrez un nombre : 42
Bravo ! Vous avez trouvé en 3 essais.
```
