# Projet : Création d'un Jeu avec Interface Graphique

Maintenant que vous avez compris comment fonctionne une Interface Homme-Machine (IHM) avec `tkinter` au travers du TP *Space Invader*, c'est à vous de jouer !

## 🎯 L'objectif

Vous devez concevoir et programmer, seul ou par groupe de deux, un mini-jeu de votre choix utilisant une interface graphique (`tkinter`, ou éventuellement `pygame` si vous le maitrisez et avez l'accord de votre professeur).

Ce projet a pour but de valider vos compétences en :
* **Programmation événementielle** : réagir aux actions de l'utilisateur (clics de souris, touches clavier).
* **Boucles de jeu et animation** : mettre à jour un affichage graphique de façon fluide.
* **Gestion des structures de données** : manipuler des listes, des dictionnaires pour stocker les objets (ennemis, scores, obstacles).

---

## 🛠️ Critères de réussite

Votre projet devra obligatoirement contenir :
1. **Une fenêtre graphique** correctement dimensionnée, avec un titre cohérent.
2. **Des éléments graphiques variés** (utilisation d'images chargées avec `PhotoImage` ou de formes géométriques via `create_rectangle`, `create_oval`, `create_text`, etc.).
3. **De l'interactivité** : le jeu réagit pertinemment aux contrôles (clavier ou clics).
4. **Une boucle d'animation** (utilisation de `after()`) qui assure l'évolution du jeu en temps réel.
5. **Des conditions de fin de jeu** : un moyen de gagner (Victoire), de perdre (Game Over) et un suivi de la partie (chronomètre, vies, score...).

---

## 💡 Idées de projets (et niveaux de difficulté)

Voici quelques exemples de jeux classiques réalisables en Tkinter, classés par niveau de difficulté pour vous aider à choisir.

### 🟢 Niveau Facile (Pour bien démarrer)

* **Clicker Game** : Une cible (image ou cercle) se déplace aléatoirement ou apparaît brièvement à l'écran. Le joueur doit cliquer dessus le plus de fois possible en 30 secondes pour faire un "High Score".
* **Jeu du Pendu Graphique** : L'interface affiche le mot à deviner avec des tirets, des lettres cliquables (ou au clavier). À chaque erreur, un élément du dessin du pendu est tracé dans le Canvas.
* **Pierre-Feuille-Ciseaux (Amélioré)** : Interface avec 3 beaux boutons. Le joueur choisit, l'ordinateur génère son choix aléatoirement. Une animation (ou images) affiche les mains et le score se met à jour.

### 🟡 Niveau Intermédiaire (Un beau défi)

* **Pong** : Deux raquettes (contrôlables au clavier de chaque côté pour 2 joueurs) et une balle qui se déplace en rebondissant. Il faut gérer les rebonds sur les bords et sur les raquettes.
* **Morpion (Tic-Tac-Toe)** : Une grille de 3x3 (lignes dessinées ou boutons). Chaque clic place une croix ou un rond. Le programme doit vérifier l'alignement pour déclarer le vainqueur.
* **Casse-briques (Breakout)** : Une raquette en bas, une balle et un mur de briques en haut. Destruction des briques quand la balle les touche.

### 🔴 Niveau Difficile (Pour les experts)

* **Snake (Le Serpent)** : Le joueur dirige un serpent (une liste de rectangles) qui s'allonge chaque fois qu'il "mange" une pomme (un rectangle aléatoire). Si le serpent touche un bord ou se touche lui-même, c'est perdu.
* **Flappy Bird** : Un oiseau (image) subit une gravité permanente (il tombe). Un appui sur *Espace* le fait sauter vers le haut. Il doit passer entre des tuyaux qui défilent en permanence de droite à gauche.
* **Pac-Man (Simplifié)** : Un labyrinthe fixe, un personnage qui se déplace pour manger des pièces jaunes, en évitant un ennemi dont le déplacement est aléatoire (ou qui suit le joueur).

---

## 📅 Organisation et Rendu

1. **Phase 1 : Conception sur papier (Cahier des charges)**
   - Dessinez l'interface de votre jeu (comment seront l'écran de jeu, les menus, le score ?).
   - Listez les variables indispensables dont vous aurez besoin au départ (ex: `score = 0`, `vitesse_balle = 5`, `vies = 3`).
   - Identifiez les fonctions principales (ex: `deplacer_balle()`, `clic_souris(event)`).

2. **Phase 2 : Développement progressif**
   - **Important :** Procédez par étapes, tout comme dans le TP Space Invader !
   - Ne commencez jamais par l'animation globale, commencez par faire afficher votre fond, puis votre personnage, puis faites-le bouger, etc.
   - Testez votre programme à chaque petite étape.

3. **Phase 3 : Améliorations esthétiques (Bonus)**
   - Changez les couleurs, trouvez des images en ligne (sans fond, format PNG) pour rendre votre jeu plus beau.

*Bon courage, l'essentiel est de coder un jeu qui vous plaît !*
