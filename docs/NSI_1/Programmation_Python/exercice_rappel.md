# 🔄 Exercices de remédiation : Rappels de programmation

## 1. Variables et affichage (`print`)

!!! abstract "Point de cours"
    * Une **variable** sert à stocker une valeur dans la mémoire de l'ordinateur.
    * Pour créer et affecter une valeur à une variable, on utilise le symbole `=` :
      ```python
      prenom = "Lucas"
      age = 16
      ```
    * Pour afficher du texte ou le contenu d'une variable à l'écran, on utilise l'instruction `print(...)` :
      ```python
      print("Bonjour", prenom)
      print("Tu as", age, "ans.")
      ```

---

### Exercice 1.1 : Mon premier message
Créez une variable `ville` qui contient le nom de votre ville préférée, puis affichez :
`J'habite à <ville>` (en remplaçant `<ville>` par la valeur de la variable).


---

### Exercice 1.2 : Modifier une variable
On considère le code suivant :
```python
score = 10
score = 25
print("Votre score final est :", score)
```
1. Sans exécuter le code dans EduPython, quelle valeur sera affichée ?
2. Testez ensuite dans EduPython pour vérifier votre réponse.

---

## 2. Les types de données (`int`, `float`, `str`, `bool`)

!!! abstract "Point de cours"
    Chaque valeur manipulée possède un **type** précis :
    
    | Type | Signification | Exemples |
    | :--- | :--- | :--- |
    | `int` | Nombre entier | `42`, `-5`, `0` |
    | `float` | Nombre à virgule (décimal) | `3.14`, `1.5`, `-0.5` |
    | `str` | Chaîne de caractères (texte entre guillemets) | `"Bonjour"`, `'NSI'` |
    | `bool` | Booléen (Vrai ou Faux) | `True`, `False` |

    On peut connaître le type d'une valeur grâce à la commande `type(...)` :
    ```python
    x = 10
    print(type(x))  # Affiche <class 'int'>
    ```

---

### Exercice 2.1 : Identifier le bon type
Pour chacune des variables suivantes, donnez le type de la donnée stockée (`int`, `float`, `str` ou `bool`) :

```python
a = 15
b = "15"
c = 15.0
d = True
e = "True"
```

??? tip "Indice"
    Attention aux guillemets ! Dès qu'une valeur est entourée de guillemets `"..."`, il s'agit d'une chaîne de caractères (`str`), même s'il y a un chiffre ou un mot à l'intérieur.

---

### Exercice 2.2 : Conversion de types
Recopiez et complétez le code ci-dessous pour que le type affiché soit bien `<class 'int'>` :

```python
chaine = "42"
# Convertir 'chaine' en entier et stocker le résultat dans 'nombre'
nombre = ...

print(type(nombre))
print("Le double est :", nombre * 2)
```

??? tip "Indice"
    Utilisez la fonction de conversion `int(...)`.

---

## 3. Les calculs et opérateurs arithmétiques

!!! abstract "Point de cours"
    Python permet d'effectuer des opérations mathématiques directes :
    
    * `+` : Addition (`5 + 2 = 7`)
    * `-` : Soustraction (`5 - 2 = 3`)
    * `*` : Multiplication (`5 * 2 = 10`)
    * `/` : Division flottante (`5 / 2 = 2.5`)
    * `//` : Division entière / quotient (`5 // 2 = 2`)
    * `%` : Modulo (reste de la division entière) (`5 % 2 = 1`)

---

### Exercice 3.1 : Calcul simple de prix
Un cahier coûte 3 euros et un stylo coûte 2 euros.

1. Créez les variables `nb_cahiers = 4` et `nb_stylos = 5`.
2. Créez une variable `prix_total` qui calcule automatiquement le montant total de la commande.
3. Affichez la phrase : `Le montant total est de <prix_total> euros.`

---

### Exercice 3.2 : Comprendre `//` et `%`
On souhaite ranger 23 bonbons dans des sachets de 5 bonbons.

1. À l'aide de l'opérateur `//`, calculez le nombre de sachets complets que l'on peut remplir.
2. À l'aide de l'opérateur `%`, calculez le nombre de bonbons restants.
3. Affichez les deux résultats avec des messages clairs.

??? tip "Indice"
    * `23 // 5` donne le quotient (nombre de sachets).
    * `23 % 5` donne le reste (bonbons restants).


---

## 4. Saisie utilisateur (`input`) et conversion

!!! abstract "Point de cours"
    * La fonction `input("Votre texte : ")` met le programme en pause et attend que l'utilisateur tape une réponse au clavier.
    * ⚠️ **Attention cruciale :** `input()` renvoie **toujours** du texte (`str`), même si l'utilisateur saisit un nombre !
    * Pour faire des calculs avec un nombre saisi, il faut impérativement convertir la saisie avec `int()` (pour un entier) ou `float()` (pour un nombre décimal) :
      ```python
      reponse = input("Entrez votre âge : ")
      age = int(reponse)
      # Ou directement en une seule ligne :
      age = int(input("Entrez votre âge : "))
      ```

---

### Exercice 4.1 : Le piège du texte
Voici le programme écrit par un élève :
```python
nb = input("Entrez un nombre : ")
print(nb + nb)
```
Si l'utilisateur tape `5`, le programme affiche `55` au lieu de `10` !

1. Pourquoi le programme affiche-t-il `55` ?
2. Corrigez le code pour qu'il effectue une vraie addition mathématique.


---

## 5. Les conditions (`if`, `elif`, `else`)

