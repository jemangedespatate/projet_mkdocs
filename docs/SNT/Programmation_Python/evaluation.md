# évaluation

<script>
  const password = "mdpi251"; // mot de passe
  const userInput = prompt("Entrez le mot de passe pour accéder à cette page :");

  if (userInput !== password) {
    alert("Mot de passe incorrect !");
    window.location.href = "/";
  }
</script>

## 🧩 **Exercice 1 — Les variables**

Crée trois variables :

* `largeur` qui doit etre egale a 5
* `logueur` qui doit etre egale a 8
* `aire` qui contient le résultat du calcul de l’aire d’un rectangle (rappel: l'aire d'un rectangle est egale au produit de sa longeur et de ca largeur)

Le programme doit ensuite afficher :

```
L’aire du rectangle est de 40 unités carrées.
```

---

## 🔁 **Exercice 2 — Les boucles**

Écris un programme qui affiche un carré de 5 étoiles de côté en utilisant une boucle `for`, comme ceci :

```
*****
*****
*****
*****
*****
```

## ⚖️ **Exercice 3 — Les conditions**

Crée une variable `vitesse` contenant la valeur `110`.

Le programme doit afficher :

* `"Trop vite !"` si la vitesse est supérieure à 130
* `"Bonne vitesse."` si elle est comprise entre 80 et 130 inclus
* `"Trop lent."` si elle est inférieure à 80
* `"a l'arret."` si la vitesse est egale a 0

## 🧩 **Exercice 4 — Les fonctions**

### Programme à observer :

```python
def convertir_minutes_en_heures(minutes):
    heures = minutes / 60
    return heures

t1 = convertir_minutes_en_heures(120)
t2 = convertir_minutes_en_heures(90)

print(t1)
print(t2)
```

---

### ✏️ Questions :

1. Quel est le **nom** de la fonction ?
2. Quel est le **paramètre** de cette fonction ?
3. Que fait la fonction avec la valeur donnée ?
4. Quelle **valeur est renvoyée** (retournée) par la fonction ?
5. Quelle est la **valeur de `t1`** après l’appel `convertir_minutes_en_heures(120)` ?
6. Quelle est la **valeur de `t2`** après l’appel `convertir_minutes_en_heures(90)` ?
7. Que va afficher le programme à l’écran ?
8. Si on écrivait `print(convertir_minutes_en_heures(45))`, que s’afficherait-il ?

