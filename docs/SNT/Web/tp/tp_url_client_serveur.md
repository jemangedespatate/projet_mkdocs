# TD : URLs et Modèle Client-Serveur

## Partie 1 : Décortiquer une URL

Une URL (*Uniform Resource Locator*) est l'adresse complète d'une ressource sur le Web. Elle est formée de plusieurs parties, chacune ayant un rôle précis.

### Rappel : Anatomie d'une URL

```
https://www.education.gouv.fr/programme-snt.html?lang=fr
  ↑           ↑                    ↑                 ↑
protocole  nom de domaine         chemin           paramètre
```

| Partie | Rôle |
|---|---|
| `https://` | **Protocole** : la « langue » utilisée pour communiquer avec le serveur |
| `www.education.gouv.fr` | **Nom de domaine** : l'adresse lisible du serveur |
| `/programme-snt.html` | **Chemin** : le fichier précis demandé sur le serveur |
| `?lang=fr` | **Paramètre** : une information supplémentaire envoyée au serveur |

---

!!! question "Exercice 1 : Identifier les composants d'une URL"

    Analysez chacune des URLs ci-dessous et complétez le tableau sur votre feuille (ou cahier) en identifiant le **protocole**, le **nom de domaine**, le **chemin** et les **paramètres** (s'il y en a).

    | # | URL |
    |---|---|
    | 1 | `https://www.wikipedia.org/wiki/Internet` |
    | 2 | `http://moodle.lycee.fr/login/index.php?lang=fr` |
    | 3 | `https://www.youtube.com/watch?v=dQw4w9WgXcQ` |
    | 4 | `https://maps.google.fr/maps?q=Paris` |

    **Questions :**

    1. Pour l'URL n°2, quel protocole est utilisé ? Est-ce que cela vous semble sécurisé ? Pourquoi ?
    2. Pour l'URL n°3, à votre avis, à quoi sert le paramètre `v=dQw4w9WgXcQ` ?
    3. Pour l'URL n°4, que se passera-t-il probablement si vous remplacez `Paris` par `Lyon` dans l'URL ?

---

!!! question "Exercice 2 : Le DNS — Traduire un nom en adresse IP"

    Comme vu en cours, les ordinateurs ne comprennent pas les noms de domaine : ils travaillent avec des **adresses IP** (une suite de chiffres comme `142.251.209.131`). C'est le **DNS** (*Domain Name System*) qui fait la traduction.

    **Faites le test suivant :**

    1. Ouvrez un nouvel onglet dans votre navigateur.
    2. Dans la barre d'adresse, tapez exactement : `142.251.209.131` puis appuyez sur Entrée.
    3. Que se passe-t-il ? Quel site s'affiche ?

    **Questions :**

    1. Expliquez avec vos propres mots à quoi sert le DNS.
    2. Pourquoi a-t-on inventé les noms de domaine plutôt que de laisser les utilisateurs taper des adresses IP ?
    3. Décomposez le nom de domaine `www.ac-versailles.fr` : que signifie chaque partie (www, ac-versailles, fr) ?

---

!!! question "Exercice 3 : Construire ses propres URLs"

    À votre tour de créer des URLs ! En vous basant sur la structure vue en cours, **inventez** les URLs correspondant aux descriptions suivantes. Vous pouvez utiliser des noms de domaine fictifs.

    | Description | URL à construire |
    |---|---|
    | La page d'accueil d'un site fictif de cinéma nommé `cineclub.fr` (protocole sécurisé) | |
    | La page `/films/aventure.html` du même site | |
    | La même page, mais avec un paramètre `?annee=2024` pour filtrer par année | |
    | Une recherche du mot `Matrix` sur un moteur fictif `recherche.fr` via le paramètre `q` | |

    **Défi :** Écrivez également l'URL d'un site de votre choix (réel ou fictif), puis échangez avec votre voisin·e pour qu'il ou elle la décompose.

---

## Partie 2 : Le Modèle Client-Serveur

À chaque fois que vous visitez un site web, un **dialogue** invisible se déroule entre votre navigateur (le **client**) et un ordinateur distant (le **serveur**). Comprendre ce dialogue, c'est comprendre comment fonctionne tout le Web.

### Rappel : Le dialogue Client-Serveur

```
   [Votre navigateur]          [Serveur du site]
        CLIENT          →  Requête HTTP  →   SERVEUR
        CLIENT          ←  Réponse HTTP  ←   SERVEUR
```

1. Le **client** (votre navigateur) envoie une **requête** : « Donne-moi la page `/index.html` ! »
2. Le **serveur** cherche la ressource et envoie une **réponse** : la page HTML, les images, etc.
3. Le navigateur **affiche** le tout à l'écran.

---

!!! question "Exercice 4 : Schématiser le modèle client-serveur"

    Lisez le scénario suivant, puis répondez aux questions sur votre feuille.

    > *Lucas ouvre Google Chrome sur son ordinateur. Il tape `https://www.wikipedia.org/wiki/Jeu_video` dans la barre d'adresse et appuie sur Entrée. Quelques instants plus tard, la page Wikipédia s'affiche.*

    **Questions :**

    1. Dans ce scénario, qui est le **client** ?
    2. Qui est le **serveur** ?
    3. Quelle ressource précise le client demande-t-il au serveur ? (Aidez-vous du chemin dans l'URL.)
    4. **Schéma :** Sur votre feuille, dessinez le dialogue client-serveur correspondant à ce scénario. Représentez l'ordinateur de Lucas, le serveur de Wikipédia, et les deux flèches (requête et réponse) en indiquant ce qui est échangé.

---

!!! question "Exercice 5 : Les codes de réponse HTTP"

    Quand un serveur répond à un client, il envoie toujours un **code de statut** pour indiquer si tout s'est bien passé (ou pas !).

    Voici les codes les plus courants :

    | Code | Signification |
    |---|---|
    | **200** | ✅ OK — La ressource a été trouvée et envoyée avec succès |
    | **301** | ↩️ Redirection — La page a changé d'adresse |
    | **403** | 🚫 Interdit — Vous n'avez pas le droit d'accéder à cette ressource |
    | **404** | ❌ Introuvable — La ressource demandée n'existe pas sur ce serveur |
    | **500** | 💥 Erreur serveur — Le serveur a rencontré un problème |

    **Questions :**

    1. Vous tapez une URL avec une faute de frappe (ex: `/programme-sntt.html` au lieu de `/programme-snt.html`). Quel code de réponse recevrez-vous probablement ? Pourquoi ?
    2. Vous essayez d'accéder à un espace élève réservé sans vous connecter. Quel code de réponse est le plus probable ?
    3. Avez-vous déjà rencontré une page avec le message **« 404 Not Found »** ? Dans quel contexte ? Expliquez maintenant ce que cela signifie techniquement.
    4. **Défi :** Que se passe-t-il côté serveur quand il renvoie un code **200** ? Décrivez les étapes depuis la réception de la requête jusqu'à l'envoi de la réponse.

---

!!! question "Exercice 6 : Simuler une conversation Client-Serveur"

    Vous allez jouer le rôle du client **ET** du serveur.

    **Mise en situation :**  
    Imaginez que vous êtes le serveur du site `www.monlycee.fr`. Ce serveur contient les fichiers suivants :

    ```
    /index.html         → page d'accueil du lycée
    /emploi-du-temps.html → page des emplois du temps
    /cantine.html       → page du menu de la cantine
    /admin/notes.html   → page réservée aux professeurs (accès restreint)
    ```

    Pour chacune des requêtes ci-dessous, indiquez :
    - Le **code de réponse** que le serveur enverrait.
    - Ce que le serveur renverrait (la page, ou un message d'erreur).

    | Requête reçue par le serveur | Code réponse | Ce que le serveur renvoie |
    |---|---|---|
    | `GET /index.html` | | |
    | `GET /programme-annuel.html` | | |
    | `GET /cantine.html` | | |
    | `GET /admin/notes.html` (depuis un élève non connecté) | | |

---

## Partie 3 : Synthèse et Bilan

!!! question "Exercice 7 : Questions de synthèse"

    Répondez aux questions suivantes en rédigeant des réponses complètes (2 à 3 phrases chacune).

    1. **Expliquez** ce qu'est une URL et à quoi elle sert, comme si vous l'expliquiez à quelqu'un qui ne connaît pas le Web.
    2. **Quelle est la différence** entre le Web et Internet ? Quel lien y a-t-il entre les deux ?
    3. **Décrivez** ce qui se passe, étape par étape, quand vous tapez `https://www.google.fr` dans votre navigateur et appuyez sur Entrée. Mentionnez au moins : le DNS, la requête HTTP, le serveur et la réponse.
    4. Pourquoi le protocole `https` est-il préférable à `http` ? Dans quelles situations est-il particulièrement indispensable ?

---

!!! tip "Pour aller plus loin"

    Si vous avez terminé, vous pouvez explorer les outils de développement de votre navigateur :

    1. Ouvrez une page web (ex: `https://www.wikipedia.org`).
    2. Appuyez sur **F12** pour ouvrir les outils développeur.
    3. Cliquez sur l'onglet **« Réseau »** (*Network*).
    4. Rechargez la page (**F5**).

    Vous verrez en temps réel toutes les **requêtes HTTP** envoyées par votre navigateur et les **codes de réponse** renvoyés par les serveurs. Pouvez-vous retrouver des codes **200** ? Des ressources chargées (images, fichiers CSS) ?

    Notez ce que vous observez et partagez vos découvertes avec la classe !
