# ✏️ Exercices - Géolocalisation

## Exercice 1 : Coordonnées GPS du lycée

!!! question "Énoncé"

    Sur votre téléphone ou avec Google Maps, retrouvez les coordonnées GPS de votre lycée.
    
    **Questions :**
    
    1. Quelle est la latitude de votre lycée ?
    2. Quelle est la longitude de votre lycée ?
    3. Votre lycée est-il situé dans l'hémisphère Nord ou Sud ?
    4. Votre lycée est-il situé à l'Est ou à l'Ouest du méridien de Greenwich ?

??? tip "Indice"

    *   Ouvrez Google Maps sur votre téléphone ou ordinateur
    *   Recherchez le nom de votre lycée
    *   Faites un clic droit sur le point et sélectionnez "Plus d'infos sur cet endroit"
    *   Les coordonnées s'affichent en bas de l'écran

## Exercice 2 : Exploration urbaine

!!! question "Énoncé"

    Recherchez les coordonnées GPS des lieux suivants :
    
    1. **Tour Eiffel** à Paris
    2. **Statue de la Liberté** à New York
    
    Utilisez ensuite l'outil [Lexilogos](https://www.lexilogos.com/calcul_distances.htm) pour calculer la distance entre ces deux lieux.
    
    **Questions :**
    
    1. Quelles sont les coordonnées de la Tour Eiffel ?
    2. Quelles sont les coordonnées de la Statue de la Liberté ?
    3. Quelle est la distance (en km) entre ces deux monuments ?
    4. Combien de temps faudrait-il en avion à 800 km/h ?

??? tip "Indice"

    *   Recherchez chaque monument sur Google Maps
    *   Notez les coordonnées au format décimal (ex: 48.8584, 2.2945)
    *   Sur Lexilogos, entrez les coordonnées de départ et d'arrivée
    *   Pour le temps de vol : Temps = Distance ÷ Vitesse

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

??? check "Réponse"

    1. **45.7640°** = 45° 45.840' N
    2. **4.8357°** = 4° 50.142' E
    3. **43.2965°** = 43° 17.790' N
    4. **5.3698°** = 5° 22.188' E

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

??? check "Réponse"

    1. **3 satellites** minimum pour une position 2D
    2. **4 satellites** minimum pour une position 3D
    3. Le satellite supplémentaire permet de **corriger l'horloge du récepteur** qui n'est pas aussi précise que les horloges atomiques des satellites
    4. Avec seulement 2 satellites, on ne peut pas déterminer une position unique (il y aurait deux points d'intersection possibles)

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

??? check "Réponse"

    1. Distance = 300 000 km/s × 0.08 s = **24 000 km**
    2. 24 000 km = **24 000 000 mètres**
    3. Oui, c'est cohérent car les satellites GPS orbitent à environ 20 200 km, et le signal peut parcourir une distance légèrement supérieure selon l'angle

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

??? check "Réponse"

    1. **17:57:37.303** (heure UTC)
    2. Latitude : **44° 49.833' N**
    3. Longitude : **0° 34.772' W**
    4. **4 satellites**
    5. Cette position correspond à **Bordeaux, France**

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

??? check "Réponse"

    **Trame 1 :**
    
    *   Coordonnées : 50.6341° N, 3.0616° E
    *   Ville : **Lille, France**
    
    **Trame 2 :**
    
    *   Coordonnées : 45.7529° N, 4.8340° E
    *   Ville : **Lyon, France**
    
    **Trame 3 :**
    
    *   Coordonnées : 45.5631° N, 5.9134° E
    *   Altitude : **154.3 mètres**
    *   Ville : **Chambéry, France**

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

??? check "Réponse"

    1. **Ajaccio**
    2. **France** (Corse)
    3. Coordonnées en DM :
        *   Latitude : 41° 55.260' N
        *   Longitude : 8° 44.100' E

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

??? check "Réponse"

    1. **5 à 10 mètres** pour un GPS civil
    2. **Galileo** (précision d'environ 1 mètre)
    3. Trois facteurs :
        *   Nombre de satellites visibles
        *   Conditions météorologiques
        *   Obstacles (bâtiments, relief, végétation)
    4. En ville, les bâtiments créent un **effet canyon** : les signaux sont réfléchis et perturbés, ce qui réduit la précision

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

??? check "Réponse"

    1. **Exemples d'applications :**
        *   Google Maps / Waze (navigation)
        *   Instagram / Snapchat (géotagging)
        *   Uber / Deliveroo (services de livraison)
    
    2. **Risques :**
        *   Surveillance de vos déplacements
        *   Cambriolage (si on sait que vous n'êtes pas chez vous)
        *   Harcèlement / stalking
        *   Collecte et revente de données personnelles
    
    3. **Protection :**
        *   Désactiver la géolocalisation quand elle n'est pas nécessaire
        *   Vérifier les autorisations des applications
        *   Utiliser le mode "position approximative" plutôt que "position précise"
        *   Ne pas partager sa position en temps réel publiquement
    
    4. **Métadonnées GPS :**
        *   Les photos contiennent souvent votre position exacte
        *   Cela peut révéler votre domicile, votre lieu de travail, vos habitudes
        *   Des personnes malveillantes pourraient utiliser ces informations
