# 🌍 Module Géolocalisation - SNT Seconde

## 📚 Contenu du module

Ce module couvre les aspects fondamentaux de la géolocalisation par satellite :

### 📖 Cours (`cours.md`)
- Point historique sur le développement du GPS
- Définitions : géolocalisation, coordonnées géographiques, trilatération
- Fonctionnement de la géolocalisation par satellite
- Le protocole NMEA-0183
- Applications pratiques et calcul d'itinéraires
- Enjeux et perspectives (vie privée, sécurité)

### ✏️ Exercices (`exercices.md`)
10 exercices progressifs couvrant :
- Manipulation de coordonnées GPS
- Conversion entre formats (décimal, degrés-minutes)
- Décodage de trames NMEA
- Calculs de distance
- Questions de vie privée et sécurité

### 💻 Travaux Pratiques (`travaux_pratique.md`)
6 activités pratiques :
- Exploration de coordonnées GPS
- Conversion de coordonnées (manuel et Python)
- Décodage de trames NMEA
- Programme complet d'analyse GPS
- Extraction de métadonnées GPS des photos

## 🎯 Objectifs pédagogiques

À la fin de ce module, les élèves seront capables de :
- Comprendre le fonctionnement du GPS et de la trilatération
- Manipuler des coordonnées géographiques
- Décoder des trames NMEA
- Créer des programmes Python pour analyser des données GPS
- Identifier les enjeux de vie privée liés à la géolocalisation

## 🛠️ Prérequis

- Connaissances de base en Python
- Notions de mathématiques (conversions, calculs simples)
- Accès à Internet pour les outils en ligne

## 📦 Ressources nécessaires

### Bibliothèques Python
```bash
pip install Pillow
```

### Outils en ligne
- [Google Maps](https://www.google.com/maps)
- [NMEA Decoder](https://rl.se/gprmc)
- [Calculateur de distances](https://www.lexilogos.com/calcul_distances.htm)
- [Activité Trilatération](https://parcours.algorea.org/fr/a/88752303685492924)

## 📁 Structure des fichiers

```
Geolocalisation/
├── README.md                 # Ce fichier
├── sommaire.md              # Table des matières
├── cours.md                 # Cours complet
├── exercices.md             # 10 exercices avec solutions
└── travaux_pratique.md      # 6 activités pratiques
```

## 🎨 Assets

Les images utilisées dans le cours sont stockées dans :
```
docs/assets/seconde/geoloc/
└── trilateration.png        # Schéma de la trilatération
```

## 📝 Notes pour l'enseignant

- **Durée estimée** : 4-5 séances de 1h30
- **Niveau** : Seconde SNT
- **Thème** : Localisation, cartographie et mobilité

### Progression suggérée

1. **Séance 1** : Cours (historique, définitions, coordonnées)
2. **Séance 2** : Cours (trilatération, NMEA) + Exercices 1-5
3. **Séance 3** : Exercices 6-10 + TP Activités 1-2
4. **Séance 4** : TP Activités 3-5 (Python)
5. **Séance 5** : TP Activité 6 + Discussions sur la vie privée

## 🔗 Liens utiles

- [Programme officiel SNT](https://eduscol.education.fr/2068/programmes-et-ressources-en-sciences-numeriques-et-technologie-voie-gt)
- [Documentation Pillow](https://pillow.readthedocs.io/)
- [Format NMEA](https://www.gpsinformation.org/dale/nmea.htm)

## 📄 Licence

Ce contenu pédagogique est destiné à un usage éducatif.
