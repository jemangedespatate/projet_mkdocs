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

## DÉFI 4 : LE PGCD (ALGORITHME D'EUCLIDE)

Le Plus Grand Commun Diviseur (PGCD) de deux nombres entiers est le plus grand entier naturel qui divise simultanément ces deux nombres sans laisser de reste.
Une méthode très élégante (et historique !) pour le trouver par ordinateur repose sur des soustractions successives : tant que les deux nombres sont différents, on soustrait toujours le plus petit au plus grand. Quand ils finissent par être strictement égaux, bingo : c'est le PGCD !

**Objectif :**
Deux nombres sont situés aux adresses **80** et **81** (ex: 15 et 25).
Calculez leur PGCD avec l'algorithme d'Euclide et stockez la réponse finale à l'adresse **82** (dans l'exemple, le résultat attendu serait 5).

!!! tip "Astuce"
    Chargez les deux valeurs dans deux registres. Comparez-les (`CMP`). S'ils sont égaux, la boucle est finie et vous pouvez sauter vers la fin du code. Sinon, identifiez le plus grand grâce à un branchement conditionnel (`BGT`) et soustrayez-lui le plus petit (`SUB`), puis repartez au tout début de votre boucle de comparaison !

---

## DÉFI 5 : LE CALCUL DE PUISSANCE (A puissance B)

En mathématiques, `A` puissance `B` consiste à multiplier le nombre `A` par lui-même `B` fois. Par exemple, `2` à la puissance `3` vaut `2 * 2 * 2 = 8`.
Problème critique : notre processeur ne sait pas multiplier nativement, et encore moins calculer des puissances. Il va falloir ruser !

**Objectif :**
Le nombre `A` (la base) est stocké à l'adresse **90** (ex: 2).
Le nombre `B` (l'exposant) est stocké à l'adresse **91** (ex: 3).
Calculez ce résultat et enregistrez-le à l'adresse **92**.

!!! tip "Astuce"
    C'est le **défi ultime** de ce TP, car il requiert de programmer des "boucles imbriquées". 
    Une boucle principale va utiliser le compteur d'exposant (ex: 3, puis 2, puis 1), et à l'intérieur de celle-ci, il faudra exécuter votre programme de multiplication par additions répétées ! Prenez une feuille de papier au brouillon pour noter le rôle précis de chaque registre (compteur global, compteur de multiplication, accumulateur des sommes, base originelle...).

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
