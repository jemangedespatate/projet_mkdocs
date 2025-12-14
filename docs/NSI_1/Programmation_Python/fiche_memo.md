#  🐍 Fiche Mémo Python

## 1. Variables

Une variable est un nom qui sert à stocker une valeur.

```python
# Affectation
x = 10        # entier
y = 3.14      # flottant
nom = "Alice" # chaîne de caractères
ok = True     # booléen
```

⚠️ les variables doivent avoir des noms coherents

---

## 2. Types de données

Les principaux types intégrés en Python :

* **int** → nombres entiers → `5, -12, 1000`
* **float** → nombres décimaux → `3.14, -2.7`
* **str** → chaînes de caractères → `"Bonjour"`
* **bool** → booléens → `True / False`

---

## 3. Conditions

Permettent de faire des choix.

```python
age = 18

if age >= 18:
    print("Majeur")
elif age >= 13:
    print("Adolescent")
else:
    print("Enfant")
```

🔑 **Opérateurs logiques et de comparaison** :

* `==` (égal) / `!=` (différent)
* `<`, `<=`, `>`, `>=`
* `and` (ET), `or` (OU), `not` (NON)

---

## 4. Boucles

### Boucle `for`:

```python
for i in range(5):   # de 0 à 4
    print(i)

for lettre in "Python":
    print(lettre)
```

---

### Boucle `while`:

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

---

## 5. Fonctions

Une fonction permet de réutiliser du code.

```python
# Définition
def dire_bonjour(nom: str) -> str:
    return "Bonjour " + nom

# Appel
print(dire_bonjour("Alice"))
```

⚠️ Une fonction possède un nom (ici le nom est `dire_bonjour`).   

⚠️ Une fonction possède des paramètres ou non (ici le paramètre est `nom`).   

⚠️ Une fonction possède un résultat ou non (ici le résultat est une chaîne de caractères).   

⚠️ L’en-tête d’une fonction peut inclure des **annotations de type** pour préciser le type des paramètres et du résultat (ici `nom: str` indique que `nom` est une chaîne, et `-> str` indique que la fonction retourne une chaîne).

---

## 6. Bonus : petites astuces utiles

* Commentaire :

Mettre `#` au sein d'un code permet de créer un commentaire qui ne sera pas exécuté lors du lancement du programme.

* Entrée utilisateur :

```python
nom = input("Quel est ton nom ? ")
```

* Conversion de type :

```python
x = int("10")    # chaîne → entier
y = str(123)     # entier → chaîne
```

* formatage rapide :

```python
age = 20
print("J’ai ", age ,"  ans")
```
