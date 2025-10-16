### 🔢 Exercice : Conversion décimal → binaire

Convertis les nombres décimaux suivants en nombres binaires :

| N° | Nombre décimal | Nombre binaire |
| -- | -------------- | -------------- |
| 1  | 6              |                |
| 2  | 13             |                |
| 3  | 25             |                |
| 4  | 42             |                |
| 5  | 100            |                |
| 6  | 255            |                |
| 7  | 73             |                |
| 8  | 128            |                |
| 9  | 37             |                |
| 10 | 200            |                |


### 🔢 Exercice : Conversion binaire → décimal

Convertis les nombres binaires suivants en nombres décimaux :

| N° | Nombre binaire | Nombre décimal |
| -- | -------------- | -------------- |
| 1  | 1010           |                |
| 2  | 1101           |                |
| 3  | 10011          |                |
| 4  | 101010         |                |
| 5  | 11111111       |                |
| 6  | 1001001        |                |
| 7  | 11001000       |                |
| 8  | 10000000       |                |
| 9  | 101101         |                |
| 10 | 11100100       |                |

### 🔢 Exercice : Conversion décimal → hexadécimal

Convertis les nombres décimaux suivants en nombres hexadécimaux :

| N° | Nombre décimal | Nombre hexadécimal |
| -- | -------------- | ------------------ |
| 1  | 10             |                    |
| 2  | 15             |                    |
| 3  | 26             |                    |
| 4  | 47             |                    |
| 5  | 64             |                    |
| 6  | 99             |                    |
| 7  | 120            |                    |
| 8  | 175            |                    |
| 9  | 200            |                    |
| 10 | 255            |                    |

### 🔢 Exercice : Conversion hexadécimal → décimal

Convertis les nombres hexadécimaux suivants en nombres décimaux :

| N° | Nombre hexadécimal | Nombre décimal |
| -- | ------------------ | -------------- |
| 1  | A                  |                |
| 2  | F                  |                |
| 3  | 1A                 |                |
| 4  | 2F                 |                |
| 5  | 3C                 |                |
| 6  | 4B                 |                |
| 7  | 7D                 |                |
| 8  | 9F                 |                |
| 9  | B4                 |                |
| 10 | FF                 |                |

### 🔢 Exercice : Conversion d’un nombre flottant (réel) → binaire

Convertis les nombres décimaux suivants (avec partie entière et partie fractionnaire) en **binaire**.
Indique les étapes de conversion pour la partie entière et pour la partie fractionnaire.

| N° | Nombre décimal (flottant) | Nombre binaire |
| -- | ------------------------- | -------------- |
| 1  | 5,5                       |                |
| 2  | 10,25                     |                |
| 3  | 3,75                      |                |
| 4  | 7,125                     |                |
| 5  | 12,375                    |                |
| 6  | 0,625                     |                |
| 7  | 19,1                      |                |
| 8  | 2,5625                    |                |
| 9  | 8,75                      |                |
| 10 | 15,9375                   |                |


### 🔢 Exercice : Conversion binaire (flottant) → décimal

Convertis les nombres binaires suivants (avec partie fractionnaire) en **nombres décimaux**.
N’oublie pas d’indiquer les étapes de calcul pour la partie entière et la partie fractionnaire.

| N° | Nombre binaire (flottant) | Nombre décimal |
| -- | ------------------------- | -------------- |
| 1  | 101.1                     |                |
| 2  | 110.01                    |                |
| 3  | 10.101                    |                |
| 4  | 1111.001                  |                |
| 5  | 1001.011                  |                |
| 6  | 0.101                     |                |
| 7  | 11.111                    |                |
| 8  | 1010.0001                 |                |
| 9  | 100.1101                  |                |
| 10 | 111.0111                  |                |

### 🔢 Exercice : Représentation avec complément à deux

Convertis les nombres décimaux suivants en **représentation binaire sur 8 bits**,
en utilisant le **bit de signe**.
Pour les nombres négatifs, utilise la **méthode du complément à deux**.

| N° | Nombre décimal | Représentation binaire (8 bits) |
| -- | -------------- | ------------------------------- |
| 1  | +7             |                                 |
| 2  | -7             |                                 |
| 3  | +12            |                                 |
| 4  | -12            |                                 |
| 5  | +25            |                                 |
| 6  | -25            |                                 |
| 7  | +64            |                                 |
| 8  | -64            |                                 |
| 9  | +100           |                                 |
| 10 | -100           |                                 |

### 🔢 **Exercice : Représentation en virgule flottante (notation scientifique binaire)**

On souhaite représenter les nombres suivants sous la forme :

$$
N = (1,\text{mantisse}) \times 2^{\text{exposant}}
$$

#### **Consignes :**

Pour chaque nombre décimal :

1. Convertis-le en binaire (partie entière + fractionnaire).
2. Normalise-le pour qu’il soit sous la forme $$1,\text{mantisse} \times 2^{\text{exposant}} $$
3. Indique la mantisse et l’exposant séparément.

| N° | Nombre décimal | Représentation binaire | Notation scientifique binaire | Mantisse | Exposant |
| -- | -------------- | ---------------------- | ----------------------------- | -------- | -------- |
| 1  | 6,5            |                        |                               |          |          |
| 2  | 10,25          |                        |                               |          |          |
| 3  | 0,375          |                        |                               |          |          |
| 4  | 19,5           |                        |                               |          |          |
| 5  | 0,1            |                        |                               |          |          |
| 6  | 3,125          |                        |                               |          |          |
| 7  | 12,75          |                        |                               |          |          |
| 8  | 7,5            |                        |                               |          |          |
| 9  | 0,625          |                        |                               |          |          |
| 10 | 25,25          |                        |                               |          |          |

### 🌟 **Exercice avancé : Représentation IEEE 754 (simple précision, 32 bits)**

On rappelle que dans le format IEEE 754 simple précision :

* **1 bit de signe** (0 = positif, 1 = négatif)
* **8 bits d’exposant** (avec un biais de 127)
* **23 bits de mantisse** (sans le 1 implicite)

La valeur représentée est :

$$
N = (-1)^{\text{signe}} \times (1,\text{mantisse}) \times 2^{(\text{exposant} - 127)}
$$

---

#### **Consignes :**

1. Pour chaque nombre décimal donné, écris :

   * sa conversion binaire,
   * sa forme normalisée ( (1,\text{mantisse}) \times 2^{\text{exposant}} ),
   * puis son codage complet sur **32 bits IEEE 754** :
     **[signe | exposant (8 bits) | mantisse (23 bits)]**
2. Vérifie le résultat final en reconvertissant le binaire vers le décimal.

---

| N° | Nombre décimal | Signe | Exposant (8 bits) | Mantisse (23 bits) | Représentation 32 bits |
| -- | -------------- | ----- | ----------------- | ------------------ | ---------------------- |
| 1  | +6,5           |       |                   |                    |                        |
| 2  | -12,75         |       |                   |                    |                        |
| 3  | +0,15625       |       |                   |                    |                        |
| 4  | -19,25         |       |                   |                    |                        |
| 5  | +100,5         |       |                   |                    |                        |
| 6  | -0,75          |       |                   |                    |                        |
| 7  | +255,125       |       |                   |                    |                        |
| 8  | -0,03125       |       |                   |                    |                        |
| 9  | +3,1416        |       |                   |                    |                        |
| 10 | -7,875         |       |                   |                    |                        |

