# 📋 Questionnaire d'Évaluation - Géolocalisation

**Durée** : 5 minutes  
**Nom** : ________________  
**Classe** : ________________  
**Date** : ________________

---

## Question 1 : Définition (2 points)

Qu'est-ce que la géolocalisation ?

!!! question ""
    
    ☐ A) Une technique pour mesurer la température d'un lieu  
    ☐ B) Une technique pour situer précisément un lieu, une personne ou un objet sur Terre  
    ☐ C) Une application pour prendre des photos  
    ☐ D) Un système de communication par satellite  

---

## Question 2 : Coordonnées géographiques (3 points)

Quelles sont les trois dimensions utilisées pour localiser un point sur Terre ?

!!! question ""
    
    1. ______________________
    2. ______________________
    3. ______________________

---

## Question 3 : Systèmes de géolocalisation (2 points)

Quel système de géolocalisation européen est le plus précis ?

!!! question ""
    
    ☐ A) GPS  
    ☐ B) GLONASS  
    ☐ C) Galileo  
    ☐ D) BeiDou  

---

## Question 4 : Nombre de satellites (3 points)

Combien de satellites minimum sont nécessaires pour déterminer une position en 3D (latitude, longitude, altitude) ?

!!! question ""
    
    ☐ A) 2 satellites  
    ☐ B) 3 satellites  
    ☐ C) 4 satellites  
    ☐ D) 5 satellites  

**Pourquoi ce nombre ?** (1 point bonus)

_________________________________________________________________

---

## Question 5 : Trilatération (2 points)

Qu'est-ce que la trilatération ?

!!! question ""
    
    ☐ A) Une technique pour mesurer les angles entre satellites  
    ☐ B) Une technique pour déterminer une position en mesurant les distances depuis au moins 3 points de référence  
    ☐ C) Un type de satellite GPS  
    ☐ D) Une application de navigation  

---

## Question 6 : Calcul de distance (3 points)

Un signal GPS met **0.06 secondes** pour arriver du satellite au récepteur.  
La vitesse du signal est de **300 000 km/s**.

**Calculez la distance entre le satellite et le récepteur :**

!!! question ""
    
    Distance = Vitesse × Temps = ______________ km

---

## Question 7 : Protocole NMEA (2 points)

Que signifie NMEA ?

!!! question ""
    
    ☐ A) National Marine Electronics Association  
    ☐ B) New Modern Electronic Application  
    ☐ C) Navigation Measurement Electronic Algorithm  
    ☐ D) Network Management Electronic Access  

---

## Question 8 : Décodage de trame (3 points)

Dans la trame NMEA suivante, identifiez le **nombre de satellites** utilisés :

```
$GPGGA,123519.487,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

!!! question ""
    
    Nombre de satellites : __________

---

## Question 9 : Précision GPS (2 points)

Quelle est la précision typique d'un GPS civil ?

!!! question ""
    
    ☐ A) 1 à 2 mètres  
    ☐ B) 5 à 10 mètres  
    ☐ C) 50 à 100 mètres  
    ☐ D) 500 mètres  

---

## Question 10 : Vie privée (3 points)

Citez **deux risques** liés au partage de votre géolocalisation :

!!! question ""
    
    1. _________________________________________________________________
    
    2. _________________________________________________________________

---

## Question 11 : Applications (2 points)

Parmi ces applications, laquelle N'utilise PAS la géolocalisation ?

!!! question ""
    
    ☐ A) Google Maps  
    ☐ B) Calculatrice  
    ☐ C) Uber  
    ☐ D) Pokémon GO  

---

## Question 12 : Formats de coordonnées (2 points)

Convertissez **45.5° en format degrés-minutes** :

!!! question ""
    
    45.5° = _____ ° _____ '

---

## Question Bonus : Culture générale (+2 points)

En quelle année le GPS est-il devenu accessible au grand public ?

!!! question ""
    
    ☐ A) Années 1970  
    ☐ B) Années 1980  
    ☐ C) Années 1990  
    ☐ D) Années 2000  

---

## 📊 Barème

**Total** : 29 points (+ 3 points bonus possibles)

| Note | Points |
|:---:|:---:|
| Très bien | 24-29 |
| Bien | 18-23 |
| Assez bien | 12-17 |
| À revoir | < 12 |

---

## ✅ Correction

??? check "Réponses"

    **Question 1** : B) Une technique pour situer précisément un lieu, une personne ou un objet sur Terre
    
    **Question 2** : 
    1. Latitude
    2. Longitude
    3. Altitude
    
    **Question 3** : C) Galileo
    
    **Question 4** : C) 4 satellites  
    *Pourquoi ?* 3 pour la position (x, y, z) + 1 pour la synchronisation temporelle
    
    **Question 5** : B) Une technique pour déterminer une position en mesurant les distances depuis au moins 3 points de référence
    
    **Question 6** : Distance = 300 000 × 0.06 = **18 000 km**
    
    **Question 7** : A) National Marine Electronics Association
    
    **Question 8** : **8 satellites** (champ n°7 de la trame)
    
    **Question 9** : B) 5 à 10 mètres
    
    **Question 10** : Exemples de réponses acceptées :
    - Surveillance/traçabilité des déplacements
    - Risque de cambriolage (si on sait que vous n'êtes pas chez vous)
    - Harcèlement/stalking
    - Collecte et revente de données personnelles
    - Révélation de votre domicile
    
    **Question 11** : B) Calculatrice
    
    **Question 12** : 45.5° = **45° 30'**  
    *Calcul :* 0.5 × 60 = 30 minutes
    
    **Question Bonus** : C) Années 1990
