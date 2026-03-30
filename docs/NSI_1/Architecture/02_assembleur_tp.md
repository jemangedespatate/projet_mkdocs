# TP NSI : ARCHITECTURE ET ASSEMBLEUR
## NOM : ................................ 
## PRÉNOM : ................................ 
## CLASSE : ............

**Lien du simulateur** : www.peterhigginson.co.uk/AQA/

---

### 1. PRISE EN MAIN DU SIMULATEUR (10 MIN)
Identifiez les zones suivantes sur votre écran :
- **L'ÉDITEUR (À GAUCHE)** : Zone verte où l'on écrit ses ordres.
- **LES REGISTRES (AU CENTRE)** : Les cases de travail rapides du CPU (R0, R1, ...).
- **LA MÉMOIRE RAM (À DROITE)** : La grille d'adresses (de 000 à 199).
- **BOUTON ASSEMBLE (EN BAS)** : Pour envoyer votre code au processeur.

---

### ÉTAPE 1 : LES CALCULS DE BASE (MOV, ADD, SUB)

**EXERCICE 1 - COMPRÉHENSION : VOTRE PREMIER PROGRAMME**
Recopiez le code suivant dans l'éditeur, puis cliquez sur **ASSEMBLE**.
```asm
MOV R0, #42        ; Met le nombre 42 dans R0
ADD R1, R0, #8     ; R1 = R0 + 8
SUB R2, R1, #10    ; R2 = R1 - 10
HALT
```
1. Réglez la vitesse sur **Slow** et exécutez le programme avec **STEP**.
   > **Question** : Quelle est la valeur finale contenue dans le registre **R2** ? ..............................

**EXERCICE 2 - CRÉATION : VOTRE TOUR !**
Écrivez un programme qui réalise le calcul suivant : `(20 + 30) - 5`. Stockez le résultat final dans le registre **R5**.
> **Votre code :**
```asm





```

---

### ÉTAPE 2 : COMMUNIQUER AVEC LA MÉMOIRE (LDR, STR)

**EXERCICE 3 - COMPLÉTION : TRANSFERTS RAM <-> CPU**
*(Commandes : **LDR** -> charger depuis RAM, **STR** -> enregistrer en RAM)*
Complétez les espaces vides pour que le programme :
1. Range **100** à l'adresse mémoire **50**.
2. Récupère ce nombre dans R0, lui retire 20, et range le résultat à l'adresse **60**.

```asm
MOV R0, #100
.......... R0, 50      ; J'enregistre 100 à l'adresse 50
.......... R1, 50      ; Je récupère le contenu de l'adresse 50 dans R1
SUB R1, R1, #20        ; Je soustrais 20
.......... R1, 60      ; J'enregistre le résultat final à l'adresse 60
HALT
```

**EXERCICE 4 - CRÉATION : CALCUL DE TAXE**
Un prix HT est stocké à l'adresse **70**. La taxe (20) est stockée à l'adresse **71**. 
Écrivez le code qui calcule le prix TTC et le sauvegarde à l'adresse **72**.
> **Votre code :**
```asm





```

---

### ÉTAPE 3 : LES DÉCISIONS DU CPU (CMP, BGT, BEQ)

**EXERCICE 5 - COMPRÉHENSION : LE BRANCHEMENT**
*(Commandes : **CMP** -> comparer, **BGT** -> sauter si plus grand)*
Analysez ce code et exécutez-le.
```asm
MOV R0, #15
CMP R0, #10    ; Comparaison R0 / 10
BGT alerte     ; Si R0 > 10, sauter à la ligne "alerte"
MOV R1, #0     ; Sinon, R1 = 0
B fin
alerte:
MOV R1, #1     ; Bloc d'alerte : R1 = 1
fin: HALT
```
> **Question** : Si on change la première ligne par `MOV R0, #5`, quel sera le contenu de **R1** ? .............
> **Question** : À quoi sert l'instruction `B fin` placée avant le label `alerte:` ? 
> ....................................................................................................................................................

**EXERCICE 6 - CRÉATION : LE GARDIEN**
Un score est stocké à l'adresse **80**. 
Si le score **est égal à 20**, écrivez `1` à l'adresse **90**, sinon écrivez `0`.
*(Aide : Utilisez `BEQ` pour "Si égal")*
> **Votre code :**
```asm





```

---

### ÉTAPE 4 : LA PUISSANCE DES BOUCLES (BNE, B)

**EXERCICE 7 - COMPLÉTION : LE COMPTE À REBOURS**
*(Commandes : **BNE** -> sauter si différent de zéro)*
Complétez la boucle pour qu'elle décompte de 5 à 0 dans R0.
```asm
MOV R0, #5
boucle:
SUB R0, R0, #1   ; Je retire 1 à R0
.......... R0, #0     ; Je compare R0 à 0
.......... boucle     ; SI DIFFÉRENT (pas encore 0) : Je remonte à "boucle:"
HALT
```

**EXERCICE 8 - CRÉATION : LA MULTIPLICATION**
Le processeur ne sait pas multiplier. Réalisez **3 x 4** à l'aide d'additions répétées (3 + 3 + 3 + 3). Rangez le résultat final à l'adresse **100**.
*(Indice : Utilisez un compteur qui descend de 4 à 0)*
> **Votre code :**
```asm





```

---

### ÉTAPE 5 : DÉFIS AVANCÉS ET INTERACTION (IN, OUT)

**EXERCICE 9 - COMPRÉHENSION : LE COFFRE-FORT**
*(Commandes : **IN** -> saisir au clavier, **OUT** -> afficher)*
Analysez ce programme de verrouillage :
```asm
MOV R0, #1234  ; Le mot de passe
debut:
IN R1, 4       ; Demande le code (Le clavier est à l'adresse 4)
CMP R1, R0     ; Compare l'entrée au mot de passe
BNE debut      ; Si différent : on recommence !
OUT R0, 4      ; Si correct : on affiche le code
HALT
```
> **Question** : Comment appelle-t-on le fait de sauter vers une ligne déjà lue (ici `debut:`) ?
> ....................................................................

**EXERCICE 10 - CHALLENGE : LE PLUS GRAND**
Deux nombres sont aux adresses **40** et **41**. Comparez-les et rangez le plus grand à l'adresse **42**.

**EXERCICE 11 - CHALLENGE EXPERT : LA FACTORIELLE**
Calculez la **Factorielle** de 5 (5 * 4 * 3 * 2 * 1) et sauvegardez le résultat à l'adresse **200**.

---

### LEXIQUE DE SURVIE (SYNTAXE)

| COMMANDE | RÔLE |
| :--- | :--- |
| **MOV** Rd, #10 | Met le nombre 10 dans Rd. |
| **LDR** Rd, 100 | Charge la valeur de l'adresse 100 dans Rd. |
| **STR** Rd, 100 | Enregistre Rd à l'adresse 100. |
| **ADD / SUB** | Additionner ou Soustraire. |
| **CMP** Rd, #5 | Compare Rd au chiffre 5. |
| **B** label | Saute directement à un endroit (ex: `loop:`). |
| **BGT / BEQ / BNE** | Saute si **Plus Grand** / **Égal** / **Différent**. |
| **IN / OUT** | Entrée clavier / Sortie écran. |
| **HALT** | Fin du programme. |
