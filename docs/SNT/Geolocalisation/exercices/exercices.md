# ✏️ Exercices - Géolocalisation

## Exercice 1 : Le Stade de France

!!! question "Énoncé"

    Recherchez les coordonnées GPS exactes du **Stade de France** à Saint-Denis.
    
    **Questions :**
    
    1. Quelle est la latitude du Stade de France ?
    2. Quelle est la longitude du Stade de France ?
    3. Est-il situé dans l'hémisphère Nord ou Sud ?
    4. Est-il situé à l'Est ou à l'Ouest du méridien de Greenwich ?

??? tip "Indice"

    *   Ouvrez [Google Maps](https://www.google.fr/maps)
    *   Recherchez "Stade de France"
    *   Faites un clic droit sur le point central et sélectionnez "Plus d'infos sur cet endroit" ou regardez l'URL
    *   Les coordonnées s'affichent (Latitude, Longitude)

## Exercice 2 : Voyage autour du monde

!!! question "Énoncé"

    Recherchez les coordonnées GPS des lieux suivants :
    
    1. **L'Empire State Building** à New York (États-Unis)
    2. **L'Opéra de Sydney** à Sydney (Australie)
    
    Utilisez ensuite l'outil [Lexilogos](https://www.lexilogos.com/calcul_distances.htm) pour calculer la distance entre ces deux lieux.
    
    **Questions :**
    
    1. Quelles sont les coordonnées de l'Empire State Building ?
    2. Quelles sont les coordonnées de l'Opéra de Sydney ?
    3. Quelle est la distance (en km) entre ces deux monuments ?
    4. Combien de temps faudrait-il en avion à 900 km/h pour relier les deux ?

??? tip "Indice"

    *   Recherchez chaque monument sur Google Maps
    *   Notez les coordonnées au format décimal (ex: 40.7484, 151.2152)
    *   Sur Lexilogos, entrez les coordonnées de départ et d'arrivée
    *   Pour le temps de vol : $Temps = \frac{Distance}{Vitesse}$

## Exercice 3 : Conversion de coordonnées

!!! question "Énoncé"

    Convertissez les coordonnées suivantes du format décimal au format degrés-minutes (DM).
    
    **Coordonnées à convertir :**
    
    1. 45.7640° N
    2. 4.8357° E
    3. 43.2965° N
    4. 5.3698° E

??? tip "Indice"

    **Méthode de conversion :**
    
    1. La partie entière = les degrés
    2. La partie décimale × 60 = les minutes
    
    **Exemple** : 48.8584°
    
    *   Degrés : 48°
    *   Minutes : 0.8584 × 60 = 51.504'
    *   Résultat : 48° 51.504'


## Exercice 4 : Nombre de satellites

!!! question "Énoncé"

    **Questions :**
    
    1. Combien de satellites minimum sont nécessaires pour déterminer une position en 2D (latitude et longitude) ?
    2. Combien de satellites minimum sont nécessaires pour déterminer une position en 3D (latitude, longitude et altitude) ?
    3. Pourquoi a-t-on besoin d'un satellite supplémentaire pour la synchronisation ?
    4. Que se passe-t-il si le récepteur GPS ne capte que 2 satellites ?

??? tip "Indice"

    *   Relisez la section sur la trilatération dans le cours
    *   Pensez aux dimensions : 2D vs 3D
    *   La synchronisation temporelle est cruciale pour calculer les distances


## Exercice 5 : Calcul de distance

!!! question "Énoncé"

    Un signal GPS met **0.08 secondes** pour arriver du satellite au récepteur.
    
    **Questions :**
    
    1. Sachant que le signal voyage à la vitesse de la lumière (300 000 km/s), calculez la distance entre le satellite et le récepteur.
    2. Exprimez cette distance en mètres.
    3. Les satellites GPS orbitent à environ 20 200 km d'altitude. Le résultat vous semble-t-il cohérent ?

??? tip "Indice"

    **Formule** : Distance = Vitesse × Temps
    
    *   Vitesse = 300 000 km/s
    *   Temps = 0.08 s
    *   1 km = 1000 m

## Exercice 6 : Décodage de trame NMEA (Niveau 1)

!!! question "Énoncé"

    Analysez la trame NMEA suivante :
    
    ```
    $GPGGA,175737.303,4449.833,N,00034.772,W,1,04,1.0,0.0,M,0.0,M,,*7C
    ```
    
    **Questions :**
    
    1. À quelle heure (UTC) cette position a-t-elle été enregistrée ?
    2. Quelle est la latitude en format degrés-minutes ?
    3. Quelle est la longitude en format degrés-minutes ?
    4. Combien de satellites ont été utilisés ?
    5. Utilisez le site [NMEA Decoder](https://rl.se/gprmc) pour identifier la ville correspondante.

??? tip "Indice"

    **Structure de la trame GPGGA :**
    
    *   Champ 1 : Heure UTC (HHMMSS.SSS)
    *   Champ 2-3 : Latitude et direction (N/S)
    *   Champ 4-5 : Longitude et direction (E/W)
    *   Champ 7 : Nombre de satellites

## Exercice 7 : Décodage de trame NMEA (Niveau 2)

!!! question "Énoncé"

    Analysez les trois trames NMEA suivantes et identifiez les villes correspondantes :
    
    **Trame 1 :**
    ```
    $GPGGA,175736.303,5038.047,N,00303.695,E,1,03,1.0,0.0,M,0.0,M,,*68
    ```
    
    **Trame 2 :**
    ```
    $GPGGA,175738.303,4545.175,N,00450.039,E,1,12,1.0,0.0,M,0.0,M,,*69
    ```
    
    **Trame 3 :**
    ```
    $GPGGA,175736.303,4533.786,N,00554.803,E,1,05,1.0,154.3,M,0.0,M,,*68
    ```
    
    **Questions pour chaque trame :**
    
    1. Convertissez les coordonnées au format décimal
    2. Identifiez la ville
    3. Pour la trame 3 : À quelle altitude se trouve l'objet ?

??? tip "Indice"

    **Conversion DM → Décimal :**
    
    *   Latitude : 4836.5375' = 48° + (36.5375/60)° = 48.6090°
    *   Utilisez Google Maps pour identifier les villes
    *   L'altitude est indiquée dans le champ après le nombre de satellites

## Exercice 8 : Coordonnées mystère

!!! question "Énoncé"

    À quelle ville correspondent les coordonnées suivantes : **41.921° N, 8.735° E** ?
    
    **Questions :**
    
    1. Identifiez la ville
    2. Dans quel pays se trouve-t-elle ?
    3. Convertissez ces coordonnées au format degrés-minutes

??? tip "Indice"

    *   Utilisez Google Maps : entrez directement les coordonnées dans la barre de recherche
    *   Format à entrer : 41.921, 8.735

## Exercice 9 : Précision GPS

!!! question "Énoncé"

    **Questions :**
    
    1. Quelle est la précision typique d'un GPS civil ?
    2. Quel système de géolocalisation européen offre une meilleure précision ?
    3. Citez trois facteurs qui peuvent dégrader la précision du GPS.
    4. Pourquoi le GPS fonctionne-t-il moins bien en ville qu'en rase campagne ?

??? tip "Indice"

    *   Relisez la section sur la précision dans le cours
    *   Pensez aux obstacles physiques
    *   Réfléchissez à l'effet des bâtiments sur les signaux satellites

## Exercice 10 : Vie privée et géolocalisation

!!! question "Énoncé"

    **Questions de réflexion :**
    
    1. Citez trois applications qui utilisent votre géolocalisation.
    2. Quels sont les risques liés au partage de votre position ?
    3. Comment peut-on protéger sa vie privée tout en utilisant la géolocalisation ?
    4. Pourquoi est-il important de supprimer les métadonnées GPS des photos avant de les partager sur les réseaux sociaux ?

??? tip "Indice"

    *   Pensez aux applications que vous utilisez quotidiennement
    *   Réfléchissez aux informations qu'on peut déduire de vos déplacements
    *   Consultez la section "Enjeux et perspectives" du cours

