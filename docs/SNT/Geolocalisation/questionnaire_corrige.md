# ✅ Corrigé - Questionnaire d'Évaluation Géolocalisation

**Document enseignant - Ne pas distribuer aux élèves**

---

## Question 1 : Définition (2 points)

**Qu'est-ce que la géolocalisation ?**

✅ **Réponse : B**

**B) Une technique pour situer précisément un lieu, une personne ou un objet sur Terre**

---

## Question 2 : Coordonnées géographiques (3 points)

**Quelles sont les trois dimensions utilisées pour localiser un point sur Terre ?**

✅ **Réponses :**

1. **Latitude** (1 point)
2. **Longitude** (1 point)
3. **Altitude** (1 point)

---

## Question 3 : Systèmes de géolocalisation (2 points)

**Quel système de géolocalisation européen est le plus précis ?**

✅ **Réponse : C**

**C) Galileo**

*Note : Galileo offre une précision d'environ 1 mètre, contre 5-10 mètres pour le GPS américain.*

---

## Question 4 : Nombre de satellites (3 points)

**Combien de satellites minimum sont nécessaires pour déterminer une position en 3D ?**

✅ **Réponse : C**

**C) 4 satellites** (2 points)

**Pourquoi ?** (1 point bonus)
- 3 satellites pour déterminer la position (x, y, z)
- 1 satellite supplémentaire pour la synchronisation temporelle (l'horloge du récepteur n'est pas aussi précise que les horloges atomiques des satellites)

**Barème :**
- Réponse correcte (C) : 2 points
- Explication correcte : +1 point bonus

---

## Question 5 : Trilatération (2 points)

**Qu'est-ce que la trilatération ?**

✅ **Réponse : B**

**B) Une technique pour déterminer une position en mesurant les distances depuis au moins 3 points de référence**

---

## Question 6 : Calcul de distance (3 points)

**Calculez la distance entre le satellite et le récepteur :**

✅ **Réponse : 18 000 km**

**Calcul :**
```
Distance = Vitesse × Temps
Distance = 300 000 km/s × 0.06 s
Distance = 18 000 km
```

**Barème :**
- Formule correcte : 1 point
- Calcul correct : 1 point
- Résultat avec unité : 1 point

*Note : Cette distance est cohérente car les satellites GPS orbitent à environ 20 200 km d'altitude.*

---

## Question 7 : Protocole NMEA (2 points)

**Que signifie NMEA ?**

✅ **Réponse : A**

**A) National Marine Electronics Association**

---

## Question 8 : Décodage de trame (3 points)

**Identifiez le nombre de satellites utilisés :**

