# 🚀 TP Bonus : Donnez vie à votre site web

## 🎯 Objectifs

Vos sites web sont fonctionnels et bien structurés, mais ils manquent peut-être un peu de dynamisme ! Dans ce TP bonus, vous allez découvrir comment animer vos pages.

Plutôt que de vous donner le code tout fait, vous allez devoir chercher et adapter des concepts à **votre propre code**. Prenez le temps d'analyser chaque notion, de faire des petites recherches, et d'intégrer ces effets de façon pertinente sur les pages web que vous avez réalisées précédemment.

---

## 🦋 Partie 1 : Des survols en douceur (`transition` et `:hover`)

La pseudo-classe `:hover` permet de changer le style d'un élément lorsque la souris passe dessus. La propriété `transition` permet d'indiquer au navigateur qu'il doit lisser et animer ce changement pour éviter un effet brutal.

### 🎯 Mission 1 : Animer votre navigation

Votre menu a peut-être déjà des couleurs qui changent au survol. 

1. Recherchez sur internet (par exemple sur la documentation MDN ou W3Schools) comment fonctionne la propriété CSS `transition`.
2. **Appliquez une transition fluide** (par exemple de `0.4s`) sur les liens de votre menu principal pour adoucir le changement de couleur (du texte et/ou du fond).

### 🎯 Mission 2 : Effet de zoom sur les images

La propriété CSS `transform` permet de modifier la forme, la rotation ou la taille d'un élément.

1. Renseignez-vous sur la fonction `scale()` qui s'associe à la propriété `transform`.
2. **Faites en sorte que vos images s'agrandissent légèrement (ex: 110%) lorsque vous les survolez**. Notez qu'il faudra combiner ceci avec une propriété `transition` sur l'image pour que l'agrandissement soit progressif.

*(Astuce : Testez sur votre page. Attention à ce que vos grandes images ne débordent pas de manière disgracieuse sur votre texte !)*

---

## 🎴 Partie 2 : Créer la subtilité avec les `@keyframes`

Jusqu'à maintenant, l'animation se déclenchait par l'action de l'utilisateur (la souris). Avec les `@keyframes`, on peut créer des animations indépendantes qui tournent "toutes seules", en boucle.

### 🎯 Mission 3 : Faire "respirer" un élément

Voici la structure de base (son "squelette") d'une animation continue en CSS :

```css
@keyframes nom_de_votre_animation {
    0% { /* État de départ */ }
    50% { /* État du milieu (ex: l'élément s'est déplacé ou agrandi) */ }
    100% { /* Retour à l'état de fin */ }
}

selecteur_de_votre_element {
    animation: nom_de_votre_animation 3s infinite ease-in-out;
}
```

1. Cherchez comment utiliser `transform: translateY()` pour déplacer un élément verticalement sur son axe Y.
2. Ou bien cherchez comment utiliser `transform: scale()` pour donner un effet de "battement de cœur".
3. **Appliquez une de ces animations continues sur un élément central de votre site** (comme votre titre principal `h1`, l'image de garde de votre page d'accueil, ou un bouton important). 

L'objectif est d'attirer subtilement l'œil du visiteur sans que visuellement cela ne devienne agressif.

---

## 🚀 Partie 3 (Bonus+) : L'interactivité avec JavaScript

Nous avons vu que le CSS gérait la présentation. Que se passe-t-il lorsque l'on veut rendre la page intelligente et réactive ? C'est là que le **JavaScript** intervient !

### 🎯 Mission 4 : Un élément qui suit la souris

Nous allons créer un petit effet visuel amusant : un élément graphique (une bulle colorée) qui traque et suit en direct le pointeur de votre vraie souris sur l'écran.

**Étape 1 : Préparation visuelle (HTML & CSS)**
- Créez une simple balise `<div id="curseur-suiveur"></div>` tout en bas de votre fichier HTML.
- Dans votre fichier CSS, donnez-lui une largeur, une hauteur, une couleur de fond et des bords arrondis (`border-radius`) pour en faire un joli cercle.
- Faites en sorte qu'il soit libre et flotte au dessus de votre page web en utilisant le CSS (`position: fixed;` et `z-index: 9999;`).
- *Contrainte forte :* Ajoutez obligatoirement la propriété `pointer-events: none;` sur ce cercle dans votre CSS. Posez-vous la question du "pourquoi a-t-on besoin de cela" en testant sans l'instruction.

**Étape 2 : L'intelligence (JavaScript)**
Voici la logique, c'est à vous de compléter les "trous" du script :

1. Le programme doit identifier (`getElementById`) la bulle dans la page.
2. Le programme doit se mettre en attente et écouter (`addEventListener`) les mouvements que fait la vraie souris de l'ordinateur.
3. À chaque mouvement détecté (`event`), la bulle est instantanément déplacée (`style.transform`) aux nouvelles coordonnées `X` / `Y` de la fameuse vraie souris.

```html
<!-- À placer tout en bas du body, sous votre <div> -->
<script>
    // Quel est l'ID de l'élément que l'on veut manipuler ?
    const curseur = document.getElementById("..."); 

    // Quel "événement" le navigateur doit-il écouter ? ("mousemove", "click", "keydown"... ?)
    document.addEventListener("...", function(event) {
        
        // On récupère les coordonnées X et Y de cet événement (la souris) 
        // avec event.clientX et event.clientY
        curseur.style.transform = `translate(${...}px, ${...}px)`;
        
    });
</script>
```

Complétez le script, sauvegardez et admirez la magie de l'interactivité !
