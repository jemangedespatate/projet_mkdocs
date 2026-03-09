---
marp: true
theme: default
paginate: true
backgroundColor: #fff
footer: "NSI Premiere - Introduction à l'IA"
---

# 🤖 Introduction à l'Intelligence Artificielle (IA)

**Thème :** Culture Numérique & Algorithmique  
**Niveau :** Première NSI  
**Objectif :** Comprendre les bases, le fonctionnement et les enjeux de l'IA.

---

## 📅 Au programme
1.  **Un peu d'histoire** : D'où vient l'IA ?
2.  **Comment ça marche ?** : La magie derrière le code.
3.  **Les données** : Le carburant de l'IA.
4.  **Critiques et Enjeux** : Faut-il avoir peur du robot ?

---

# 1. 📜 Un peu d'histoire

> **Question de réflexion :**  
> À votre avis, depuis quelle décennie parle-t-on d'Intelligence Artificielle ?  
> (1950, 1980, 2010 ?)

---

## Les grandes étapes
- **1950 : Alan Turing** pose la question : "Les machines peuvent-elles penser ?" et invente le *Test de Turing*.
- **1956 : Conférence de Dartmouth**, naissance officielle du terme "Intelligence Artificielle".
- **1997 : Deep Blue** (IBM) bat Garry Kasparov aux échecs.
- **2016 : AlphaGo** bat Lee Sedol au jeu de Go.
- **2022 : ChatGPT** (OpenAI) démocratise l'IA générative.

> **Question :** Pourquoi a-t-on attendu 70 ans pour que l'IA explose vraiment ?

---

# 2. 🧠 Comment ça marche ?

> **Question de réflexion :**  
> Quelle est la différence entre un programme "classique" et une IA ?

---

## Programmation classique vs Machine Learning
- **Classique** : On donne des **règles** précises à l'ordinateur. 
  *(Ex: "Si le ciel est gris, alors il va pleuvoir")*
- **IA (Machine Learning)** : On donne des **exemples** à l'ordinateur et il trouve les règles tout seul.
  *(Ex: On lui montre 10 000 photos de pluie et il apprend à la reconnaître)*

---

## Le neurone artificiel (Simplifié)
Une IA moderne utilise des **réseaux de neurones**.
1. Elle reçoit des entrées (pixels, mots).
2. Elle applique des "poids" (importance) à ces entrées.
3. Elle produit une prédiction (99% de chance que ce soit un chat).

> **Question :** Que se passe-t-il si on montre une photo de chien à une IA qui n'a vu que des chats ?

---

# 3. 📊 Les Données : Le carburant

> **Question de réflexion :**  
> "L'IA est une éponge." À votre avis, d'où viennent les informations que contient ChatGPT ?

---

## D'où viennent les données ?
Pour apprendre, une IA a besoin de milliards d'exemples. Elles sont extraites de :
- **Le Web** (Wikipedia, journaux, forums locaux).
- **Les Livres** numérisés.
- **Le code informatique** (GitHub).
- **Vos interactions** (quand vous corrigez une IA, elle apprend !).

> **Question :** Si l'IA apprend sur Internet, risque-t-elle d'apprendre des mensonges ou des insultes ?

---

# 4. ⚖️ Critiques et Limites

> **Question de réflexion :**  
> Est-ce que l'IA "comprend" vraiment ce qu'elle dit, ou est-ce juste une calculatrice géante ?

---

## Les points noirs de l'IA
1. **Les Biais** : Si les données sont sexistes ou racistes, l'IA le sera aussi.
2. **L'Énergie** : Entraîner une IA consomme énormément d'électricité et d'eau (refroidissement des serveurs).
3. **Le Copyright** : L'IA utilise des œuvres d'artistes sans toujours les payer.
4. **Les Hallucinations** : L'IA peut affirmer une bêtise avec une assurance totale.

---

## 🚦 Conclusion
L'IA est un **outil puissant** mais ce n'est pas une "intelligence" au sens humain. C'est un moteur de probabilités.

> **Dernière question :** À votre avis, quel métier ne pourra JAMAIS être remplacé par une IA ?

---

# 🛠️ Activité Débranchée : L'Atelier des Neurones

**Objectif** : Comprendre comment une IA "apprend" en ajustant l'importance des informations (les poids).

**Rôles :**
1. **La Machine** (1 élève) : Dos au tableau, doit deviner si l'objet est un "Fruit" ou un "Légume".
2. **Les Neurones** (3-4 élèves) : Observent l'image d'un objet et donnent une note de 0 à 10 pour un critère précis :
   - Neurone 1 : "C'est sucré ?"
   - Neurone 2 : "C'est croquant ?"
   - Neurone 3 : "Ça pousse dans un arbre ?"

---

## 🛠️ Le fonctionnement (Atelier débranché)

**Étape 1 : Le test**
La Machine écoute les notes et annonce sa décision (ex: "C'est un fruit !").

**Étape 2 : L'ajustement (L'Apprentissage)**
Si la Machine se trompe :
- On demande : "Quel neurone nous a induit en erreur ?"
- On décide de donner **moins d'importance** (moins de poids) à ce critère la prochaine fois.

**C'est exactement ça, l'entraînement d'une IA !**
On répète cela des millions de fois jusqu'à ce que les "poids" soient parfaits.
