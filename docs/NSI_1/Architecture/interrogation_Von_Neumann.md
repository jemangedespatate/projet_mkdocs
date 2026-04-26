# Évaluation : Architecture & Assembleur

**Nom :** ......................................
**Prénom :** ...................................

site : www.peterhigginson.co.uk/AQA/

---

## PARTIE 1 : Architecture de Von Neumann

**Question 1:**

Quelle est la nouveauté majeure apportée par le modèle de Von Neumann concernant le stockage des programmes, par rapport aux tout premiers ordinateurs ?

................................................................

**Question 2:**

Un processeur (CPU) réalise des milliards de "cycles CPU" par seconde. Citez les quatre étapes principales (en anglais ou en français) de ce cycle, dans l'ordre chronologique :

1. ................................................................
2. ................................................................
3. ................................................................
4. ................................................................

**Question 3:**

Expliquez le rôle des composants suivants :

* **Unité de Contrôle (CU)** : ................................................................
* **Unité Arithmétique et Logique (ALU)** : ................................................................
* **Le Program Counter (PC)** : ................................................................

**Question 4:**

L'ordinateur vient de réaliser le calcul `10 + 5`. Quel type d'emplacement mémoire, situé au cœur même du processeur, permet de stocker ce résultat immédiat de la manière la plus rapide possible ?

................................................................

**Question 5:**

Classez les langages suivants du plus proche de la machine (1) au plus proche de l'humain (3) : Python, Langage Machine (binaire), Assembleur.

1. ........................................
2. ........................................
3. ........................................

**Question 6:**

classez les composants suivants dans les 4 categorie suivantes :

(carte mère, processeur, ram, disque dur, carte graphique, carte son, carte réseau)

* L'Unité Centrale de Traitement: ................................................................
* La Mémoire Vive : ................................................................
* Les Entrées / Sorties : ................................................................
* Les Bus : ................................................................

---

## PARTIE 2 : Lecture et Exécution de Code Assembleur

On considère le programme écrit en assembleur suivant pour le simulateur en classe :

```asm
MOV R0, #25
MOV R1, #10
LDR R2, 100
ADD R2, R2, R0
SUB R2, R2, R1
STR R2, 100
HALT
```

**Question 7:**

Expliquez précisément en une ou deux phrases ce que fait l'instruction `LDR R2, 100`.

................................................................

**Question 8:**

On suppose qu'avant le lancement du programme, la case mémoire d'adresse **100** contient la valeur **`5`**.

Tracez l'évolution du contenu des registres ou de la mémoire pour obtenir la valeur finale qui sera stockée à l'adresse 100 en fin de programme. Détaillez vos calculs.

etapes|ligne 1|ligne 2|ligne 3|ligne 4|ligne 5|ligne 6|
|:-:|-|-|-|-|-|-|
|R0|||||||
|R1|||||||
|R1|||||||
|100|||||||

**Question 9:**

Expliquez en une phrase à quoi sert l'instruction `STR R2, 100`. Quelle est la différence avec la commande `LDR` ?
................................................................

---

## PARTIE 3 : Complétion de Boucle et de Condition

Le programme assembleur suivant permet de réaliser la multiplication de **5 par 3** en effectuant des additions successives (on ajoute le nombre 3 cinq fois de suite).
Certaines instructions ou valeurs ont été effacées.

**Question 10:**

Complétez les espaces manquants (`.........`) dans le code ci-dessous pour que la boucle fonctionne correctement.

```asm
MOV R0, #5           ; Initialise le compteur à 5
MOV R1, #0           ; Initialise le résultat à 0
boucle:
......... R0, #0     ; Compare le compteur à 0
......... fin        ; Si c'est égal à 0, saute à la fin du programme
ADD R1, R1, #3       ; Ajoute 3 au résultat partiel
......... R0, R0, #1 ; Enlève 1 au compteur
B .........          ; Remonte au début de la boucle
fin: HALT
```

**Question 11:**

Expliquez à quoi sert l'instruction `B` insérée à l'avant-dernière ligne, et pourquoi elle est indispensable au fonctionnement d'une boucle.
................................................................................................................................

---

## PARTIE 4 : Création de Code

**Question 12: Comparaison en Mémoire**

Une valeur entière est stockée à l'adresse mémoire **`40`**.

Écrivez un programme en assembleur qui :

1. Charge cette valeur depuis la mémoire.
2. La compare au nombre **30**.
3. Si la valeur est strictement **supérieure** à 30, il écrit la valeur **`1`** à l'adresse mémoire **`50`**.
4. Sinon (valeur inférieure ou égale), il écrit la valeur **`0`** à l'adresse mémoire **`50`**.
5. S'arrête.

**Votre code ici :**
```asm










```

**Question 13: Opération Conditionnelle**

Deux valeurs entières sont stockées respectivement aux adresses mémoire **`60`** et **`61`**.

Écrivez un programme en assembleur qui :

1. Charge ces deux valeurs en mémoire.
2. Vérifie si elles sont égales.
3. Si elles sont **égales**, le programme les additionne et stocke le résultat à l'adresse mémoire **`62`**.
4. Si elles sont **différentes**, il écrit simplement la valeur **`0`** à l'adresse **`62`**.
5. S'arrête.

**Votre code ici :**
```asm










```

## LEXIQUE DE SURVIE (SYNTAXE)

| COMMANDE | utilisation |
| :--- | :--- |
| **MOV** | `MOV R0, #25` |
| **LDR** | `LDR R2, 100` |
| **STR** | `STR R2, 100` |
| **ADD / SUB** | `ADD R1, R1, #3` / `SUB R0, R0, #1` |
| **CMP** | `CMP R0, #0` |
| **B** | `B boucle` |
| **BGT / BEQ / BNE** | `BGT fin` |
| **HALT** | `HALT` |