---
marp: true
theme: default
paginate: true
backgroundColor: #0f172a
color: #e2e8f0
style: |
  section {
    font-family: 'Inter', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 60px;
    background: radial-gradient(circle at top left, #1e293b, #0f172a);
  }
  h1 {
    color: #38bdf8;
    font-size: 2.2em;
    border-bottom: 2px solid #38bdf8;
    padding-bottom: 10px;
    margin-bottom: 40px;
    text-transform: uppercase;
    letter-spacing: 2px;
  }
  h2 {
    color: #818cf8;
    font-size: 1.6em;
  }
  code {
    background: #1e293b;
    color: #fca5a5;
    border-radius: 4px;
    padding: 2px 6px;
  }
  pre {
    background: #111827 !important;
    border: 1px solid #334155;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
  }
  ul {
    margin-top: 20px;
  }
  li {
    margin-bottom: 15px;
  }
  .highlight {
    color: #facc15;
    font-weight: bold;
  }
  footer {
    color: #64748b;
  }
---

# L'Architecture de Von Neumann
## Partie 1 : Modélisation & Principes 🏗️

---

# 🕰️ Alan Turing : L'Origine Théorique

![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/7/79/Alan_Turing_az_1930-as_%C3%A9vekben.jpg)

Avant la construction physique, il y a eu la théorie. 
- **1936** : Alan Turing imagine une machine capable de réaliser n'importe quel calcul si on lui donne les bonnes instructions.
- C'est le concept de **Machine Universelle**.

---

# 🔌 Le Problème des Débuts

![bg left:45% 80%](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Glen_Beck_and_Betty_Snyder_program_the_ENIAC_in_building_328_at_the_Ballistic_Research_Laboratory.jpg/1280px-Glen_Beck_and_Betty_Snyder_program_the_ENIAC_in_building_328_at_the_Ballistic_Research_Laboratory.jpg)

- Les premiers ordinateurs étaient "figés".
- Pour changer de programme, il fallait manipuler des milliers de câbles et d'interrupteurs.
- **La machine et le programme ne faisaient qu'un.** C'était extrêmement long et complexe !

---

# ✍️ La Solution de Von Neumann

![bg right:40% 70%](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/JohnvonNeumann-LosAlamos.jpg/960px-JohnvonNeumann-LosAlamos.jpg)

- **1945** : John Von Neumann propose une idée qui va tout changer.
- **Le concept** : On n'a plus besoin de toucher aux câbles !
- Les instructions sont stockées **en mémoire**, exactement comme des nombres. 
- Pour changer de programme, il suffit de charger un nouveau fichier en mémoire.

---

# 💾 Un mot sur la Mémoire 📦

![bg left:40% 90%](https://upload.wikimedia.org/wikipedia/commons/d/df/Ferrite_core_memory.jpg)

- Au début, stocker des données était complexe !
- **Mémoire à tores de ferrite** (photo) : De petits anneaux magnétiques traversés par des fils.
- Chaque anneau stockait **1 bit**.
- 1 Mo de RAM aurait pris la taille d'une salle entière !

---

# 🏗️ Le Modèle de Von Neumann

Donnez les different composant d'un ordianteur

---

# 🏗️ Le Modèle de Von Neumann

Lesquels sont essentiels ?

---

# 🏗️ Le Modèle de Von Neumann

Un ordinateur moderne repose sur 4 piliers fondamentaux :

1.  **L'Unité Centrale de Traitement (CPU)** : Le "cerveau" de la machine.
2.  **La Mémoire Vive (RAM)** : L'espace de stockage temporaire (instructions + données).
3.  **Les Entrées / Sorties (I/O)** : Interface avec le monde (clavier, écran, disque).
4.  **Les Bus** : Les canaux de communication qui relient tout ce beau monde.

---

# 🧠 Le Cœur : Le CPU

![bg left:40% 90%](https://cours-informatique-gratuit.fr/wp-content/uploads/2014/05/processeur-intel.jpg)

Il est divisé en deux parties essentielles :

### 1. L'Unité Arithmétique et Logique (ALU)
Elle réalise tous les calculs mathématiques (`+`, `-`, `*`) et les opérations logiques (`ET`, `OU`, `NON`).

### 2. L'Unité de Contrôle (CU)
C'est le chef d'orchestre : elle lit l'instruction en mémoire, la décode et donne les ordres aux autres composants.

---

# 💾 Mémoire & Registres

![bg right:45% 90%](https://infomaxparis.com/img/cms/Blog/image-ram-4-stick2.jpg)

*   **La Mémoire (RAM)** : Grande capacité, mais située à l'extérieur du CPU. C'est le plan de travail où l'ordinateur pose ses dossiers.

---

# 💾 Mémoire & Registres

![bg right:45% 90%](https://infomaxparis.com/img/cms/Blog/image-ram-4-stick2.jpg)

*   **Les Registres** : Zones de stockage ultra-rapides situées *directement* dans le CPU.
    *   **PC (Program Counter)** : Maintient l'adresse de la prochaine instruction.
    *   **Accumulateur** : Stocke le résultat immédiat d'un calcul.

---

# 🔄 Le Cycle CPU

C'est ce que fait votre ordinateur des milliards de fois par seconde !

1.  **FETCH (Recherche)** : Aller chercher l'instruction stockée à l'adresse indiquée par le `PC` dans la RAM.
2.  **DECODE (Décodage)** : L'unité de contrôle traduit l'instruction binaire en opération compréhensible par le matériel.
3.  **EXECUTE (Exécution)** : L'ALU fait le calcul et le résultat est rangé dans un registre ou en RAM.
4.  **RE-PC** : Incrémenter le `PC` pour passer à l'instruction suivante.

---

# 🏗️ Le Modèle de Von Neumann

Associer chaque composant à son rôle :

- **L'Unité Centrale de Traitement** : Travaille et calcule (Cerveau).
- **La Mémoire Vive** : Stocke temporairement (Plan de travail).
- **Les Entrées / Sorties** : Communique (Interfaces).
- **Les Bus** : Transporte (Autoroutes).

---

# ❓ Mais comment parle-t-on à cette machine ?

- On a vu que le CPU exécute des instructions binaires (`0` et `1`).
- **Problème** : Un humain a beaucoup de mal à lire ou écrire des millions de `0` et de `1` sans faire d'erreur.
- **Solution** : On a créé des "couches" d'abstraction pour faciliter la communication.

---

# 📊 Les Niveaux de Langage

Du plus proche de l'humain au plus proche du silicium :

| Niveau | Nom | Exemple | Description |
| :---: | :--- | :--- | :--- |
| **3** | Haut Niveau | `score = 10 + 5` | Lisible comme de l'anglais.|
| **2** | **Assembleur** | `ADD R0, #10, #5` | Traduction directe du binaire en mots. |
| **1** | Machine | `1110 0010 ...` | La seule langue que parle le CPU. |

---

# 🏁 Quiz de Récapitulation

### Testons vos connaissances ! 🧠

---

# ❓ Question 1

**Avant Von Neumann, si on voulait changer de calcul, il fallait :**

A) Appuyer sur un bouton Reset.
B) Changer physiquement des câbles et des interrupteurs.
C) Taper une commande au clavier.

---

# ❓ Question 1

**Avant Von Neumann, si on voulait changer de calcul, il fallait :**

A) Appuyer sur un bouton Reset.
B) Changer physiquement des câbles et des interrupteurs.
C) Taper une commande au clavier.

