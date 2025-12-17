# 🎄 DM de Vacances : Gestionnaire d'Inventaire RPG (Dictionnaires)

## 🎯 Objectif

Pendant ces vacances, nous allons créer le **cerveau** d'une application de gestion d'inventaire pour un jeu vidéo type RPG (Role Playing Game).

Dans un jeu, l'inventaire est souvent ce qui permet au joueur de voir ce qu'il possède (potions, armes, nourriture) et en quelle quantité. 
La structure de données idéale pour cela est le **dictionnaire Python** !

Dans ce DM, vous compléterez les fonctions manquantes dans le fichier `logique.py`. Une interface graphique complète (`interface.py`) vous est fournie pour tester votre code de manière visuelle et ludique.

## Organisation des fichiers 📂

Pour que votre projet fonctionne correctement, vous devez placer tous les fichiers dans **un même répertoire** (dossier).

Les fichiers nécessaires sont :

- [logique.py](../dm_vacances/logique.py){:download="logique.py"} : contient les fonctions de gestion du dictionnaire que vous devez compléter.
- [interface.py](../dm_vacances/interface.py){:download="interface.py"} : l'interface graphique (ne pas modifier).

👉 Arborescence attendue :

```
mon_dm_rpg/
│
├── logique.py   <-- C'est ici que tu codes !
└── interface.py <-- Touche pas à ça p'tit con (sauf si tu es curieux)
```

---

## 1. Structure de l'Inventaire

L'inventaire est représenté par un **dictionnaire Python**.
- Les **CLÉS** sont les noms des objets (des chaînes de caractères `str`).
- Les **VALEURS** sont les quantités possédées (des entiers `int`).

??? example "Exemple d'inventaire initial :"

    ```python
    sac_a_dos = {
        "Potion de vie": 5,
        "Épée rouillée": 1,
        "Pain elfique": 10
    }
    ```

👉 **À vous d’écrire la fonction :**

```python
def creer_inventaire():
    """
    Initialise l'inventaire de départ.
    Retourne un dictionnaire contenant quelques objets de base.
    """
```

---

## 2. Ajouter un objet (Gestion des Clés)

Quand le joueur ramasse un objet, deux cas se présentent :
1.  L'objet est **déjà dans le sac** : on augmente simplement sa quantité.
2.  L'objet est **nouveau** : on doit créer une nouvelle entrée (clé) dans le dictionnaire.

C'est LE point fort des dictionnaires : l'accès direct par clé.

👉 **Complétez la fonction :**

```python
def ajouter_objet(inventaire, nom, quantite):
    """
    Ajoute une quantité d'un objet à l'inventaire.
    - Si l'objet existe déjà, augmenter sa quantité.
    - Si l'objet n'existe pas, le créer avec cette quantité.
    """
```

---

## 3. Retirer un objet (Gestion des suppressions)

Quand le joueur utilise une potion ou jette un objet, la quantité diminue.
Mais attention : si la quantité atteint **0**, l'objet ne doit plus encombrer l'affichage. Il faut **supprimer la clé** du dictionnaire.

Rappel : `del dictionnaire[cle]` ou `dictionnaire.pop(cle)` permettent de supprimer une entrée.

👉 **Complétez la fonction :**

```python
def retirer_objet(inventaire, nom, quantite):
    """
    Retire des objets de l'inventaire.
    - Décrémente la quantité.
    - Si la quantité <= 0, supprime complètement la clé du dictionnaire.
    """
```

---

## 4. Afficher le contenu (Parcours)

Pour que l'interface graphique puisse afficher la liste des objets, elle a besoin d'une liste de textes formatés.
Vous devez parcourir le dictionnaire pour transformer chaque paire `(clé, valeur)` en une phrase lisible.

Format attendu : `"Nom de l'objet : Quantité"` (Exemple : `"Potion : 5"`)

👉 **Complétez la fonction :**

```python
def lister_objets(inventaire):
    """
    Dresse la liste des objets pour l'affichage.
    Doit retourner une LISTE de chaînes de caractères.
    Exemple: ["Potion : 5", "Épée : 1"]
    """
```

---

## 5. Lancer le projet 🎮

Une fois vos fonctions complétées dans `logique.py` :

1.  Testez d'abord vos fonctions en exécutant directement `logique.py` (regardez le bloc `if __name__ == "__main__":` tout en bas du fichier).
2.  Si tout semble correct, lancez `interface.py` !

```bash
python interface.py
```

Si votre code est bon, vous pourrez ajouter et retirer des objets via les boutons, et voir la liste se mettre à jour magiquement !

Bon courage et bonnes vacances ! 🎄
