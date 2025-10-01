# 🐍 Fiche Mémo Python

## 🔹 Variables

```python
x = 10
nom = "Alice"
pi = 3.14
vrai = True

x = x - 1
```

👉 Une **variable** sert à stocker une valeur (nombre, texte, booléen…).
👉 Il est possible de modifier une variable.

---

## 🔹 Conditions

```python
age = 18

if age >= 18:
    print("Majeur")
elif age > 12:
    print("Adolescent")
else:
    print("Enfant")
```

👉 Les **conditions** permettent d’exécuter du code seulement si une règle est respectée.
👉 Comparaisons possibles : `==` (égal), `!=` (différent), `<` (plus petit), `>` (plus grand), `<=` (plus petit ou égal), `>=` (plus grand ou égal).
👉 Une fois une condition validée, Python n’examine plus les suivantes.

---

## 🔹 Boucle `for`

```python
for i in range(5):   # de 0 à 4
    print(i)
```

👉 Une **boucle** répète un bloc de code plusieurs fois.
👉 `range(n)` fait tourner la boucle **n fois**.
👉 `i` est la variable de boucle qui change à chaque tour.
👉 `i` commence à 0 et évolue de 1 en 1 à chaque tour de boucle.

---

## 🔹 Fonctions

```python
def ajoute_un(nombre):
    return nombre + 1 

print(ajoute_un(5))   # affiche 6
```

👉 Une **fonction** est un bloc de code réutilisable.
👉 Une fonction peut prendre des **paramètres**.
👉 Une fonction peut renvoyer un **résultat**.
👉 Ici, la fonction s’appelle `ajoute_un`, elle prend un nombre en paramètre et renvoie ce nombre + 1.