```
$GPGGA,123519.487,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

✅ **Réponse : 8 satellites**

**Explication :** Le nombre de satellites se trouve dans le 7ème champ de la trame GPGGA (après les 6 premières virgules).

**Barème :**
- Réponse correcte : 3 points
- Si l'élève a identifié le bon champ mais s'est trompé dans le comptage : 2 points

---

## Question 9 : Précision GPS (2 points)

**Quelle est la précision typique d'un GPS civil ?**

✅ **Réponse : B**

**B) 5 à 10 mètres**

*Note : Galileo offre une meilleure précision (environ 1 mètre).*

---

## Question 10 : Vie privée (3 points)

**Citez deux risques liés au partage de votre géolocalisation :**

✅ **Exemples de réponses acceptées :**

- Surveillance / Traçabilité des déplacements
- Risque de cambriolage (si on sait que vous n'êtes pas chez vous)
- Harcèlement / Stalking
- Collecte et revente de données personnelles
- Révélation de votre domicile ou lieu de travail
- Atteinte à la vie privée
- Utilisation commerciale non consentie

**Barème :**
- Chaque risque pertinent et bien expliqué : 1.5 point
- Total : 3 points

**Critères d'évaluation :**
- La réponse doit être claire et précise
- Accepter toute formulation correcte du risque
- Ne pas accepter des réponses trop vagues comme "c'est dangereux"

---

## Question 11 : Applications (2 points)

**Parmi ces applications, laquelle N'utilise PAS la géolocalisation ?**

✅ **Réponse : B**

**B) Calculatrice**

*Note : Google Maps, Uber et Pokémon GO utilisent tous la géolocalisation.*

---

## Question 12 : Formats de coordonnées (2 points)

**Convertissez 45.5° en format degrés-minutes :**

✅ **Réponse : 45° 30'**

**Calcul :**
```
Partie entière : 45°
Partie décimale : 0.5 × 60 = 30'
Résultat : 45° 30'
```

**Barème :**
- Résultat correct : 1.5 point
- Calcul détaillé : 0.5 point

---

## Question Bonus : Culture générale (+2 points)

**En quelle année le GPS est-il devenu accessible au grand public ?**

✅ **Réponse : C**

**C) Années 1990**

*Note : Le GPS a été développé dans les années 1960-1970 par l'armée américaine, les premiers satellites ont été lancés dans les années 1980, mais il n'est devenu accessible au grand public que dans les années 1990.*

---

## 📊 Grille de notation

| Question | Points | Thème |
|:---:|:---:|:---|
| Q1 | 2 | Définition |
| Q2 | 3 | Coordonnées |
| Q3 | 2 | Systèmes |
| Q4 | 3 (+1) | Satellites |
| Q5 | 2 | Trilatération |
| Q6 | 3 | Calcul |
| Q7 | 2 | NMEA |
| Q8 | 3 | Décodage |
| Q9 | 2 | Précision |
| Q10 | 3 | Vie privée |
| Q11 | 2 | Applications |
| Q12 | 2 | Conversion |
| Bonus | 2 | Culture |
| **TOTAL** | **29 (+3)** | |

---

## 📈 Analyse des résultats

### Questions les plus difficiles (attendues)
- **Q6** (Calcul) : Nécessite de maîtriser la formule et les calculs
- **Q8** (Décodage NMEA) : Demande de compter les champs
- **Q10** (Vie privée) : Question ouverte nécessitant réflexion

### Questions discriminantes
- **Q4** (avec bonus) : Sépare ceux qui ont compris le principe de ceux qui ont juste retenu
- **Q12** (Conversion) : Teste la compréhension des formats

### Compétences évaluées

| Compétence | Questions |
|:---|:---|
| **Connaissances** | Q1, Q3, Q7, Q9, Q11, Bonus |
| **Compréhension** | Q2, Q4, Q5 |
| **Application** | Q6, Q8, Q12 |
| **Réflexion** | Q10 |

---

## 💡 Conseils de correction

1. **Soyez indulgent sur l'orthographe** des termes techniques (Galileo, trilatération, etc.)
2. **Acceptez les formulations équivalentes** pour les questions ouvertes
3. **Valorisez le raisonnement** même si le résultat final est faux (Q6, Q12)
4. **Pour Q10**, acceptez toute réponse pertinente même si elle n'est pas dans la liste
5. **Le bonus** ne doit pas pénaliser : il récompense les meilleurs

---

## 🎯 Objectifs pédagogiques vérifiés

Ce questionnaire permet de vérifier que les élèves ont compris :

✅ La définition et le principe de la géolocalisation  
✅ Le système de coordonnées géographiques  
✅ Le fonctionnement du GPS (satellites, trilatération)  
✅ Le protocole NMEA et le décodage de trames  
✅ Les applications pratiques  
✅ Les enjeux de vie privée  

---

## 📝 Remarques pour l'amélioration

Si les résultats sont globalement faibles sur certaines questions, prévoir :

- **Q6** : Revoir les calculs avec la formule Distance = Vitesse × Temps
- **Q8** : Faire un exercice supplémentaire de décodage NMEA
- **Q10** : Organiser un débat sur la vie privée et la géolocalisation
- **Q12** : Multiplier les exercices de conversion

---

## ⏱️ Timing de correction

**Correction en classe** (recommandé) : 10-15 minutes
- Permet de revenir sur les points mal compris
- Favorise les échanges et questions
- Renforce l'apprentissage

**Correction individuelle** : 2-3 minutes par copie
