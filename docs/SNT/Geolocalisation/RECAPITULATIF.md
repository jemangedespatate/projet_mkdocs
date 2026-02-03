# 📦 Module Géolocalisation - Récapitulatif Complet

## ✅ Contenu créé

### 📚 Documents pédagogiques

| Fichier | Description | Taille | Usage |
|:---|:---|:---:|:---|
| `cours.md` | Cours complet | 10 Ko | Lecture élèves |
| `presentation.md` | Diaporama Marp (30 slides) | 9 Ko | Projection en classe |
| `exercices.md` | 10 exercices avec solutions | 10 Ko | Travail autonome |
| `travaux_pratique.md` | 6 activités Python | 13 Ko | TP informatique |

### 📋 Évaluation

| Fichier | Description | Taille | Usage |
|:---|:---|:---:|:---|
| `questionnaire.md` | Version MkDocs avec corrections | 6 Ko | Documentation |
| `questionnaire_eleves.md` | Version imprimable | 5 Ko | Distribution élèves |
| `questionnaire_corrige.md` | Corrigé détaillé + barème | 8 Ko | Enseignant uniquement |

### 📖 Documentation

| Fichier | Description | Taille | Usage |
|:---|:---|:---:|:---|
| `README.md` | Vue d'ensemble du module | 3 Ko | Information générale |
| `GUIDE_PRESENTATION.md` | Guide d'utilisation Marp | 5 Ko | Aide enseignant |
| `sommaire.md` | Table des matières | <1 Ko | Navigation |

### 🎨 Ressources visuelles

| Fichier | Description | Emplacement |
|:---|:---|:---|
| `trilateration.png` | Schéma GPS | `docs/assets/seconde/geoloc/` |

---

## 📊 Statistiques

- **Total fichiers** : 10 fichiers Markdown + 1 image
- **Taille totale** : ~68 Ko
- **Questions** : 12 + 1 bonus = 13 questions
- **Exercices** : 10 exercices progressifs
- **Activités TP** : 6 activités pratiques
- **Slides** : ~30 diapositives

---

## 🎯 Déroulement pédagogique suggéré

### Séance 1 : Cours magistral (1h)

1. **Présentation** (55 min)
   - Utiliser `presentation.md` avec Marp
   - Interaction avec les élèves
   - Démonstrations en direct (Google Maps, NMEA Decoder)

2. **Questionnaire d'évaluation** (5 min)
   - Distribuer `questionnaire_eleves.md`
   - Correction rapide en classe

### Séance 2 : Exercices (1h30)

1. **Correction du questionnaire** (10 min)
2. **Exercices 1-5** (40 min)
   - Coordonnées GPS
   - Conversions
   - Calculs
3. **Exercices 6-10** (40 min)
   - Décodage NMEA
   - Vie privée

### Séance 3 : TP Python Partie 1 (1h30)

1. **Activités 1-2** (45 min)
   - Exploration coordonnées
   - Conversion Python
2. **Activité 3** (45 min)
   - Décodage NMEA manuel et Python

### Séance 4 : TP Python Partie 2 (1h30)

1. **Activités 4-5** (60 min)
   - Conversion DM → Décimal
   - Programme complet
2. **Activité 6** (30 min)
   - Métadonnées GPS photos

### Séance 5 : Évaluation finale (optionnel)

- Évaluation sommative
- Projet personnel (créer une application GPS)

---

## 🛠️ Prérequis techniques

### Pour la présentation

**Option 1 : VS Code + Extension Marp**
```bash
# Installer l'extension Marp for VS Code
# Depuis le marketplace VS Code
```

**Option 2 : Marp CLI**
```bash
npm install -g @marp-team/marp-cli
marp presentation.md --pdf
```

