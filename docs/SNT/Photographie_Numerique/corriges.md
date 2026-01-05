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
    *   Nouvelles coordonnées : **(255, 130, 70)**.
