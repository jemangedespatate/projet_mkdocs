# TP NSI : DÉFIS BONUS EN ASSEMBLEUR


**Lien du simulateur** : www.peterhigginson.co.uk/AQA/

---

## DÉFI 1 : LA DIVISION EUCLIDIENNE

Tout comme la multiplication, la division n'existe pas de base dans les instructions de notre processeur. Mais diviser, c'est finalement soustraire en boucle !

**Objectif :**
Divisez un nombre initial par un diviseur.
* Le nombre initial est situé à l'adresse **50** (ex: 23).
* Le diviseur est situé à l'adresse **51** (ex: 5).

Rangez le **quotient** (le résultat de la division, soit combien de fois le diviseur rentre en entier dans le nombre initial) à l'adresse **52** et le **reste** de cette division à l'adresse **53**.

!!! tip "Astuce"
    Soustrayez le diviseur au nombre initial dans une boucle tant que c'est possible. Utilisez un registre différent pour compter le nombre de soustractions (c'est votre quotient) !

---

## DÉFI 2 : LE TRI DE 3 NOMBRES

La mémoire RAM contient trois nombres désordonnés aux adresses **60**, **61** et **62**. 

**Objectif :**
Écrivez un programme qui les trie dans l'ordre croissant en réécrivant par dessus : le plus petit en **60**, le nombre du milieu en **61**, et le plus grand en **62**.

!!! tip "Astuce"
    Lisez les trois valeurs dans des registres. Comparez-les deux par deux. Si les nombres ne sont pas dans le bon ordre à l'intérieur de vos registres, échangez-les (on appelle ça faire un "swap") en utilisant un registre temporaire vide. Une fois que l'ordre est parfait, re-sauvegardez le tout en RAM !

---

## DÉFI 3 : LA SUITE DE FIBONACCI

La célèbre suite mathématique de Fibonacci commence par les nombres `0` et `1`. Ensuite, chaque nouveau nombre est simplement la somme des deux précédents.
La suite commence donc comme cela : `0, 1, 1, 2, 3, 5, 8, 13, 21, 34...`

**Objectif :**
Écrivez un programme exhaustif qui calcule et fait avancer la suite, pour trouver le **10ème terme** (qui doit logiquement être `34`) et le stocke à l'adresse **150**.

!!! tip "Astuce"
    Vous aurez besoin de plusieurs registres mobilisés. Par exemple, `R1` pour l'avant-dernier terme, `R2` pour le dernier terme, et `R3` pour faire l'addition et stocker le suivant.
    **Attention** : prévoyez un registre spécifique comme "compteur de boucle" pour vous arrêter exactement au 10ème terme, sinon votre processeur tournera à l'infini !

---

## AIDE-MÉMOIRE (RAPPEL SYNTAXE)

Si vous avez un trou de mémoire, voici un rappel des commandes de survie :

| COMMANDE | RÔLE |
| :--- | :--- |
| **MOV** Rd, #10 | Met le nombre 10 dans le registre Rd. |
| **LDR** Rd, 100 | Charge la valeur de l'adresse RAM 100 dans Rd. |
| **STR** Rd, 100 | Enregistre le contenu de Rd à l'adresse RAM 100. |
| **ADD / SUB** | Additionner ou Soustraire. |
| **CMP** Rd, #5 | Compare le registre Rd au chiffre 5. |
| **B** label | Saute directement à la ligne nommée (ex: `boucle:`). |
| **BGT / BEQ / BNE** | Saute si **Plus Grand** / **Égal** / **Différent** en se basant sur la dernière comparaison. |
| **HALT** | Arrêt immédiat et total du programme. |
