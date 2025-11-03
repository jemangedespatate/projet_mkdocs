# <u>🧮 FICHE MÉMO – CONVERSIONS ET REPRÉSENTATIONS BINAIRES</u>

## <u>🔹 1. Base 10 → Base 2</u>

### <u>🔸 Méthode : Division successive par 2</u>

1. Divise le nombre par 2.
2. Note le **reste** (0 ou 1).
3. Recommence avec le **quotient** jusqu’à 0.
4. Lis les **restes à l’envers** → résultat binaire.

??? example "🟢 Exemple :"

    ```
    25 = 12 ÷ 2 + 1   
    12 = 6 ÷ 2  + 0   
    6 = 3 ÷ 2 + 0   
    3 = 1 ÷ 2 + 1   
    1 = 0 ÷ 2 + 1  

    25₁₀ = 11001₂  
    ```
---

## <u>🔹 2. Base 2 → Base 10</u>

### <u>🔸 Méthode : Somme des puissances de 2</u>

Multiplie chaque bit par sa puissance de 2, en partant de la droite.

??? example "🟢 Exemple :"

    ```
    11001₂ = (1×2⁴) + (1×2³) + (0×2²) + (0×2¹) + (1×2⁰)

    = 16 + 8 + 1
    = 25₁₀
    ```

---

## <u>🔹 3. Base 16 → Base 10</u>

### <u>🔸 Méthode : Somme des puissances de 16</u>

Chaque chiffre hexadécimal vaut 0–15 (A=10, B=11, C=12, D=13, E=14, F=15).

??? example "🟢 Exemple :"

    ```
    3A₁₆ = (3×16¹) + (10×16⁰) = 48 + 10 = 58₁₀
    ```
---

## <u>🔹 4. Base 10 → Base 16</u>

### <u>🔸 Méthode : Division par 16</u>

1. Divise par 16.
2. Note le reste (0–9 ou A–F).
3. Lis les restes à l’envers.

??? example "🟢 Exemple :"

    ```
    254 = 15 × 16 + 14   → reste 14 → E  
    15  = 0 × 16  + 15   → reste 15 → F  

    254₁₀ = FE₁₆
    ```
---

## <u>🔹 5. Partie fractionnaire (décimale ↔ binaire)</u>

### <u>🔸 a) Décimal → Binaire (partie après la virgule)</u>

1. Divise la partie fractionnaire par 2.
2. Note la **partie entière** (0 ou 1).
3. Garde la **partie fractionnaire restante** et recommence.
4. Lis les bits dans l’ordre obtenu.

??? example "🟢 Exemple :"

    ```
    0,625 = 1 × 2 + 1,25
    0,25 = 0 × 2 + 0,5
    0,5 = 1 × 2 + 0

    0,625₁₀ = 0,101₂
    ```
---

### <u>🔸 b) Binaire → Décimal (partie après la virgule)</u>

Chaque bit après la virgule vaut une puissance **négative** de 2 : 2⁻¹, 2⁻², etc.

??? example "🟢 Exemple :"

    $$
    0{,}101_2 = (0 \times 2^{0}) + (1 \times 2^{-1}) + (0 \times 2^{-2}) + (1 \times 2^{-3})
    $$

    $$
    0{,}101_2 = 0 + 0{,}5 + 0 + 0{,}125 = 0{,}625_{10}
    $$


---

## <u>🔹 6. Virgule fixe</u>

* La **position de la virgule** est **fixe** dans le nombre binaire.

??? example "🟢 Exemple :"

  * 4 bits avant la virgule, 4 après → 1010.0110₂

* Simple mais **peu flexible** (gamme limitée).

---

## <u>🔹 7. Virgule flottante</u>

* La **virgule “flotte”** : le nombre est écrit sous la forme
  **± mantisse × base^exposant**
* En binaire : **signe | exposant | mantisse**

??? example "🟢 Exemple :"
  
  1,101 × 2³ = **1101₁₀₀₀₂**

* Grande plage de valeurs, mais moins précis.

---

## <u>🔹 8. Bit de signe</u>

* Le **bit le plus à gauche** indique le **signe** :

  * 0 → nombre positif
  * 1 → nombre négatif

??? example "🟢 Exemple :"

    * 0 1011010 = +90
    * 1 1011010 = -90 (en complément à deux)

---

## <u>🔹 9. Complément à 2 (représentation des négatifs)</u>

### <u>🔸 Pour obtenir le complément à 2 :</u>

1. Inverse tous les bits (0 → 1, 1 → 0).
2. Ajoute **1** au résultat.

??? example "🟢 Exemple :"

    Nombre : 00010110 (22)

    * Inversion : 11101001
    * +1 : 11101010 = **–22**

### <u>🔸 Pour retrouver la valeur :</u>

1. Inverse les bits.
2. Ajoute 1.

