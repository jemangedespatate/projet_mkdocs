---
marp: true
theme: default
paginate: true
backgroundColor: #0f1117
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Fira+Code&display=swap');

  section {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    color: #e2e8f0;
    font-size: 22px;
    padding: 50px 60px;
    background: #0f1117;
  }

  section.title-slide {
    background: linear-gradient(135deg, #0f1117 0%, #1a1f2e 50%, #0f1117 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  section.title-slide h1 {
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    border: none;
    margin-bottom: 10px;
  }

  section.title-slide p {
    font-size: 1.1em;
    color: #94a3b8;
    margin-top: 10px;
  }

  section.title-slide .badge {
    display: inline-block;
    background: rgba(56,189,248,0.15);
    border: 1px solid #38bdf8;
    color: #38bdf8;
    border-radius: 30px;
    padding: 6px 20px;
    font-size: 0.85em;
    font-weight: 600;
    margin-top: 30px;
  }

  section.chapter-slide {
    background: linear-gradient(135deg, #1e1b4b, #0f1117);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  section.chapter-slide h1 {
    font-size: 2.5em;
    font-weight: 900;
    color: #818cf8;
    border: none;
    text-align: center;
  }

  section.chapter-slide .emoji {
    font-size: 4em;
    margin-bottom: 20px;
  }

  section.chapter-slide p {
    color: #94a3b8;
    font-size: 1em;
  }

  h1 {
    font-size: 1.8em;
    font-weight: 700;
    color: #38bdf8;
    border-bottom: 3px solid #38bdf8;
    padding-bottom: 12px;
    margin-bottom: 25px;
  }

  h2 {
    font-size: 1.3em;
    font-weight: 600;
    color: #818cf8;
    border-left: 5px solid #818cf8;
    padding-left: 15px;
    margin-top: 25px;
    margin-bottom: 15px;
  }

  h3 {
    font-size: 1.1em;
    color: #f472b6;
    font-weight: 600;
  }

  ul {
    margin-top: 10px;
    padding-left: 20px;
  }

  li {
    margin-bottom: 8px;
    line-height: 1.5;
  }

  .box-blue {
    background: rgba(56,189,248,0.1);
    border: 1px solid #38bdf8;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 15px 0;
  }

  .box-purple {
    background: rgba(129,140,248,0.1);
    border: 1px solid #818cf8;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 15px 0;
  }

  .box-pink {
    background: rgba(244,114,182,0.1);
    border: 1px solid #f472b6;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 15px 0;
  }

  .box-green {
    background: rgba(52,211,153,0.1);
    border: 1px solid #34d399;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 15px 0;
  }

  .box-yellow {
    background: rgba(251,191,36,0.1);
    border: 1px solid #fbbf24;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 15px 0;
  }

  .box-red {
    background: rgba(248,113,113,0.1);
    border: 2px solid #f87171;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 15px 0;
  }

  .timer {
    display: inline-block;
    background: #fbbf24;
    color: #0f1117;
    border-radius: 20px;
    padding: 4px 14px;
    font-weight: 700;
    font-size: 0.8em;
  }

  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 15px;
  }

  .easy  { color: #34d399; font-weight: 700; }
  .medium { color: #fbbf24; font-weight: 700; }
  .hard  { color: #f87171; font-weight: 700; }

  .fiche {
    background: #1e2233;
    border: 2px dashed #818cf8;
    border-radius: 15px;
    padding: 25px 30px;
    font-size: 0.9em;
    line-height: 2;
  }

  .fiche-title {
    color: #818cf8;
    font-weight: 700;
    font-size: 1.1em;
    border-bottom: 1px solid #818cf8;
    padding-bottom: 8px;
    margin-bottom: 12px;
  }

  .step {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    margin-bottom: 18px;
  }

  .step-num {
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    color: #0f1117;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 0.9em;
    flex-shrink: 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
    font-size: 0.9em;
  }

  th {
    background: rgba(56,189,248,0.2);
    color: #38bdf8;
    padding: 10px 15px;
    text-align: left;
    border-bottom: 2px solid #38bdf8;
  }

  td {
    padding: 10px 15px;
    border-bottom: 1px solid #1e2233;
    color: #cbd5e1;
  }

  tr:nth-child(even) td {
    background: rgba(255,255,255,0.03);
  }

  header, footer {
    font-size: 0.7em;
    color: #475569;
  }

  section::after {
    font-size: 0.7em;
    color: #475569;
  }
---

<!-- _class: title-slide -->

<div class="emoji">✍️</div>

# Grand Quiz NSI
## Phase 1 — Création des questions

<p>À vous de jouer : construisez les questions du quiz !</p>

<div class="badge">⏱️ Durée : 2 heures &nbsp;|&nbsp; NSI Première — 2025-2026</div>

---

# 🎯 Objectif de cette séance

<div class="box-blue">

Vous allez **créer les questions** qui serviront lors du quiz de révision de la séance suivante.

Chaque question que vous rédigez aujourd'hui sera posée à toute la classe lors du quiz.

</div>

<div class="box-yellow">

⚠️ **Soyez rigoureux !** Vos questions seront lues et évaluées devant tous vos camarades. Une question mal formulée ou une réponse incorrecte sera signalée.

</div>

---

# 📋 Les règles

<div class="step">
<div class="step-num">1</div>
<div>Chaque élève doit rédiger <strong>au minimum 3 questions par thème</strong>.</div>
</div>

<div class="step">
<div class="step-num">2</div>
<div>Chaque question doit respecter un <strong>niveau de difficulté</strong> précis : facile, moyen ou difficile.</div>
</div>

<div class="step">
<div class="step-num">3</div>
<div>Chaque question doit être complétée sur une <strong>fiche individuelle</strong> selon le modèle fourni.</div>
</div>

<div class="step">
<div class="step-num">4</div>
<div>À la fin de la séance, <strong>toutes les fiches sont remises</strong> au professeur.</div>
</div>

---

# 🎯 Les niveaux de difficulté

<div class="grid-2">
<div>

<div class="box-green">

### <span class="easy">🟢 Facile</span>

- Question de définition
- Question vrai / faux
- Identification simple d'un élément

*Exemple : « Qu'est-ce qu'une variable ? »*

</div>

<div class="box-yellow">

### <span class="medium">🟡 Moyen</span>

- Application d'une notion
- Lecture ou complétion de code
- Explication d'un mécanisme

*Exemple : « Que renvoie `[1,2,3][1:3]` ? »*

</div>

</div>
<div>

<div class="box-pink">

### <span class="hard">🔴 Difficile</span>

- Raisonnement algorithmique
- Analyse ou débogage
- Question de complexité ou de comparaison

*Exemple : « Combien de comparaisons pour une dichotomie sur 1024 éléments ? »*

</div>

</div>
</div>

---

# 📝 Modèle de fiche question

<div class="fiche">

<div class="fiche-title">📝 Fiche Question — à remplir pour chaque question</div>

**Prénom / Nom :** _______________________________

**Thème :** _______________________________

**Niveau :** &nbsp; <span class="easy">🟢 Facile</span> &nbsp; / &nbsp; <span class="medium">🟡 Moyen</span> &nbsp; / &nbsp; <span class="hard">🔴 Difficile</span>

**Question :** _______________________________

**Réponse correcte :** _______________________________

**Autres réponses possibles (optionnel) :** _______________________________

**Indice (optionnel) :** _______________________________

</div>

---

# 📊 Récapitulatif — Ce que vous devez produire

<table>
<thead>
<tr><th>Thème</th><th>Nombre minimum de questions</th><th>Niveaux attendus</th></tr>
</thead>
<tbody>
<tr><td>🐍 Le langage Python</td><td><strong>3 questions minimum</strong></td><td>Au moins un par niveau</td></tr>
<tr><td>🖥️ La machine</td><td><strong>3 questions minimum</strong></td><td>Au moins un par niveau</td></tr>
<tr><td>🔢 Les algorithmes</td><td><strong>3 questions minimum</strong></td><td>Au moins un par niveau</td></tr>
<tr><td>🌐 Web & Réseaux</td><td><strong>3 questions minimum</strong></td><td>Au moins un par niveau</td></tr>
<tr><td>💡 Informatique générale</td><td><strong>3 questions minimum</strong></td><td>Au moins un par niveau</td></tr>
</tbody>
</table>

<div class="box-red">

🔴 **Total minimum attendu : 15 questions par élève**

</div>

---

<!-- _class: chapter-slide -->

<div class="emoji">🐍</div>

# Thème 1
## Le Langage Python

---

# 🐍 Thème 1 — Le Langage Python

## Notions à couvrir

<div class="grid-2">
<div class="box-blue">

**Types de base**
- `int`, `float`, `str`, `bool`
- Conversions de types (`int()`, `str()`…)
- Opérations arithmétiques et logiques

**Variables & affectation**
- Nommage, portée
- Affectation simple et multiple

</div>
<div class="box-purple">

**Structures de données**
- Listes : `append`, `pop`, indexation, slicing
- Tuples : immuabilité
- Dictionnaires : accès par clé

**Traitement de données en table**
- Lecture de fichier CSV
- Filtrage et tri de tables

</div>
</div>

---

<!-- _class: chapter-slide -->

<div class="emoji">🖥️</div>

# Thème 2
## La Machine

---

# 🖥️ Thème 2 — La Machine

## Notions à couvrir

<div class="grid-2">
<div class="box-blue">

**Modèle de Von Neumann**
- Les 4 composants : UC, mémoire, entrées/sorties, bus
- Cycle d'exécution : Fetch → Decode → Execute
- Registres : PC, IR, ACC

</div>
<div class="box-purple">

**Langage Assembleur**
- Instructions : `MOV`, `LDR`, `STR`, `ADD`, `SUB`, `CMP`, `B`, `HALT`
- Notion de registre
- Lecture et interprétation de code assembleur

</div>
</div>

<div class="box-green">

**Système d'exploitation**
- Rôle du noyau, gestion des processus
- Notion de fichier, droits d'accès

</div>

---

<!-- _class: chapter-slide -->

<div class="emoji">🔢</div>

# Thème 3
## Les Algorithmes

---

# 🔢 Thème 3 — Les Algorithmes

## Notions à couvrir

<div class="grid-2">
<div class="box-blue">

**Algorithmes de tri**
- Tri par insertion
- Tri par sélection
- Complexité : O(n²)

</div>
<div class="box-purple">

**K Plus Proches Voisins (KNN)**
- Principe de classification
- Calcul de distance euclidienne
- Influence du choix de k

</div>
</div>

<div class="box-green">

**Recherche dichotomique**
- Prérequis : tableau trié
- Principe de division par 2
- Complexité : O(log n)

</div>

---

<!-- _class: chapter-slide -->

<div class="emoji">🌐</div>

# Thème 4
## Web & Réseaux

---

# 🌐 Thème 4 — Web & Réseaux

## Notions à couvrir

<div class="grid-2">
<div class="box-blue">

**HTML**
- Structure de base : `<html>`, `<head>`, `<body>`
- Balises courantes : titres, paragraphes, listes, liens, images
- Formulaires

**CSS**
- Sélecteurs, propriétés courantes
- Box model (margin, padding, border)

</div>
<div class="box-purple">

**JavaScript**
- Variables, conditions, boucles
- Manipulation du DOM
- Gestion d'événements

**Réseaux**
- Protocoles HTTP / HTTPS
- Notion d'adresse IP et de DNS
- Modèle client / serveur

</div>
</div>

---

<!-- _class: chapter-slide -->

<div class="emoji">💡</div>

# Thème 5
## Informatique Générale

---

# 💡 Thème 5 — Informatique Générale

## Notions à couvrir

<div class="grid-2">
<div class="box-blue">

**Intelligence Artificielle**
- Principe du Machine Learning
- Données d'entraînement
- Biais algorithmiques

**Histoire de l'informatique**
- Figures clés : Turing, Von Neumann, Ada Lovelace
- Grandes étapes de l'évolution des ordinateurs

</div>
<div class="box-purple">

**Chiffrement & Sécurité**
- Chiffrement symétrique et asymétrique
- Hachage, mots de passe
- Phishing, ingénierie sociale

**Bonnes pratiques**
- Licences logicielles (libre, propriétaire)
- Données personnelles et RGPD
- Impact environnemental du numérique

</div>
</div>

---

# ✅ Avant de rendre vos fiches

<div class="box-purple">

## Vérifiez pour chaque fiche :

<div class="step">
<div class="step-num">1</div>
<div>Votre <strong>nom</strong> est bien indiqué.</div>
</div>

<div class="step">
<div class="step-num">2</div>
<div>Le <strong>thème</strong> est correctement renseigné.</div>
</div>

<div class="step">
<div class="step-num">3</div>
<div>Le <strong>niveau de difficulté</strong> est précisé.</div>
</div>

<div class="step">
<div class="step-num">4</div>
<div>La <strong>réponse correcte</strong> est clairement indiquée.</div>
</div>

<div class="step">
<div class="step-num">5</div>
<div>La question est <strong>compréhensible</strong> par quelqu'un qui ne l'a pas rédigée.</div>
</div>

</div>

---

<!-- _class: title-slide -->

<div class="emoji">📬</div>

# Remise des fiches

<p>Déposez l'ensemble de vos fiches sur le bureau du professeur.</p>
<p>La séance de quiz aura lieu lors du prochain cours.</p>

<div class="badge">Merci pour votre travail !</div>