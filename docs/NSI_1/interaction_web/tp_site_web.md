# TP/DM : Mon premier site web

## 🎯 Objectifs

Dans ce travail pratique, vous allez créer votre **premier site web** sur un thème de votre choix !

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

---

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

??? note "Quelques palettes simples :"

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

**Ce que ça fait** : Quand on clique sur le bouton, un message s'affiche.

### Option moyenne : Changer une image au clic

**Ce que ça fait** : Quand on clique sur le bouton, l'image change.

### Critères d'évaluation JavaScript

| Critère | Points |
|---------|--------|
| Le code fonctionne | 1 pt |
| Le code est bien placé et commenté | 1 pt |

---

## 📦 Rendu du travail

### Ce que vous devez rendre

**Un dossier compressé (.zip)** contenant :

   - Tous vos fichiers HTML
   - Votre fichier CSS
   - Votre dossier `images/` avec les images
   - (Optionnel) Votre fichier JavaScript

**Un fichier texte** `README.txt` avec :   

   - Votre nom et prénom
   - Le thème de votre site
   - Ce que vous avez fait (HTML, CSS, JavaScript ?)
   - Les difficultés rencontrées

### Nommage du fichier

Nommez votre fichier zip : `NOM_Prenom_MonSite.zip`

**Exemple** : `DUPONT_Marie_MonSite.zip`

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
