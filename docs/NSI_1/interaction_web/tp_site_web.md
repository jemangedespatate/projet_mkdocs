# TP/DM : Mon premier site web

## 🎯 Objectifs

Dans ce travail pratique, vous allez créer votre **premier site web** sur un thème de votre choix !

---

## 📚 Avant de commencer

### Prérequis

Avant de faire ce TP, assurez-vous d'avoir :

1. ✅ Lu le cours sur HTML, CSS et JavaScript
2. ✅ Fait les exercices de découverte (au moins les exercices 1 à 10)
3. ✅ Un éditeur de texte (Notepad++, Visual Studio Code, ou Bloc-notes)
4. ✅ Un navigateur web (Chrome, Firefox, Edge...)

### Outils nécessaires

* **Éditeur de code** : Pour écrire votre code
* **Navigateur** : Pour tester votre site
* **Dossier de travail** : Créez un dossier `mon_site_web` sur votre Bureau

---

## 🎨 Choisir votre thème

Vous êtes **libre** de choisir le thème de votre site web. Voici des idées simples pour débuter :

- 🎮 Présentation de votre jeu vidéo préféré
- 🎵 Site sur votre artiste ou groupe de musique favori
- 🏀 Page dédiée à votre sport ou équipe favorite
- 📚 Blog sur vos livres ou films préférés
- 🌍 Site de présentation d'un pays ou d'une ville
- 🎨 Portfolio artistique ou photographique
- 🔬 Présentation d'une découverte scientifique
- 🍕 Site de recettes de cuisine
- 🐾 Présentation d'une espèce animale
- 💻 Présentation de vous-même (page "À propos de moi")
- 🏀 Votre sport préféré
- 🎬 Vos films ou séries préférés

**Important** : Choisissez un thème que vous connaissez bien et qui vous intéresse !

---

## 📋 Ce que votre site doit contenir (minimum)

Pour réussir ce TP, votre site doit avoir **au minimum** :

### Structure de base

