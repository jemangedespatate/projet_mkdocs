# 📝 Travaux Dirigés : Photographie Numérique

Ces exercices sont à réaliser sur feuille ou directement sur ce document numérique. Ils visent à vérifier votre compréhension du codage des images.

## Exercice 1 : Définition et Résolution

On considère une image numérique de **800 pixels de large** et **600 pixels de haut**.

1.  **Calculez la définition** de cette image (nombre total de pixels).
2.  On souhaite imprimer cette image sur une photo de **10 pouces** de large (environ 25 cm).
    *   **Calculez la résolution** de l'impression en **ppp** (points par pouce).
    *   La qualité sera-t-elle suffisante pour une impression photo standard (généralement 300 ppp) ?

??? success "Correction Exercice 1"
    1.  **Définition** : $800 \times 600 = 480\,000$ pixels (ou 0,48 Mpx).
    2.  **Résolution** :
        *   La largeur est de 800 pixels pour 10 pouces.
        *   Résolution = $800 / 10 = 80$ ppp (dpi).
        *   **Conclusion** : 80 ppp est très inférieur à 300 ppp. L'image paraîtra "pixelisée" ou floue à l'impression.

---

## Exercice 2 : Le Poids des Images

On souhaite stocker une image de définition $1024 \times 1024$ pixels.
Calculez le poids de cette image (en octets, puis en Mo) dans les cas suivants :

1.  **Image binaire** (Noir et Blanc pur, 1 bit par pixel).
2.  **Image en niveaux de gris** (256 nuances, 8 bits par pixel).
3.  **Image en couleurs RVB** (16 millions de couleurs, 24 bits par pixel).

*Rappel : $1 \text{ octet} = 8 \text{ bits}$. $1 \text{ Mo} \approx 1\,000\,000 \text{ octets}$ (ou $1024 \times 1024$ selon la convention, ici on utilisera $10^6$ pour simplifier).*

??? success "Correction Exercice 2"
    Le nombre total de pixels est $1024 \times 1024 = 1\,048\,576$ pixels.
    
    1.  **Binaire (1 bit/pixel)** :
        *   Poids en bits : $1\,048\,576$ bits.
        *   Poids en octets : $1\,048\,576 / 8 = 131\,072$ octets.
        *   Poids en Ko : $\approx 131$ Ko.
    
    2.  **Niveaux de gris (1 octet/pixel)** :
        *   Poids en octets : $1\,048\,576 \times 1 = 1\,048\,576$ octets.
        *   Poids en Mo : $\approx 1$ Mo.
    
    3.  **Couleurs RVB (3 octets/pixel)** :
        *   Poids en octets : $1\,048\,576 \times 3 = 3\,145\,728$ octets.
        *   Poids en Mo : $\approx 3,14$ Mo.

---

## Exercice 3 : Codage des Couleurs RVB

Dans le système RVB (Rouge, Vert, Bleu), chaque couleur est codée par un triplet de valeurs comprises entre 0 et 255.

1.  Donnez le code RVB du **Noir** et du **Blanc**.
2.  Quelle couleur obtient-on avec le code `(255, 0, 0)` ?
3.  Quelle couleur obtient-on avec le code `(0, 255, 255)` ? (Mélange de Vert et Bleu)
4.  On a une couleur `(100, 100, 100)`. Est-elle colorée ou grise ? Est-elle plus claire ou plus sombre que `(200, 200, 200)` ?

??? success "Correction Exercice 3"
    1.  **Noir** : `(0, 0, 0)` | **Blanc** : `(255, 255, 255)`.
    2.  `(255, 0, 0)` correspond au **Rouge** pur.
    3.  `(0, 255, 255)` correspond au **Cyan**.
    4.  C'est un **Gris** (car R=V=B). `(100, 100, 100)` est plus **sombre** que `(200, 200, 200)` (qui se rapproche du blanc).

---

## Exercice 4 : Métadonnées et Vie Privée

Alice prend une photo de son chat avec son smartphone dernier cri et la poste immédiatement sur un forum public sans modification.
Un inconnu télécharge la photo et regarde les métadonnées EXIF.

1.  Citez **trois informations** que l'inconnu pourrait trouver dans le fichier image.
2.  Quelle information est la plus critique pour la sécurité d'Alice ?
3.  Comment Alice aurait-elle dû procéder pour se protéger ?

??? success "Correction Exercice 4"
    1.  Date/Heure, Modèle du smartphone, Réglages (ISO/Flash), **Coordonnées GPS**.
    2.  Les **Coordonnées GPS** (Latitude/Longitude) sont critiques car elles permettent de localiser le domicile d'Alice précisèment.
    3.  Elle aurait dû **désactiver la géolocalisation** dans l'appareil photo avant la prise de vue, ou utiliser un logiciel pour **supprimer les métadonnées** avant de publier la photo.
