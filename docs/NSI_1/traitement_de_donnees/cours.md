# 📊 Cours de NSI : Traitement de données en tables

---

## 1. Introduction

Dans le monde réel, les données sont souvent organisées sous forme de **tables** (comme dans un tableur Excel ou Google Sheets). Chaque ligne représente un **enregistrement** (par exemple, une personne, une ville, un produit) et chaque colonne représente un **attribut** (nom, âge, prix, etc.).

En Python, nous pouvons représenter ces tables comme des **listes de dictionnaires**, où :
- Chaque **dictionnaire** = une ligne (un enregistrement)
- Chaque **clé** du dictionnaire = un attribut (une colonne)

Cette structure est très puissante et permet de manipuler facilement de grandes quantités de données.

---

## 2. Représentation d'une table en Python

### ➤ Structure : Liste de dictionnaires

Imaginons une table de données sur des élèves :

| nom     | age | classe | moyenne |
|---------|-----|--------|---------|
| Alice   | 16  | 1NSI1  | 15.5    |
| Bob     | 15  | 1NSI2  | 12.0    |
| Charlie | 16  | 1NSI1  | 14.8    |

En Python, cette table devient :

```python
eleves = [
    {"nom": "Alice", "age": 16, "classe": "1NSI1", "moyenne": 15.5},
    {"nom": "Bob", "age": 15, "classe": "1NSI2", "moyenne": 12.0},
    {"nom": "Charlie", "age": 16, "classe": "1NSI1", "moyenne": 14.8}
]
```

Chaque élève est un **dictionnaire**, et tous les élèves forment une **liste**.

---

## 3. Lecture de fichiers CSV

### ➤ Qu'est-ce qu'un fichier CSV ?

**CSV** signifie **Comma-Separated Values** (valeurs séparées par des virgules). C'est un format de fichier texte très utilisé pour stocker des données tabulaires.

Exemple de fichier `communes.csv` :

```
nom_commune,code_postal,departement,population
Paris,75000,Paris,2161000
Lyon,69000,Rhône,516092
Marseille,13000,Bouches-du-Rhône,869815
```

### ➤ La bibliothèque `csv`

Python possède un module intégré appelé `csv` qui permet de lire et écrire des fichiers CSV facilement.

```python
import csv

# Lire un fichier CSV et le transformer en liste de dictionnaires
def charger_donnees(nom_fichier):
    donnees = []
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            donnees.append(dict(ligne))
    return donnees

# Utilisation
villes = charger_donnees('communes.csv')
```

**Explication :**
- `csv.DictReader(fichier)` : crée un lecteur qui transforme chaque ligne en dictionnaire
- La première ligne du CSV devient automatiquement les **clés** des dictionnaires
- Chaque ligne suivante devient un **dictionnaire** dans la liste

---

## 4. Projection de données

La **projection** consiste à extraire une ou plusieurs colonnes d'une table.

### ➤ Extraire une seule colonne

Pour obtenir la liste de tous les noms de communes :

```python
def extraire_noms(villes):
    noms = []
    for ville in villes:
        noms.append(ville["nom_commune"])
    return noms

# Ou en version compacte avec une compréhension de liste
noms = [ville["nom_commune"] for ville in villes]
```

### ➤ Extraire plusieurs colonnes

Pour obtenir uniquement le nom et la population :

```python
def extraire_nom_population(villes):
    resultat = []
    for ville in villes:
        resultat.append({
            "nom": ville["nom_commune"],
            "population": ville["population"]
        })
    return resultat
```

---

## 5. Sélection de données (Filtrage)

La **sélection** consiste à ne garder que les lignes qui respectent une **condition**.

### ➤ Filtrer selon un critère simple

Pour obtenir uniquement les villes du département "Rhône" :

```python
def villes_du_rhone(villes):
    resultat = []
    for ville in villes:
        if ville["departement"] == "Rhône":
            resultat.append(ville)
    return resultat

# Ou en version compacte
villes_rhone = [v for v in villes if v["departement"] == "Rhône"]
```

