# 🎬 Mini-Projet : Analyseur de Données Cinématographiques

---

## 🎯 Objectif du projet

Créer un programme Python qui analyse une base de données de films au format CSV et permet d'effectuer diverses recherches et statistiques.

Ce projet vous permettra de mettre en pratique toutes les compétences vues dans le cours :
- Lecture de fichiers CSV
- Projection et sélection de données
- Agrégation et calculs statistiques
- Tri de données
- Interface utilisateur en ligne de commande

---

## 📂 Organisation du projet

Créez un dossier `analyseur_films` contenant :

```
analyseur_films/
│
├── films.csv           ← Base de données (à créer)
├── logique.py          ← Fonctions de traitement (à compléter)
└── interface.py        ← Interface utilisateur (à créer)
```

---

## 1. Création de la base de données

### ➤ Fichier `films.csv`

Créez un fichier `films.csv` avec le contenu suivant (vous pouvez ajouter vos propres films !) :

```csv
titre,realisateur,annee,duree,note,genre,pays
Inception,Christopher Nolan,2010,148,8.8,Science-fiction,USA
Interstellar,Christopher Nolan,2014,169,8.6,Science-fiction,USA
Le Parrain,Francis Ford Coppola,1972,175,9.2,Drame,USA
Pulp Fiction,Quentin Tarantino,1994,154,8.9,Policier,USA
The Dark Knight,Christopher Nolan,2008,152,9.0,Action,USA
Forrest Gump,Robert Zemeckis,1994,142,8.8,Drame,USA
Matrix,Lana et Lilly Wachowski,1999,136,8.7,Science-fiction,USA
Gladiator,Ridley Scott,2000,155,8.5,Action,USA
Le Fabuleux Destin d'Amélie Poulain,Jean-Pierre Jeunet,2001,122,8.3,Comédie,France
La Haine,Mathieu Kassovitz,1995,98,8.1,Drame,France
Intouchables,Olivier Nakache et Éric Toledano,2011,112,8.5,Comédie,France
Parasite,Bong Joon-ho,2019,132,8.6,Thriller,Corée du Sud
Spirited Away,Hayao Miyazaki,2001,125,8.6,Animation,Japon
Your Name,Makoto Shinkai,2016,106,8.4,Animation,Japon
La La Land,Damien Chazelle,2016,128,8.0,Comédie musicale,USA
```

---

## 2. Fonctions de traitement (`logique.py`)

Créez le fichier `logique.py` et implémentez les fonctions suivantes :

### ➤ Fonction 1 : Chargement des données

```python
import csv

def charger_films(nom_fichier):
    """
    Charge les données depuis un fichier CSV.
    Retourne une liste de dictionnaires.
    """
    # À COMPLÉTER
    pass
```

**Indice :** Utilisez `csv.DictReader` et n'oubliez pas de convertir les types (annee, duree, note en nombres).

---

### ➤ Fonction 2 : Recherche par titre

```python
def rechercher_par_titre(films, titre):
    """
    Recherche un film par son titre (recherche partielle, insensible à la casse).
    Retourne la liste des films correspondants.
    
    Exemple : rechercher_par_titre(films, "dark") 
              doit trouver "The Dark Knight"
    """
    # À COMPLÉTER
    pass
```

**Indice :** Utilisez `.lower()` pour rendre la recherche insensible à la casse et `in` pour la recherche partielle.

---

### ➤ Fonction 3 : Films par réalisateur

```python
def films_par_realisateur(films, realisateur):
    """
    Retourne tous les films d'un réalisateur donné.
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 4 : Films par période

```python
def films_par_periode(films, annee_debut, annee_fin):
    """
    Retourne les films sortis entre annee_debut et annee_fin (inclus).
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 5 : Films par genre

```python
def films_par_genre(films, genre):
    """
    Retourne tous les films d'un genre donné.
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 6 : Films par pays

```python
def films_par_pays(films, pays):
    """
    Retourne tous les films d'un pays donné.
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 7 : Top films

```python
def top_films(films, n=10):
    """
    Retourne les n films les mieux notés (par défaut 10).
    Les films sont triés par note décroissante.
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 8 : Statistiques générales

```python
def statistiques_generales(films):
    """
    Retourne un dictionnaire contenant :
    - nombre_total : nombre de films
    - note_moyenne : note moyenne de tous les films
    - duree_moyenne : durée moyenne des films
    - film_le_mieux_note : dictionnaire du film avec la meilleure note
    - film_le_plus_long : dictionnaire du film le plus long
    - annee_la_plus_ancienne : année du film le plus ancien
    - annee_la_plus_recente : année du film le plus récent
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 9 : Statistiques par réalisateur

