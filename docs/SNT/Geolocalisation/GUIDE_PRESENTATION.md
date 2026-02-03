# 📖 Guide d'utilisation de la présentation

## 🎬 Présentation du cours (Marp)

La présentation `presentation.md` est créée avec **Marp** (Markdown Presentation Ecosystem), un outil qui permet de créer des diaporamas à partir de fichiers Markdown.

## 🚀 Comment utiliser la présentation ?

### Option 1 : Extension VS Code (Recommandé)

1. **Installer l'extension Marp for VS Code**
   - Ouvrir VS Code
   - Aller dans Extensions (Ctrl+Shift+X)
   - Rechercher "Marp for VS Code"
   - Installer l'extension

2. **Ouvrir le fichier**
   - Ouvrir `presentation.md` dans VS Code

3. **Prévisualiser**
   - Cliquer sur l'icône de prévisualisation (en haut à droite)
   - Ou utiliser le raccourci : `Ctrl+K V`

4. **Exporter en PDF ou HTML**
   - Clic droit sur le fichier → "Marp: Export slide deck..."
   - Choisir le format (PDF, HTML, PPTX)

### Option 2 : Marp CLI

1. **Installer Marp CLI**
   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. **Générer un PDF**
   ```bash
   marp presentation.md --pdf
   ```

3. **Générer un HTML**
   ```bash
   marp presentation.md --html
   ```

4. **Mode présentation avec serveur local**
   ```bash
   marp -s presentation.md
   ```

### Option 3 : En ligne (Marp Web)

1. Aller sur [https://web.marp.app/](https://web.marp.app/)
2. Copier-coller le contenu de `presentation.md`
3. Exporter en PDF ou présenter directement

## 📊 Structure de la présentation

La présentation est organisée en **6 parties** :

1. **Introduction et historique** (5 slides)
2. **Coordonnées géographiques** (4 slides)
3. **Fonctionnement du GPS** (5 slides)
4. **Protocole NMEA** (3 slides)
5. **Applications pratiques** (4 slides)
6. **Enjeux et vie privée** (4 slides)

**Total** : ~30 slides pour 1 heure de cours

## ⏱️ Timing suggéré

| Section | Durée | Slides |
|:---|:---:|:---:|
| Introduction | 8 min | 1-5 |
| Coordonnées | 10 min | 6-9 |
| GPS | 15 min | 10-14 |
| NMEA | 10 min | 15-17 |
| Applications | 10 min | 18-21 |
| Vie privée | 10 min | 22-25 |
| Récap + Questions | 7 min | 26-28 |
| **TOTAL** | **~55 min** | |

*Reste 5 minutes pour le questionnaire d'évaluation*

## 🎨 Personnalisation

### Modifier le thème

Dans l'en-tête du fichier, vous pouvez changer :

```yaml
---
theme: default  # ou gaia, uncover
backgroundColor: #fff
---
```

### Ajouter des images

```markdown
![width:500px](chemin/vers/image.png)
```

### Créer une slide de titre

```markdown
<!-- _class: lead -->
# Mon Titre
```

## 📝 Notes pour l'enseignant

### Points d'interaction suggérés

- **Slide 8** : Faire chercher les coordonnées du lycée en direct
- **Slide 13** : Faire calculer ensemble la distance
- **Slide 17** : Analyser une trame NMEA en direct
- **Slide 24** : Ouvrir un débat sur la vie privée

### Matériel nécessaire

- Vidéoprojecteur ou écran
- Connexion Internet (pour les liens vers outils en ligne)
- Smartphones des élèves (optionnel, pour l'activité coordonnées)

## 🔗 Ressources complémentaires

- [Documentation Marp](https://marpit.marp.app/)
- [Exemples de thèmes](https://github.com/marp-team/marp-core/tree/main/themes)
- [Marp VS Code Extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)

## 📋 Questionnaire d'évaluation

Après la présentation, distribuer :

- **Pour les élèves** : `questionnaire_eleves.md` (version imprimable)
- **Pour l'enseignant** : `questionnaire_corrige.md` (avec barème)

**Durée** : 5 minutes  
**Format** : QCM + questions courtes  
**Total** : 29 points (+ 3 bonus)

## 💡 Conseils pédagogiques

1. **Interaction** : Poser des questions régulièrement
2. **Exemples concrets** : Utiliser des situations du quotidien
3. **Démonstrations** : Montrer Google Maps, NMEA Decoder en direct
4. **Participation** : Faire venir des élèves au tableau
5. **Rythme** : Adapter selon les réactions de la classe

## 🎯 Objectifs d'apprentissage

À la fin de la présentation, les élèves doivent être capables de :

✅ Définir la géolocalisation  
✅ Identifier les 3 coordonnées géographiques  
✅ Expliquer le principe de la trilatération  
✅ Comprendre le rôle des satellites  
✅ Décoder une trame NMEA simple  
✅ Identifier les enjeux de vie privée  

## 📞 Support

Pour toute question sur l'utilisation de Marp ou de la présentation, consulter :
- [FAQ Marp](https://github.com/marp-team/marp/discussions)
- [Documentation officielle](https://marp.app/)
