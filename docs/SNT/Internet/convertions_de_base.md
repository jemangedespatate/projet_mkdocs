# Le système binaire

## 🤔 Introduction

Les ordinateurs ne comprennent pas les nombres comme nous les utilisons au quotidien. Ils fonctionnent uniquement avec deux valeurs : **0** et **1**. Pour cette raison, ils utilisent le **système binaire**, aussi appelé **base 2**.

Dans ce cours, nous allons voir :

* comment **passer d’un nombre décimal à un nombre binaire** ;
* comment **passer d’un nombre binaire à un nombre décimal**.

---

## 🔢 Les bases de numération

* Le **système décimal** (base 10) utilise 10 chiffres : de 0 à 9.
* Le **système binaire** (base 2) utilise seulement 2 chiffres : 0 et 1.

Chaque position d’un chiffre dépend de la base utilisée.

---

## ➡️ Passage d’un nombre décimal à un nombre binaire

Pour convertir un nombre décimal en binaire, on utilise la méthode des **divisions successives par 2**.

### Méthode

1. On divise le nombre par 2.
2. On note le **reste** (0 ou 1).
3. On recommence avec le **quotient** obtenu.
4. On s’arrête lorsque le quotient vaut 0.
5. Le nombre binaire est obtenu en **lisant les restes de bas en haut**.

---

### Exemple : convertir 21 en binaire


$$21 = 10 \times 2 + 1 \$$
$$10 = 5 \times 2 + 0 \$$
$$5 = 2 \times 2 + 1 \$$
$$2 = 1 \times 2 + 0 \$$
$$1 = 0 \times 2 + 1$$


On lit les restes de bas en haut :

$$
21_{10} = 10101_2
$$

---

## ⬅️ Passage d’un nombre binaire à un nombre décimal

Pour convertir un nombre binaire en décimal, on utilise les **puissances de 2**.

Chaque chiffre du nombre binaire est multiplié par une puissance de 2, en commençant par la droite.

---

### Méthode

1. On numérote les positions à partir de la droite, en commençant par 0.
2. On multiplie chaque bit par $$2^{\text{position}}$$
3. On additionne tous les résultats.

---

### Exemple : convertir 110 en décimal

$$
110_2 = 1 \times 2^2 + 1 \times 2^1 + 0 \times 2^0
$$

$$
= 4 + 2 + 0 = 6
$$

Donc :

$$
110_2 = 6_{10}
$$
