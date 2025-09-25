# <u>Évaluation</u>

## <u>Premier exercice</u>

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
4. De quel type seront les résultats de ces fonctions ?
5. Pour chaque fonction, indiquer ce qui est stocké dans la variable `resultat` à la première ligne.
6. Pour chaque fonction, quelle est la condition pour que la boucle `while` s’arrête ?
7. Pour chaque fonction, comment évolue la variable `resultat` à chaque itération (tour) de la boucle ?
8. Compléter le tableau suivant pour chaque fonction avec les cas proposés :

| a | b | Fonction   | résultat attendu |
| - | - | ---------- | ---------------- |
| 2 | 3 | mystere\_1 | ?                |
| 2 | 3 | mystere\_2 | ?                |
| 2 | 3 | mystere\_3 | ?                |
| 5 | 0 | mystere\_1 | ?                |
| 5 | 0 | mystere\_2 | ?                |
| 5 | 0 | mystere\_3 | ?                |

9. Finalement, que font ces fonctions (donner leur vrai rôle mathématique) ?

## <u>Deuxième exercice</u>

Compléter la fonction suivante qui renvoie la position d’un caractère (mis en paramètre) dans un texte (également mis en paramètre).

⚠️ Contraintes :

* Vous ne devez **pas utiliser** `in`, `find` ou toute autre fonction Python déjà existante pour rechercher dans une chaîne.
* Si le caractère est présent plusieurs fois, on renvoie uniquement **la première position**.
* ne pas recopier la documentation

```python
def recherche(texte: str, caractere: str) -> int | bool:
    """
    Renvoie l’indice de la première occurrence de `caractere` dans `texte` s’il est présent,
    sinon renvoie False.
    
    Paramètres :
        texte : str, une chaîne de caractères
        caractere : str, un caractère à trouver
    
    Résultat :
        int | bool : l’indice du caractère dans le texte s’il est présent, sinon False
    
    Exemples :
    >>> recherche("bonjour", "b")
    0
    >>> recherche("bonjour", "o")
    1
    >>> recherche("bonjour", "i")
    False
    """
```

## <u>Troisième exercice</u>

Écrire une fonction qui renvoie un mot inversé **sans utiliser** `mot[::-1]` ni la fonction `reverse()`.

```python
def inverse(mot):
    # réponse à compléter

# Quelques tests
print(inverse("NSI"))     # attendu : "ISN"
print(inverse("kayak"))   # attendu : "kayak"
```

## <u>Quatrième exercice</u>

Écrire une fonction `moyenne` qui demande une **note** (avec `input`) à l’utilisateur et renvoie :

* `"Très bien"` si la note ≥ 16
* `"Assez bien"` si la note ≥ 12
* `"Passable"` si la note ≥ 10
* `"Insuffisant"` sinon

⚠️ Contraintes et précisions :

* La note est comprise entre 0 et 20.
* Bonus : améliorer le programme pour que la note puisse être un **nombre décimal** (par exemple `12.5`).
* Bonus : afficher un message d’erreur si la note saisie est en dehors de l’intervalle \[0,20].