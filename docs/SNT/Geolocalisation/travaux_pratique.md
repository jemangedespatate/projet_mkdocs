# 💻 TP - Coordonnées GPS et Trames NMEA

## 🎯 Objectifs

Dans ce TP, vous allez :

*   Manipuler des coordonnées GPS
*   Décoder des trames NMEA
*   Créer un programme Python pour analyser des données GPS
*   Visualiser des positions sur une carte

## 📋 Prérequis

*   Connaissances de base en Python
*   Compréhension du format NMEA (voir cours)
*   Accès à Internet pour utiliser les outils en ligne

## Activité 1 : Exploration de coordonnées GPS

### Étape 1 : Localisation de lieux célèbres

Utilisez Google Maps pour trouver les coordonnées GPS des lieux suivants et complétez le tableau :

| Lieu | Latitude | Longitude | Pays |
| :--- | :---: | :---: | :---: |
| Colisée (Rome) | | | |
| Big Ben (Londres) | | | |
| Taj Mahal (Inde) | | | |
| Christ Rédempteur (Rio) | | | |
| Opéra de Sydney | | | |

!!! tip "Astuce"

    Sur Google Maps, faites un clic droit sur le lieu et sélectionnez "Plus d'infos sur cet endroit" pour voir les coordonnées.

### Étape 2 : Calcul de distances

Utilisez l'outil [Lexilogos](https://www.lexilogos.com/calcul_distances.htm) pour calculer :

1. La distance entre le Colisée et la Tour Eiffel
2. La distance entre Big Ben et le Taj Mahal
3. La distance entre votre lycée et l'Opéra de Sydney

!!! question "Question"

    Quel est le lieu le plus éloigné de votre lycée parmi ceux listés ci-dessus ?

## Activité 2 : Conversion de coordonnées

### Étape 1 : Conversion manuelle

Convertissez les coordonnées suivantes du format décimal au format degrés-minutes (DM) :

1. **Mont Blanc** : 45.8326° N, 6.8652° E
2. **Mont Fuji** : 35.3606° N, 138.7274° E
3. **Kilimandjaro** : -3.0674° S, 37.3556° E

!!! note "Rappel"

    **Formule** : 
    
    *   Degrés = partie entière
    *   Minutes = partie décimale × 60

### Étape 2 : Vérification avec Python

Créez un programme Python pour automatiser la conversion :

```python
def decimal_vers_dm(coord_decimal):
    """
    Convertit une coordonnée décimale en format degrés-minutes
    
    Paramètre:
        coord_decimal (float): coordonnée en format décimal
    
    Retour:
        tuple: (degrés, minutes)
    """
    # À compléter
    pass

# Test
lat_decimal = 45.8326
degres, minutes = decimal_vers_dm(lat_decimal)
print(f"{lat_decimal}° = {degres}° {minutes}'")
```

??? tip "Indice"

    *   Utilisez `int()` pour obtenir la partie entière
    *   La partie décimale = coord_decimal - partie_entiere
    *   Multipliez la partie décimale par 60

??? check "Solution"

    ```python
    def decimal_vers_dm(coord_decimal):
        degres = int(coord_decimal)
        minutes = (coord_decimal - degres) * 60
        return degres, minutes
    
    # Test
    lat_decimal = 45.8326
    degres, minutes = decimal_vers_dm(lat_decimal)
    print(f"{lat_decimal}° = {degres}° {minutes:.4f}'")
    # Résultat : 45.8326° = 45° 49.9560'
    ```

## Activité 3 : Décodage de trames NMEA

### Étape 1 : Analyse manuelle

Analysez la trame NMEA suivante :

```
$GPGGA,123519.487,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

Complétez le tableau :

| Champ | Valeur | Signification |
| :--- | :---: | :--- |
| Type de trame | | |
| Heure UTC | | |
| Latitude (DM) | | |
| Latitude (décimal) | | |
| Longitude (DM) | | |
| Longitude (décimal) | | |
| Nombre de satellites | | |
| Altitude | | |

!!! tip "Astuce"

    Utilisez le site [NMEA Decoder](https://rl.se/gprmc) pour vérifier vos réponses.

### Étape 2 : Décodeur Python

Créez un programme Python pour décoder automatiquement une trame GPGGA :

```python
def decoder_gpgga(trame):
    """
    Décode une trame NMEA GPGGA
    
    Paramètre:
        trame (str): trame NMEA complète
    
    Retour:
        dict: dictionnaire contenant les informations décodées
    """
    # Supprimer le $ et le checksum (*XX)
    trame = trame.strip()
    if trame.startswith('$'):
        trame = trame[1:]
    if '*' in trame:
        trame = trame.split('*')[0]
    
    # Séparer les champs
    champs = trame.split(',')
    
    # Extraire les informations
    info = {}
    info['type'] = champs[0]
    info['heure'] = champs[1]
    info['latitude_dm'] = champs[2]
    info['lat_direction'] = champs[3]
    info['longitude_dm'] = champs[4]
    info['lon_direction'] = champs[5]
    info['nb_satellites'] = champs[7]
    info['altitude'] = champs[9]
    
    return info

