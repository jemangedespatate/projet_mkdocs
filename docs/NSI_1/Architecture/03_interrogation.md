# Évaluation : Architecture & Assembleur

**Nom :** ......................................
**Prénom :** ...................................

site : www.peterhigginson.co.uk/AQA/

---

## PARTIE 1 : Architecture de Von Neumann (7 points)

**Question 1 (1 point) :**

Quelle est la nouveauté majeure apportée par le modèle de Von Neumann concernant le stockage des programmes, par rapport aux tout premiers ordinateurs ?
<br><br><br>

**Question 2 (1,5 point) :**

Un processeur (CPU) réalise des milliards de "cycles CPU" par seconde. Citez les quatre étapes principales (en anglais ou en français) de ce cycle, dans l'ordre chronologique :

1. ................................................................
2. ................................................................
3. ................................................................
4. ................................................................

**Question 3 (1,5 point) :**

Expliquez le rôle des composants suivants :

* **Unité de Contrôle (CU)** : ................................................................
* **Unité Arithmétique et Logique (ALU)** : ................................................................
* **Le Program Counter (PC)** : ................................................................

**Question 4 (1 point) :**

L'ordinateur vient de réaliser le calcul `10 + 5`. Quel type d'emplacement mémoire, situé au cœur même du processeur, permet de stocker ce résultat immédiat de la manière la plus rapide possible ?
<br><br>

**Question 5 (2 points) :**

Classez les langages suivants du plus proche de la machine (1) au plus proche de l'humain (3) : Python, Langage Machine (binaire), Assembleur.

1. ........................................
2. ........................................
3. ........................................

**Question 6 (1,5 point) :**

classez les composants suivants dans les 4 categorie suivantes :

(carte mère, processeur, ram, disque dur, carte graphique, carte son, carte réseau)

* L'Unité Centrale de Traitement
* La Mémoire Vive
* Les Entrées / Sorties
* Les Bus

---

## PARTIE 2 : Lecture et Exécution de Code Assembleur (6 points)

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

**Question 7 (1,5 point) :**

Expliquez précisément en une ou deux phrases ce que fait l'instruction `LDR R2, 100`.
<br><br>

**Question 8 (2,5 points) :**

On suppose qu'avant le lancement du programme, la case mémoire d'adresse **100** contient la valeur **`5`**.

Tracez l'évolution du contenu des registres ou de la mémoire pour obtenir la valeur finale qui sera stockée à l'adresse 100 en fin de programme. Détaillez vos calculs.
<br><br><br><br><br>

**Question 9 (2 points) :**

Expliquez en une phrase à quoi sert l'instruction `STR R2, 100`. Quelle est la différence avec la commande `LDR` ?
<br><br><br>

---

## PARTIE 3 : Complétion de Boucle et de Condition (4 points)

Le programme assembleur suivant permet de réaliser la multiplication de **5 par 3** en effectuant des additions successives (on ajoute le nombre 3 cinq fois de suite).
Certaines instructions ou valeurs ont été effacées.

**Question 10 (2 points) :**

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

**Question 11 (2 points) :**

Expliquez à quoi sert l'instruction `B` insérée à l'avant-dernière ligne, et pourquoi elle est indispensable au fonctionnement d'une boucle.
<br><br><br>

---

## PARTIE 4 : Création de Code (3 points)

**Question 12 (3 points) : Le Thermostat Intelligent**

Un capteur de température dépose sa valeur (un nombre entier) en permanence à l'adresse mémoire **`40`**.
La température d'alerte pour allumer un ventilateur est fixée à **30** degrés.

Écrivez un programme en assembleur qui :

1. Récupère la température mesurée.
2. La compare à **30**.
3. Si la température est strictement **supérieure** à 30, il écrit la valeur **`1`** à l'adresse mémoire **`50`** (ce qui allumera le ventilateur).
4. Sinon (c'est-à-dire inférieure ou égale), il écrit la valeur **`0`** à l'adresse mémoire **`50`** (ce qui éteindra le ventilateur).
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