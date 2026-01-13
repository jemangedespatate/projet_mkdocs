# ✏️ Exercices : Photographie Numérique

Ces exercices sont à réaliser sur feuille ou directement sur ce document numérique. Ils visent à vérifier votre compréhension du codage des images.

## Exercice 1 : Définition et Résolution

On considère une image numérique de **800 pixels de large** et **600 pixels de haut**.

1.  **Calculez la définition** de cette image (nombre total de pixels).
2.  On souhaite imprimer cette image sur une photo de **10 pouces** de large (environ 25 cm).
    *   **Calculez la résolution** de l'impression en **ppp** (points par pouce).
    *   La qualité sera-t-elle suffisante pour une impression photo standard (généralement 300 ppp) ?

??? tip "Indications pour l'Exercice 1"
    1.  Pour la **définition** : multipliez la largeur par la hauteur.
    2.  Pour la **résolution** :
        *   Divisez le nombre de pixels en largeur par la largeur en pouces.
        *   Comparez le résultat obtenu avec le standard de 300 ppp pour l'impression photo.

---

## Exercice 2 : Décoder une image binaire

On a reçu une suite de bits représentant une petite image binaire de **5x5 pixels**. Les bits sont envoyés ligne par ligne :

`01110 10001 10101 10001 01110`

1.  **Dessinez la grille** de 5x5 cases correspondante.
2.  **Coloriez en noir** les cases valant `1` et laissez en blanc les cases valant `0`.
3.  **Quelle forme** apparaît sur votre dessin ?

??? tip "Indications pour l'Exercice 2"
    1.  Préparez une grille de 5 lignes et 5 colonnes.
    2.  Prenez le premier groupe de 5 bits (`01110`) et remplissez la première ligne (0=Blanc, 1=Noir).
    3.  Observez le dessin global (c'est une forme géométrique simple).

---

## Exercice 3 : Le Poids des Images

On souhaite stocker une image de définition **1024 × 1024** pixels.
Calculez le poids de cette image (en octets, puis en Mo) dans les cas suivants :

1.  **Image binaire** (Noir et Blanc pur, 1 bit par pixel).
2.  **Image en niveaux de gris** (256 nuances, 8 bits par pixel).
3.  **Image en couleurs RVB** (16 millions de couleurs, 24 bits par pixel).

*Rappel : **1 octet = 8 bits**. **1 Mo ≈ 1 000 000 octets** (ou 1024 × 1024 selon la convention, ici on utilisera 10⁶ pour simplifier).*

??? tip "Indications pour l'Exercice 3"
    **Démarche générale :**
    
    1.  Commencez par calculer le **nombre total de pixels** de l'image.
    
    2.  Pour chaque type d'image :
        *   **Binaire** : Chaque pixel = 1 bit. Calculez le total en bits, puis divisez par 8 pour obtenir les octets.
        *   **Niveaux de gris** : Chaque pixel = 1 octet. Multipliez le nombre de pixels par 1.
        *   **Couleurs RVB** : Chaque pixel = 3 octets. Multipliez le nombre de pixels par 3.
    
    3.  Pour convertir en Mo, divisez le résultat en octets par 1 000 000.

---

## Exercice 4 : Codage des Couleurs RVB

Dans le système RVB (Rouge, Vert, Bleu), chaque couleur est codée par un triplet de valeurs comprises entre 0 et 255.

1.  Donnez le code RVB du **Noir** et du **Blanc**.
2.  Quelle couleur obtient-on avec le code `(255, 0, 0)` ?
3.  Quelle couleur obtient-on avec le code `(0, 255, 255)` ? (Mélange de Vert et Bleu)
4.  On a une couleur `(100, 100, 100)`. Est-elle colorée ou grise ? Est-elle plus claire ou plus sombre que `(200, 200, 200)` ?

??? tip "Indications pour l'Exercice 4"
    **Rappels utiles :**
    
    *   Le **Noir** correspond à l'absence totale de lumière (toutes les composantes à 0).
    *   Le **Blanc** correspond à la lumière maximale (toutes les composantes à 255).
    *   Une couleur **pure** (Rouge, Vert ou Bleu) a une seule composante à 255 et les autres à 0.

---

## Exercice 5 : Métadonnées et Vie Privée

Alice prend une photo de son chat avec son smartphone dernier cri et la poste immédiatement sur un forum public sans modification.
Un inconnu télécharge la photo et regarde les métadonnées EXIF.

1.  Citez **trois informations** que l'inconnu pourrait trouver dans le fichier image.
2.  Quelle information est la plus critique pour la sécurité d'Alice ?
3.  Comment Alice aurait-elle dû procéder pour se protéger ?

??? tip "Indications pour l'Exercice 5"
    **Réfléchissez aux métadonnées EXIF :**
    
    1.  Les métadonnées peuvent contenir :
        *   Des informations **temporelles** (quand la photo a été prise)
        *   Des informations **techniques** (quel appareil, quels réglages)
        *   Des informations **géographiques** (où la photo a été prise)
    
    2.  Quelle information pourrait révéler l'**adresse personnelle** d'Alice ?
    
    3.  Pensez aux **paramètres de l'appareil photo** et aux **outils de traitement d'image** qui peuvent supprimer ces données.
---

## Exercice 6 : Profondeur de couleur

La profondeur de couleur correspond au nombre de bits utilisés pour coder la couleur d'un pixel. Plus ce nombre est grand, plus on peut afficher de couleurs différentes.

1.  Si un pixel est codé sur **2 bits**, combien de couleurs différentes peut-il afficher ? Listez les combinaisons de bits possibles.
2.  Dans le codage **RVB standard**, on utilise **8 bits par canal** (soit 24 bits au total). Calculez le nombre total de couleurs possibles (utilisez la puissance de 2).

??? tip "Indications pour l'Exercice 6"
    *   Pour **n bits**, le nombre de valeurs possibles est **2ⁿ**.
    *   Pour 2 bits, les combinaisons sont 00, 01, 10, 11.
    *   Pour le RVB standard, calculez **2²⁴**.

---

## Exercice 7 : Retouche d'image (Calcul)

On considère un pixel de couleur **RVB (120, 50, 200)**. On applique une retouche pour augmenter la luminosité en ajoutant **30** à chaque composante.

1.  Donnez les nouvelles coordonnées RVB du pixel après retouche.
2.  Si un autre pixel a pour valeur **(240, 100, 40)** et qu'on lui ajoute aussi 30 à chaque canal, quelle sera sa nouvelle valeur pour le canal **Rouge** ? (Rappel : la valeur d'un octet est limitée).

??? tip "Indications pour l'Exercice 7"
    1.  Additionnez simplement 30 à chaque nombre : (120+30, 50+30, 200+30).
    2.  **Attention :** Une composante ne peut jamais dépasser **255**. Si le calcul donne plus (ex: 240 + 30 = 270), le résultat est "plafonné" à 255.
