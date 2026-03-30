# TP : Créez votre site sur l'Histoire du Jeu Vidéo !

Bienvenue dans ce premier Travaux Pratiques sur le Web. Aujourd'hui, vous allez apprendre à coder votre propre site internet. 

Le projet : créer une page web dédiée à l'un de vos jeux vidéo préférés ou à l'histoire du gaming.

---

## Étape 1 : Les bases (HTML)

Le HTML (HyperText Markup Language) est le langage qui permet de structurer le contenu d'une page. On utilise des balises comme `<h1>` (titre principal) et `<p>` (paragraphe).

!!! question "Exercice 1 : Votre premier titre"
    Affichez votre titre et un petit message d'accueil sur votre jeu préféré.
    
    **Pour cet exercice, voici le code à recopier :**
    ```html
    <h1>Le Monde de Minecraft</h1>
    <p>Bienvenue sur mon site ! Minecraft est un jeu de construction "sandbox" sorti en 2011.</p>
    ```

    ```live-editor
    <!-- Tapez votre code HTML ici -->
    
    ```

---

## Étape 2 : Organiser les données (Les Listes)

Pour lister des caractéristiques (comme les modes de jeu ou vos consoles), on utilise les balises de liste :

*   `<ul>` : Ouvre la liste (Unordered List).
*   `<li>` : Crée un élément dans la liste (List Item).
*   `</ul>` : Ferme la liste.

!!! question "Exercice 2 : Vos modes de jeu"
    Sous votre titre et votre paragraphe de l'exercice précédent, ajoutez une liste de 3 modes ou éléments de votre jeu préféré.
    
    **Consignes :**

    1. Utilisez la balise `<ul>` pour commencer votre liste.
    2. Utilisez trois balises `<li>` pour vos éléments.
    3. N'oubliez pas de fermer chaque balise !

    ```live-editor
    <!-- Tapez votre code HTML ici -->

    ```

---

## Étape 3 : Médias et Liens

Un site web est plus vivant avec des images et des liens.

*   `<img src="URL_IMAGE">` : Affiche l'image située à l'adresse URL indiquée.
*   `<a href="URL_LIEN">Texte</a>` : Crée un lien vers l'adresse URL indiquée.

!!! question "Exercice 3 : Ajouter une image et un lien"
    Essayez d'ajouter une image de Pac-Man (`https://static.wikia.nocookie.net/logopedia/images/e/e2/Pac-ManJP.png/revision/latest/scale-to-width-down/1000?cb=20240313115916`) et un lien vers sa page Wikipedia.
    
    **Consignes :**

    1. Utilisez la balise `<img>` avec l'attribut `src`.
    2. En dessous, créez un lien avec la balise `<a>` et l'attribut `href`.
    3. Entre l'ouverture `<a>` et la fermeture `</a>`, écrivez le texte qui sera cliquable.

    ```live-editor
    <!-- Tapez votre code HTML ici -->

    ```

---

## Étape 4 : Le Style (CSS)

Le CSS (Cascading Style Sheets) permet de changer l'apparence. On écrit le style entre les balises `<style>`.

!!! question "Exercice 4 : Un look Gamer"

    Donnez un style plus sombre et moderne à votre page.
    
    **Consignes :**

    1. Dans le volet **CSS**, modifiez le `body` pour mettre le fond (`background-color`) en noir et le texte (`color`) en blanc.
    2. Modifiez le `h1` pour lui donner une couleur vive (comme `cyan` ou `orange`).

    ```live-editor-dual
    ---html---
    <h1>Gaming Live</h1>
    <p>Bienvenue sur mon site futuriste.</p>
    ---css---
    /* Tapez votre CSS ici */
    ```

---

## Étape 5 : Bordures et Arrondis (CSS)

Pour rendre un site "Premium", on utilise souvent des bordures et des angles arrondis.

*   `border: 2px solid white;` : Ajoute une bordure.
*   `border-radius: 10px;` : Arrondit les coins.
*   `box-shadow: 5px 5px 15px gray;` : Ajoute une ombre.

!!! question "Exercice 5 : Styliser votre image"

    Donnez une allure de "carte à collectionner" à votre image.
    
    **Consignes :**

    1. Dans le volet **CSS**, sélectionnez la balise `img`.
    2. Ajoutez une bordure de votre couleur préférée.
    3. Arrondissez les coins avec `border-radius: 20px`.
    4. Bonus : ajoutez une ombre.

    ```live-editor-dual
    ---html---
    <img src="https://static.wikia.nocookie.net/logopedia/images/e/e2/Pac-ManJP.png/revision/latest/scale-to-width-down/1000?cb=20240313115916" width="300">
    ---css---
    img {
      /* Vos bordures ici */
    }
    ```

---

## Étape 6 : Espacements (Marges et Padding)

Pour éviter que le texte ne colle aux bords de l'image ou de la page, on utilise les marges :

*   `margin` : Espace **autour** de l'élément (à l'extérieur).
*   `padding` : Espace **dedans** (à l'intérieur de la bordure).

!!! question "Exercice 6 : Aérer votre page"

    Ajoutez de l'espace pour que votre site soit agréable à lire.
    
    **Consignes :**

    1. Dans le volet **CSS**, ajoutez un `padding: 20px` sur votre `body`.
    2. Ajoutez une `margin-bottom: 30px` sur votre titre `h1` pour l'éloigner du texte d'après.

    ```live-editor-dual
    ---html---
    <h1>Espace de jeu</h1>
    <p>Ce texte est un peu trop collé en haut...</p>
    ---css---
    body {
       /* Ajoutez du padding ici */
    }
    h1 {
       /* Ajoutez de la marge ici */
    }
    ```

---

## Étape 7 : Le Projet Final

C'est le moment de prouver que vous êtes devenu un développeur Web !

!!! question "Le Grand Défi"

    Créez une page de présentation complète sur une console ou un jeu historique.
    
    **Contraintes :**

    1. Un design complet en CSS (couleurs, fond, police).
    2. Utilisation des bordures arrondies sur les images.
    3. Texte bien aéré avec des marges et du rembourrage (padding).
    4. Utilisation de listes et de liens.
    
    ```live-editor-dual
    ---html---
    <!-- Votre HTML ici -->
    ---css---
    /* Votre CSS ici */
    ```

---
Astuce : Si vous êtes fier de votre résultat, vous pouvez faire une capture d'écran pour la partager !