**Option 3 : En ligne**
- [https://web.marp.app/](https://web.marp.app/)

### Pour les TP Python

```bash
pip install Pillow
```

### Outils en ligne

- [Google Maps](https://www.google.com/maps)
- [NMEA Decoder](https://rl.se/gprmc)
- [Calculateur distances](https://www.lexilogos.com/calcul_distances.htm)
- [Activité Trilatération](https://parcours.algorea.org/fr/a/88752303685492924)

---

## 📁 Structure des fichiers

```
docs/SNT/Geolocalisation/
├── README.md                      # Vue d'ensemble
├── GUIDE_PRESENTATION.md          # Guide Marp
├── sommaire.md                    # Table des matières
│
├── cours.md                       # Cours complet
├── presentation.md                # Diaporama (Marp)
│
├── questionnaire.md               # QCM avec corrections (MkDocs)
├── questionnaire_eleves.md        # Version imprimable élèves
├── questionnaire_corrige.md       # Corrigé enseignant
│
├── exercices.md                   # 10 exercices
└── travaux_pratique.md            # 6 activités Python

docs/assets/seconde/geoloc/
└── trilateration.png              # Schéma GPS
```

---

## 🎓 Compétences travaillées

### Connaissances

- ✅ Définir la géolocalisation
- ✅ Identifier les systèmes GPS (GPS, Galileo, GLONASS, BeiDou)
- ✅ Comprendre le protocole NMEA
- ✅ Connaître les formats de coordonnées

### Savoir-faire

- ✅ Manipuler des coordonnées géographiques
- ✅ Convertir entre formats (décimal, DM, DMS)
- ✅ Décoder des trames NMEA
- ✅ Calculer des distances
- ✅ Programmer en Python (décodage, conversion)
- ✅ Extraire des métadonnées EXIF

### Savoir-être

- ✅ Comprendre les enjeux de vie privée
- ✅ Adopter un comportement responsable
- ✅ Maîtriser ses paramètres de confidentialité

---

## 📈 Évaluation

### Questionnaire rapide (5 min)

- **Format** : QCM + questions courtes
- **Points** : 29 + 3 bonus
- **Objectif** : Vérifier la compréhension immédiate

### Exercices

- **Format** : 10 exercices progressifs
- **Objectif** : Approfondir et pratiquer

### TP Python

- **Format** : 6 activités pratiques
- **Objectif** : Mise en application informatique

### Évaluation finale (optionnel)

- Synthèse des connaissances
- Projet personnel

---

## 💡 Conseils pédagogiques

### Pour la présentation

1. **Interaction** : Poser des questions régulièrement
2. **Démonstrations** : Montrer les outils en direct
3. **Exemples concrets** : Utiliser des situations du quotidien
4. **Rythme** : Adapter selon les réactions

### Pour les exercices

1. **Progression** : Du plus simple au plus complexe
2. **Indices** : Disponibles pour aider
3. **Corrections** : Détaillées et pédagogiques
4. **Autonomie** : Encourager la recherche

### Pour les TP

1. **Binômes** : Travail en équipe recommandé
2. **Guidage** : Code partiellement fourni
3. **Expérimentation** : Encourager les tests
4. **Validation** : Tester avec plusieurs trames

---

## 🔗 Liens utiles

### Documentation officielle

- [Programme SNT](https://eduscol.education.fr/2068/programmes-et-ressources-en-sciences-numeriques-et-technologie-voie-gt)
- [Marp Documentation](https://marpit.marp.app/)
- [Pillow Documentation](https://pillow.readthedocs.io/)

### Outils en ligne

- [Google Maps](https://www.google.com/maps)
- [NMEA Decoder](https://rl.se/gprmc)
- [GPS Visualizer](https://www.gpsvisualizer.com/)
- [Marp Web](https://web.marp.app/)

### Ressources complémentaires

- [Format NMEA](https://www.gpsinformation.org/dale/nmea.htm)
- [GPS.gov](https://www.gps.gov/)
- [Galileo](https://www.gsa.europa.eu/european-gnss/galileo/galileo-european-global-satellite-based-navigation-system)

---

## 📞 Support

Pour toute question ou suggestion d'amélioration :

- Consulter le `README.md` pour la vue d'ensemble
- Consulter le `GUIDE_PRESENTATION.md` pour l'utilisation de Marp
- Adapter le contenu selon vos besoins pédagogiques

---

## 📝 Notes de version

**Version** : 1.0  
**Date** : 03/02/2026  
**Auteur** : Cours créé à partir du contenu de Clément Braun  
**Niveau** : Seconde SNT  
**Thème** : Localisation, cartographie et mobilité  

---

## ✨ Points forts du module

✅ **Complet** : Cours, présentation, exercices, TP, évaluation  
✅ **Progressif** : Du simple au complexe  
✅ **Interactif** : Nombreuses activités pratiques  
✅ **Moderne** : Utilisation de Marp, Python, outils en ligne  
✅ **Pédagogique** : Indices, corrections détaillées  
✅ **Actuel** : Enjeux de vie privée abordés  
✅ **Clé en main** : Prêt à l'emploi  

---

**🎉 Le module est prêt à être utilisé !**
