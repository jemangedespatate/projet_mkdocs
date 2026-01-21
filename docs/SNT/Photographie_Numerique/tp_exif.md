# 🕵️‍♂️ Travaux Pratiques : Enquête sur les Métadonnées EXIF

Ce TP est destiné aux élèves ayant terminé les activités de base. Nous allons explorer les **métadonnées** cachées dans vos photos : les données **EXIF** (Exchangeable Image File Format).

## 🎯 Objectifs
- Comprendre ce que sont les données EXIF.
- Apprendre à utiliser un script Python pour extraire ces informations.
- Découvrir comment les supprimer pour protéger sa vie privée.

---

## 🔍 Activité 1 : Observation en ligne

Pour cette enquête, nous allons utiliser une image de test contenant des données de localisation.

1. **Téléchargez l'image de test** : [photo_mystere.jpg](../img/photo_mystere.jpg){:download="photo_mystere.jpg"}
2. Allez sur le site [jimpl.com](https://jimpl.com/).
3. Téléversez l'image `photo_mystere.jpg`.
4. **Observez les résultats :**
    - À quelle date et heure précise la photo a-t-elle été prise ?
    - Quel est le modèle exact de l'appareil photo ?
    - **Le clou du spectacle** : Trouvez les coordonnées GPS et cliquez sur le lien pour voir le lieu sur une carte. Où se trouve-t-on ?

!!! warning "Vie privée"
    Vous venez de voir qu'une simple photo peut révéler l'endroit exact où vous étiez (votre maison, votre école, etc.). C'est pourquoi il faut être prudent avant de partager ses photos originales !

---

## 🐍 Activité 2 : Extraction avec Python

Nous allons maintenant utiliser le script **code_exif.py** pour automatiser cette lecture.

### 1. Préparation
1. Téléchargez le script complet : [code_exif.py](code_exif.py){:download="code_exif.py"}.
2. Placez-le dans le même dossier que l'image [photo_mystere.jpg](../img/photo_mystere.jpg).
3. Lancez le script.

### 2. Observation
Le script affiche les informations suivantes :
- Le modèle de l'appareil.
- La date de la prise de vue.
- Les coordonnées GPS converties.
- Un lien Google Maps pour localiser l'image.

!!! info "Le saviez-vous ?"
    Le script doit transformer les coordonnées GPS du format "Degrés, Minutes, Secondes" (utilisé par l'appareil) en format "Décimal" (utilisé par Google Maps).

---

## 🧮 Activité 3 : Comment fonctionne le calcul ? (Analyse)

Regardez la fonction `convertir_gps` dans le fichier `code_exif.py`. L'appareil photo ne stocke pas un simple nombre mais trois valeurs (Degrés, Minutes, Secondes).

La formule mathématique utilisée par le script est :
$$ \text{Décimal} = \text{Degré} + \frac{\text{Minute}}{60} + \frac{\text{Seconde}}{3600} $$

Si vous avez une photo avec des données GPS, vérifiez que le lien généré par le script correspond bien au site où la photo a été prise.

---

## 🧹 Activité 4 : Effacer les traces

Il est important de savoir "nettoyer" ses photos avant de les envoyer ou de les poster.

### Méthode 1 : Avec le script Python
1. Lancez `code_exif.py`.
2. Après l'analyse, répondez `o` (oui) à la question *"Voulez-vous créer une version 'propre' ?"*.
3. Un nouveau fichier `CLEAN_...` sera créé. Analysez ce nouveau fichier avec le script : que remarquez-vous ?

### Méthode 2 : Sans Python (Windows)
1. Faites un **clic droit** sur votre image > **Propriétés**.
2. Allez dans l'onglet **Détails**.
3. Tout en bas, cliquez sur **"Supprimer les propriétés et les informations personnelles"**.
4. Choisissez "Créer une copie en supprimant toutes les propriétés possibles".
5. Comparez le poids (en octets) de l'image originale et de l'image nettoyée.

---

## 📝 Bilan
Répondez aux questions suivantes :
1. Pourquoi les réseaux sociaux (Instagram, WhatsApp, Facebook) suppriment-ils automatiquement les EXIF des photos que vous postez ?
2. Citez deux avantages des données EXIF pour un photographe professionnel.
3. Quel est le principal risque lié aux métadonnées pour un utilisateur lambda ?
