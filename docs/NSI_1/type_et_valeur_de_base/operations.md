# <u>🔢 representation des nombre en machine</u>

## <u>ℹ️ Introduction</u>

Les ordinateurs ne comprennent que deux symboles : 0 et 1.   
Ces deux valeurs correspondent à deux états électriques (passage du courant ou absence de courant) et constituent la base du langage binaire.

Mais comment représenter, avec uniquement des suites de 0 et de 1, tous les nombres que nous utilisons en mathématiques : entiers positifs, entiers négatifs, fractions, nombres très grands ou très petits ?

La réponse repose sur différentes méthodes de représentation des nombres en machine.
Au fil du temps, des conventions se sont imposées pour :

* coder les entiers positifs et négatifs,

* représenter les fractions et nombres réels grâce à la virgule fixe ou la virgule flottante,

* normaliser cette écriture avec des standards modernes comme la norme IEEE 754.

## <u>➕ Les entiers positifs</u>

Un ordinateur manipule les entiers positifs en utilisant le **système binaire**.   
Chaque chiffre binaire (bit) peut être **0** ou **1**.

* Avec **n bits**, on peut représenter des entiers allant de :

$$
0 \quad \text{à} \quad 2^n - 1
$$

!!! example "Exemples :"

    * Avec **3 bits** → nombres de 0 à 7 :

        * 000 = 0
        * 001 = 1
        * 010 = 2
        * 011 = 3
        * 100 = 4
        * 101 = 5
        * 110 = 6
        * 111 = 7

    * Avec **8 bits (1 octet)** → nombres de 0 à 255.

    * Avec **16 bits** → nombres de 0 à 65 535.

## <u>🌊 Les nombres flottants</u>

Jusqu’ici, nous avons vu comment représenter les entiers en machine.
Cependant, dans de nombreux calculs, il est nécessaire de manipuler des nombres décimaux : par exemple des mesures (3,14 mètres, 0,25 seconde), des résultats scientifiques ou encore des valeurs financières.

Le problème est que l’ordinateur ne dispose que d’un nombre limité de bits, et il faut donc trouver une manière efficace de représenter ces nombres qui comportent une partie fractionnaire.

Deux grandes approches ont été développées :

* La virgule fixe, qui consiste à réserver un certain nombre de bits pour la partie entière et un certain nombre pour la partie décimale.

* La virgule flottante, qui utilise une écriture proche de la notation scientifique (en base 2), permettant de représenter des nombres très grands comme des nombres très petits avec une certaine précision.

Ces méthodes ont chacune leurs avantages et leurs limites, et elles ont conduit à l’établissement de normes modernes pour assurer une représentation standardisée dans tous les ordinateurs.

### <u>1. La virgule fixe</u>

Dans ce système, on réserve un certain nombre de bits pour la **partie entière** et un certain nombre de bits pour la **partie fractionnaire**.

!!! example "Exemple :"
    
    Imaginons qu’on ait 8 cases (bits) pour écrire un nombre : on peut en utiliser 4 pour la partie avant la virgule (la partie entière) et 4 pour la partie après la virgule (la partie décimale).

    ```
    1101.0101
    ```

    * Partie entière : `1101` = 13
    * Partie fractionnaire : `0101` = 0,3125
    * Résultat = **13,3125**

✅ Avantage : simple à comprendre et à utiliser.

❌ Inconvénient : la précision est **fixe** et limitée. On ne peut pas représenter à la fois de très grands nombres et de très petits nombres.


