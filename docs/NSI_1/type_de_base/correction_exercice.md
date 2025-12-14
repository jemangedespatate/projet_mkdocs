# Correction : Listes et tuples en Python



## 🟢 **Niveau 1 — Découverte et manipulation de base**

### **Exercice 1 : Création et affichage**

```python
# 1. Création de la liste
fruits = ["pomme", "banane", "cerise"]

# 2. Affichage
print(fruits[0])   # Premier élément -> "pomme"
print(fruits[-1])  # Dernier élément -> "cerise"

# 3. Ajout
fruits.append("kiwi")

# 4. Remplacement
fruits[1] = "orange"

# 5. Suppression
fruits.remove("pomme")

# 6. Affichage final
print(fruits)
# Résultat attendu : ['orange', 'cerise', 'kiwi']
```



### **Exercice 2 : Moyenne de notes**

```python
notes = [14, 9, 12, 16, 10]

# Moyenne
somme = sum(notes)
nombre = len(notes)
moyenne = somme / nombre

print(f"Moyenne : {moyenne}")
print(f"Note maximale : {max(notes)}")
print(f"Note minimale : {min(notes)}")
```



### **Exercice 3 : Parcours d’une liste**

```python
# On reprend la liste de l'exercice 1 comme exemple
fruits = ["pomme", "orange", "kiwi"]

for i in range(len(fruits)):
    print(f"Indice {i} -> {fruits[i]}")
```



### **Exercice 4 : Saisie utilisateur**

```python
prenoms = []

for _ in range(3):
    nom = input("Entrez un prénom : ")
    prenoms.append(nom)

print("Liste des prénoms :", prenoms)
```



## 🟡 **Niveau 2 — Approfondissement et traitement**

### **Exercice 5 : Inversion et tri**

```python
nombres = [5, 1, 9, 3, 7]

# Tri croissant
nombres.sort()
print("Trié :", nombres)

# Inversion
nombres.reverse()
print("Inversé :", nombres)
```



### **Exercice 6 : Filtrage**

```python
nombres = [5, 12, 7, 3, 18, 9, 2]
pairs = []

for n in nombres:
    if n % 2 == 0:
        pairs.append(n)

print("Nombres pairs :", pairs)
```



### **Exercice 7 : Comptage**

```python
mots = ["elle", "est", "en", "été"]
compteur = 0

for mot in mots:
    # On compte le nombre de 'e' dans chaque mot
    compteur += mot.count("e")

print(f"La lettre 'e' apparaît {compteur} fois.")
```



### **Exercice 8 : Liste de listes**

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

somme_ligne_2 = sum(matrice[1]) # matrice[1] est [4, 5, 6]
element_centre = matrice[1][1]  # ligne 1, colonne 1

print(f"Somme ligne 2 : {somme_ligne_2}")
print(f"Élément central : {element_centre}")
```



## 🔵 **Niveau 3 — Tuples et données structurées**

### **Exercice 9 : Coordonnées**

```python
point = (3, 5)
x, y = point  # Unpacking

print(f"Le point a pour coordonnées x={x} et y={y}")
```



### **Exercice 10 : Données d’élèves**

```python
eleves = [("Alice", 15), ("Bob", 12), ("Clara", 17)]

for eleve in eleves:
    nom, note = eleve # ou directement: for nom, note in eleves:
    print(f"{nom} a obtenu {note}")
```



### **Exercice 11 : Recherche d’un élément**

```python
def cherche(liste, element):
    for x in liste:
        if x == element:
            return True
    return False

# Tests
print(cherche([1, 4, 9, 2], 9))  # True
print(cherche([1, 4, 9, 2], 5))  # False
```



### **Exercice 12 : Conversion**

```python
t = (1, 2, 3, 4)

# Conversion en liste
l = list(t)
l.append(5)

# Reconversion en tuple
t = tuple(l)

print(t) # (1, 2, 3, 4, 5)
```



## 🔴 **Niveau 4 — Raisonnement algorithmique**

### **Exercice 13 : Moyenne générale**

```python
notes_eleves = [("Alice", [15, 14, 13]), ("Bob", [10, 12, 11]), ("Clara", [18, 17, 19])]

for nom, notes in notes_eleves:
    moyenne = sum(notes) / len(notes)
    print(f"{nom} -> moyenne : {moyenne}")
```



### **Exercice 14 : Rotation de liste**

```python
def rotation(liste):
    if not liste:
        return liste
    premier = liste.pop(0)
    liste.append(premier)
    return liste

# Exemple
ma_liste = [1, 2, 3, 4]
rotation(ma_liste)
print(ma_liste) # [2, 3, 4, 1]
```



### **Exercice 15 : Maximum d’une matrice**

```python
def max_matrice(m):
    maximum = m[0][0] # On initialise avec le premier élément
    for ligne in m:
        for val in ligne:
            if val > maximum:
                maximum = val
    return maximum

m = [[4, 7, 2], [9, 3, 8], [1, 6, 5]]
print(max_matrice(m)) # 9
```

## **Niveau 5 — Challenge**

### **Exercice 1 – Rotation de liste**

```python
def rotation(liste, n):
    if not liste:
        return liste
    # Calcul du décalage effectif (module)
    n = n % len(liste)
    # Découpage et concaténation
    return liste[-n:] + liste[:-n]

print(rotation([1, 2, 3, 4, 5], 2))
# [4, 5, 1, 2, 3]
```



### **Exercice 2 – Aplatir une liste imbriquée**

```python
def aplatir(liste):
    resultat = []
    for element in liste:
        if isinstance(element, list):
            # Si l'élément est une liste, on appelle récursivement la fonction
            resultat.extend(aplatir(element))
        else:
            resultat.append(element)
    return resultat

print(aplatir([[1, [2, 3]], [4, [5, [6]]]]))
# [1, 2, 3, 4, 5, 6]
```



### **Exercice 3 – Matrice : diagonale principale**

```python
def diag(matrice):
    # Vérification matrice carrée
    nb_lignes = len(matrice)
    for ligne in matrice:
        if len(ligne) != nb_lignes:
            print("Erreur : La matrice n'est pas carrée.")
            return None
    
    somme = 0
    for i in range(nb_lignes):
        somme += matrice[i][i]
    return somme

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(diag(m)) # 15
```



### **Exercice 4 – Détection de motif**

```python
def contient_motif(liste, motif):
    len_liste = len(liste)
    len_motif = len(motif)
    
    # On parcourt la liste jusqu'à ce qu'il ne reste plus assez d'éléments pour le motif
    for i in range(len_liste - len_motif + 1):
        # On extrait une sous-liste de la taille du motif
        if liste[i : i + len_motif] == motif:
            return True
    return False

print(contient_motif([1, 2, 3, 4, 5, 3, 4], [3, 4])) # True
print(contient_motif([1, 2, 3, 4], [4, 3])) # False
```
