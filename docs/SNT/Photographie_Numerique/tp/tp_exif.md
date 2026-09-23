# 🕵️‍♂️ Exercices Avancé : Enquête sur les Métadonnées EXIF

Ces exercices sont destinés aux élèves ayant terminé les activités de base. Nous allons explorer les **métadonnées** cachées dans vos photos : les données **EXIF** (Exchangeable Image File Format).

## 🔍 Activité 1 : Observation en ligne

Pour cette enquête, nous allons utiliser une image de test contenant des données de localisation.

1. **Téléchargez les images de test** :
    - [photo_mystere.jpg](../../img/photo_mystere.jpg){:download="photo_mystere.jpg"}
    - [photo_mystere_2.jpg](../../img/photo_mystere_2.jpg){:download="photo_mystere_2.jpg"}
    - [photo_mystere_3.jpg](../../img/photo_mystere_3.jpg){:download="photo_mystere_3.jpg"}
2. Allez sur le site [jimpl.com](https://jimpl.com/).
3. Téléversez l'une des images (par exemple `photo_mystere.jpg`).

!!! question "Question 1"
    Relevez les informations suivantes pour `photo_mystere.jpg` :

    *   **Date et Heure** de la prise de vue : ...
    *   **Modèle** de l'appareil photo : ...
    *   **Coordonnées GPS** (Latitude, Longitude) : ...

!!! question "Question 2"
    Cliquez sur la carte ou le lien de localisation.

    *   **Où** a été prise cette photo (Ville, Rue ou Monument) ? : ...

!!! warning "Vie privée"
    Vous venez de voir qu'une simple photo peut révéler l'endroit exact où vous étiez (votre maison, votre école, etc.). C'est pourquoi il faut être prudent avant de partager ses photos originales !

---

## 🐍 Activité 2 : Extraction avec Python

Nous allons maintenant utiliser le script **code_exif.py** pour automatiser cette lecture.

### 1. Préparation

1. Téléchargez le script complet : [code_exif.py](code_exif.py){:download="code_exif.py"}.
2. Placez-le dans le même dossier que les images téléchargées.
3. Ouvrez le fichier `code_exif.py` avec votre éditeur Python (Thonny, IDLE, etc.).

!!! question "Question 3"
    Regardez les premières lignes du code.
 
    *   Quelle **bibliothèque** Python est utilisée pour gérer les images ? (Indice : ligne `from ... import ...`) : ...

### 2. Exécution et Analyse
Lancez le script et choisissez l'image `photo_mystere.jpg`.

!!! question "Question 4"
    Recopiez les informations affichées par le script dans la console :

    *   Modèle : ...
    *   Date : ...
    *   Lien Google Maps : ...

!!! question "Question 5"
    Le script affiche-t-il exactement la même localisation que le site Jimpl.com ? Si non, est-ce proche ?

---

## 🧮 Activité 3 : Le calcul GPS

Les coordonnées GPS stockées dans l'image sont souvent en **Degrés, Minutes, Secondes (DMS)** (ex: 48° 51' 24").
Pour les utiliser sur Google Maps, il faut les convertir en **Degrés Décimaux (DD)** (ex: 48.8566).
La formule est :

**Décimal = Degré + (Minute / 60) + (Seconde / 3600)**

!!! question "Question 6"
    À vous de calculer !
    Convertissez la coordonnée suivante : **45° 30' 36"**

    *   Calcul : ...
    *   Calcul intermédiaire : ...
    *   Résultat décimal : ...

---

## 🧹 Activité 4 : Effacer les traces

Il est important de savoir "nettoyer" ses photos avant de les publier.

### Méthode 1 : Avec le script Python

1. Lancez `code_exif.py`.
2. Après l'analyse, répondez `o` (oui) à la question *"Voulez-vous créer une version 'propre' ?"*.
3. Un nouveau fichier (commençant par `CLEAN_`) est créé.

!!! question "Question 7"
    Analysez ce nouveau fichier `CLEAN_...` avec le site Jimpl.com ou le script.

    *   Trouvez-vous encore des données GPS ?
    *   Trouvez-vous encore la date de prise de vue ?

### Méthode 2 : Comparaison de poids
Regardez la taille (en octets ou Ko) du fichier original et du fichier nettoyé.

!!! question "Question 8"

    *   Taille de l'image originale : ...
    *   Taille de l'image nettoyée : ...
    *   Quelle est la différence de taille ? Pourquoi le fichier est-il plus léger ?


