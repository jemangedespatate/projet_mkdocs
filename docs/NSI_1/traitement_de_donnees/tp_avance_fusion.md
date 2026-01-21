# 🚀 TP Avancé : Fusion de Tables et Analyse Complexe

## 📂 Préparation des données

Nous allons travailler avec deux fichiers CSV :

1. `villes.csv` : contient des informations sur les communes (nom, code postal, population).
2. `departements.csv` : contient les noms des départements et leur région d'appartenance.

Vous devez télécharger les deux fichiers suivants et les placer dans votre dossier de travail :

- [villes.csv](./tp_fusion/villes.csv){:download="villes.csv"} : contient des informations sur les communes (nom, code postal, population). Ce fichier contient volontairement des erreurs à filtrer.
- [departements.csv](./tp_fusion/departements.csv){:download="departements.csv"} : contient les noms des départements et leur région d'appartenance.

## 🛠️ Travail à réaliser

### Mission 1 : Nettoyage et Chargement
Écrivez une fonction `charger_villes(nom_fichier)` qui :

1. Charge les données.
2. **Filtre les erreurs** : Ignore les lignes où la population n'est pas un nombre ou est négative.
3. Retourne une liste de dictionnaires propres.

??? note "Solution :"

    ```python
    def charger_donnees(nom_fichier):
        donnees = []
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                try:
                    if int(ligne["population"]) > 0:
                        donnees.append(dict(ligne))
                except ValueError:
                    pass
        return donnees
    ```

### Mission 2 : La Fusion (Jointure "Inner Join")
L'objectif est de créer une nouvelle table `villes_enrichies`.

**Contrainte :** Si une ville possède un `code_dep` qui n'existe pas dans votre fichier `departements.csv`, elle ne doit pas apparaître dans le résultat final (c'est ce qu'on appelle une jointure interne).

```python
def fusionner_tables(villes, departements):
    # À COMPLÉTER
    pass
```
    
### Mission 3 : Statistiques Avancées
En utilisant la table fusionnée, implémentez les fonctions suivantes :

1. `stats_par_region(table)` : Retourne un dictionnaire dont les clés sont les régions et les valeurs sont la **somme des populations**.
2. `moyenne_regionale(table)` : Calcule la population moyenne des villes par région.
3. `densite_relative(table)` : Pour chaque ville, calculez le pourcentage de la population qu'elle représente par rapport à sa région. Ajoutez cette information (`pourcent_region`) dans le dictionnaire de la ville.

### Mission 4 : Visualisation ASCII (Régions)
Créez une fonction `afficher_graphique_regions(stats_region)` qui affiche un petit histogramme textuel dans la console pour comparer les régions.

**Exemple de rendu attendu :**
```text
Île-de-France          : #################### (2161000)
Occitanie              : ####### (749580)
Grand Est              : #### (461346)
...
```
*(Indice : Une `#` peut représenter 100 000 habitants)*

### Mission 5 : Top 10 des Villes
Créez une fonction `afficher_top_villes(table, n=10)` qui :
1. Trie les villes par population décroissante.
2. Affiche un histogramme ASCII pour les **n** premières villes.

**Contrainte :** Comme les populations des villes sont plus petites que celles des régions, adaptez l'échelle (par exemple : une `#` pour 10 000 habitants).

### Mission 6 : Interface de recherche
Proposez un petit menu permettant de :

1. Chercher une ville par son nom et afficher TOUTES ses infos (département et région compris).
2. Lister tous les départements d'une région donnée.

## 🚀 Le Défi de l'Expert : Optimisation Dictionnarique
Actuellement, votre fonction `fusionner_tables` contient probablement une boucle dans une boucle.

**Défi :** Transformez d'abord la liste des départements en un **dictionnaire** où la clé est le `code_dep`. Utilisez ensuite ce dictionnaire pour faire la fusion en un seul parcours de la liste des villes.


## 💡 Pistes d'optimisation
Pour la recherche du département (Mission 2), parcourir toute la table des départements pour chaque ville peut être lent si les fichiers sont gros.

**Défi :** Comment utiliser un **dictionnaire de recherche** pour rendre la fusion instantanée ?

