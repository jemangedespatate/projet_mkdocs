# 🔑 Correction du TP : Traitement d'Image avec Python

Ce document contient les solutions attendues pour le TP de photographie numérique.

---

## Activité 1 : Ouvrir et Analyser
**Question :** Pourquoi l'accès au pixel `(largeur, hauteur)` provoque-t-il une erreur ?
**Réponse :** En informatique, les indices commencent à **0**. Si une image fait 800 pixels de large, les coordonnées vont de **0 à 799**. Le pixel `800` est donc hors limites.

---

## Activité 2 : Le Négatif
```python
# Dans activite_2() :
r_new = 255 - r
v_new = 255 - v  # Inversion du vert
b_new = 255 - b  # Inversion du bleu
```

---

## Activité 3 : Niveaux de Gris
```python
# Dans activite_3() :
moyenne = (r + v + b) // 3
r_new = moyenne
v_new = moyenne
b_new = moyenne
```

---

## Activité 4 : Filtre Rouge
```python
# Dans activite_4() :
for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        
        r_new = r   # On garde le rouge
        v_new = 0   # On supprime le vert
        b_new = 0   # On supprime le bleu
        
        img_new.putpixel((x, y), (r_new, v_new, b_new))
```

---

## Activité 5 : Stéganographie
```python
# Dans activite_5() :
b_new = b * 255

# Sécurité pour ne pas dépasser 255
if b_new > 255:
    b_new = 255
```
**Le message caché est :** "SNT 2026"

---

## ⚡ Solutions des Compléments (Facultatif)

### Luminosité (+50)
```python
r_new = min(255, r + 50)
v_new = min(255, v + 50)
b_new = min(255, b + 50)
```

### Miroir Horizontal
```python
# On prend le pixel à l'opposé en X
r, v, b = img.getpixel((largeur - 1 - x, y))
img_new.putpixel((x, y), (r, v, b))
```
