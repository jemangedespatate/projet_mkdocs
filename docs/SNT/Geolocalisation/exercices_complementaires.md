# 🚀 Exercices Complémentaires — Géolocalisation

!!! warning "À qui s'adresse cette feuille ?"
    Ces exercices sont destinés aux élèves ayant **déjà terminé** la feuille d'exercices principale. Ils nécessitent plus de rigueur dans les calculs et une compréhension plus fine des mécanismes de la géolocalisation.

---

## Exercice A : Conversion complète — Degrés, Minutes, Secondes (DMS) ↔ Décimal

!!! question "Énoncé"

    Le format **DMS** (Degrés, Minutes, Secondes) est encore utilisé en cartographie et en navigation.

    **Partie 1 — Conversion DMS → Décimal**

    Convertissez les coordonnées suivantes au format décimal (arrondi à 5 décimales) :

    | Lieu | Latitude DMS | Longitude DMS |
    |------|-------------|--------------|
    | Tour Eiffel | 48° 51' 29.6" N | 2° 17' 40.2" E |
    | Mont Blanc | 45° 49' 57" N | 6° 51' 54" E |
    | Cap Finistère (Bretagne) | 48° 22' 34" N | 4° 46' 48" W |

    **Partie 2 — Conversion Décimal → DMS**

    Convertissez maintenant ces coordonnées au format DMS (arrondi à la seconde entière) :

    1. 43.29695° N, 5.38107° E
    2. 1.35208° N, 103.81984° E

    **Questions :**

    1. Pour le Cap Finistère, comment interpréter la longitude avec la direction **W** dans le résultat décimal ?
    2. Vérifiez vos réponses avec Google Maps : entrez directement les coordonnées décimales et identifiez le lieu.

??? tip "Méthode de conversion"

    **DMS → Décimal :**

    ```
    Décimal = Degrés + (Minutes / 60) + (Secondes / 3600)
    ```

    Si la direction est **S** ou **W**, le résultat décimal est **négatif**.

    **Décimal → DMS :**

    1. La partie entière donne les **degrés**
    2. La partie décimale x 60 donne les **minutes** (partie entière)
    3. La partie décimale des minutes x 60 donne les **secondes**

    **Exemple :** 48.8584° N

    - Degrés : **48°**
    - Minutes : 0.8584 x 60 = 51.504 → **51'**
    - Secondes : 0.504 x 60 = 30.24 → **30"**
    - Résultat : **48° 51' 30" N**

---

## Exercice B : Calcul de distance avec la formule de Haversine

