## 🧠 Cours : Les booléens en NSI (Première)

### 1. Qu’est-ce qu’un booléen ?

Un **booléen** (ou *bool*) est un type de donnée logique qui ne peut prendre **que deux valeurs** :

* `True` → Vrai
* `False` → Faux

Ces deux valeurs permettent à un programme de **prendre des décisions** : faire une action **si** une condition est vraie, ou une autre **sinon**.

> En Python :

```python
a = True
b = False
print(a, b)
```

??? Example "Exercice :"

    ### 1️⃣ Partie A — Logique du quotidien

    | N° | Affirmation                       | Réponse (Vrai / Faux) |
    | -- | --------------------------------- | --------------------- |
    | 1  | Le soleil se lève à l’ouest.      |                       |
    | 2  | Un carré a quatre côtés égaux.    |                       |
    | 3  | 2 + 2 = 5                         |                       |
    | 4  | L’eau gèle à 0°C.                 |                       |
    | 5  | Tous les chiens sont des animaux. |                       |

    ---

    ### 2️⃣ Partie B — Expressions logiques

    | Expression                      | Résultat booléen | Justification |
    | ------------------------------- | ---------------- | ------------- |
    | 5 est plus grand que 3          |                  |               |
    | 8 est égal à 8                  |                  |               |
    | 10 est plus petit que 4         |                  |               |
    | “bleu” est différent de “rouge” |                  |               |


### 2. Les expressions booléennes

Une **expression booléenne** est une expression qui **se calcule en vrai ou faux**.
Exemples :

```python
5 > 3        # True
10 == 2 * 5  # True
7 <= 4       # False
"a" != "b"   # True
```

👉 Les opérateurs de comparaison :

| Opérateur | Signification     | Exemple  | Résultat |
| --------- | ----------------- | -------- | -------- |
| `==`      | égal à            | `3 == 3` | True     |
| `!=`      | différent de      | `3 != 2` | True     |
| `<`       | inférieur à       | `2 < 5`  | True     |
| `<=`      | inférieur ou égal | `3 <= 3` | True     |
| `>`       | supérieur à       | `7 > 10` | False    |
| `>=`      | supérieur ou égal | `5 >= 2` | True     |

??? Example "Exercice :"

    ### 1️⃣ Partie A — Vrai ou Faux ?

    Pour chaque affirmation, indique si elle est **vraie** ou **fausse**.

    | Affirmation | Réponse (Vrai / Faux) | Justification |
    |--------------|----------------------|----------------|
    | 9 est supérieur à 4 | | |
    | 7 est inférieur à 7 | | |
    | 12 est égal à 3 × 4 | | |
    | 15 est différent de 5 × 3 | | |
    | 8 est supérieur ou égal à 8 | | |

    ---

    ### 2️⃣ Partie B — Trouve la comparaison correcte

    Complète les phrases suivantes avec le bon signe parmi : `<`, `>`, `==`, `!=`, `<=`, `>=`.

    1. 5 ___ 3  
    2. 10 ___ 2 × 5  
    3. 7 ___ 9  
    4. 6 × 2 ___ 11 + 1  
    5. 15 ___ 3 × 5  

    ---

    ### 3️⃣ Partie C — Lecture de phrases

    Coche les phrases qui pourraient être **vraies** dans un programme informatique :

    - [ ] Le mot de passe est égal à “secret”.  
    - [ ] Le nombre de vies du joueur est inférieur à 0.  
    - [ ] Le score est supérieur à 1000.  
    - [ ] Le nombre de pommes est différent du nombre de poires.  
    - [ ] 2 est plus grand que 8.  


---

### 3. Les opérateurs logiques

Les booléens peuvent être **combinés** à l’aide d’opérateurs logiques.

| Opérateur | Signification | Exemple          | Résultat |
| --------- | ------------- | ---------------- | -------- |
| `and`     | ET logique    | `True and False` | False    |
| `or`      | OU logique    | `True or False`  | True     |
| `not`     | NON logique   | `not True`       | False    |

**Exemples en Python :**

```python
x = 5
print(x > 0 and x < 10)   # True (les deux conditions sont vraies)
print(x < 0 or x > 10)    # False (aucune condition vraie)
print(not(x == 5))        # False (car x == 5 est vrai)
```

??? Example "Exercice :"

    ### 1️⃣ Partie A — Comprendre les opérateurs

    Recopie les phrases suivantes et indique si la **conclusion est vraie ou fausse**.

    #### a) Opérateur **ET (and)**

    > La phrase est **vraie seulement si les deux affirmations sont vraies.**

    | Situation                                                                          | Résultat (Vrai / Faux) |
    | ---------------------------------------------------------------------------------- | ---------------------- |
    | Il fait **beau** ET il fait **chaud**. (Il fait beau : Vrai, il fait chaud : Vrai) |                        |
    | Il fait **beau** ET il fait **froid**. (Vrai, Faux)                                |                        |
    | Il **pleut** ET il fait **froid**. (Faux, Faux)                                    |                        |

    🧠 *Quand utilise-t-on “ET” dans la vie de tous les jours ?*

    ---

    #### b) Opérateur **OU (or)**

    > La phrase est **vraie si au moins une des deux affirmations est vraie.**

    | Situation                                                               | Résultat (Vrai / Faux) |
    | ----------------------------------------------------------------------- | ---------------------- |
    | Je mange **une pomme** OU une **banane**. (pomme : Vrai, banane : Faux) |                        |
    | Je mange **une pomme** OU une **banane**. (pomme : Faux, banane : Vrai) |                        |
    | Je ne mange **ni pomme** ni **banane**. (Faux, Faux)                    |                        |

    💡 *→ L’opérateur “OU” en logique signifie “au moins un des deux est vrai”.*

    ---

    #### c) Opérateur **NON (not)**

    > “NON” inverse la valeur logique :
    > Vrai devient Faux, et Faux devient Vrai.

    | Situation                                              | Résultat (Vrai / Faux) |
    | ------------------------------------------------------ | ---------------------- |
    | Il **ne pleut pas** (si “il pleut” est Faux)           |                        |
    | Il **ne fait pas chaud** (si “il fait chaud” est Vrai) |                        |
    | Il **ne neige pas** (si “il neige” est Faux)           |                        |

    ---

    ### 2️⃣ Partie B — Logique combinée

    Lis les affirmations et détermine si elles sont **vraies ou fausses**.
    Tu peux t’aider des règles précédentes.

    | Affirmation         | Résultat (Vrai / Faux) |
    | ------------------- | ---------------------- |
    | (Vrai ET Faux)      |                        |
    | (Vrai OU Faux)      |                        |
    | NON(Vrai)           |                        |
    | (Faux OU Faux)      |                        |
    | NON(Faux)           |                        |
    | (Vrai ET NON(Faux)) |                        |


---

### 4. Les tables de vérité

#### a. Opérateur `and`

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

#### b. Opérateur `or`

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

#### c. Opérateur `not`

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

### 5. Booléens et conditions

Les booléens sont souvent utilisés dans les **structures conditionnelles** :

```python
x = 7

if x > 5:
    print("x est grand")
else:
    print("x est petit")
```

Le test `x > 5` est une **expression booléenne** qui détermine quelle partie du code s’exécute.

---

### 6. Conversion en booléen

Python peut convertir n’importe quelle valeur en booléen avec `bool()` :

```python
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False (chaîne vide)
print(bool("test"))  # True
```

> ⚠️ Attention : en Python, **0, "", [], {}, None** sont considérés comme **False**.
