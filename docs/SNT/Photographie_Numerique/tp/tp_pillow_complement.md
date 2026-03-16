# ⚡ Compléments de TP : Photographie Numérique

Ces activités sont destinées aux élèves ayant terminé les 5 activités principales du TP et souhaitant approfondir leurs connaissances en traitement d'image.

---

## Exercice 1 : Réglage de la luminosité
**Objectif :** Modifier l'intensité lumineuse d'une image.

1.  Créez une nouvelle fonction `luminosite(img, valeur)` dans votre fichier Python.
2.  Pour chaque pixel $(r, v, b)$, demandez-vous comment augmenter ou diminuer sa luminosité.
    *   *Indice :* Il faut ajouter ou soustraire un nombre à chaque composante (ex: +50 ou -50).
3.  **Attention :** Veillez à ce que les valeurs restent entre 0 et 255 (utilisez les fonctions `min()` et `max()`).
4.  Testez votre fonction.

---

## Exercice 2 : Effet Miroir (Symétrie Horizontale)
**Objectif :** Retourner l'image comme dans un miroir.

1.  Créez une fonction `miroir_horizontal()`.
2.  Si un pixel est à la position $(x, y)$, par quel pixel $(x', y')$ de l'image d'origine doit-il être remplacé ?
    *   *Réponse :* $x' = largeur - 1 - x$ et $y' = y$.
3.  Implémentez cette transformation.

---

## Exercice 3 : Binarisation (Seuillage)
**Objectif :** Transformer l'image pour qu'elle ne contienne que du noir pur et du blanc pur.

1.  Transformez d'abord l'image en niveaux de gris.
2.  Choisissez un **seuil** (par exemple $128$).
3.  Pour chaque pixel, si sa valeur est supérieure au seuil, mettez-le en blanc $(255, 255, 255)$. Sinon, mettez-le en noir $(0, 0, 0)$.

---

## Exercice 4 : Filtrage Sépia (Plus complexe)
**Objectif :** Donner un aspect ancien à une photo.

L'effet Sépia s'obtient avec les formules suivantes pour chaque pixel :
*   `tr = 0.393*r + 0.769*v + 0.189*b`
*   `tg = 0.349*r + 0.686*v + 0.168*b`
*   `tb = 0.272*r + 0.534*v + 0.131*b`

Implémentez cela en n'oubliant pas d'arrondir les résultats (`int()`) et de limiter les valeurs à 255.
