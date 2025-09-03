# exercice complementaire

## exercice 1:

analyse de code:

```python
nombre = 0
condition = True
while condition == True:
    if nombre == 10:
        condition = False
    print(i)
    i = i+1
```

1. quelles sont les variables utiliser ici ?
2. quelles valeur contiennes-t-elles ?
3. de quelle type de boucle il s'agit ici ? quelle est la conditions necessaire pour que cette boucle s'arrete
4. a quelle moment cette conditions intervient
5. qu'affiche le programme ? donnez le premier et dernier element afficher par le programme

```python
nombre = 0
condition = True
while condition == True:
    i = i+1
    if nombre == 10:
        condition = False
    print(i)
```

6. et maintenant que va afficher le programme ?
7. transformer le premier programme pour le simplifier
8. recreer le permier programme avec une boucle for (2 ligne)

## exercice 2:

```python
def reste(a,b):
    return a % b

def quotient(a,b):
    return a // b

def affichage(a,b):
    r = reste(a,b)
    q = quotient(a,b)
    print(a , " = ", b, " ⨯ ", quotient, " + ", reste )

for i in range(10):
    a = alea(10)
    b = alea(10)
    affichage(a,b)
```

1. cité le nom de toute les fonctions presente dans ce code?
2. que fait la fonction reste?
3. que fait la fonction quotient?
4. que fait la fonction affichage?
5. au sein de affichage, dans quelle variable sont stocker le quotien et le reste?
6. combien d'iteration(tours) la boucle for va effectuer 
7. donner les valeur que i va prendre au fur et a mesure
8. que fait la fonction alea
9. finalement que va faire le programme ?

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

   Écrivez un programme qui inverse la chaîne `"informatique"`.

**Exemple attendu :**

```
euqitamrofni
```