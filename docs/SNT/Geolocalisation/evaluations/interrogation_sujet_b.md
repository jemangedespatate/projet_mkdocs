# Interrogation de SNT - Géolocalisation (Sujet B)

**Nom :** .......................................... **Prénom :** .......................................... **Classe :** ............  
**Note :** ..... / 10

---

### Exercice 1 : Fonctionnement et définitions (2 points)
1. Définissez ce que sont la **latitude** et la **longitude**. (1 pt)
<br><br><br>
2. Lors d'un positionnement par satellite en 3D, pourquoi un **4ème satellite** est-il indispensable pour calculer correctement sa position (alors que 3 suffiraient pour la trilatération) ? (1 pt)
<br><br><br><br>

### Exercice 2 : Calcul de distance (2 points)
Un signal émis par un satellite GPS met **0,09 seconde** pour atteindre un récepteur au sol. Sachant que la vitesse de ce signal est de **300 000 km/s**, calculez la distance entre le satellite et le récepteur.  
*Détaillez votre calcul.*
<br><br><br><br>

### Exercice 3 : Conversion de coordonnées (2 points)
Il est souvent nécessaire de convertir les coordonnées pour les exploiter dans différents logiciels. *Détaillez vos calculs.*
1. Convertissez la coordonnée suivante du format decimo-degrés (décimal) vers le format degrés-minutes (DM) : **48,25°** (1 pt)
<br><br><br>
2. Convertissez la coordonnée suivante du format degrés-minutes (DM) vers le format décimal : **10° 45'** (1 pt)
<br><br><br>

### Exercice 4 : Trame NMEA (2 points)
Voici une trame NMEA transmise par un objet connecté :  
`$GPGGA,142530.500,4851.5000,N,00217.5000,E,1,06,1.5,50.5,M,,,,0000*1A`

1. Quelle est l'heure (UTC) de ce relevé de position ? (0.5 pt)
<br><br>
2. Combien de satellites ont été nécessaires pour ce calcul de la position ? (0.5 pt)
<br><br>
3. À quelle altitude se situe le capteur GPS au moment de la mesure ? (1 pt)
<br><br>

### Exercice 5 : Vie privée et enjeux (2 points)
Donnez **deux** actions simples à réaliser pour limiter les risques liés à la géolocalisation et protéger sa vie privée sur son smartphone.
<br><br><br><br>

---

??? success "Correction Sujet B"

    **Exercice 1 :**
    1. La latitude permet de déterminer la position Nord/Sud, et la longitude détermine la position Est/Ouest sur la planète.
    2. Le 4ème satellite sert à synchroniser très précisément l'horloge interne du récepteur avec le temps exact des satellites, sans quoi le calcul de distance serait erroné.

    **Exercice 2 :**
    - Formule : Distance = Vitesse × Temps
    - Calcul : Distance = 300 000 × 0,09
    - Résultat : 27 000 km.

    **Exercice 3 :**
    1. 48° et 0,25 × 60 = 15' => **48° 15'**
    2. 10 + (45 / 60) = 10 + 0,75 => **10,75°**

    **Exercice 4 :**
    1. À **14:25:30** (UTC).
    2. **6** satellites ont été utilisés (champ `06`).
    3. L'altitude est de **50.5 mètres** (champ `50.5,M`).

    **Exercice 5 :**
    Types de réponses attendues : Désactiver la localisation de son appareil quand on ne s'en sert pas, vérifier/révoquer les autorisations de localisation pour les applications non critiques, désactiver la géolocalisation lors de la prise de photos.
