# TP : Crée ton site sur l'Histoire du Jeu Vidéo !

Bienvenue dans ce premier Travaux Pratiques sur le Web. Aujourd'hui, tu vas apprendre à coder ton propre site internet. 

Le projet : créer une page web dédiée à l'un de tes jeux vidéo préférés ou à l'histoire du gaming.

---

## Étape 1 : Les bases (HTML)

Le HTML (HyperText Markup Language) est le langage qui permet de structurer le contenu d'une page. On utilise des balises comme `<h1>` (titre principal) et `<p>` (paragraphe).

!!! question "Exercice 1 : Ton premier titre"
    Affiche ton titre et un petit message d'accueil sur ton jeu préféré.
    
    **Pour cet exercice, voici le code à recopier :**
    ```html
    <h1>Le Monde de Minecraft</h1>
    <p>Bienvenue sur mon site ! Minecraft est un jeu de construction "sandbox" sorti en 2011.</p>
    ```

    ```live-editor
    <!-- Tape ton code HTML ici -->
    
    ```

---

## Étape 2 : Organiser les données (Les Listes)

Pour lister des caractéristiques (comme les modes de jeu ou tes consoles), on utilise les balises de liste :

*   `<ul>` : Ouvre la liste (Unordered List).
*   `<li>` : Crée un élément dans la liste (List Item).
*   `</ul>` : Ferme la liste.

!!! question "Exercice 2 : Tes modes de jeu"
    Sous ton titre et ton paragraphe de l'exercice précédent, ajoute une liste de 3 modes ou éléments de ton jeu préféré.
    
    **Consignes :**

    1. Utilise la balise `<ul>` pour commencer ta liste.
    2. Utilise trois balises `<li>` pour tes éléments.
    3. N'oublie pas de fermer chaque balise !

    ```live-editor
    <!-- Tape ton code HTML ici -->

    ```

---

## Étape 3 : Médias et Liens

Un site web est plus vivant avec des images et des liens.

*   `<img src="URL_IMAGE">` : Affiche l'image située à l'adresse URL indiquée.
*   `<a href="URL_LIEN">Texte</a>` : Crée un lien vers l'adresse URL indiquée.

!!! question "Exercice 3 : Ajouter une image et un lien"
    Essaye d'ajouter une image de Pac-Man (`https://static.wikia.nocookie.net/logopedia/images/e/e2/Pac-ManJP.png/revision/latest/scale-to-width-down/1000?cb=20240313115916`) et un lien vers sa page Wikipedia.
    
    **Consignes :**

    1. Utilise la balise `<img>` avec l'attribut `src`.
    2. En dessous, crée un lien avec la balise `<a>` et l'attribut `href`.
    3. Entre l'ouverture `<a>` et la fermeture `</a>`, écris le texte qui sera cliquable.

    ```live-editor
    <!-- Tape ton code HTML ici -->

    ```

---

## Étape 4 : Le Style (CSS)

Le CSS (Cascading Style Sheets) permet de changer l'apparence. On écrit le style entre les balises `<style>`.

!!! question "Exercice 4 : Un look Gamer"

    Donne un style plus sombre et moderne à ta page.
    
    **Consignes :**

    1. Dans le volet **CSS**, modifie le `body` pour mettre le fond (`background-color`) en noir et le texte (`color`) en blanc.
    2. Modifie le `h1` pour lui donner une couleur vive (comme `cyan` ou `orange`).

    ```live-editor-dual
    ---html---
    <h1>Gaming Live</h1>
    <p>Bienvenue sur mon site futuriste.</p>
    ---css---
    /* Tape ton CSS ici */
    ```

---

## Étape 5 : Bordures et Arrondis (CSS)

Pour rendre un site "Premium", on utilise souvent des bordures et des angles arrondis.

*   `border: 2px solid white;` : Ajoute une bordure.
*   `border-radius: 10px;` : Arrondit les coins.
*   `box-shadow: 5px 5px 15px gray;` : Ajoute une ombre.

!!! question "Exercice 5 : Styliser ton image"

    Donne une allure de "carte à collectionner" à ton image.
    
    **Consignes :**

    1. Dans le volet **CSS**, sélectionne la balise `img`.
    2. Ajoute une bordure de ta couleur préférée.
    3. Arrondis les coins avec `border-radius: 20px`.
    4. Bonus : ajoute une ombre.

    ```live-editor-dual
    ---html---
    <img src="https://static.wikia.nocookie.net/logopedia/images/e/e2/Pac-ManJP.png/revision/latest/scale-to-width-down/1000?cb=20240313115916" width="300">
    ---css---
    img {
      /* Tes bordures ici */
    }
    ```

---

## Étape 6 : Espacements (Marges et Padding)

Pour éviter que le texte ne colle aux bords de l'image ou de la page, on utilise les marges :

*   `margin` : Espace **autour** de l'élément (à l'extérieur).
*   `padding` : Espace **dedans** (à l'intérieur de la bordure).

!!! question "Exercice 6 : Aérer ta page"

    Ajoute de l'espace pour que ton site soit agréable à lire.
    
    **Consignes :**

    1. Dans le volet **CSS**, ajoute un `padding: 20px` sur ton `body`.
    2. Ajoute une `margin-bottom: 30px` sur ton titre `h1` pour l'éloigner du texte d'après.

    ```live-editor-dual
    ---html---
    <h1>Espace de jeu</h1>
    <p>Ce texte est un peu trop collé en haut...</p>
    ---css---
    body {
       /* Ajoute du padding ici */
    }
    h1 {
       /* Ajoute de la marge ic i */
    }
    ```

---

## Étape 7 : Le Projet Final

C'est le moment de prouver que tu es devenu un développeur Web !

!!! question "Le Grand Défi"

    Crée une page de présentation complète sur une console ou un jeu historique.
    
    **Contraintes :**

    1. Un design complet en CSS (couleurs, fond, police).
    2. Utilisation des bordures arrondies sur les images.
    3. Texte bien aéré avec des marges et du rembourrage (padding).
    4. Utilisation de listes et de liens.
    
    ```live-editor-dual
    ---html---
    <!-- Ton HTML ici -->
    ---css---
    /* Ton CSS ici */
    ```

---
Astuce : Si tu es fier de ton résultat, tu peux faire une capture d'écran pour la partager !