```python
def statistiques_realisateur(films, realisateur):
    """
    Retourne un dictionnaire contenant les statistiques pour un réalisateur :
    - nombre_films : nombre de films réalisés
    - note_moyenne : note moyenne de ses films
    - meilleur_film : titre de son film le mieux noté
    """
    # À COMPLÉTER
    pass
```

---

### ➤ Fonction 10 : Réalisateurs les plus prolifiques

```python
def realisateurs_prolifiques(films, n=5):
    """
    Retourne les n réalisateurs ayant réalisé le plus de films.
    Format : liste de tuples (realisateur, nombre_de_films)
    triée par nombre décroissant.
    """
    # À COMPLÉTER
    # Indice : utilisez un dictionnaire pour compter les films par réalisateur
    pass
```

---

## 3. Interface utilisateur (`interface.py`)

Créez un menu interactif permettant d'utiliser toutes les fonctions :

```python
import logique

def afficher_menu():
    """Affiche le menu principal."""
    print("\n" + "="*50)
    print("🎬 ANALYSEUR DE FILMS 🎬")
    print("="*50)
    print("1. Rechercher un film par titre")
    print("2. Films d'un réalisateur")
    print("3. Films par période")
    print("4. Films par genre")
    print("5. Films par pays")
    print("6. Top films")
    print("7. Statistiques générales")
    print("8. Statistiques d'un réalisateur")
    print("9. Réalisateurs les plus prolifiques")
    print("0. Quitter")
    print("="*50)

def afficher_films(films):
    """Affiche une liste de films de manière formatée."""
    if not films:
        print("❌ Aucun film trouvé.")
        return
    
    print(f"\n📽️  {len(films)} film(s) trouvé(s) :\n")
    for film in films:
        print(f"  • {film['titre']} ({film['annee']}) - {film['realisateur']}")
        print(f"    ⭐ Note: {film['note']} | ⏱️  Durée: {film['duree']} min | 🎭 Genre: {film['genre']}")
        print()

def main():
    """Fonction principale du programme."""
    # Charger les données
    print("📂 Chargement de la base de données...")
    films = logique.charger_films('films.csv')
    print(f"✅ {len(films)} films chargés avec succès !\n")
    
    while True:
        afficher_menu()
        choix = input("Votre choix : ")
        
        if choix == "1":
            titre = input("Entrez le titre (ou une partie) : ")
            resultats = logique.rechercher_par_titre(films, titre)
            afficher_films(resultats)
        
        elif choix == "2":
            realisateur = input("Nom du réalisateur : ")
            resultats = logique.films_par_realisateur(films, realisateur)
            afficher_films(resultats)
        
        elif choix == "3":
            annee_debut = int(input("Année de début : "))
            annee_fin = int(input("Année de fin : "))
            resultats = logique.films_par_periode(films, annee_debut, annee_fin)
            afficher_films(resultats)
        
        elif choix == "4":
            genre = input("Genre : ")
            resultats = logique.films_par_genre(films, genre)
            afficher_films(resultats)
        
        elif choix == "5":
            pays = input("Pays : ")
            resultats = logique.films_par_pays(films, pays)
            afficher_films(resultats)
        
        elif choix == "6":
            n = input("Nombre de films à afficher (défaut: 10) : ")
            n = int(n) if n else 10
            resultats = logique.top_films(films, n)
            afficher_films(resultats)
        
        elif choix == "7":
            stats = logique.statistiques_generales(films)
            print("\n📊 STATISTIQUES GÉNÉRALES")
            print("="*50)
            print(f"Nombre total de films : {stats['nombre_total']}")
            print(f"Note moyenne : {stats['note_moyenne']:.2f}/10")
            print(f"Durée moyenne : {stats['duree_moyenne']:.0f} minutes")
            print(f"Film le mieux noté : {stats['film_le_mieux_note']['titre']} ({stats['film_le_mieux_note']['note']})")
            print(f"Film le plus long : {stats['film_le_plus_long']['titre']} ({stats['film_le_plus_long']['duree']} min)")
            print(f"Période : {stats['annee_la_plus_ancienne']} - {stats['annee_la_plus_recente']}")
        
        elif choix == "8":
            realisateur = input("Nom du réalisateur : ")
            stats = logique.statistiques_realisateur(films, realisateur)
            if stats:
                print(f"\n📊 STATISTIQUES POUR {realisateur.upper()}")
                print("="*50)
                print(f"Nombre de films : {stats['nombre_films']}")
                print(f"Note moyenne : {stats['note_moyenne']:.2f}/10")
                print(f"Meilleur film : {stats['meilleur_film']}")
            else:
                print("❌ Réalisateur non trouvé.")
        
        elif choix == "9":
            n = input("Nombre de réalisateurs à afficher (défaut: 5) : ")
            n = int(n) if n else 5
            resultats = logique.realisateurs_prolifiques(films, n)
            print(f"\n🏆 TOP {n} DES RÉALISATEURS LES PLUS PROLIFIQUES")
            print("="*50)
            for i, (realisateur, nb_films) in enumerate(resultats, 1):
                print(f"{i}. {realisateur} : {nb_films} film(s)")
        
        elif choix == "0":
            print("\n👋 Au revoir !")
            break
        
        else:
            print("❌ Choix invalide.")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
```

