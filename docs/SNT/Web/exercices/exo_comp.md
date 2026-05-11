# Exercices complémentaires : Web et Modèle Client-Serveur

Ces exercices permettent d'approfondir les notions d'URL, de dialogue HTTP et d'arborescence serveur. Ils sont destinés aux élèves ayant déjà terminé le TP de base.

---

!!! question "Exercice 1 : L'URL « tout-en-un » (Ancres et Multi-paramètres)"

    On analyse souvent des URLs simples, mais elles peuvent contenir d'autres informations. Observez celle-ci :
    `https://fr.wikipedia.org/wiki/Web#Histoire?uselang=fr&action=view`

    **Questions :**

    1. **L'Ancre (`#`) :** À quoi sert la partie `#Histoire` à votre avis ? Que se passe-t-il à l'écran si on charge cette URL ? rechercher comment fonctionne une ancre sur internet .
    2. **Multi-paramètres :** Combien de paramètres sont envoyés au serveur ici ? Quel symbole permet de les séparer ?

---

!!! question "Exercice 2 : Dans la peau d'un administrateur système (Arborescence)"

    Un serveur web est avant tout un ordinateur avec des dossiers. L'URL reflète souvent cette organisation.
    Imaginez l'arborescence de fichiers suivante sur le serveur `lycee-fictif.fr` :

    *   📂 `racine`
        *   📄 `index.html` (Accueil)
        *   📂 `snt`
            *   📄 `cours.pdf`
            *   📂 `tp`
                *   📄 `tp1.html`
                *   🖼️ `schema.png`

    **Questions :**

    1. Quelle est l'URL complète pour accéder au fichier `tp1.html` ?
    2. Si un élève tape `https://lycee-fictif.fr/snt/`, quel fichier le serveur va-t-il chercher à envoyer par défaut (même s'il n'est pas précisé dans l'URL) ?
    3. Un utilisateur tente d'accéder à `https://lycee-fictif.fr/snt/tp/photo.jpg`. Quel code de statut HTTP le serveur va-t-il renvoyer ? Pourquoi ?

---

!!! question "Exercice 3 : L'illusion d'une seule requête (Outils de développement)"

    *Nécessite un ordinateur avec accès au navigateur.*

    1. Ouvrez le site `https://www.wikipedia.org`.
    2. Appuyez sur **F12** (ou clic droit > Inspecter) et allez dans l'onglet **Réseau (Network)**.
    3. Actualisez la page (**F5**).
    4. **Observation :** Regardez la liste qui s'affiche.
        * Y a-t-il une seule ligne ou plusieurs dizaines ?
        * Trouvez une ligne où le "Type" est `png`, `jpg` ou `svg`. À quoi correspond cette requête ?
        * **Conclusion :** Expliquez pourquoi on dit qu'afficher une seule page web nécessite en réalité des dizaines de dialogues client-serveur.

---

!!! question "Exercice 4 : Le mystère de la redirection (Code 301/302)"

    Parfois, le serveur répond : *"La ressource n'est plus ici, allez là-bas"*. C'est une redirection.

    1. Dans votre navigateur, tapez l'URL suivante exactement : `http://google.fr` (sans le `s` de https et sans les `www`).
    2. Observez bien la barre d'adresse une fois la page chargée. Que s'est-il passé ?
    3. Techniquement, quel code de statut le serveur a-t-il probablement envoyé au navigateur pour faire ce changement automatiquement ?
    4. Pourquoi est-ce indispensable pour la sécurité des utilisateurs que le serveur force le passage de `http` à `https` ?

---

!!! tip "Défi pour les experts (Vers la NSI)"

    *   **User-Agent :** Dans l'onglet Réseau, cliquez sur la toute première requête et cherchez le "User-Agent" dans les en-têtes (Headers). Comment le serveur sait-il si vous utilisez un iPhone ou un PC sous Windows ?
    *   **Stateless :** Si le protocole HTTP ne "garde rien en mémoire", comment se fait-il que vous restiez connecté à votre compte sur un site même si vous changez de page ? (Indice : cherchez le mot "Cookie").