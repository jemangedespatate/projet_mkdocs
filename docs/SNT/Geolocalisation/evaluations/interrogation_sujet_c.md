# Interrogation de SNT - Géolocalisation (Sujet C)

### Exercice 1 : Fonctionnement et définitions

1. Définissez les termes **latitude** et **longitude**. Quelle ligne de référence sert d'origine pour chacune d'elles ?
2. Expliquez le principe de la **trilatération**. Combien de satellites sont nécessaires pour localiser précisément un point en trois dimensions ?
3. Expliquez brièvement pourquoi les signaux GPS sont **moins fiables à l'intérieur des bâtiments**.
4. Donnez un exemple concret d'application du quotidien utilisant la géolocalisation.

### Exercice 2 : Calcul de distance

Un signal radio met **320 µs** pour voyager depuis un satellite jusqu'à votre smartphone. Sachant que la vitesse du signal est d'environ **300 m/µs**, calculez la distance qui les sépare en détaillant le calcul. Donnez ensuite le résultat en km.

### Exercice 3 : Conversion de coordonnées

La conversion est indispensable pour passer des formats GPS aux formats lisibles sur des cartes.

1. Convertissez la coordonnée suivante du format décimal vers le format degrés-minutes-secondes (DMS) : **27,50°**
2. Convertissez la coordonnée suivante du format degrés-minutes-secondes (DMS) vers le format décimal : **36° 20' 24"**

### Exercice 4 : Trame NMEA

Voici une trame NMEA captée par un récepteur GPS :

`$GPGGA,101500.000,4545.0000,N,00453.0000,E,1,07,1.5,170.0,M,,,,0000*0F`

1. À quelle heure (UTC) cette position a-t-elle été enregistrée ?
2. Quelle est la latitude à laquelle se trouve le capteur ?
3. Quelle est la longitude à laquelle se trouve le capteur ?
4. Convertissez les données trouvées pour la latitude et la longitude au format décimal.

### Exercice 5 : Vie privée et enjeux

Citez **trois** risques liés à l'utilisation constante de la géolocalisation sur les smartphones concernant la vie privée des utilisateurs.

### Exercice 6 : Systèmes satellites

1. Le GPS est le système américain de navigation par satellite. Citez le nom de son concurrent **européen**.
2. Quel est l'avantage principal de ce système européen par rapport au GPS ?
3. Citez un facteur autre que les batiments pouvant affecter la précision d'un récepteur GPS.
