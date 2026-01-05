# Série d'exercices : Traitement de données en tables

---

## 📋 Données de travail

Pour tous les exercices, nous utiliserons la table suivante représentant des films :

```python
films = [
    {"titre": "Inception", "realisateur": "Nolan", "annee": 2010, "note": 8.8, "genre": "Science-fiction"},
    {"titre": "Interstellar", "realisateur": "Nolan", "annee": 2014, "note": 8.6, "genre": "Science-fiction"},
    {"titre": "Le Parrain", "realisateur": "Coppola", "annee": 1972, "note": 9.2, "genre": "Drame"},
    {"titre": "Pulp Fiction", "realisateur": "Tarantino", "annee": 1994, "note": 8.9, "genre": "Policier"},
    {"titre": "The Dark Knight", "realisateur": "Nolan", "annee": 2008, "note": 9.0, "genre": "Action"},
    {"titre": "Forrest Gump", "realisateur": "Zemeckis", "annee": 1994, "note": 8.8, "genre": "Drame"},
    {"titre": "Matrix", "realisateur": "Wachowski", "annee": 1999, "note": 8.7, "genre": "Science-fiction"},
    {"titre": "Gladiator", "realisateur": "Scott", "annee": 2000, "note": 8.5, "genre": "Action"}
]
```

---

## 🟢 **Niveau 1 — Projection simple**

### **Exercice 1 : Liste des titres**

Écris une fonction `extraire_titres(films)` qui retourne la liste de tous les titres de films.

**Résultat attendu :**
```python
["Inception", "Interstellar", "Le Parrain", "Pulp Fiction", ...]
```

👉 *Objectif : parcourir une liste de dictionnaires et extraire une clé.*

---

### **Exercice 2 : Années de sortie**

Écris une fonction `extraire_annees(films)` qui retourne la liste de toutes les années de sortie (sans doublons).

**Indice :** Utilise un ensemble (`set`) pour éliminer les doublons, puis convertis en liste.

👉 *Objectif : manipulation de sets pour éliminer les doublons.*

---

### **Exercice 3 : Projection multiple**

Écris une fonction `extraire_titre_note(films)` qui retourne une liste de dictionnaires contenant uniquement le titre et la note de chaque film.

**Résultat attendu :**
```python
[
    {"titre": "Inception", "note": 8.8},
    {"titre": "Interstellar", "note": 8.6},
    ...
]
```

👉 *Objectif : créer de nouveaux dictionnaires avec seulement certaines clés.*

---

## 🟡 **Niveau 2 — Sélection (Filtrage)**

### **Exercice 4 : Films récents**

Écris une fonction `films_apres_2000(films)` qui retourne la liste des films sortis après l'an 2000.

👉 *Objectif : filtrer selon une condition numérique.*

---

### **Exercice 5 : Films par réalisateur**

Écris une fonction `films_de_nolan(films)` qui retourne la liste des films réalisés par "Nolan".

**Bonus :** Généralise en créant une fonction `films_par_realisateur(films, realisateur)` qui prend le nom du réalisateur en paramètre.

👉 *Objectif : filtrer selon une condition sur une chaîne de caractères.*

---

### **Exercice 6 : Films bien notés**

Écris une fonction `films_note_superieure(films, seuil)` qui retourne les films ayant une note supérieure ou égale au seuil donné.

**Exemple :** `films_note_superieure(films, 9.0)` doit retourner "Le Parrain" et "The Dark Knight".

👉 *Objectif : filtrage avec paramètre.*

---

### **Exercice 7 : Films par genre**

Écris une fonction `films_par_genre(films, genre)` qui retourne tous les films d'un genre donné.

**Exemple :** `films_par_genre(films, "Science-fiction")` doit retourner Inception, Interstellar et Matrix.

👉 *Objectif : filtrage par catégorie.*

---

## 🔵 **Niveau 3 — Projection + Sélection**

### **Exercice 8 : Titres des films de Nolan**

Écris une fonction `titres_nolan(films)` qui retourne uniquement les **titres** des films réalisés par Nolan.

**Résultat attendu :**
```python
["Inception", "Interstellar", "The Dark Knight"]
```

👉 *Objectif : combiner filtrage et projection.*

---

### **Exercice 9 : Années des films bien notés**

Écris une fonction `annees_films_excellents(films)` qui retourne les années de sortie des films ayant une note supérieure ou égale à 9.0.

👉 *Objectif : projection sur un sous-ensemble filtré.*

---

### **Exercice 10 : Films d'action récents**