# Test
trame = "$GPGGA,123519.487,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
resultat = decoder_gpgga(trame)

print("=== Décodage de la trame GPGGA ===")
print(f"Type : {resultat['type']}")
print(f"Heure UTC : {resultat['heure']}")
print(f"Latitude : {resultat['latitude_dm']} {resultat['lat_direction']}")
print(f"Longitude : {resultat['longitude_dm']} {resultat['lon_direction']}")
print(f"Satellites : {resultat['nb_satellites']}")
print(f"Altitude : {resultat['altitude']} m")
```

!!! question "Question"

    Testez votre programme avec les trames suivantes. Identifiez les villes correspondantes.

    ```
    $GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E
    $GPGGA,175737.303,4449.833,N,00034.772,W,1,04,1.0,0.0,M,0.0,M,,*7C
    $GPGGA,175738.303,4545.175,N,00450.039,E,1,12,1.0,0.0,M,0.0,M,,*69
    ```

## Activité 4 : Conversion DM → Décimal

### Étape 1 : Comprendre le format

Dans le format NMEA, les coordonnées sont au format DDMM.MMMM :

*   **DD** = degrés (2 chiffres pour la latitude, 3 pour la longitude)
*   **MM.MMMM** = minutes

**Exemple** : 4807.038 = 48° 07.038'

### Étape 2 : Fonction de conversion

Complétez la fonction suivante :

```python
def dm_vers_decimal(coord_dm, est_longitude=False):
    """
    Convertit une coordonnée NMEA (DDMM.MMMM) en format décimal
    
    Paramètres:
        coord_dm (str): coordonnée au format DDMM.MMMM
        est_longitude (bool): True si c'est une longitude (3 chiffres pour les degrés)
    
    Retour:
        float: coordonnée en format décimal
    """
    # À compléter
    pass

# Test
lat_nmea = "4807.038"
lat_decimal = dm_vers_decimal(lat_nmea, est_longitude=False)
print(f"{lat_nmea} = {lat_decimal}°")
```

??? tip "Indice"

    1. Si c'est une longitude, les 3 premiers caractères sont les degrés, sinon les 2 premiers
    2. Le reste représente les minutes
    3. Formule : décimal = degrés + (minutes / 60)

??? check "Solution"

    ```python
    def dm_vers_decimal(coord_dm, est_longitude=False):
        if est_longitude:
            degres = int(coord_dm[:3])
            minutes = float(coord_dm[3:])
        else:
            degres = int(coord_dm[:2])
            minutes = float(coord_dm[2:])
        
        decimal = degres + (minutes / 60)
        return decimal
    
    # Test
    lat_nmea = "4807.038"
    lat_decimal = dm_vers_decimal(lat_nmea, est_longitude=False)
    print(f"{lat_nmea} = {lat_decimal:.6f}°")
    # Résultat : 4807.038 = 48.117300°
    ```

## Activité 5 : Programme complet d'analyse GPS

### Objectif

Créez un programme complet qui :

1. Lit une trame NMEA GPGGA
2. Décode les informations
3. Convertit les coordonnées en format décimal
4. Affiche un résumé formaté

### Code à compléter

```python
def decoder_et_convertir_gpgga(trame):
    """
    Décode une trame GPGGA et convertit les coordonnées en décimal
    
    Paramètre:
        trame (str): trame NMEA complète
    
    Retour:
        dict: informations décodées avec coordonnées décimales
    """
    # 1. Décoder la trame (réutiliser la fonction decoder_gpgga)
    info = decoder_gpgga(trame)
    
    # 2. Convertir latitude
    lat_decimal = dm_vers_decimal(info['latitude_dm'], est_longitude=False)
    if info['lat_direction'] == 'S':
        lat_decimal = -lat_decimal
    
    # 3. Convertir longitude
    lon_decimal = dm_vers_decimal(info['longitude_dm'], est_longitude=True)
    if info['lon_direction'] == 'W':
        lon_decimal = -lon_decimal
    
    # 4. Ajouter les coordonnées décimales
    info['latitude_decimal'] = lat_decimal
    info['longitude_decimal'] = lon_decimal
    
    return info