!!! question "Énoncé"

    En géolocalisation, calculer la distance entre deux points à la surface de la Terre n'est **pas** une simple différence de coordonnées, car la Terre est une sphère.

    La **formule de Haversine** permet ce calcul. Elle s'écrit en plusieurs étapes :

    ```
    Étape 1 — Convertir les coordonnées en radians :
        lat_rad = latitude (°) x (π / 180)
        lon_rad = longitude (°) x (π / 180)
        (π ≈ 3.14159)

    Étape 2 — Calculer les différences :
        Δlat = lat2_rad - lat1_rad
        Δlon = lon2_rad - lon1_rad

    Étape 3 — Calculer le terme intermédiaire a :
        a = sin(Δlat/2)² + cos(lat1_rad) x cos(lat2_rad) x sin(Δlon/2)²

    Étape 4 — Calculer la distance :
        d = 2 x R x arcsin(racine(a))
        avec R = 6 371 km (rayon moyen de la Terre)
    ```

    **Points à utiliser :**

    | Lieu | Latitude (°) | Longitude (°) |
    |------|-------------|--------------|
    | Paris (Tour Eiffel) | 48.8584 | 2.2945 |
    | Marseille (Vieux-Port) | 43.2965 | 5.3698 |

    **Questions :**

    1. Convertissez les latitudes et longitudes de Paris et Marseille en radians.
    2. Appliquez la formule de Haversine pour calculer la distance entre les deux villes. Vous pouvez utiliser la calculatrice scientifique de votre ordinateur.
    3. Comparez votre résultat avec la distance indiquée par Google Maps (itinéraire « à vol d'oiseau »). Quelle est l'écart ? Comment l'expliquer ?
    4. **Bonus :** Pourquoi ne peut-on pas simplement calculer `racine( (lat2 - lat1)² + (lon2 - lon1)² )` pour obtenir une distance en km ?

??? tip "Valeurs intermédiaires pour vous guider"

    ```
    lat1_rad = 48.8584 x (π / 180) ≈ 0.85298 rad
    lat2_rad = 43.2965 x (π / 180) ≈ 0.75545 rad
    lon1_rad =  2.2945 x (π / 180) ≈ 0.04004 rad
    lon2_rad =  5.3698 x (π / 180) ≈ 0.09373 rad
    ```

    La distance attendue est de l'ordre de **660 à 670 km**.

---

## Exercice C : Analyse avancée de trames NMEA — Reconstitution de trajet

!!! question "Énoncé"

    Voici une séquence de **5 trames NMEA** enregistrées toutes les 30 secondes par le GPS d'un randonneur :

    ```
    $GPGGA,080000.000,4553.920,N,00614.310,E,1,08,0.9,1204.0,M,0.0,M,,*6A
    $GPGGA,080030.000,4554.102,N,00614.285,E,1,08,0.9,1215.0,M,0.0,M,,*6B
    $GPGGA,080100.000,4554.350,N,00613.970,E,1,08,0.9,1231.0,M,0.0,M,,*6C
    $GPGGA,080130.000,4554.612,N,00613.740,E,1,07,1.1,1245.0,M,0.0,M,,*6D
    $GPGGA,080200.000,4554.880,N,00613.505,E,1,06,1.2,1258.0,M,0.0,M,,*6E
    ```

    **Questions :**

    1. Convertissez les coordonnées de **chaque trame** du format degrés-minutes au format décimal (arrondi à 4 décimales).
    2. Quelle est la durée totale du trajet enregistré ?
    3. Le randonneur monte-t-il ou descend-il ? Justifiez avec les données d'altitude.
    4. À partir de la trame 4, la qualité du signal change. Comment le voit-on dans les données ? À quoi cela peut-il être dû ?
    5. **Bonus :** En utilisant [Google My Maps](https://www.google.fr/mymaps), placez les 5 points sur une carte et décrivez le terrain traversé.

??? tip "Rappel : Structure d'une trame GPGGA"

    ```
    $GPGGA, HHMMSS.SSS, Lat, N/S, Lon, E/W, Qualité, NbSat, HDOP, Altitude, M, ...
    ```

    - **HDOP** (Horizontal Dilution Of Precision) : indicateur de précision horizontale.  
      Une valeur proche de **1** est excellente, au-delà de **2** c'est médiocre.
    - **Altitude** : exprimée en mètres au-dessus du niveau de la mer.

---

## Exercice D : Trilatération — Raisonnement géométrique

!!! question "Énoncé"

    On se place dans un repère 2D simplifié (vue du dessus). Trois antennes relais de téléphonie mobile sont positionnées comme suit :

    | Antenne | Position (x, y) en km |
    |---------|----------------------|
    | A       | (0, 0)               |
    | B       | (10, 0)              |
    | C       | (5, 8)               |

    Le téléphone de Mario reçoit les signaux des trois antennes. On mesure les **temps de trajet** suivants (les signaux se propagent à **300 000 km/s**) :

    | Antenne | Temps de trajet |
    |---------|----------------|
    | A       | 0.0000200 s    |
    | B       | 0.0000167 s    |
    | C       | 0.0000233 s    |

    **Questions :**

    1. Calculez la distance entre Mario et chacune des trois antennes avec la formule :  
       `distance = vitesse x temps`

    2. Pour chaque antenne, écrivez l'équation du **cercle** de centre l'antenne et de rayon la distance calculée.  
       L'équation d'un cercle de centre (a, b) et de rayon r est :  
       `(x - a)² + (y - b)² = r²`

    3. En soustrayant l'équation du cercle A à celle du cercle B, obtenez une équation linéaire en x et y.

    4. En soustrayant l'équation du cercle A à celle du cercle C, obtenez une deuxième équation linéaire.

    5. Résolvez le système de deux équations pour trouver la position (x, y) de Mario.

    6. Vérifiez votre résultat en recalculant les distances depuis le point trouvé vers chaque antenne.

??? tip "Coup de pouce — Étape 3"

    En soustrayant les équations des cercles A et B :

    ```
    Cercle A : x² + y² = rA²
    Cercle B : (x - 10)² + y² = rB²

    En développant (x - 10)² = x² - 20x + 100, puis en soustrayant :
    x² - (x² - 20x + 100) = rA² - rB²
    20x - 100 = rA² - rB²
    ```

    On obtient ainsi une équation linéaire en x uniquement, facile à résoudre !

---

## Exercice E : Vie privée numérique — Étude de cas approfondie

!!! question "Énoncé"

    **Contexte :** En 2018, un journaliste du New York Times a acheté légalement un fichier contenant les données de localisation de millions de smartphones américains sur plusieurs mois. Ces données avaient été collectées par des applications et revendues à des courtiers en données.

    En analysant les données d'un seul individu, le journaliste a pu :

    - Reconstituer ses trajets quotidiens domicile / travail
    - Identifier ses rendez-vous médicaux et ses lieux de culte
    - Deviner ses opinions politiques à partir des meetings qu'il avait fréquentés
    - Retrouver son identité complète, sans jamais avoir eu son nom dans le fichier

    **Questions :**

    1. Le fichier de données ne contenait **aucun nom**. Pourtant, l'identification a été possible. Expliquez comment.
    2. Quelles données, autres que la position, peuvent être **déduites** d'un historique de localisation ?
    3. En France, quel texte de loi encadre la collecte et l'utilisation des données personnelles, y compris les données de localisation ?
    4. Lorsqu'une application mobile vous demande l'accès à votre localisation, elle peut proposer trois niveaux d'autorisation. Lesquels ? Quel niveau recommandez-vous d'utiliser par défaut ?
    5. **Question de synthèse :** Rédigez un paragraphe d'environ 8 lignes expliquant pourquoi la géolocalisation, bien qu'utile, constitue un enjeu majeur pour la vie privée, et comment un citoyen numérique responsable peut s'en protéger.

??? tip "Pistes de réflexion"

    - Le concept d'**anonymisation** et ses limites : les données de position permettent souvent une **ré-identification** par croisement avec d'autres informations.
    - Le **RGPD** (Règlement Général sur la Protection des Données) est en vigueur dans l'Union Européenne depuis 2018.
    - Pensez aux notions de **consentement**, **minimisation des données**, et **droit à l'effacement**.

---

## Exercice F : Défi — Encodage et vérification d'une trame NMEA

!!! question "Énoncé"

    La dernière partie d'une trame NMEA est une **somme de contrôle** (checksum), calculée par l'opération **XOR** sur tous les octets compris entre `$` et `*` (exclus).

    **Exemple simple :**

    Trame : `$GPGGA,123456.000*2A`

    - On calcule le XOR des codes ASCII de : `G`, `P`, `G`, `G`, `A`, `,`, `1`, `2`, `3`, `4`, `5`, `6`, `.`, `0`, `0`, `0`
    - Le résultat `2A` est affiché en hexadécimal après `*`

    **Travail à faire :**

    Voici une trame NMEA avec une **somme de contrôle incorrecte** :

    ```
    $GPRMC,120000.000,A,4836.5375,N,00220.9133,E,0.00,0.00,050326,,,A*5F
    ```

    1. Identifiez la chaîne sur laquelle calculer le XOR (entre `$` et `*`).
    2. En utilisant le tableau ASCII disponible sur [asciitable.com](https://www.asciitable.com), retrouvez le code décimal de chaque caractère.
    3. Calculez le XOR successif de tous ces codes. *(Rappel : XOR bit à bit, opération logique « ou exclusif »)*
    4. Convertissez le résultat en hexadécimal.
    5. La somme de contrôle `5F` inscrite dans la trame est-elle correcte ? Quelle est la valeur attendue ?

??? tip "Rappel sur le XOR"

    Le XOR (ou exclusif) bit à bit fonctionne ainsi :

    | A | B | A XOR B |
    |---|---|---------|
    | 0 | 0 |    0    |
    | 0 | 1 |    1    |
    | 1 | 0 |    1    |
    | 1 | 1 |    0    |

    **Exemple :** `G` (71 = 0100 0111) XOR `P` (80 = 0101 0000) = 0001 0111 = 23

    Pour vérifier votre calcul final, vous pouvez utiliser un [calculateur XOR en ligne](https://www.scadacore.com/tools/programming-calculators/online-checksum-calculator/).

