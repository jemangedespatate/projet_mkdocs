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
