<script>
  const password = "mdp1nsieval2$"; // mot de passe
  const userInput = prompt("Entrez le mot de passe pour accéder à cette page :");

  if (userInput !== password) {
    alert("Mot de passe incorrect !");
    window.location.href = "/";
  }
</script>

# Évaluation de Programmation Python — Sujet B (2 heures)

## Exercice 1 — Analyse et compréhension de code

On considère les trois fonctions suivantes :

```python
def mystere_A(n: int) -> int:
    resultat = 0
    while n > 0:
        resultat = resultat + 3
        n = n - 1
    return resultat

def mystere_B(a: int, b: int) -> int:
    resultat = 0
    while a >= b:
        resultat = resultat + 1
        a = a - 1
    return resultat

def mystere_C(a: int, b: int) -> int:
    resultat = 1
    while b != 0:
        resultat = resultat * a
        b = b - 1
    return resultat
```

1. Comment s’appellent les différentes fonctions déclarées ici ?
2. Quels sont les paramètres de la fonction `mystere_B` et de quel type sont-ils ?
3. De quel type sont les valeurs renvoyées par ces trois fonctions ?
4. Pour chaque fonction, indiquer la valeur stockée dans la variable `resultat` avant l'entrée dans la boucle `while`.
5. Pour la fonction `mystere_A`, quelle est la condition pour que la boucle `while` s'arrête ?
6. Pour la fonction `mystere_B`, comment évolue la variable `a` à chaque itération (tour de boucle) ?
7. Compléter le tableau d'exécution suivant avec les valeurs proposées :

| Fonction | Valeurs des paramètres | Résultat attendu |
| :---: | :---: | :---: |
| `mystere_A` | `n = 4` | |
| `mystere_A` | `n = 0` | |
| `mystere_B` | `a = 14, b = 4` | |
| `mystere_B` | `a = 3, b = 5` | |
| `mystere_C` | `a = 3, b = 3` | |
| `mystere_C` | `a = 5, b = 0` | |


---

## Exercice 2 — Boucles `for` et calculs cumulés

### Partie A : Somme des carrés

Écrire une fonction `somme_carres(n: int) -> int` qui prend en paramètre un nombre entier positif `n` et renvoie la somme des carrés de tous les entiers de `1` à `n` inclus :
$$1^2 + 2^2 + 3^2 + \dots + n^2$$

⚠️ **Contraintes :**

* Utiliser une boucle `for` avec la fonction `range()`.

```python
def somme_carres(n: int) -> int:
    # À compléter
```

Exemples attendus :
```python
print(somme_carres(3))   # Affiche 14 (car 1² + 2² + 3² = 1 + 4 + 9 = 14)
print(somme_carres(4))   # Affiche 30 (car 14 + 16 = 30)
print(somme_carres(1))   # Affiche 1
```

### Partie B : Somme des multiples d'un nombre (Bonus)

Écrire une fonction `somme_multiples(n: int, k: int) -> int` qui prend en paramètres deux entiers strictement positifs `n` et `k`, et renvoie la **somme** de tous les entiers compris entre `1` et `n` (inclus) qui sont des **multiples de `k`**.

⚠️ **Contraintes et rappel :**

* Utiliser une boucle `for` avec la fonction `range()`.
* Tester si chaque entier est divisible par `k` à l'aide de l'opérateur modulo `%` et d'une condition `if`.
* Accumuler la somme des multiples trouvés dans une variable.

```python
def somme_multiples(n: int, k: int) -> int:
    # À compléter
```

Exemples attendus :
```python
print(somme_multiples(10, 3))  # Affiche 18 (multiples : 3, 6, 9 -> 3 + 6 + 9 = 18)
print(somme_multiples(12, 5))  # Affiche 15 (multiples : 5, 10 -> 5 + 10 = 15)
print(somme_multiples(6, 10))  # Affiche 0  (aucun multiple de 10 entre 1 et 6)
```

---

## Exercice 3 — Arithmétique entière et division euclidienne

### Répartition et conditionnement