!!! note "partie fractionnaire"
    
    Dans le système binaire, la **partie entière** se lit comme d’habitude (avec des puissances de 2 positives).
    En revanche, la **partie fractionnaire** se calcule avec des puissances de 2 **négatives** :

    $$
    0,abcd₂ = a \times \frac{1}{2} + b \times \frac{1}{2^2} + c \times \frac{1}{2^3} + d \times \frac{1}{2^4} + \dots
    $$

    ### <u>Exemple avec `0,0101₂` :</u>

    * Le premier chiffre après la virgule est `0` → $$0 \times \frac{1}{2} = 0$$
    * Le deuxième chiffre est `1` → $$1 \times \frac{1}{4} = 0,25$$
    * Le troisième chiffre est `0` → $$0 \times \frac{1}{8} = 0$$
    * Le quatrième chiffre est `1` → $$1 \times \frac{1}{16} = 0,0625$$

    On additionne :

    $$
    0,25 + 0,0625 = 0,3125
    $$

    Donc :

    $$
    0,0101₂ = 0,3125_{10}
    $$

!!! question "📝 Exercice 1:"

    Convertis les nombres binaires suivants en décimal :

    1. `0,1₂`
    2. `0,01₂`
    3. `0,11₂`
    4. `0,101₂`
    5. `0,1101₂`

!!! question "📝 Exercice 2:"

    Représente les nombres décimaux suivants en binaire sur 8 bits, 
    en utilisant 4 bits pour la partie entière et 4 bits pour la partie fractionnaire.

    1. 5,5  
    2. 2,25  
    3. 7,75  
    4. 3,125

### <u>2. La virgule flottante</u>

Pour dépasser les limites de la virgule fixe, on utilise une écriture proche de la **notation scientifique**.
    
$$
314 = 3,14 \times 10^2
$$

En binaire, on applique la même idée :

$$
N = (1,\text{mantisse}) \times 2^{\text{exposant}}
$$

* **Mantisse** : contient les chiffres significatifs
* **Exposant** : détermine où se situe la virgule


!!! example "Exemple :"

    Nombre décimal : 13,25
    Conversion en binaire : 13,25 = 1101,01₂
    Écriture scientifique binaire : 1,10101 × 2^3

    - Exposant : 3 = 011₂
    - Mantisse : 10101 (on garde 5 bits après la virgule)

    → Stockage en machine sur 8 bits (sans biais, sans bit de signe) :
    ```
    011 10101
    ```

    Explication :  
    - Les **3 premiers bits** représentent l’exposant (`011`).  
    - Les **5 bits suivants** représentent la mantisse (`10101`).  
    - La valeur décimale peut être reconstruite :  
    1,10101₂ × 2^3 ≈ 13,25

!!! question "📝 Exercice 3:"

    Représente les nombres décimaux suivants en virgule flottante 
    dans un format simplifié sur 8 bits :

    - 3 bits pour l’exposant
    - 4 bits pour la mantisse (après la virgule)

    1. +5,5
    2. +0,75

!!! question "📝 Exercice code:"

    * completez la fonction suivante

    ```py
    def frac_to_bin(fraction: float, m: int) -> str:
        """
        Fonction permettant de convertir la partie fractionnaire d'un nombre décimal
        en binaire sur m bits.

        Paramètres:
            fraction: float, la partie fractionnaire (0 <= fraction < 1)
            m: int, le nombre de bits maximum à générer

        Retour:
            str, la chaîne de caractères représentant la partie fractionnaire en binaire

        Exemple:
        >>> frac_to_bin(0.625, 5)
        '10100'
        """
    ```

    * completez la fonction suivante

    ```py
    def bin_to_frac(bits: str) -> float:
        """
        Fonction permettant de convertir une chaîne binaire représentant la partie
        fractionnaire d’un nombre en sa valeur décimale.

        Paramètres:
            bits: str, la chaîne binaire (ex: "101" correspond à 0.101₂)

        Retour:
            float, la valeur décimale correspondante

        Exemple:
        >>> bin_to_frac("101")
        0.625
        >>> bin_to_frac("00011")
        0.09375
        """
    ```

✅ Avantage : permet de représenter à la fois des **nombres très grands** et des **nombres très petits**.

❌ Inconvénient : pas tous les nombres décimaux sont représentables exactement (par exemple 0,1 en binaire).

## <u>➖ Les nombres négatifs</u>

