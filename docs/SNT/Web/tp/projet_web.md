# TP : Projet Final Web

Bienvenue dans ce projet final sur le thème du Web ! Vous allez mettre en pratique tout ce que vous avez appris lors des séances précédentes pour créer un site internet complet.

Le projet : créer une (ou plusieurs) page(s) web sur le **thème de votre choix** (votre groupe de musique préféré, un sport, un film, l'écologie, un jeu vidéo, etc.). Vous pouvez réaliser ce projet **seul ou à plusieurs** selon les consignes de votre professeur.

---

## Les attendus du projet

!!! question "Cahier des charges"
    Votre projet sera évalué sur les critères suivants. Assurez-vous de bien tous les respecter pour valider ce TP !
    
    **Structure (HTML) :**

    - La page doit contenir un **titre principal** (`<h1>`).
    - Le contenu doit être structuré avec des vrais paragraphes (`<p>`) et éventuellement des sous-titres (`<h2>`).
    - Vous devez utiliser au moins une **liste** (`<ul>` et `<li>`).
    - Vous devez intégrer au moins une **image** en rapport avec votre thème (`<img>` avec attribut `src`), ou plus si vous le souhaitez.
    - Vous devez insérer au moins un **lien** (`<a>` avec attribut `href`) pointant vers une ressource externe (Wikipédia, site officiel...) ou vers une autre page de votre site.
    
    **Design (CSS) :**

    - La page doit avoir un design personnalisé (couleur de fond du site et couleur du texte modifiées).
    - La mise en page doit être soignée et aérée (utilisation de `margin` ou de `padding`).
    - Vous devez utiliser des bordures (`border`) ou des coins arrondis (`border-radius`) sur certains éléments, comme les images.
    
    **Contenu et Originalité :**

    - Le texte doit être rédigé par vos soins, sans "faux texte" ni copié-collé brut.
    - Le site doit être cohérent avec le thème choisi (polices, couleurs, ambiance).
    
    *(Optionnel / Pour aller plus loin)* : Réaliser plusieurs pages avec un moyen de navigation permettant de passer d'une page à l'autre.

---

## Étape 1 : Le squelette du site (HTML)

!!! question "Votre code HTML"
    Commencez par rédiger tout le contenu de votre site internet en HTML. N'utilisez **que** les balises HTML. Ne vous préoccupez pas encore de l'apparence visuelle, c'est ce qu'on appelle écrire le "squelette" du site !
    
    N'oubliez pas d'insérer vos textes, vos titres, votre image et votre lien hypertexte.

    ```live-editor-dual
    ---html---

    




    ---css---
    /* Ne touchez pas encore au CSS dans cette étape ! */
    ```

---

## Étape 2 : Le style et l'habillage (CSS)

!!! question "Styliser le site avec le CSS"
    Maintenant que votre page HTML est bien structurée, vous pouvez y ajouter votre style pour la rendre belle et agréable à lire.
    
    **Consignes :**

    1. Dans le volet **HTML**, copiez et collez le contenu que vous avez créé à l'étape précédente. N'hésitez pas à **ajouter toujours plus de contenu et d'images** pour étoffer votre site !
    2. Dans le volet **CSS**, commencez à appliquer vos couleurs, vos arrondis (`border-radius`), vos marges, et tout le reste.
    3. Testez les **ombres** derrière les textes ou les images avec les propriétés `box-shadow` et `text-shadow`.
    4. Commencez à concevoir une **deuxième page web** avec la même interface graphique pour lier vos pages entre elles.

    ```live-editor-dual
    ---html---
    <!-- Copiez-collez votre HTML de l'étape 1 ici et ajoutez du contenu supplémentaire -->




    ---css---




    ```

---

## Étape 3 (Pour aller plus loin) : Finitions professionnelles

Pour ce projet sur plusieurs séances, votre site peut devenir extrêmement riche. Voici de nouvelles idées pour obtenir un rendu final digne des vrais professionnels du Web !

!!! question "Améliorations avancées"

    **1. Intégrer une vidéo :**

    Allez sur YouTube, cherchez une vidéo sur votre thème, cliquez sur "Partager" puis "Intégrer", et copiez-collez la balise `<iframe>` dans votre code HTML.
    
    **2. Créer un vrai menu de navigation (`<nav>`) :**

    Organisez les liens vers vos différentes pages ou sections dans un menu en haut de l'écran. 
    Stylisez les liens pour qu'ils ressemblent à de vrais boutons : sans soulignement (`text-decoration: none`), avec un encadrement (`padding`) et une belle `background-color`.
    
    **3. Les effets au survol (`:hover`) :**

    Rendez votre site interactif ! En CSS, vous pouvez utiliser `:hover` pour changer l'allure d'un bouton ou d'une image quand la souris pointe dessus. N'oubliez pas d'ajouter `transition: 0.5s;` à votre élément d'origine pour que le changement soit joli et fluide.
    
    **4. Modifier la typographie :**

    Remplacez la police d'écriture par défaut du site en utilisant la propriété `font-family` avec des polices adaptées à l'ambiance de votre thème (histoire, jeu, musique, etc.).

    ```live-editor-dual
    ---html---





    ---css---

    ```

---

## Étape Bonus : Créer le site "pour de vrai" localement !

Pour le moment, vous codez à l'intérieur d'un éditeur virtuel sur cette page. Cela a cependant ses limites : vous ne pouvez pas utiliser vos propres images locales par défaut, et la création de liens vers d'autres pages est fastidieuse (tout l'univers virtuel doit être géré sur cette seule page).

Pour repousser ces limites et découvrir comment travaillent les vrais développeurs Web, voici comment héberger votre site sur votre propre ordinateur :

!!! tip "Créer de vrais fichiers web sur la machine"

    1. Sur l'ordinateur, créez un **nouveau dossier** sur le bureau ou dans vos documents. Nommez-le `Mon_Projet_Web`.
    2. À l'intérieur, créez un nouveau document texte. Renommez-le très exactement en **`index.html`** (attention à bien vérifier que vous avez remplacé l'extension `.txt`). C'est le nom officiel mondial pour la page d'accueil d'un site !
    3. Créez un deuxième document texte nommé **`style.css`**.
    4. **Déplacez les fichiers d'images** locaux que vous souhaitez utiliser directement dans ce dossier `Mon_Projet_Web`.
    5. Ouvrez vos fichiers `.html` et `.css` avec un **éditeur de code** (comme le *Bloc-notes* Windows) via Clic-Droit "Ouvrir avec...".

    C'est ici que vous allez pouvoir copier-coller tout le code libre que vous avez produit dans ce TP ! Dans votre `<head>`, n'oubliez pas d'insérer la balise de lien pour relier votre fichier HTML à votre fichier CSS :

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Titre de ma page</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        
        <!-- C'est ici, entre les balises body, qu'il faut coller le code HTML du site ! -->

    </body>
    </html>
    ```

    **Pour afficher le site :**
    Double-cliquez simplement sur votre fichier `index.html` ! Il s'ouvrira dans votre navigateur web habituel (Chrome, Edge, Firefox...). 
    À chaque fois que vous modifiez le code dans votre éditeur textuel, n'oubliez pas de **sauvegarder votre fichier (`Ctrl` + `S`)** puis de retourner **actualiser la page de votre navigateur (`F5`)** !
    
    **L'avantage majeur de cette méthode de pros :** vous pouvez dorénavant créer autant de pages que vous désirez (ex: `page2.html`, `contact.html`...) et faire de vrais liens de navigation `<a href="page2.html">` pour naviguer entre vos pages !
