# 🔑 Correction des Exercices : Photographie Numérique

*Ce document est destiné à l'enseignant. Il contient les solutions détaillées des 7 exercices.*

---

## Exercice 1 : Définition et Résolution

1.  **Définition** : **800 × 600 = 480 000** pixels (ou 0,48 Mpx).
2.  **Résolution** :
    *   Résolution = **800 pixels / 10 pouces = 80 ppp** (ou dpi).
    *   **Qualité** : Non, c'est insuffisant. Pour une impression photo de qualité, on vise généralement **300 ppp**. À 80 ppp, l'image paraîtra floue ou pixelisée.

---

## Exercice 2 : Le Poids des Images

Définition totale : **1024 × 1024 = 1 048 576** pixels.

1.  **Image binaire** (1 bit/px) :
    *   **1 048 576 bits / 8 = 131 072 octets**.
    *   Soit environ **131 Ko**.
2.  **Image niveaux de gris** (8 bits = 1 octet/px) :
    *   **1 048 576 × 1 = 1 048 576 octets**.
    *   Soit environ **1 Mo**.
3.  **Image couleurs RVB** (24 bits = 3 octets/px) :
    *   **1 048 576 × 3 = 3 145 728 octets**.
    *   Soit environ **3,14 Mo**.

---

## Exercice 3 : Codage des Couleurs RVB

1.  **Noir** : `(0, 0, 0)` | **Blanc** : `(255, 255, 255)`.
2.  `(255, 0, 0)` : **Rouge** pur.
3.  `(0, 255, 255)` : **Cyan** (mélange de Vert et de Bleu).
4.  `(100, 100, 100)` : C'est une nuance de **gris** (R=V=B). Elle est plus **sombre** que `(200, 200, 200)` car les valeurs sont plus proches de 0.

---

## Exercice 4 : Métadonnées et Vie Privée

1.  **Trois informations** : Date et heure de prise de vue, modèle de l'appareil (ex: iPhone 15), et coordonnées GPS.
2.  **Information critique** : Les **coordonnées GPS** (car elles permettent de trouver l'adresse d'Alice).
3.  **Protection** : Désactiver la géolocalisation dans les réglages de l'appareil photo ou utiliser un logiciel "EXIF cleaner" pour supprimer les données avant publication.

---

## Exercice 6 : Profondeur de couleur

1.  **2 bits** : **2² = 4** couleurs possibles.
    *   Combinaisons : `00`, `01`, `10`, `11`.
2.  **RVB standard (24 bits)** : **2²⁴ = 16 777 216** couleurs différentes.

---

## Exercice 6 : Formats de fichiers et Usages

1.  **Transparence** : Il faut choisir le **PNG**. Le JPEG ne gère pas la transparence (canal Alpha).
2.  **Photo détaillée/Légèreté** : Le **JPEG** est plus adapté grâce à sa compression efficace pour les photographies.
3.  **Compression "avec perte"** : Cela signifie que l'algorithme supprime définitivement certaines données de l'image (détails fins, nuances de couleurs très proches) pour réduire la taille du fichier. On ne peut pas revenir en arrière.

---

## Exercice 7 : Retouche d'image (Calcul)

1.  **Nouvelles coordonnées** :
    *   R : **120 + 30 = 150**
    *   V : **50 + 30 = 80**
    *   B : **200 + 30 = 230**
    *   Résultat : **(150, 80, 230)**.
2.  **Cas du pixel (240, 100, 40)** :
    *   Calcul pour le Rouge : **240 + 30 = 270**.
    *   **Plafonnement** : Puisqu'un octet est limité à 255, la valeur sera **255**.
---
 
 ## Exercice 8 : Compression d'Image
 
 1.  **Poids théorique** : $2000 \times 1500 \times 3 = 9\ 000\ 000$ octets = **9 Mo**.
 2.  **Taux de compression** : 9 Mo = 9 000 Ko. $9000 / 600 =$ **15**. Le poids a été divisé par 15.
 3.  **Usage Internet** : Les fichiers compressés se téléchargent beaucoup plus vite, ce qui est crucial pour la fluidité de la navigation et pour économiser de la bande passante.
 
 ---
 
 ## Exercice 9 : Codage Hexadécimal
 
 1.  `#FF0000` : **Rouge** pur.
 2.  `#000000` : **Noir**.
 3.  `#FFFFFF` : `(255, 255, 255)` — **Blanc**.
 4.  `(0, 255, 0)` : **#00FF00**.
 
 ---
 
 ## Exercice 10 : Transformation mathématique
 
 1.  **Pixel (10, 200, 50)** :
     - R : $255 - 10 = 245$
     - V : $255 - 200 = 55$
     - B : $255 - 50 = 205$
     - Résultat : **(245, 55, 205)**.
 2.  **Négatif du Blanc** : **Noir** `(0, 0, 0)`.
 3.  **Négatif du Noir** : **Blanc** `(255, 255, 255)`.
 4.  **Double application** : L'opération est une symétrie par rapport au milieu (127.5). Mathématiquement : $255 - (255 - x) = x$. On retrouve donc la valeur de départ.
 
 ---
 
 ## Exercice 11 : Le Capteur et les Photosites
 
 1.  **24 Mégapixels** : Environ **24 millions** de photosites.
 2.  **Sensibilité du Vert** : L'œil humain est naturellement plus sensible au vert et perçoit mieux les nuances dans cette couleur (héritage de l'évolution pour distinguer les nuances de feuillage). Doubler les photosites verts permet d'obtenir une image qui semble plus nette et plus fidèle à notre vision.
 
 ---
 
 ## Exercice 12 : Analyse de cas (Les Métadonnées)
 
 1.  **Exposition** : Temps de pose **très court** (1/1000 s). Oui, c'est idéal pour figer un mouvement rapide (sport, animal en course) sans flou.
 2.  **Monument** : Les coordonnées correspondent à la **Tour Eiffel** à Paris.
 3.  **Danger** : Les coordonnées GPS révèlent le **lieu exact** où la photo a été prise. Si le vendeur prend la photo chez lui, n'importe qui peut localiser son domicile, ce qui pose un problème de sécurité et de vie privée.