En mathématiques sur papier, on indique simplement qu’un nombre est négatif en mettant un signe “-” devant.
En informatique, les ordinateurs ne comprennent que des suites de 0 et de 1. Il faut donc définir une **méthode précise pour représenter les nombres négatifs** en binaire.

Différentes méthodes ont été utilisées pour coder les nombres négatifs, dont :

1. le **bit de poids fort** (où un bit indique simplement le signe),
2. le **complément à 2**, la méthode standard utilisée dans tous les ordinateurs modernes.

### <u>1. Bit de poids fort</u>

* Idée : le **bit le plus à gauche** (bit de poids fort) indique le signe du nombre :

  * `0` → positif
  * `1` → négatif

!!! example "Exemple :"

    Le nombre 13 s’écrit `1101` en binaire. 

    Pour le représenter sur 8 bits en machine :  

    * +13 → `00001101`  
    * -13 → `10001101` (en utilisant le bit de poids fort pour indiquer le signe)

!!! question "📝 Exercice 4:"

    Représente les nombres décimaux suivants en binaire sur 8 bits en utilisant le **bit de poids fort** pour le signe :

    1. +14  
    2. -9  
    3. +12  
    4. -5

❌ Inconvénient :

* Deux représentations du zéro : `00000000` et `10000000`
* Les calculs arithmétiques deviennent compliqués


### <u>2. Complément à 2</u>

Le complément à 2 est la **méthode standard** pour représenter les nombres négatifs en binaire.

**Règle :**
Pour obtenir -N :

1. On écrit N en binaire.
2. On inverse tous les bits (complément à 1).
3. On ajoute 1.


!!! example "Exemple :" 
    
    représenter -13 sur 8 bits a l'aide du complément à 2:

    1. +13 = `00001101`
    2. Inversion (complément à 1) = `11110010`
    3. Ajouter 1 = `11110011` → -13

!!! question "📝 Exercice 5:"

    Représenter les nombres suivants en **complément à 2** sur 8 bits :

    1. +12  
    2. -12  
    3. +7  
    4. -7

!!! question "📝 Exercice code:"

    * completez la fonction suivante

    ```py
    def bin_to_comp_2(nombre: str, n: int) -> str:
        """
        Fonction permettant de représenter en complément à 2, sur n bits,
        un nombre binaire donné en paramètre.

        Paramètres:
            nombre: str, le nombre binaire à convertir
            n: int, le nombre de bits utilisés pour la représentation

        Retour:
            str, la chaîne de caractères représentant le complément à 2
            du nombre en utilisant n bits

        Exemple:
        >>> bin_to_comp_2("101", 5)
        '11011'
        >>> bin_to_comp_2("1", 7)
        '1111111'
        """
    ```


    * completez la fonction suivante

    ```py
    def dec_to_comp_2(nombre: int, n: int) -> str:
    """
    Fonction permettant de convertir un entier en sa représentation
    en complément à 2 sur n bits.

    Paramètres:
        nombre: int, le nombre à convertir
        n: int, le nombre de bits utilisés pour la représentation

    Retour:
        str, la chaîne de caractères représentant le complément à 2
        du nombre en utilisant n bits

    Exemple:
    >>> dec_to_comp_2(5, 5)
    '00101'
    >>> dec_to_comp_2(-5, 5)
    '11011'
    >>> dec_to_comp_2(-1, 7)
    '1111111'
    """
    ```

    * completez la fonction suivante

    ```py
def dec_to_repr(nombre: int, n: int) -> str:
    """
    Fonction permettant de convertir un entier en binaire sur n bits :
    - si le nombre est positif ou nul → représentation binaire classique
    - si le nombre est négatif → représentation en complément à 2

    Paramètres:
        nombre: int, le nombre à convertir
        n: int, le nombre de bits utilisés pour la représentation

    Retour:
        str, la chaîne de caractères représentant le nombre en binaire
        classique si positif, ou en complément à 2 si négatif, sur n bits

    Exemple:
    >>> dec_to_repr(-5, 5)
    '11011'
    >>> dec_to_repr(5, 5)
    '00101'
    >>> dec_to_repr(-1, 7)
    '1111111'
    >>> dec_to_repr(1, 7)
    '0000001'
    """
    ```

