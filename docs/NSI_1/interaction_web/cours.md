# 🌟 Découverte du Web : créer sa première page internet

## 🎯 Introduction

Avez-vous déjà voulu créer votre propre site web ? Bonne nouvelle : **c'est plus simple que vous ne le pensez !**

Quand vous visitez un site web (YouTube, Instagram, un site de jeux...), votre navigateur affiche une **page web**. Cette page est créée avec trois technologies simples que nous allons découvrir ensemble.

---

## 1. 🏗️ Les trois ingrédients d'une page web

Pour créer une page web, on utilise **trois langages** qui travaillent ensemble. Imaginez que vous construisez une maison :

| Langage | Rôle | C'est comme... |
|---------|------|----------------|
| **HTML** | Le contenu | Les murs et les pièces de la maison |
| **CSS** | Le style | La peinture et la décoration |
| **JavaScript** | L'interactivité | L'électricité et les interrupteurs |

---

### 1.1 📝 HTML : le contenu de la page

#### Qu'est-ce que c'est ?

HTML signifie "HyperText Markup Language" (langage de balisage). C'est le langage qui dit au navigateur **quoi afficher** sur la page.

#### Comment ça marche ?

HTML utilise des **balises** (tags en anglais). Une balise ressemble à ceci : `<balise>contenu</balise>`

**Exemple simple :**
```html
<h1>Bonjour !</h1>
```
Cette ligne affiche un grand titre avec le texte "Bonjour !"