Écris une fonction `films_action_recents(films)` qui retourne les films du genre "Action" sortis après 2005.

👉 *Objectif : filtrage avec plusieurs conditions.*

---

## 🟣 **Niveau 4 — Agrégation**

### **Exercice 11 : Nombre de films**

Écris une fonction `nombre_films(films)` qui retourne le nombre total de films dans la table.

👉 *Objectif : utiliser `len()`.*

---

### **Exercice 12 : Note moyenne**

Écris une fonction `note_moyenne(films)` qui calcule et retourne la note moyenne de tous les films.

👉 *Objectif : calculer une moyenne avec `sum()` et `len()`.*

---

### **Exercice 13 : Film le mieux noté**

Écris une fonction `meilleur_film(films)` qui retourne le dictionnaire complet du film ayant la meilleure note.

**Indice :** Parcours la liste en gardant trace du film avec la note maximale.

👉 *Objectif : recherche du maximum.*

---

### **Exercice 14 : Film le plus ancien**

Écris une fonction `film_plus_ancien(films)` qui retourne le titre du film le plus ancien.

👉 *Objectif : recherche du minimum.*

---

### **Exercice 15 : Comptage par réalisateur**

Écris une fonction `nombre_films_par_realisateur(films, realisateur)` qui compte combien de films ont été réalisés par un réalisateur donné.

**Exemple :** `nombre_films_par_realisateur(films, "Nolan")` doit retourner 3.

👉 *Objectif : comptage conditionnel.*

---

## 🔴 **Niveau 5 — Tri et opérations avancées**

### **Exercice 16 : Tri par note**

Écris une fonction `trier_par_note(films)` qui retourne la liste des films triés par note décroissante.

**Indice :** Utilise `sorted()` avec le paramètre `key`.

👉 *Objectif : tri avec fonction lambda.*

---

### **Exercice 17 : Tri par année**

Écris une fonction `trier_par_annee(films)` qui retourne la liste des films triés par année croissante.

👉 *Objectif : tri chronologique.*

---

### **Exercice 18 : Top 3 des films**

Écris une fonction `top_3_films(films)` qui retourne les 3 films les mieux notés.

**Indice :** Trie d'abord par note, puis prends les 3 premiers avec `[:3]`.

👉 *Objectif : combinaison tri + slicing.*

---

### **Exercice 19 : Statistiques par genre**

Écris une fonction `note_moyenne_par_genre(films, genre)` qui calcule la note moyenne des films d'un genre donné.

**Exemple :** `note_moyenne_par_genre(films, "Science-fiction")` doit calculer la moyenne de Inception, Interstellar et Matrix.

👉 *Objectif : agrégation sur un sous-ensemble.*

---

## 🔥 **Niveau 6 — Challenge**

### **Exercice 20 : Dictionnaire de réalisateurs**

Écris une fonction `grouper_par_realisateur(films)` qui retourne un dictionnaire où :
- Les **clés** sont les noms des réalisateurs
- Les **valeurs** sont des listes de titres de films

**Résultat attendu :**
```python
{
    "Nolan": ["Inception", "Interstellar", "The Dark Knight"],
    "Coppola": ["Le Parrain"],
    "Tarantino": ["Pulp Fiction"],
    ...
}
```

👉 *Objectif : créer une structure de données complexe.*

---

### **Exercice 21 : Lecture depuis un fichier CSV**

Crée un fichier `films.csv` avec le contenu suivant :

```
titre,realisateur,annee,note,genre
Inception,Nolan,2010,8.8,Science-fiction
Interstellar,Nolan,2014,8.6,Science-fiction
Le Parrain,Coppola,1972,9.2,Drame
```

Écris une fonction `charger_films(nom_fichier)` qui lit ce fichier et retourne une liste de dictionnaires.

**Indice :** Utilise le module `csv` et `csv.DictReader`.

👉 *Objectif : manipulation de fichiers CSV.*

---

### **Exercice 22 : Analyse complète**

Écris une fonction `analyser_films(films)` qui affiche :
1. Le nombre total de films
2. La note moyenne
3. Le film le mieux noté
4. Le film le plus ancien
5. Le réalisateur ayant le plus de films

👉 *Objectif : combiner plusieurs opérations d'analyse.*

---

## 💡 Conseils

- Commence par les exercices de niveau 1 pour bien comprendre la structure
- Teste tes fonctions avec des `print()` pour vérifier les résultats
- N'hésite pas à utiliser des compréhensions de liste pour simplifier ton code
- Pour les exercices avancés, décompose le problème en plusieurs étapes

Bon courage ! 🚀