### ➤ Filtrer selon plusieurs critères

Pour obtenir les villes du Rhône avec plus de 100 000 habitants :

```python
def grandes_villes_rhone(villes):
    resultat = []
    for ville in villes:
        if ville["departement"] == "Rhône" and int(ville["population"]) > 100000:
            resultat.append(ville)
    return resultat
```

⚠️ **Attention :** Les données lues depuis un CSV sont souvent des **chaînes de caractères**. Il faut parfois les convertir en `int` ou `float` pour faire des comparaisons numériques.

---

## 6. Combinaison : Projection + Sélection

On peut combiner les deux opérations pour obtenir des résultats précis.

**Exemple :** Obtenir les noms des villes de plus de 500 000 habitants

```python
def noms_grandes_villes(villes):
    noms = []
    for ville in villes:
        if int(ville["population"]) > 500000:
            noms.append(ville["nom_commune"])
    return noms

# Version compacte
noms = [v["nom_commune"] for v in villes if int(v["population"]) > 500000]
```

---

## 7. Opérations d'agrégation

Les **agrégations** permettent de calculer des statistiques sur les données.

### ➤ Compter le nombre d'enregistrements

```python
nombre_villes = len(villes)
```

### ➤ Calculer une somme

Population totale de toutes les villes :

```python
def population_totale(villes):
    total = 0
    for ville in villes:
        total += int(ville["population"])
    return total

# Ou avec sum()
total = sum(int(v["population"]) for v in villes)
```

### ➤ Trouver le maximum/minimum

Ville la plus peuplée :

```python
def ville_max_population(villes):
    ville_max = villes[0]
    for ville in villes:
        if int(ville["population"]) > int(ville_max["population"]):
            ville_max = ville
    return ville_max

# Ou avec max()
ville_max = max(villes, key=lambda v: int(v["population"]))
```

### ➤ Calculer une moyenne

Moyenne de population :

```python
def moyenne_population(villes):
    total = sum(int(v["population"]) for v in villes)
    return total / len(villes)
```

---

## 8. Tri de données

Pour trier une table selon un attribut :

```python
# Trier par nom (ordre alphabétique)
villes_triees = sorted(villes, key=lambda v: v["nom_commune"])

# Trier par population (ordre décroissant)
villes_triees = sorted(villes, key=lambda v: int(v["population"]), reverse=True)
```

---

## 9. Résumé des opérations

| Opération | Description | Exemple |
|-----------|-------------|---------|
| **Projection** | Extraire certaines colonnes | Liste des noms |
| **Sélection** | Filtrer selon une condition | Villes du Rhône |
| **Agrégation** | Calculer des statistiques | Population totale |
| **Tri** | Ordonner les données | Villes par population |

---

## 10. Bonnes pratiques

✅ **Toujours vérifier le type des données** : les CSV renvoient souvent des chaînes de caractères

✅ **Utiliser des fonctions** : pour rendre le code réutilisable et lisible

✅ **Gérer les erreurs** : vérifier que les clés existent avant d'y accéder

✅ **Documenter le code** : ajouter des commentaires pour expliquer la logique

---

## 11. Exemple complet

```python
import csv

# 1. Charger les données
def charger_villes(fichier):
    villes = []
    with open(fichier, 'r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            villes.append(dict(ligne))
    return villes

# 2. Projection : noms des villes
def extraire_noms(villes):
    return [v["nom_commune"] for v in villes]

# 3. Sélection : villes de plus de 100k habitants
def grandes_villes(villes):
    return [v for v in villes if int(v["population"]) > 100000]

# 4. Agrégation : population moyenne
def moyenne_population(villes):
    total = sum(int(v["population"]) for v in villes)
    return total / len(villes)

# Utilisation
villes = charger_villes('communes.csv')
print("Noms:", extraire_noms(villes))
print("Grandes villes:", grandes_villes(villes))
print("Moyenne:", moyenne_population(villes))
```