!!! abstract "Point de cours"
    Les conditions permettent d'exécuter des instructions seulement si un test est vrai.
    
    * **Opérateurs de comparaison :**
        * `==` : égal à (⚠️ deux signes `=` !)
        * `!=` : différent de
        * `<` et `<=` : strictement inférieur, inférieur ou égal
        * `>` et `>=` : strictement supérieur, supérieur ou égal
    * **Structure générale :**
      ```python
      if condition_1:
          # bloc exécuté si condition_1 est VRAIE
      elif condition_2:
          # bloc exécuté si condition_1 est FAUSSE mais condition_2 est VRAIE
      else:
          # bloc exécuté si TOUTES les conditions précédentes sont FAUSSES
      ```
    * ⚠️ **Attention à l'indentation :** En Python, les instructions à l'intérieur d'un bloc doivent être décalées vers la droite (4 espaces ou touche Tabulation).


---

### Exercice 5.1 : Positif, négatif ou nul ?
Écrivez un programme qui demande un nombre entier à l'utilisateur :
* Si le nombre est strictement supérieur à 0, affichez `"Nombre positif"`.
* Si le nombre est strictement inférieur à 0, affichez `"Nombre négatif"`.
* Sinon (le nombre vaut 0), affichez `"Nombre nul"`.

??? tip "Indice"
    Utilisez une structure `if ... elif ... else`.

---

### Exercice 5.2 : Pair ou impair ?
On rappelle qu'un nombre entier est **pair** si le reste de sa division par 2 est nul (c'est-à-dire `nombre % 2 == 0`).
Écrivez un programme qui demande un entier à l'utilisateur et affiche s'il est pair ou impair.

---

## 6. Les boucles (`while` et `for`)

Une boucle permet de répéter un bloc d'instructions plusieurs fois.

### 6.1. La boucle `while` (tant que)

!!! abstract "Point de cours"
    La boucle `while` répète un bloc d'instructions **tant qu'une condition reste vraie**.
    
    ```python
    compteur = 1
    while compteur <= 3:
        print("Tour numéro :", compteur)
        compteur = compteur + 1  # Très important pour ne pas tourner à l'infini !
    ```
    * ⚠️ **Attention à la boucle infinie :** Il faut obligatoirement qu'une variable change dans la boucle pour que la condition devienne fausse à un moment donné.

---

### Exercice 6.1 : Le compte à rebours
À l'aide d'une boucle `while`, écrivez un programme qui initialise une variable `decompte = 5` et affiche les nombres de 5 à 1 en décroissant, puis termine en affichant `"Décollage !"`.

Exemple d'affichage attendu :
```text
5
4
3
2
1
Décollage !
```

??? tip "Indice"
    Faites tourner la boucle tant que `decompte > 0` et pensez à décrémenter de 1 (`decompte = decompte - 1`) à chaque tour.

---

### 6.2. La boucle `for` (pour)

!!! abstract "Point de cours"
    La boucle `for` est utilisée quand on connaît le nombre de répétitions à effectuer.
    On utilise souvent la fonction `range()` :
    
    * `range(n)` génère les entiers de `0` à `n - 1` (ex : `range(4)` produit `0, 1, 2, 3`).
    * `range(debut, fin)` génère les entiers de `debut` à `fin - 1` (ex : `range(1, 5)` produit `1, 2, 3, 4`).
    * `range(debut, fin, pas)` permet de préciser le pas (ex : `range(0, 10, 2)` produit `0, 2, 4, 6, 8`).

    ```python
    for i in range(1, 4):
        print("Étape", i)
    ```

---

### Exercice 6.2 : Table de multiplication
À l'aide d'une boucle `for` et de la fonction `range()`, écrivez un programme qui affiche la table de multiplication de 7, de 1 à 10 :

```text
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

??? tip "Indice"
    Utilisez `for i in range(1, 11):` pour faire varier `i` de 1 à 10 inclus.

---

## 7. Les fonctions (`def` et `return`)

!!! abstract "Point de cours"
    Une fonction est un bloc d'instructions réutilisable qui réalise une tâche précise.
    
    * On la définit avec `def`, suivi de son nom et de ses paramètres entre parenthèses.
    * Elle renvoie un résultat grâce au mot-clé `return` :
      ```python
      def double(n):
          return n * 2

      # Appel de la fonction :
      resultat = double(6)
      print(resultat)  # Affiche 12
      ```
    * ⚠️ **`print` vs `return` :** 
        * `print()` sert seulement à afficher du texte à l'écran.
        * `return` renvoie une valeur utilisable par le reste du programme (pour la stocker dans une variable ou faire d'autres calculs).

---

### Exercice 7.1 : Périmètre d'un rectangle

1. Écrivez une fonction `perimetre(longueur, largeur)` qui prend en paramètres la longueur et la largeur d'un rectangle et renvoie son périmètre ($2 \times (\text{longueur} + \text{largeur})$).
2. Testez votre fonction dans la console ou le script en affichant le résultat pour un rectangle de longueur 8 et de largeur 5 :
   ```python
   print("Périmètre :", perimetre(8, 5))
   ```

??? tip "Indice"
    Votre fonction doit contenir l'instruction `return 2 * (longueur + largeur)`.

---

## 8. Synthèse : Êtes-vous prêt pour la suite ?

Maintenant que vous avez revu chaque brique séparément, vous pouvez retenter l'exercice initial :

!!! question "Exercice récapitulatif"
    Écrivez un programme qui demande à l'utilisateur :
    
    1. Son **nom**.
    2. Son **âge**.
    
    Le programme doit afficher :
    ```text
    Bonjour <nom>, dans 10 ans tu auras <âge+10> ans.
    ```
    Puis, si l'âge dans 10 ans est supérieur ou égal à 18, afficher `"Tu seras majeur."`, sinon `"Tu seras mineur."`.

