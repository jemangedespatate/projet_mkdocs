# 🎯 Exercices de découverte HTML/CSS

## 📝 Partie 1 : Découverte du HTML

### Exercice 1 : Ma première page web ⭐

1. Créez un fichier `exercice1.html`
2. Copiez ce code de base :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ma première page</title>
</head>
<body>
    <h1>Bonjour le monde !</h1>
    <p>Ceci est ma première page web.</p>
</body>
</html>
```

3. Ouvrez le fichier dans votre navigateur (double-clic ou clic droit > Ouvrir avec > Navigateur)
4. **Modifiez** le titre et le paragraphe avec votre propre texte
5. Ajoutez un deuxième paragraphe avec la balise `<p>`

**Résultat attendu** : Une page simple avec un titre et deux paragraphes.

---

### Exercice 2 : Les titres ⭐

Créez une page `exercice2.html` qui contient :

* Un titre principal (`<h1>`) : "Mon animal préféré"
* Un sous-titre (`<h2>`) : "Description"
* Un paragraphe qui décrit l'animal
* Un autre sous-titre (`<h2>`) : "Pourquoi je l'aime"
* Un paragraphe qui explique pourquoi

---

### Exercice 3 : Les listes ⭐

Créez une page `exercice3.html` avec :

1. Un titre "Mes activités préférées"
2. Une **liste à puces** de 3 activités que vous aimez
3. Un titre "Mon top 3 des films"
4. Une **liste numérotée** de vos 3 films préférés

??? note "Aide :"
    ```html
    <!-- Liste à puces -->
    <ul>
        <li>Premier élément</li>
        <li>Deuxième élément</li>
    </ul>

    <!-- Liste numérotée -->
    <ol>
        <li>Premier élément</li>
        <li>Deuxième élément</li>
    </ol>
    ```

---

### Exercice 4 : Les liens ⭐⭐

Créez une page `exercice4.html` avec :

* Un titre "Mes sites préférés"
* Au moins 3 liens vers des sites que vous aimez (YouTube, Wikipédia, etc.)
* Chaque lien doit s'ouvrir dans un nouvel onglet

??? note "Aide :"
    ```html
    <a href="https://www.youtube.com" target="_blank">YouTube</a>
    ```

---

### Exercice 5 : Les images ⭐⭐

Créez une page `exercice5.html` qui affiche des images :

1. Créez un dossier `images` à côté de votre fichier HTML
2. Trouvez 2-3 images sur internet et enregistrez-les dans ce dossier
3. Créez une page `exercice5.html` qui affiche ces images
4. Ajoutez une description (attribut `alt`) pour chaque image

??? note "Aide :"
    ```html
    <img src="images/mon_image.jpg" alt="Description de l'image">
    ```

**Important** : L'attribut `alt` décrit l'image (utile pour l'accessibilité).

---

## 🎨 Partie 2 : Découverte du CSS

### Exercice 6 : Mes premières couleurs ⭐

1. Créez un fichier `exercice6.html` et copier les ligne suivantes :

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Exercice CSS</title>
        <link rel="stylesheet" href="style6.css">
    </head>
    <body>
        <h1>Mon titre coloré</h1>
        <p>Un paragraphe avec du style !</p>
    </body>
    </html>
    ```

2. Créez un fichier `style6.css` dans le même dossier
3. Dans le CSS, changez la couleur du titre et du texte

---

### Exercice 7 : Changer la taille et la police ⭐

Reprenez l'exercice 6 et modifiez le CSS pour :

* Mettre le titre en taille 40px
* Mettre le paragraphe en taille 18px
* Changer la police du titre en Arial
* Changer la police du paragraphe en Verdana

??? note "Aide :"

    ```css
    h1 {
        font-size: 40px;
        font-family: Arial, sans-serif;
    }
    ```

---

### Exercice 8 : Centrer et espacer ⭐⭐

Créez une page avec un titre et un paragraphe, puis :

* Centrez le titre
* Ajoutez une marge de 20px autour du paragraphe
* Ajoutez un padding (espace intérieur) de 15px au paragraphe
* Donnez une couleur de fond au paragraphe

??? note "Aide :"

    ```css
    h1 {
        text-align: center;
    }

    p {
    margin: 20px;
    padding: 15px;
    background-color: lightblue;
    }
    ```

---

### Exercice 9 : Les bordures et les coins arrondis ⭐⭐

Créez une "carte" (un `<div>`) avec :

* Une bordure de 2px, solide, noire
* Des coins arrondis de 10px
* Un padding de 20px
* Une couleur de fond claire
* Une ombre portée (bonus)

??? note "Aide :"

    ```html
    <div class="carte">
        <h2>Titre de la carte</h2>
        <p>Contenu de la carte</p>
    </div>
    ```

    ```css
    .carte {
        border: 2px solid black;
        border-radius: 10px;
        padding: 20px;
        background-color: #f0f0f0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    ```

---

### Exercice 10 : Un bouton stylisé ⭐⭐

Créez un bouton avec ces caractéristiques :

* Couleur de fond : bleu (`#3498db`)
* Couleur du texte : blanc
* Padding : 15px 30px
* Bordure : aucune
* Coins arrondis : 5px
* Curseur : pointeur (main) au survol
* Effet au survol : couleur plus foncée

??? note "Aide :"

    ```html
    <button class="mon-bouton">Cliquez ici</button>
    ```

    ```css
    .mon-bouton {
    background-color: #3498db;
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    }

    .mon-bouton:hover {
    background-color: #2980b9;
    }
    ```

---

## ⚡ Partie 3 : Première interaction JavaScript

### Exercice 11 : Afficher une alerte ⭐

Créez une page avec un bouton qui affiche un message quand on clique dessus.

??? note "Aide :"

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Mon premier JS</title>
    </head>
    <body>
        <h1>Cliquez sur le bouton !</h1>
        <button onclick="direBonjour()">Cliquez-moi</button>

        <script>
            function direBonjour() {
                alert("Bonjour ! Vous avez cliqué sur le bouton !");
            }
        </script>
    </body>
    </html>
    ```

**À faire** : Changez le message affiché !

---

### Exercice 12 : Changer le texte d'une page ⭐⭐

Créez une page avec :
* Un titre qui dit "Cliquez sur le bouton"
* Un bouton qui change le titre quand on clique dessus

??? note "Aide :"

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Changer le texte</title>
    </head>
    <body>
        <h1 id="titre">Cliquez sur le bouton</h1>
        <button onclick="changerTitre()">Changer le titre</button>

        <script>
            function changerTitre() {
                document.getElementById("titre").textContent = "Vous avez cliqué !";
            }
        </script>
    </body>
    </html>
    ```

**À faire** : Changez le nouveau texte du titre !

---

### Exercice 13 : Compteur simple ⭐⭐⭐

Créez un compteur qui :
* Affiche un nombre (commence à 0)
* A un bouton "+" qui augmente le nombre de 1
* A un bouton "-" qui diminue le nombre de 1

??? note "Aide :"

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Compteur</title>
    </head>
    <body>
        <h1>Compteur</h1>
        <p id="affichage">0</p>
        <button onclick="incrementer()">+</button>
        <button onclick="decrementer()">-</button>

        <script>
            let compteur = 0;

            function incrementer() {
                compteur = compteur + 1;
                document.getElementById("affichage").textContent = compteur;
            }

            function decrementer() {
                compteur = compteur - 1;
                document.getElementById("affichage").textContent = compteur;
            }
        </script>
    </body>
    </html>
    ```

**Bonus** : Ajoutez du CSS pour rendre le compteur plus joli !