✅ **2 pages HTML minimum** :
- `index.html` (page d'accueil)
- Une autre page de votre choix (ex: `galerie.html`, `contact.html`)

✅ **1 fichier CSS** :
- `style.css` (pour la mise en forme)

✅ **Un dossier pour les images** :
- `images/` (contenant vos photos)

### Organisation des fichiers

Votre dossier doit ressembler à ceci :

```
mon_site_web/
│
├── index.html          ← Page d'accueil
├── page2.html          ← Deuxième page
├── style.css           ← Fichier CSS
│
└── images/             ← Dossier des images
    ├── photo1.jpg
    └── photo2.jpg
```

---

## 📝 Partie 1 : HTML (10 points)

### Ce que vous devez avoir dans votre HTML

| Élément | Points | Explication |
|---------|--------|-------------|
| Structure de base | 1 pt | `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>` |
| Titre de la page | 1 pt | Balise `<title>` dans le `<head>` |
| Au moins 1 titre h1 | 1 pt | Un grand titre sur chaque page |
| Au moins 3 paragraphes | 1 pt | Du texte avec la balise `<p>` |
| Au moins 2 images | 1 pt | Balise `<img>` avec attribut `alt` |
| Un menu de navigation | 2 pts | Liens entre vos pages avec `<a>` |
| Une liste | 1 pt | `<ul>` ou `<ol>` avec au moins 3 éléments |
| Code bien indenté | 2 pts | Code propre et facile à lire |

### Exemple de page HTML simple

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon Site - Accueil</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Menu de navigation -->
    <nav>
        <a href="index.html">Accueil</a>
        <a href="galerie.html">Galerie</a>
    </nav>

    <!-- Contenu principal -->
    <h1>Bienvenue sur mon site</h1>
    
    <img src="images/photo1.jpg" alt="Ma photo">
    
    <p>Ceci est ma première page web. Je vais vous présenter...</p>
    <p>Voici quelques informations intéressantes...</p>
    
    <h2>Mes passions</h2>
    <ul>
        <li>Le sport</li>
        <li>La musique</li>
        <li>Les jeux vidéo</li>
    </ul>
</body>
</html>
```

---

## 🎨 Partie 2 : CSS (8 points)

### Ce que vous devez avoir dans votre CSS

| Élément | Points | Explication |
|---------|--------|-------------|
| Fichier CSS séparé | 1 pt | Créer un fichier `style.css` |
| Couleurs | 2 pts | Changer les couleurs du texte et du fond |
| Polices | 1 pt | Changer la taille et le type de police |
| Espacements | 2 pts | Utiliser `margin` et `padding` |
| Menu stylisé | 1 pt | Rendre le menu joli |
| Code propre | 1 pt | Code bien organisé et commenté |

### Exemple de fichier CSS simple

```css
/* === COULEURS GÉNÉRALES === */
body {
    background-color: #f5f5f5;  /* Fond gris clair */
    color: #333;                /* Texte gris foncé */
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* === TITRES === */
h1 {
    color: #2c3e50;             /* Bleu foncé */
    font-size: 36px;
    text-align: center;
    margin: 20px 0;
}

h2 {
    color: #3498db;             /* Bleu */
    font-size: 24px;
    margin: 15px 0;
}

/* === PARAGRAPHES === */
p {
    font-size: 16px;
    line-height: 1.6;           /* Espacement entre les lignes */
    margin: 10px 0;
}

/* === MENU DE NAVIGATION === */
nav {
    background-color: #3498db;  /* Fond bleu */
    padding: 15px;
}

nav a {
    color: white;               /* Texte blanc */
    text-decoration: none;      /* Enlever le soulignement */
    margin: 0 15px;
    font-size: 18px;
}

nav a:hover {
    text-decoration: underline; /* Souligner au survol */
}

/* === IMAGES === */
img {
    max-width: 100%;            /* L'image ne dépasse pas son conteneur */
    height: auto;
    border-radius: 8px;         /* Coins arrondis */
}

/* === LISTES === */
ul {
    list-style-type: square;    /* Puces carrées */
    padding-left: 20px;
}

li {
    margin: 5px 0;
}
```

### Conseils pour débuter en CSS

**1. Commencez simple**
- Changez d'abord les couleurs
- Puis les tailles de police
- Ensuite les espacements

**2. Testez au fur et à mesure**
- Modifiez une propriété
- Rechargez la page (F5)
- Observez le résultat

**3. Utilisez des couleurs harmonieuses**

Quelques palettes simples :

* **Bleu et blanc** : `#3498db` (bleu), `#ecf0f1` (gris clair), `#2c3e50` (gris foncé)
* **Vert et blanc** : `#27ae60` (vert), `#f0f0f0` (gris clair), `#2c3e50` (gris foncé)
* **Rouge et blanc** : `#e74c3c` (rouge), `#ecf0f1` (gris clair), `#2c3e50` (gris foncé)

**4. Propriétés CSS essentielles**

| Propriété | Effet | Exemple |
|-----------|-------|---------|
| `color` | Couleur du texte | `color: blue;` |
| `background-color` | Couleur de fond | `background-color: #f0f0f0;` |
| `font-size` | Taille du texte | `font-size: 18px;` |
| `margin` | Espace extérieur | `margin: 20px;` |
| `padding` | Espace intérieur | `padding: 15px;` |
| `text-align` | Alignement du texte | `text-align: center;` |
| `border-radius` | Coins arrondis | `border-radius: 10px;` |

---

## ⚡ Partie 3 : JavaScript (BONUS - 2 points)

Cette partie est **optionnelle** et permet d'obtenir **2 points bonus**.

**Important** : Ne faites cette partie que si vous avez bien compris HTML et CSS !

### Option simple : Bouton qui affiche un message

C'est la fonctionnalité JavaScript la plus simple à ajouter.

**HTML** :
```html
<button onclick="direBonjour()">Cliquez-moi !</button>

<script>
    function direBonjour() {
        alert("Merci d'avoir visité mon site !");
    }
</script>
```

**Ce que ça fait** : Quand on clique sur le bouton, un message s'affiche.

### Option moyenne : Changer une image au clic

**HTML** :
```html
<img id="monImage" src="images/photo1.jpg" alt="Photo">
<button onclick="changerImage()">Changer l'image</button>

<script>
    function changerImage() {
        document.getElementById("monImage").src = "images/photo2.jpg";
    }
</script>
```

**Ce que ça fait** : Quand on clique sur le bouton, l'image change.

### Critères d'évaluation JavaScript

| Critère | Points |
|---------|--------|
| Le code fonctionne | 1 pt |
| Le code est bien placé et commenté | 1 pt |

---

## 📦 Rendu du travail

### Ce que vous devez rendre

1. **Un dossier compressé (.zip)** contenant :
   - Tous vos fichiers HTML
   - Votre fichier CSS
   - Votre dossier `images/` avec les images
   - (Optionnel) Votre fichier JavaScript

2. **Un fichier texte** `README.txt` avec :
   - Votre nom et prénom
   - Le thème de votre site
   - Ce que vous avez fait (HTML, CSS, JavaScript ?)
   - Les difficultés rencontrées

### Nommage du fichier

Nommez votre fichier zip : `NOM_Prenom_MonSite.zip`

**Exemple** : `DUPONT_Marie_MonSite.zip`

---

## ✅ Avant de rendre : vérifiez !

Cochez ces points avant de rendre votre travail :

- [ ] Mon site a au moins 2 pages HTML
- [ ] Les pages sont liées par un menu de navigation
- [ ] Mon fichier CSS est séparé du HTML
- [ ] Toutes mes images ont un attribut `alt`
- [ ] Mon code est bien indenté (facile à lire)
- [ ] J'ai testé tous les liens
- [ ] Mon site s'affiche correctement dans le navigateur
- [ ] J'ai créé le fichier README.txt
- [ ] J'ai compressé mon dossier en .zip

---

## 💡 Conseils pour réussir

### 1. Commencez simple

Ne cherchez pas à faire quelque chose de trop compliqué. Un site simple mais bien fait vaut mieux qu'un site complexe qui ne fonctionne pas !

### 2. Testez souvent

Après chaque modification :
1. Sauvegardez votre fichier
2. Rechargez la page dans le navigateur (F5)
3. Vérifiez que tout fonctionne

### 3. Demandez de l'aide

Si vous êtes bloqué :
- Relisez le cours
- Regardez les exercices
- Demandez à votre professeur
- Cherchez sur internet (W3Schools, MDN)

### 4. Soyez créatif !

C'est **votre** site web. Choisissez un thème qui vous plaît et amusez-vous !

---

## 📊 Barème récapitulatif

| Partie | Points | Détails |
|--------|--------|---------|
| **HTML** | 10 pts | Structure, contenu, balises |
| **CSS** | 8 pts | Couleurs, polices, mise en page |
| **JavaScript** | 2 pts | BONUS (optionnel) |
| **Total** | 20 pts | |

**Bonus possibles** :
- Code très propre et bien commenté : +0.5 pt
- Site particulièrement original : +0.5 pt
- Effort supplémentaire visible : +0.5 pt

---

## 🎉 Bon courage !

Vous allez créer votre premier site web ! C'est une étape importante dans votre apprentissage du développement web.

**N'oubliez pas** : l'objectif est d'apprendre et de prendre du plaisir. Même si votre site n'est pas parfait, vous aurez appris beaucoup de choses !

**Amusez-vous bien ! 🚀**


---

## Critères d'évaluation globaux

| Critère | Points |
|---------|--------|
| **HTML** | 10 pts |
| **CSS** | 8 pts |
| **JavaScript (bonus)** | 2 pts |
| **Total** | 20 pts |

### Bonus supplémentaires

- **Originalité du thème** : +0.5 pt
- **Qualité du contenu** : +0.5 pt
- **Accessibilité** (attributs alt, contraste) : +0.5 pt
- **Code propre et commenté** : +0.5 pt

---

## Conseils pratiques

### 1. Planification

Avant de coder, faites un **schéma** de votre site :
- Quelles pages ?
- Quelle navigation ?
- Quels contenus sur chaque page ?

### 2. Développement progressif

1. Commencez par le **HTML** de toutes les pages
2. Ajoutez le **CSS** pour la mise en forme
3. Testez la navigation entre les pages
4. Ajoutez le **JavaScript** (bonus) en dernier

### 3. Outils de développement

- **Éditeur de code** : Visual Studio Code, Sublime Text, Notepad++
- **Navigateur** : Chrome, Firefox (avec outils de développement F12)
- **Validation** : [W3C Validator](https://validator.w3.org/)

### 4. Tester régulièrement

- Ouvrez votre `index.html` dans un navigateur
- Testez tous les liens
- Vérifiez que les images s'affichent
- Testez sur différentes tailles de fenêtre

### 5. Ressources utiles

- **Images gratuites** : [Unsplash](https://unsplash.com), [Pexels](https://pexels.com)
- **Icônes** : [Font Awesome](https://fontawesome.com)
- **Polices** : [Google Fonts](https://fonts.google.com)
- **Couleurs** : [Coolors](https://coolors.co)

---

## Rendu du travail

### Format de rendu

Vous devez rendre :

1. **Un dossier compressé** (.zip) contenant tous vos fichiers
2. **Une capture d'écran** de votre page d'accueil
3. **Un fichier README.txt** contenant :
   - Votre nom et prénom
   - Le thème choisi
   - Les fonctionnalités JavaScript implémentées (si bonus)
   - Les difficultés rencontrées

### Nommage

Nommez votre fichier : `NOM_Prenom_SiteWeb.zip`

### Date limite

**À définir par votre professeur**

---

## Grille d'auto-évaluation

Avant de rendre votre travail, vérifiez :

- [ ] Mon site contient au moins 3 pages HTML
- [ ] Toutes les pages ont un menu de navigation fonctionnel
- [ ] Mon fichier CSS est dans un fichier séparé
- [ ] J'ai utilisé des balises sémantiques (`<header>`, `<nav>`, `<main>`, `<footer>`)
- [ ] Toutes mes images ont un attribut `alt`
- [ ] Mon code est indenté et lisible
- [ ] J'ai testé tous les liens
- [ ] Mon site s'affiche correctement dans le navigateur
- [ ] J'ai commenté les parties complexes de mon code
- [ ] (Bonus) J'ai ajouté au moins une fonctionnalité JavaScript

---

## Exemples d'inspiration

Voici quelques exemples de sites simples mais bien réalisés :

### Exemple 1 : Site sur le football

- **Page d'accueil** : Présentation du club, actualités
- **Page joueurs** : Galerie des joueurs avec photos
- **Page contact** : Formulaire de contact

### Exemple 2 : Site de recettes

- **Page d'accueil** : Présentation, recette du jour
- **Page recettes** : Liste de recettes avec images
- **Page à propos** : Histoire du site, auteur

### Exemple 3 : Portfolio artistique

- **Page d'accueil** : Présentation de l'artiste
- **Page galerie** : Galerie d'œuvres avec effet lightbox (JS)
- **Page contact** : Formulaire et réseaux sociaux

---

## Aide et support

Si vous rencontrez des difficultés :

1. **Consultez le cours** sur les interactions web
2. **Utilisez les outils de développement** du navigateur (F12)
3. **Recherchez sur internet** : MDN Web Docs, W3Schools
4. **Demandez à votre professeur** pendant les heures de TP

---

## Bon courage ! 🚀

N'oubliez pas : l'important est d'apprendre et de prendre du plaisir à créer votre site web. Soyez créatifs et amusez-vous !
