# <u>📝 Mini-projet : Snake et Listes en Python</u>

## <u>🎯 Objectif</u>

Nous allons programmer le célèbre **jeu Snake** en Python.

Le but est de guider un serpent pour qu'il mange des pommes. À chaque pomme mangée, le serpent grandit. Si le serpent touche un mur ou sa propre queue, la partie est perdue.

Ce projet a pour but principal de vous faire manipuler les **listes** en Python, car le corps du serpent est représenté par une liste de coordonnées.

Dans ce TP, vous compléterez les fonctions manquantes dans le fichier `logique.py`, tandis que l'interface graphique est déjà fournie dans `main.py`.

## <u>Organisation des fichiers 📂</u>

Pour que votre projet fonctionne correctement, vous devez placer tous les fichiers dans **un même répertoire** (dossier).

Les fichiers nécessaires sont :

- [logique.py](../snake_demo/logique.py){:download="logique.py"} : contient les fonctions que vous devez compléter.
- [main.py](../snake_demo/main.py){:download="main.py"} : l'interface graphique (ne pas modifier).
- [requirements.txt](../snake_demo/requirements.txt){:download="requirements.txt"} : les bibliothèques nécessaires.
- [console.py](../snake_demo/console.py){:download="console.py"} : contient les fonctions que vous devez compléter.


👉 Arborescence attendue :

```
mon_projet_snake/
│
├── logique.py
├── main.py
└── requirements.txt
```

## <u>1. Représentation du Serpent</u>

Le serpent est une **liste de tuples**. Chaque tuple `(x, y)` représente une case de la grille.
- Le premier élément de la liste (`index 0`) est la **tête** du serpent.
- Le dernier élément est le bout de la **queue**.

??? example "Exemple:"

    ```python
    serpent = [
        (10, 10),  # Tête
        (10, 11),  # Corps
        (10, 12)   # Queue
    ]
    ```

👉 **À vous d’écrire la fonction :**

```python
def creer_serpent()->list:
    """
    Crée la liste initiale représentant le serpent.
    Retour: list, une liste de tuples (x, y)
    """
```

## <u>2. Calculer la nouvelle tête</u>

Quand le serpent avance, on doit calculer la position de sa nouvelle tête en fonction de la direction.
La direction est donnée par un tuple `(dx, dy)`.

??? example "Exemple:"

    Si la tête est en `(10, 10)` et la direction est `(0, -1)` (haut) :
    La nouvelle tête sera `(10 + 0, 10 - 1) = (10, 9)`.

👉 **Complétez la fonction :**

```python
def calculer_nouvelle_tete(serpent:list, direction:tuple)->tuple:
    """
    Calcule la position de la nouvelle tête du serpent.
    
    Paramètres: serpent, la liste du serpent
                direction, le tuple (dx, dy)
    Retour:     tuple, la nouvelle position (x, y)
    """
```

## <u>3. Faire avancer le serpent (Insertion)</u>

Pour faire avancer le serpent, on ajoute la nouvelle tête au début de la liste.
Quelle méthode de liste permet d'ajouter un élément à une position précise (ici l'index 0) ?

👉 **Complétez la fonction :**

```python
def inserer_tete(serpent:list, nouvelle_tete:tuple)->None:
    """
    Insère la nouvelle tête au début de la liste du serpent.
    La modification se fait en place (pas de retour).
    """
```

## <u>4. Gérer la queue (Suppression)</u>

Si le serpent ne mange pas de pomme, il doit garder la même taille. Comme on a ajouté une tête, il faut supprimer le dernier élément de la queue.

👉 **Complétez la fonction :**

```python
def supprimer_queue(serpent:list)->None:
    """
    Supprime le dernier élément de la liste du serpent.
    La modification se fait en place.
    """
```

## <u>5. Vérifier les collisions 💥</u>

Le jeu s'arrête si :
1.  La tête sort de la grille (coordonnées < 0 ou >= taille).
2.  La tête touche une autre partie du corps du serpent.

👉 **Complétez la fonction :**

```python
def verifier_collision(serpent:list, largeur_grille:int, hauteur_grille:int)->bool:
    """
    Vérifie si la tête du serpent (serpent[0]) est en collision.
    Retour: True si collision, False sinon.
    """
```

## <u>6. Lancer le jeu 🎮</u>

Une fois vos fonctions complétées, lancez le fichier `main.py` pour tester votre jeu !

```bash
python main.py
```

Si tout fonctionne, vous verrez votre serpent bouger et la liste se mettre à jour en temps réel sur le côté de l'écran.

👉 **Question :** Observez la liste affichée à droite pendant que vous jouez. Que se passe-t-il dans la liste quand vous mangez une pomme ?

## <u>7. Bonus : Interface Console / Texte 📟</u>

Pour bien comprendre que **la logique du jeu (les listes)** est indépendante de **l'interface graphique**, nous allons créer un affichage simple dans la console.

Ouvrez le fichier `console.py`. Vous y trouverez une structure de jeu alternative qui utilise les **mêmes fonctions** de `logique.py` !

👉 **Votre mission :**

1.  Complétez la fonction `afficher_grille(serpent, pomme, largeur, hauteur)` pour dessiner le jeu avec des caractères :
    *   `O` pour la tête
    *   `o` pour le corps
    *   `X` pour la pomme
    *   `.` pour le vide
2.  Complétez `demander_direction()` pour gérer les touches `z, q, s, d`.
3.  (Optionnel) Intégrez la gestion de la collision et de la pomme (copiez la logique du `main.py`).

Lancez le jeu avec :
```bash
python console.py
```