---

## 4. Extensions possibles (Bonus)

Une fois le projet de base terminé, vous pouvez ajouter des fonctionnalités :

### 🌟 Extension 1 : Recherche avancée

Créez une fonction `recherche_avancee(films, **criteres)` qui permet de combiner plusieurs critères :

```python
# Exemple d'utilisation
resultats = recherche_avancee(
    films,
    genre="Science-fiction",
    annee_min=2000,
    note_min=8.5
)
```

---

### 🌟 Extension 2 : Exportation des résultats

Ajoutez une fonction pour exporter les résultats de recherche dans un nouveau fichier CSV :

```python
def exporter_resultats(films, nom_fichier):
    """Exporte une liste de films dans un fichier CSV."""
    # À COMPLÉTER
    pass
```

---

### 🌟 Extension 3 : Graphiques

Utilisez la bibliothèque `matplotlib` pour créer des graphiques :
- Histogramme des notes
- Répartition des films par genre
- Évolution du nombre de films par année

---

### 🌟 Extension 4 : Recommandations

Créez une fonction qui recommande des films similaires :

```python
def recommander_films(films, titre_reference, n=5):
    """
    Recommande n films similaires au film de référence.
    Critères de similarité : même genre, même réalisateur, note proche.
    """
    # À COMPLÉTER
    pass
```

---

### 🌟 Extension 5 : Gestion de favoris

Ajoutez un système de favoris qui permet de :
- Marquer des films comme favoris
- Sauvegarder la liste de favoris dans un fichier
- Charger les favoris au démarrage

---

## 5. Critères d'évaluation

Votre projet sera évalué sur :

| Critère | Points |
|---------|--------|
| **Fonctionnalité** : Toutes les fonctions de base fonctionnent | 8 pts |
| **Qualité du code** : Code propre, commenté, bien structuré | 4 pts |
| **Interface** : Menu clair et gestion des erreurs | 3 pts |
| **Créativité** : Ajout de fonctionnalités bonus | 3 pts |
| **Documentation** : README expliquant comment utiliser le programme | 2 pts |
| **TOTAL** | 20 pts |

---

## 6. Conseils de réalisation

✅ **Commencez par les bases** : Implémentez d'abord les fonctions simples (chargement, recherche par titre)

✅ **Testez au fur et à mesure** : Vérifiez chaque fonction avant de passer à la suivante

✅ **Gérez les erreurs** : Que se passe-t-il si le fichier n'existe pas ? Si l'utilisateur entre une année invalide ?

✅ **Utilisez des fonctions auxiliaires** : Créez des petites fonctions réutilisables

✅ **Commentez votre code** : Expliquez la logique complexe

✅ **Améliorez l'affichage** : Utilisez des emojis et des couleurs pour rendre l'interface agréable

---

## 7. Exemple de session

```
📂 Chargement de la base de données...
✅ 15 films chargés avec succès !

==================================================
🎬 ANALYSEUR DE FILMS 🎬
==================================================
1. Rechercher un film par titre
2. Films d'un réalisateur
3. Films par période
4. Films par genre
5. Films par pays
6. Top films
7. Statistiques générales
8. Statistiques d'un réalisateur
9. Réalisateurs les plus prolifiques
0. Quitter
==================================================
Votre choix : 2

Nom du réalisateur : Nolan

📽️  3 film(s) trouvé(s) :

  • Inception (2010) - Christopher Nolan
    ⭐ Note: 8.8 | ⏱️  Durée: 148 min | 🎭 Genre: Science-fiction

  • Interstellar (2014) - Christopher Nolan
    ⭐ Note: 8.6 | ⏱️  Durée: 169 min | 🎭 Genre: Science-fiction

  • The Dark Knight (2008) - Christopher Nolan
    ⭐ Note: 9.0 | ⏱️  Durée: 152 min | 🎭 Genre: Action

Appuyez sur Entrée pour continuer...
```

---

## 8. Ressources utiles

- [Documentation du module csv](https://docs.python.org/fr/3/library/csv.html)
- [Compréhensions de liste en Python](https://docs.python.org/fr/3/tutorial/datastructures.html#list-comprehensions)
- [Fonction sorted() et lambda](https://docs.python.org/fr/3/howto/sorting.html)

---

Bon courage pour ce projet ! 🚀🎬
