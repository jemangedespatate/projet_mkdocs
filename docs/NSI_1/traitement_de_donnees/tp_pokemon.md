# 🎮 TP : Création d'un Pokédex (Génération 1)

---

## � Objectif

Dans ce TP, nous allons mettre en pratique nos connaissances sur le **traitement de données en tables**. L'objectif est de créer un mini-Pokédex capable de rechercher un Pokémon de la première génération par son nom et d'afficher ses types ainsi que ses statistiques de combat.

Dans ce TP, vous analyserez le chargement des données et compléterez les fonctions de recherche manquantes dans le fichier Python fourni.

## Organisation des fichiers 📂

Pour que votre projet fonctionne correctement, vous devez placer tous les fichiers dans **un même répertoire** (dossier).

Les fichiers nécessaires sont :

- [pokedex.py](./pokedex.py){:download="pokedex.py"} : contient le code de l'interface et les fonctions à compléter.
- [pokemon.csv](./pokemon.csv){:download="pokemon.csv"} : la base de données des 151 Pokémon.
- [Dossier e](./e.zip){:download="e.zip"} : contient les sprites des Pokémon (déjà présent dans ton espace de travail).

👉 Arborescence attendue :

```
mon_projet_pokedex/
│
├── pokedex.py
├── pokemon.csv
└── e/ (dossier des images)
```

---

## 🐍 Étape 2 : Développement du moteur

Télécharge le fichier `pokedex.py` fourni par ton professeur. Ce fichier contient déjà l'interface graphique. Ton travail est de compléter les deux fonctions à l'intérieur pour faire fonctionner le Pokédex.

### 1. Analyse du chargement des données

Ouvre le fichier `pokedex.py`. La fonction `charger_pokemons(nom_fichier)` est déjà écrite. Observe son code et réponds aux questions suivantes sur ton compte-rendu :

1. À quoi sert la ligne `lecteur = csv.DictReader(fichier)` ?
2. Pourquoi utilise-t-on la fonction `int()` pour des clés comme `"pv"` ou `"attaque"` ? Que se passerait-il si on ne le faisait pas ?
3. Quel est le type de la variable `pokemons` retournée par la fonction ? Et que contient-elle précisément ?

### 2. Mission : Recherche d'un Pokémon

**Mission :** Complète la fonction `rechercher_pokemon(nom_recherche, table)` qui :
- Parcourt la liste des Pokémon.
- Compare le nom de chaque Pokémon avec `nom_recherche`.
- **Indice :** Utilise `.lower()` pour que la recherche fonctionne même si on oublie la majuscule.
- Retourne le dictionnaire du Pokémon s'il est trouvé, sinon retourne `None`.

---

## 🖥️ Étape 3 : Visualisation

Une fois tes fonctions complétées, lance le fichier `pokedex.py`. Une fenêtre s'ouvrira, te permettant de tester ton code en direct. Si tes fonctions sont correctes, les statistiques du Pokémon s'afficheront automatiquement dans l'interface !

---

---

## 🚀 Défis Bonus (Pour les plus rapides)

Une fois ton Pokédex opérationnel, tente de relever ces défis en complétant les fonctions correspondantes dans `pokedex.py`.

### Bonus 1 : Statistiques moyennes

**Mission :** Complète la fonction `calculer_moyenne_vitesse(table)` qui :
- Calcule la somme de toutes les vitesses de la table.
- Retourne la moyenne (somme / nombre de Pokémon).
- **Test :** Clique sur le bouton "Vitesse moyenne" dans l'interface.

### Bonus 2 : Filtrer par type

**Mission :** Complète la fonction `filtrer_par_type(type_recherche, table)` qui :
- Crée une liste vide pour stocker les noms trouvés.
- Parcourt la table.
- Si le type recherché correspond au `type1` **OU** au `type2` du Pokémon, ajoute son nom à la liste.
- Retourne la liste finale des noms.
- **Test :** Saisis un type (ex: "Feu") dans la barre de recherche et clique sur "Filtrer par type".

---

💡 **Conseil :** Utilise le cours sur le [Traitement de données en tables](./cours.md) pour t'aider !