> **Réponse B** : Il fallait littéralement "reconfigurer" la machine.

---

# ❓ Question 2

**Votre ordinateur doit réaliser une opération mathématique. Quel composant effectue le calcul ?**

A) L'Unité de Contrôle (CU).
B) L'Unité Arithmétique et Logique (ALU).
C) La Mémoire Vive (RAM).

---

# ❓ Question 2

**Votre ordinateur doit réaliser une opération mathématique. Quel composant effectue le calcul ?**

- A) L'Unité de Contrôle (CU).
- B) L'Unité Arithmétique et Logique (ALU).
- C) La Mémoire Vive (RAM).

> **Réponse B** : L'ALU (Arithmetic Logic Unit).

---

# ❓ Question 3

**Quel est l'endroit le plus rapide pour stocker une donnée pendant un calcul ?**

A) La RAM.
B) Le Disque Dur (SSD).
C) Un Registre.

---

# ❓ Question 3

**Quel est l'endroit le plus rapide pour stocker une donnée pendant un calcul ?**

- A) La RAM.
- B) Le Disque Dur (SSD).
- C) Un Registre.

> **Réponse C** : Les registres sont intégrés au CPU.

---

# ❓ Question 4

**Quelle est la seule langue que le processeur comprend réellement ?**

A) Le Python.
B) L'Assembleur.
C) Le Langage Machine (Binaire).

---

# ❓ Question 4

**Quelle est la seule langue que le processeur comprend réellement ?**

- A) Le Python.
- B) L'Assembleur.
- C) Le Langage Machine (Binaire).

> **Réponse C** : Tout le reste doit être traduit en binaire.