Une personne récolte des œufs et souhaite automatiser leur conditionnement en boîtes de 6 œufs.  
Chaque boîte pleine est vendue au prix de **3.50 €**. Les œufs restants (ne permettant pas de remplir une boîte complète) ne peuvent pas être vendus en boîte.

On rappelle les rôles des différents opérateurs arithmétiques en Python :
* `/` : division flottante (résultat décimal)
* `//` : quotient de la division entière
* `%` : reste de la division entière (modulo)

Compléter la fonction `gestion_recolte(nb_oeufs: int)` qui utilise chacun de ces opérateurs :

```python
def gestion_recolte(nb_oeufs: int):
    # 1. Nombre de boîtes complètes de 6 œufs que l'on peut remplir
    boites_pleines = ...                 

    # 2. Nombre d'œufs restants qui ne rentrent pas dans une boîte
    oeufs_restants = ...                

    # 3. Montant total des ventes des boîtes complètes (3.50 € par boîte)
    recette_totale = boites_pleines * 3.50

    # 4. Prix moyen réel rapporté par œuf récolté (recette totale divisée par tous les œufs récoltés)
    prix_moyen_par_oeuf = ...        

    print("Boîtes pleines :", boites_pleines)
    print("Œufs non emballés :", oeufs_restants)
    print("Prix moyen par œuf récolté :", round(prix_moyen_par_oeuf, 3), "€")
```

Exemple attendu :
```python
gestion_recolte(50)
# Affiche :
# Boîtes pleines : 8
# Œufs non emballés : 2
# Prix moyen par œuf récolté : 0.56 €
```

## Exercice 4 — Conditions et programme complet

### Partie 1 : Fonction de décision

Un cinéma applique des tarifs selon la tranche d'âge des spectateurs :

* `"Erreur : age invalide"` si `age < 0` ou `age > 120`.
* `5.0` si `age < 12` (tarif enfant).
* `7.5` si `12 <= age <= 17` (tarif jeune).
* `10.5` si `18 <= age <= 64` (tarif plein).
* `6.5` si `age >= 65` (tarif senior).

Écrire une fonction `tarif_cinema(age: int)` qui prend en paramètre l'âge et renvoie le tarif correspondant (ou le texte d'erreur) :

```python
def tarif_cinema(age: int):
    # À compléter
```

### Partie 2 : Programme interactif complet

Écrire un programme Python complet qui :

1. Demande son prénom au client (`input()`).
2. Demande son âge au client (`input()`).
3. Convertit l'âge saisi en nombre entier (`int(...)`).
4. Fait appel à la fonction `tarif_cinema` pour déterminer le montant à régler.
5. Affiche le récapitulatif sous la forme :  
   `"Client <prenom> (<age> ans) : Tarif = <tarif> €"`

---

## 🌟 Exercice Bonus : Le compte à rebours de sécurité

On souhaite simuler la saisie d'un code de sécurité avec une réserve d'énergie.  
Le système dispose d'une réserve de **100 points d'énergie**.

Écrire une fonction `desamorcage(code_secret: int)` qui :

1. Demande au joueur de saisir le code entier (avec `input()`).
2. À chaque tentative incorrecte : 

    - La réserve perd **25 points d'énergie**.
    - Le programme affiche : `"Code faux ! Énergie restante : <energie>"`.

3. Répète la saisie **tant que** le joueur n'a pas trouvé le code ET qu'il reste de l'énergie (`energie > 0`).
4. Si le code secret est trouvé, affiche :  
   `"Système déverrouillé avec succès !"`
5. Si l'énergie tombe à 0 sans succès, affiche :  
   `"Alerte : Système bloqué, énergie épuisée !"`

⚠️ **Contraintes :**

* Veiller à convertir la saisie avec `int()`.
* La boucle doit s'arrêter dès que le code est trouvé ou dès que l'énergie atteint 0.

```python
def desamorcage(code_secret: int):
    # À compléter
```

Exemple d'exécution :
```text
>>> desamorcage(1234)
Entrez le code : 0000
Code faux ! Énergie restante : 75
Entrez le code : 1111
Code faux ! Énergie restante : 50
Entrez le code : 1234
Système déverrouillé avec succès !
```