✅ Avantages :

* Un seul zéro (`00000000`)
* Les additions et soustractions fonctionnent directement comme avec des nombres positifs

## <u>🖥️ La norme IEEE 754</u>

La norme **IEEE 754** définit comment représenter les nombres réels (à virgule flottante) en mémoire de manière standardisée, afin que tous les ordinateurs et logiciels manipulent les mêmes valeurs. Elle garantit la compatibilité et la précision dans les calculs scientifiques, financiers ou techniques.

### <u>1. Principe général</u>

Un nombre flottant est représenté par trois éléments :

$$
N = (-1)^{\text{signe}} \times 1,\text{mantisse} \times 2^{\text{exposant - biais}}
$$

1. **Signe** : 1 bit

    * `0` → nombre positif
    * `1` → nombre négatif

2. **Exposant** : stocke la puissance de 2.

    * Il est **biaisé** pour permettre la représentation d’exposants négatifs.
    * Exemple : en simple précision, le biais est 127. Si l’exposant réel est 3, on stocke 3 + 127 = 130.

3. **Mantisse** (ou fraction) : représente les chiffres significatifs du nombre.

    * Elle est toujours **normalisée**, ce qui signifie que le premier chiffre avant la virgule est toujours 1 (implémenté de manière implicite dans la norme IEEE 754).


### <u>2. Formats les plus courants</u>

#### <u>a. Simple précision (32 bits)</u>

* 1 bit pour le **signe**
* 8 bits pour l’**exposant** (biais = 127)
* 23 bits pour la **mantisse**

#### <u>b. Double précision (64 bits)</u>

* 1 bit pour le **signe**
* 11 bits pour l’**exposant** (biais = 1023)
* 52 bits pour la **mantisse**

### <u>3. Exemple pratique</u>

Nombre : `-13,25`

1. Conversion en binaire : 13,25 = `1101,01₂`
2. Écriture scientifique binaire : `1,10101 × 2^3`
3. Signe : `1` (négatif)
4. Exposant biaisé : 3 + 127 = 130 = `10000010`
5. Mantisse : `10101000000000000000000` (23 bits)

**Stockage IEEE 754 (32 bits) :**

```
1 10000010 10101000000000000000000
```

* 1er bit = signe
* 8 bits suivants = exposant biaisé
* 23 bits suivants = mantisse

### <u>4.✅ Avantages de la norme IEEE 754</u>

* **Standard universel** : même représentation sur tous les ordinateurs
* **Grande plage de valeurs** : peut représenter à la fois des nombres très grands et très petits
* **Gestion des cas particuliers** :

  * `+0` et `-0`
  * `+∞` et `-∞`
  * `NaN` (Not a Number, utilisé pour indiquer un résultat invalide)

* **Précision contrôlée** : le nombre de bits pour la mantisse définit la précision maximale


!!! question "📝 Exercice 6:"

    Convertis les nombres suivants en **notation IEEE 754 simple précision** (32 bits) :

    a. ( +10,5 )
    b. ( -0,75 )
    c. ( +5,25 )

    Pour chacun :

    1. Écris le nombre en **binaire**.
    2. Mets-le sous **forme scientifique binaire** (ex. : (1,xxx \times 2^n)).
    3. Indique :

    * le **bit de signe**
    * l’**exposant biaisé** (avec biais = 127)
    * la **mantisse** (23 bits)
    4. Donne la **représentation finale sur 32 bits**.

---

!!! question "📝 Exercice 7:"

    Le nombre suivant est stocké en IEEE 754 simple précision :

    ```
    0 10000010 01000000000000000000000
    ```

    a. Décode-le (signe, exposant, mantisse).
    b. Trouve la **valeur décimale** correspondante.
