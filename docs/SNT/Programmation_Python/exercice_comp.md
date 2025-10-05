# <u>Exercices pratiques</u>

**<u>1. Variables et affichage**</u>

Créer deux variables, **nom** et **âge**, puis afficher :

```
Bonjour <nom>, dans 10 ans tu auras <âge + 10> ans.
```

---

**<u>2. Opérations mathématiques**</u>

Écrivez un programme qui demande deux nombres à l’utilisateur et affiche :

* la somme
* la différence
* le produit

---

**<u>3. Conditions**</u>

Écrire un programme qui crée une variable note et affiche :

* `"Très bien"` si la note ≥ 16
* `"Assez bien"` si la note ≥ 12
* `"Passable"` si la note ≥ 10
* `"Insuffisant"` sinon

---

**<u>4. Boucles**</u>

Affichez tous les nombres **pairs** de 1 à 20 en utilisant une boucle `for`
Voici une version claire et pédagogique de ta phrase, avec une **explication du modulo** incluse 👇

💡 *Indice : l’opérateur `%` s’appelle le **modulo**. Il donne le **reste** d’une division entre deux nombres.*

Par exemple :

* `7 % 2 = 1` car 7 ÷ 2 = 3 reste 1
* `8 % 2 = 0` car 8 ÷ 2 = 4 reste 0

👉 Donc, **si un nombre % 2 est égal à 0, cela signifie qu’il est pair** (car il est divisible par 2 sans reste).

---

**<u>5. Fonctions**</u>

créez une fonction `carre(x)` qui renvoie le carré d’un nombre.

Testez-la avec plusieurs nombres et affichez les résultats.

### exercie complémentaire: calcul de moyenne

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
