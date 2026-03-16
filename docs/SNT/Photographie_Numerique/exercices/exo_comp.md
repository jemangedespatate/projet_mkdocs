# 📝 Exercices Complémentaires : Photographie Numérique

Ces exercices sont à réaliser sur feuille. Ils prolongent les notions abordées dans la première série d'exercices et le TP.

---

## Exercice 8 : Compression d'Image
**Objectif :** Comprendre l'intérêt de la compression.

On a une image de **2000 x 1500 pixels** en couleurs RVB (24 bits).

1. Calculez le poids théorique de cette image en **Mo** sans compression.
2. Après l'avoir enregistrée au format **JPEG**, le fichier ne pèse plus que **600 Ko**.
   - Par combien le poids de l'image a-t-il été divisé ? (C'est le *taux de compression*).
3. À votre avis, pourquoi le format JPEG est-il plus utilisé que le format BMP (non compressé) sur Internet ?

??? tip "Indications pour l'Exercice 8"
    1. Calculez le nombre de pixels (2000 x 1500), puis multipliez par 3 octets (car 24 bits = 3 octets). Divisez par 1 000 000 pour les Mo.
    2. Convertissez les Mo de la question 1 en Ko (x 1000) et divisez par 600.
    3. Pensez au temps de chargement des pages web et au stockage sur les serveurs.

---

## Exercice 9 : Codage Hexadécimal
**Objectif :** Faire le lien entre les couleurs RVB et le codage Web (Hexadécimal).

Sur le Web, les couleurs sont souvent notées `#RRGGBB` où chaque couleur est écrite en hexadécimal (de `00` à `FF`).
*Rappel : `FF` en hexadécimal vaut `255` en décimal.*

1. À quelle couleur correspond le code `#FF0000` ?
2. À quelle couleur correspond le code `#000000` ?
3. On a le code `#FFFFFF`. À quel triplet RVB cela correspond-il ? Quelle est cette couleur ?
4. Convertissez la couleur RVB `(0, 255, 0)` en code hexadécimal.

??? tip "Indications pour l'Exercice 9"
    * Chaque paire de caractères correspond à un canal : `RR` (Rouge), `GG` (Vert), `BB` (Bleu).
    * `00` = absence (0) ; `FF` = maximum (255).
    * Pour la question 4, le vert est au maximum, les autres à 0.

---

## Exercice 10 : Transformation mathématique
**Objectif :** Calculer le résultat d'un filtre "Négatif".

Pour obtenir le négatif d'une image, on applique la formule : `valeur_neuve = 255 - valeur_ancienne`.

1. Calculez les nouvelles composantes RVB pour un pixel valant `(10, 200, 50)`.
2. Quel est le négatif d'un pixel **Blanc** ?
3. Quel est le négatif d'un pixel **Noir** ?
4. Expliquez pourquoi, si on applique deux fois de suite l'effet "Négatif", on retrouve l'image d'origine.

??? tip "Indications pour l'Exercice 10"
    1. Faites `255 - 10`, puis `255 - 200`, puis `255 - 50`.
    2. Le Blanc est `(255, 255, 255)`.
    3. Le Noir est `(0, 0, 0)`.
    4. Que vaut `255 - (255 - x)` ?

---

## Exercice 11 : Le Capteur et les Photosites
**Objectif :** Comprendre comment l'appareil "capture" la lumière.

Un capteur photographique est composé de millions de petites cellules photoélectriques appelées **photosites**.

