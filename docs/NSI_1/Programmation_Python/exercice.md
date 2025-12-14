# Exercices pratiques

**1. Variables et affichage**

Demandez à l’utilisateur son **nom** et son **âge**, puis affiche :

```
Bonjour <nom>, dans 10 ans tu auras <âge+10> ans.
```

indice: utiliser la fonction `input()`

---

**2. Types de données**

Créez trois variables : une **entière**, une **décimale** et une **chaîne de caractères**.
Affiche le type de chaque variable avec la fonction `type()`.

---

**3. Opérations mathématiques**

Écrivez un programme qui demande deux nombres à l’utilisateur et affiche :

* la somme
* la différence
* le produit
* le quotient entier
* le reste de la division

---

**4. Conditions**

Écrivait un programme qui demande une **note** à l’utilisateur et affiche :

* `"Très bien"` si la note ≥ 16
* `"Assez bien"` si la note ≥ 12
* `"Passable"` si la note ≥ 10
* `"Insuffisant"` sinon

---

**5. Boucles**

Affichez tous les nombres **pairs** de 1 à 20 en utilisant :

* une boucle `for`
* une boucle `while`

---

**6. Fonctions**

créez une fonction `carre(x)` qui renvoie le carré d’un nombre.

Testez-la avec plusieurs nombres et affichez les résultats.

### calcul de moyenne

1. Demandez à l’utilisateur combien de notes il veut entrer.
2. Utilisez une **boucle** pour demander chaque note une par une. (indice: utilisez `input`)
3. À chaque note saisie :

   * ajoutez-la à un **total** pour calculer la moyenne
   * vérifiez si elle est supérieure à la moyenne courante (facultatif pour avancer pas à pas).

4. Créez une **fonction** `mention(note)` qui renvoie :

   * `"Très bien"` si la note ≥ 16
   * `"Assez bien"` si la note ≥ 12
   * `"Passable"` si la note ≥ 10
   * `"Insuffisant"` sinon

5. Après la saisie de toutes les notes, calculez la **moyenne** et affichez la **mention correspondante**.

6. Affichez ensuite combien de notes sont **supérieures à la moyenne**.

**Exemple d’exécution :**

```
Combien de notes ? 5
Note 1 : 14
Note 2 : 18
Note 3 : 9
Note 4 : 12
Note 5 : 16

Moyenne : 13.8 → Assez bien
Nombre de notes supérieures à la moyenne : 3
```

# Exercice complémentaire

## Exercice 1

Analyse de code :

```python
nombre = 0
condition = True
while condition == True:
    if nombre == 10:
        condition = False
    print(nombre)
    nombre = nombre + 1
```

1. Quelles sont les variables utilisées ici ?
2. Quelles valeurs contiennent-elles ?
3. De quel type de boucle s’agit-il ici ? Quelle est la condition nécessaire pour que cette boucle s’arrête ?
4. À quel moment cette condition intervient-elle ?
5. Qu’affiche le programme ? Donnez le premier et le dernier élément affichés par le programme.

```python
nombre = 0
condition = True
while condition == True:
    nombre = nombre + 1
    if nombre == 10:
        condition = False
    print(nombre)
```

6. Et maintenant, que va afficher le programme ?
7. Transformez le premier programme pour le simplifier.
8. Recréez le premier programme avec une boucle **for** (en 2 lignes).

## Exercice 2

```python
import random

def reste(a, b):
    return a % b

def quotient(a, b):
    return a // b

def affichage(a, b):
    r = reste(a, b)
    q = quotient(a, b)
    print(a, " = ", b, " × ", q, " + ", r)

for i in range(10):
    a = random.randint(1, 10)  # évite b=0
    b = random.randint(1, 10)
    affichage(a, b)
```

1. Citez le nom de toutes les fonctions présentes dans ce code.
2. Que fait la fonction `reste` ?
3. Que fait la fonction `quotient` ?
4. Que fait la fonction `affichage` ?
5. Dans la fonction `affichage`, dans quelles variables sont stockés le quotient et le reste ?
6. Combien d’itérations (tours) la boucle `for` va-t-elle effectuer ?
7. Donnez les valeurs que `i` va prendre au fur et à mesure.
8. Que fait la fonction `random.randint` ?
9. Finalement, que va faire le programme ?

## Exercice 3

On considère la chaîne suivante :

```python
texte = "informatique"
```

---

Écrivez un programme qui affiche chaque caractère de la chaîne sur une nouvelle ligne.

**Exemple attendu :**

   ```
   i
   n
   f
   o
   r
   m
   a
   t
   i
   q
   u
   e
   ```

---

Affichez chaque caractère de la chaîne avec sa position (indice).

   **Exemple attendu :**

   ```
   0 : i
   1 : n
   2 : f
   3 : o
   ...
   10 : e
   ```

---

   Écrivez un programme qui compte combien de fois la lettre `"i"` apparaît dans la chaîne `"informatique"`.

   **Exemple attendu :**

   ```
   La lettre i apparaît 2 fois.
   ```

---

## bonus

   Écrivez un programme qui inverse la chaîne `"informatique"`.

**Exemple attendu :**

```
euqitamrofni
```