# Interrogation de SNT - Géolocalisation (Sujet A)

**Nom :** .......................................... **Prénom :** .......................................... **Classe :** ............  
**Note :** ..... / 10

---

### Exercice 1 : Fonctionnement et définitions (2 points)
1. Définissez brièvement le terme **Géolocalisation**. (1 pt)
<br><br>
2. Expliquez le principe de la **trilatération** utilisé par les récepteurs GPS pour trouver leur position sur Terre. (1 pt)
<br><br><br><br>

### Exercice 2 : Calcul de distance (2 points)
Un signal radio met **0,07 seconde** pour voyager depuis un satellite jusqu'à votre smartphone. Sachant que la vitesse du signal est d'environ **300 000 km/s**, calculez la distance qui les sépare.  
*Détaillez votre calcul.*
<br><br><br><br>

### Exercice 3 : Conversion de coordonnées (2 points)
La conversion est indispensable pour passer des formats GPS aux formats lisibles sur des cartes. *Détaillez vos calculs.*
1. Convertissez la coordonnée suivante du format décimal vers le format degrés-minutes (DM) : **45,50°** (1 pt)
<br><br><br>
2. Convertissez la coordonnée suivante du format degrés-minutes (DM) vers le format décimal : **12° 15'** (1 pt)
<br><br><br>

### Exercice 4 : Trame NMEA (2 points)
Voici une trame NMEA captée par un smartphone :  
`$GPGGA,083000.000,4317.0000,N,00522.0000,E,1,05,2.0,150.0,M,,,,0000*0F`

1. À quelle heure (UTC) cette position a-t-elle été enregistrée ? (0.5 pt)
<br><br>
2. Combien de satellites ont été utilisés pour obtenir cette position ? (0.5 pt)
<br><br>
3. Quelle est l'altitude à laquelle se trouve le capteur ? (1 pt)
<br><br>

### Exercice 5 : Vie privée et enjeux (2 points)
Citez **deux** risques liés à l'utilisation constante de la géolocalisation sur les smartphones concernant la vie privée des utilisateurs.
<br><br><br><br>

---

??? success "Correction Sujet A"

    **Exercice 1 :**
    1. La géolocalisation est une technique permettant de situer de manière précise un lieu, une personne ou un objet sur la planète grâce à des coordonnées géographiques.
    2. La trilatération consiste à calculer la distance entre le récepteur et plusieurs satellites dont on connaît la position. L'intersection des cercles (ou sphères) formées par ces distances permet de déterminer la position exacte.

    **Exercice 2 :**
    - Formule : Distance = Vitesse × Temps
    - Calcul : Distance = 300 000 × 0,07
    - Résultat : 21 000 km.

    **Exercice 3 :**
    1. 45° et 0,50 × 60 = 30' => **45° 30'**
    2. 12 + (15 / 60) = 12 + 0,25 => **12,25°**

    **Exercice 4 :**
    1. À **08:30:00** (UTC).
    2. **5** satellites ont été utilisés (champ `05`).
    3. L'altitude est de **150.0 mètres** (champ `150.0,M`).

    **Exercice 5 :**
    Types de réponses attendues : Traçabilité permanente de nos déplacements, risque de collecte/revente de nos données personnelles par les applications, surveillance par des tiers.