1. Si un appareil photo est vendu pour **24 Mégapixels**, combien de photosites possède-t-il environ ?
2. Chaque photosite ne mesure que l'intensité lumineuse. Pour obtenir de la couleur, on place devant chaque photosite un petit filtre coloré (souvent une *Matrice de Bayer*).
   Sur un carré de 4 photosites, on trouve généralement : **1 filtre Rouge, 1 filtre Bleu et 2 filtres Verts**.
   - Pourquoi, selon vous, y a-t-il deux fois plus de filtres verts que de rouges ou de bleus ? (Indice : regardez la sensibilité de l'œil humain).

??? tip "Indications pour l'Exercice 11"
    1. "Méga" signifie "Million".
    2. L'évolution a rendu l'œil humain beaucoup plus sensible aux nuances d'une certaine couleur pour mieux distinguer les prédateurs ou la nourriture dans la nature... laquelle ?

---

## Exercice 12 : Analyse de cas (Les Métadonnées)
**Objectif :** Savoir lire et interpréter des informations techniques.

Voici un extrait de métadonnées EXIF d'une photo :

- **Appareil :** iPhone 13
- **Date :** 12/07/2025  14:32:05
- **Exposition :** 1/1000 s
- **ISO :** 50
- **GPS :** 48.8584° N, 2.2945° E

**Questions :**

1. La photo a-t-elle été prise avec un temps de pose long ou court ? Est-ce adapté pour un sujet en mouvement rapide ?
2. En utilisant un outil de recherche ou vos connaissances, trouvez quel monument célèbre se trouve aux coordonnées GPS indiquées.
3. Si cette photo est celle d'un objet en vente sur un site de petites annonces, quel danger cela représente-t-il pour le vendeur ?

??? tip "Indications pour l'Exercice 12"
    1. 1/1000 de seconde, c'est très rapide. Cela permet de "figer" le mouvement.
    2. Tapez "48.8584 N, 2.2945 E" dans un moteur de recherche ou une carte. C'est à Paris.
    3. Si la photo est prise *chez le vendeur*, que révèle la position GPS ?

---

## Exercice 13 : Capacité de stockage
**Objectif :** Calculer le nombre d'images que l'on peut stocker sur un support.

On dispose d'une carte mémoire de **4 Go** (Gigaoctets).
On souhaite y enregistrer des photos non compressées (format BMP par exemple) de définition **2000 x 2000 pixels** en **couleurs RVB** (24 bits par pixel).

1.  Calculez le poids d'une seule image en **Mo**.
2.  Combien de photos peut-on stocker sur la carte mémoire ?
3.  Si on utilise le format JPEG qui divise le poids par 10, combien de photos peut-on stocker ?

??? tip "Indications pour l'Exercice 13"
    1.  Nombre de pixels = 2000 x 2000. Poids = Pixels x 3 octets. Convertissez en Mo (/ 1 000 000).
    2.  Convertissez 4 Go en Mo (4000 Mo) et divisez par le poids d'une image.
    3.  Multipliez simplement le résultat précédent par 10.

---

## Exercice 14 : Conversion en Niveaux de Gris
**Objectif :** Comprendre comment passer de la couleur au noir et blanc.

Pour transformer un pixel couleur RVB en un pixel "gris", une méthode simple consiste à faire la moyenne des trois composantes.
Formule : `Gris = (Rouge + Vert + Bleu) / 3`

On a le pixel **P1 (100, 50, 210)**.

1.  Calculez la valeur de gris correspondante (arrondissez à l'entier).
2.  Quelle sera la couleur finale du pixel P1 après conversion ? (Donnez le triplet RVB).
3.  Le pixel **P2 (0, 255, 0)** correspond à du vert pur. Quelle sera sa valeur de gris ? Est-ce un gris clair ou foncé ?

??? tip "Indications pour l'Exercice 14"
    1.  Additionnez 100 + 50 + 210 puis divisez par 3.
    2.  Un pixel gris a ses trois composantes égales : (Gris, Gris, Gris).
    3.  255 / 3 = 85. Comparez 85 à 128 (gris moyen) pour savoir si c'est clair ou foncé.

---

## Exercice 15 : Le "Seuillage" (Image Binaire)
**Objectif :** Transformer une image en niveaux de gris vers une image strictement Noir et Blanc (0 ou 1).

Le **seuillage** est une technique pour ne garder que deux couleurs : Noir ou Blanc.
On choisit un **seuil**, par exemple **128**.
*   Si la valeur du pixel est **inférieure** au seuil (< 128), il devient **Noir (0)**.
*   Si la valeur est **supérieure ou égale** au seuil (>= 128), il devient **Blanc (255)**.

Appliquez ce seuil de 128 aux pixels suivants (valeurs de gris) :
1.  Pixel A : **85**
2.  Pixel B : **120**
3.  Pixel C : **200**
4.  Pixel D : **128**

??? tip "Indications pour l'Exercice 15"
    *   Comparez chaque valeur à 128.
    *   C'est une logique "Tout ou Rien".
    *   Le pixel D vaut exactement 128, donc il devient Blanc selon la règle énoncée.