??? Example "Exemple de code HTML :"

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Ma première page</title>
    </head>
    <body>
        <h1>Bienvenue sur mon site</h1>
        <p>Ceci est un paragraphe de texte.</p>
        <img src="photo.jpg" alt="Une photo">
        <a href="https://www.exemple.com">Cliquez ici</a>
    </body>
    </html>
    ```

---

#### 📋 Balises principales

| Balise | Signification | Utilisation |
|--------|---------------|-------------|
| `<h1>` à `<h6>` | Titres | Hiérarchie des titres (h1 = plus important) |
| `<p>` | Paragraphe | Bloc de texte |
| `<a>` | Lien | Créer un lien hypertexte |
| `<img>` | Image | Afficher une image |
| `<div>` | Division | Conteneur générique |
| `<span>` | Span | Conteneur en ligne |
| `<ul>`, `<ol>`, `<li>` | Listes | Listes à puces ou numérotées |
| `<button>` | Bouton | Bouton cliquable |
| `<input>` | Champ de saisie | Formulaire |

---

### 1.2 🎨 CSS (Cascading Style Sheets)

CSS est la **peau** de la page web. Il définit :

* Les couleurs, polices, tailles
* Les espacements, marges, bordures
* La disposition des éléments (layout)
* Les animations et transitions

👉 CSS permet de **séparer le contenu (HTML) de la présentation**. Un même HTML peut avoir plusieurs apparences différentes !

??? Example "Exemple de code CSS :"

    ```css
    /* Sélectionner tous les titres h1 */
    h1 {
        color: #2c3e50;
        font-size: 32px;
        text-align: center;
        font-family: Arial, sans-serif;
    }

    /* Sélectionner tous les paragraphes */
    p {
        color: #34495e;
        line-height: 1.6;
        margin: 20px;
    }

    /* Sélectionner un élément avec l'id "menu" */
    #menu {
        background-color: #3498db;
        padding: 10px;
    }

    /* Sélectionner tous les éléments avec la classe "bouton" */
    .bouton {
        background-color: #e74c3c;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    ```

??? Example "HTML associé à ce CSS :"

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Exemple CSS</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Mon titre principal</h1>
        
        <div id="menu">
            <p>Ceci est le menu avec un fond bleu</p>
        </div>
        
        <p>Ceci est un paragraphe normal avec une couleur et des marges.</p>
        
        <button class="bouton">Cliquez ici</button>
    </body>
    </html>
    ```
    
    **Résultat** : 
    
    - Le titre `<h1>` sera centré, en bleu foncé, taille 32px
    - Le `<div id="menu">` aura un fond bleu
    - Les paragraphes `<p>` auront une couleur grise et des marges de 20px
    - Le bouton avec `class="bouton"` sera rouge avec du texte blanc


---

#### 🔍 Les sélecteurs CSS

Les sélecteurs permettent de **cibler** les éléments HTML à styliser :

* **Sélecteur de balise** : `p { ... }` → affecte tous les `<p>`
* **Sélecteur de classe** : `.ma-classe { ... }` → affecte tous les éléments avec `class="ma-classe"`
* **Sélecteur d'ID** : `#mon-id { ... }` → affecte l'élément avec `id="mon-id"`

👉 Un ID est **unique** dans une page, une classe peut être **réutilisée** plusieurs fois.

---

#### 🎯 Propriétés CSS courantes

| Propriété | Effet | Exemple |
|-----------|-------|---------|
| `color` | Couleur du texte | `color: red;` |
| `background-color` | Couleur de fond | `background-color: #fff;` |
| `font-size` | Taille de police | `font-size: 16px;` |
| `margin` | Marge extérieure | `margin: 10px;` |
| `padding` | Marge intérieure | `padding: 20px;` |
| `border` | Bordure | `border: 1px solid black;` |
| `width` / `height` | Dimensions | `width: 300px;` |
| `display` | Type d'affichage | `display: flex;` |


---

### 1.3 ⚡ JavaScript

JavaScript est le **cerveau** de la page web. Il permet :

* De réagir aux actions de l'utilisateur (clics, saisies)
* De modifier le contenu de la page dynamiquement
* De communiquer avec des serveurs
* De créer des animations complexes

👉 JavaScript est un **langage de programmation** qui s'exécute dans le navigateur web.

??? Example "Exemple de code JavaScript :"

    ```javascript
    // Afficher un message dans la console
    console.log("Bonjour !");

    // Modifier le contenu d'un élément
    document.getElementById("titre").textContent = "Nouveau titre";

    // Réagir à un clic
    document.getElementById("monBouton").addEventListener("click", function() {
        alert("Vous avez cliqué sur le bouton !");
    });

    // Modifier le style d'un élément
    document.querySelector(".ma-classe").style.color = "red";
    ```

---

#### 💡 Concepts de base en JavaScript

* **Variables** : `let nom = "Alice";` ou `const age = 15;`
* **Fonctions** : `function direBonjour() { alert("Bonjour !"); }`
* **Événements** : `click`, `mouseover`, `keypress`, etc.
* **DOM (Document Object Model)** : représentation de la page que JavaScript peut manipuler

---

## 2. 🖱️ Interaction avec l'utilisateur dans une page Web

### 2.1 🔄 Le modèle événementiel

Les pages web modernes fonctionnent selon un **modèle événementiel** :

1. L'utilisateur effectue une action (clic, saisie, mouvement de souris)
2. Cette action génère un **événement**
3. JavaScript peut **écouter** cet événement
4. Quand l'événement se produit, une **fonction** est exécutée

---

#### ⚡ Événements courants

| Événement | Déclenchement |
|-----------|---------------|
| `click` | Clic sur un élément |
| `dblclick` | Double-clic |
| `mouseover` | Survol avec la souris |
| `mouseout` | Sortie de la souris |
| `keydown` | Touche enfoncée |
| `keyup` | Touche relâchée |
| `submit` | Soumission d'un formulaire |
| `change` | Modification d'un champ |

---

### 2.2 💻 Exemple complet d'interaction

Voici un exemple très simple : un bouton qui affiche un message quand on clique dessus.

**1. Le fichier HTML (`index.html`) :**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemple simple</title>
</head>
<body>

    <!-- Le bouton -->
    <button id="monBouton">Cliquez-moi !</button>

    <!-- Lien vers le fichier JavaScript -->
    <script src="script.js"></script>

</body>
</html>
```

**2. Le fichier JavaScript (`script.js`) :**

```javascript
// On sélectionne le bouton
const bouton = document.getElementById("monBouton");

// On ajoute l'événement "click"
bouton.addEventListener("click", function() {
    alert("Bravo ! Vous avez réussi votre première interaction !");
});
```

**Explication étape par étape :**

1. Dans le HTML, on crée un bouton avec `<button id="monBouton">`.
2. On lie le fichier JavaScript avec `<script src="script.js"></script>`.
3. Dans le fichier JS, on récupère ce bouton grâce à son ID : `getElementById`.
4. On lui dit : "quand tu reçois un **click**, lance la fonction qui affiche l'alerte".

---