def afficher_position(info):
    """
    Affiche les informations GPS de manière formatée
    """
    print("\n" + "="*50)
    print("📍 POSITION GPS")
    print("="*50)
    print(f"🕐 Heure UTC     : {info['heure'][:2]}:{info['heure'][2:4]}:{info['heure'][4:]}")
    print(f"🌍 Latitude      : {info['latitude_dm']} {info['lat_direction']} ({info['latitude_decimal']:.6f}°)")
    print(f"🌍 Longitude     : {info['longitude_dm']} {info['lon_direction']} ({info['longitude_decimal']:.6f}°)")
    print(f"🛰️  Satellites    : {info['nb_satellites']}")
    print(f"⛰️  Altitude      : {info['altitude']} m")
    print(f"🔗 Google Maps  : https://www.google.com/maps?q={info['latitude_decimal']},{info['longitude_decimal']}")
    print("="*50)

# Programme principal
if __name__ == "__main__":
    # Trames de test
    trames = [
        "$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E",
        "$GPGGA,175737.303,4449.833,N,00034.772,W,1,04,1.0,0.0,M,0.0,M,,*7C",
        "$GPGGA,123519.487,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
    ]
    
    for trame in trames:
        info = decoder_et_convertir_gpgga(trame)
        afficher_position(info)
```

!!! success "Résultat attendu"

    Le programme devrait afficher pour chaque trame :
    
    *   L'heure formatée
    *   Les coordonnées en format DM et décimal
    *   Le nombre de satellites
    *   L'altitude
    *   Un lien Google Maps cliquable

## Activité 6 : Métadonnées GPS dans les photos

### Objectif

Extraire les coordonnées GPS des métadonnées EXIF d'une photo.

### Code Python

```python
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extraire_gps(chemin_image):
    """
    Extrait les coordonnées GPS des métadonnées EXIF d'une image
    
    Paramètre:
        chemin_image (str): chemin vers l'image
    
    Retour:
        tuple: (latitude, longitude) ou None si pas de GPS
    """
    try:
        image = Image.open(chemin_image)
        exif = image._getexif()
        
        if not exif:
            return None
        
        # Chercher les données GPS
        for tag, valeur in exif.items():
            nom_tag = TAGS.get(tag, tag)
            if nom_tag == 'GPSInfo':
                gps_data = {}
                for t in valeur:
                    sous_tag = GPSTAGS.get(t, t)
                    gps_data[sous_tag] = valeur[t]
                
                # Extraire latitude et longitude
                if 'GPSLatitude' in gps_data and 'GPSLongitude' in gps_data:
                    lat = gps_data['GPSLatitude']
                    lon = gps_data['GPSLongitude']
                    
                    lat_ref = gps_data.get('GPSLatitudeRef', 'N')
                    lon_ref = gps_data.get('GPSLongitudeRef', 'E')
                    
                    # Convertir en décimal
                    lat_decimal = lat[0] + lat[1]/60 + lat[2]/3600
                    lon_decimal = lon[0] + lon[1]/60 + lon[2]/3600
                    
                    if lat_ref == 'S':
                        lat_decimal = -lat_decimal
                    if lon_ref == 'W':
                        lon_decimal = -lon_decimal
                    
                    return (lat_decimal, lon_decimal)
        
        return None
    
    except Exception as e:
        print(f"Erreur : {e}")
        return None

# Test
# chemin = "photo_avec_gps.jpg"
# coords = extraire_gps(chemin)
# if coords:
#     print(f"Coordonnées GPS : {coords[0]}, {coords[1]}")
#     print(f"Google Maps : https://www.google.com/maps?q={coords[0]},{coords[1]}")
# else:
#     print("Pas de données GPS dans cette image")
```

!!! warning "Attention"

    Cette activité nécessite la bibliothèque Pillow. Installez-la avec :
    ```
    pip install Pillow
    ```

## 🎓 Pour aller plus loin

!!! tip "Défis supplémentaires"

    1. **Calculateur de distance** : Créez une fonction qui calcule la distance entre deux coordonnées GPS (formule de Haversine)
    2. **Tracé GPS** : Lisez plusieurs trames NMEA et tracez le parcours sur une carte
    3. **Simulation GPS** : Générez des trames NMEA pour un trajet fictif
    4. **Analyse de fichier GPX** : Lisez un fichier GPX (format XML utilisé pour les traces GPS) et extrayez les coordonnées

## 📝 Compte-rendu

À rendre :

1. Le tableau des coordonnées de l'Activité 1
2. Les conversions de l'Activité 2
3. Le code Python complet et fonctionnel
4. Les villes identifiées pour chaque trame de test
5. Une capture d'écran de votre programme en action
