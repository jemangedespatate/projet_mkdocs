# TP : Simulation de réseaux avec Filius

**Durée :** 2 heures
**Objectif :** Mettre en pratique les notions vues lors du Jigsaw sur le modèle TCP/IP en construisant et en configurant un réseau virtuel complet de bout en bout à l'aide du logiciel éducatif Filius.

---

## Introduction à Filius

Filius est un logiciel qui permet de simuler graphiquement des réseaux informatiques. Il possède deux modes principaux :
- **Mode Conception (Marteau) :** Pour ajouter des machines, des câbles, et configurer le matériel et les adresses IP.
- **Mode Simulation (Flèche verte) :** Pour installer des logiciels sur les machines virtuels, tester les connexions (lignes de commande) et observer les échanges de données.

> 💡 **Conseil :** Passez en mode Simulation pour tester votre réseau, mais n'oubliez pas de revenir en mode Conception si vous devez modifier les adresses IP ou les câbles.

---

## Partie 1 : Création d'un réseau local (Couches Accès Réseau & Internet)

### 1.1 Mise en place du matériel (Couche Accès Réseau)
1. En mode **Conception**, placez sur l'espace de travail :
   - Deux ordinateurs portables (Portable 1 et Portable 2).
   - Un commutateur (Switch).
2. Reliez les deux portables au commutateur à l'aide de câbles.
3. Double-cliquez sur l'un des portables pour voir sa configuration.
   - *Question 1 : Quelle est l'adresse physique (adresse MAC) de cet ordinateur ? En vous rappelant du Jigsaw, à quelle couche du modèle TCP/IP cette adresse appartient-elle ?*

### 1.2 Configuration logique (Couche Internet)
Pour que les machines communiquent, l'adresse MAC ne suffit pas, il leur faut une adresse logique.
1. Toujours dans la configuration du portable, attribuez les adresses IP suivantes :
   - Portable 1 : `192.168.1.10`
   - Portable 2 : `192.168.1.20`
   *(Laissez le masque de sous-réseau par défaut : `255.255.255.0`)*
2. Passez en mode **Simulation**.
3. Cliquez sur le Portable 1, installez le logiciel **Ligne de commande** et démarrez-le.
4. Tapez la commande `ping 192.168.1.20` pour tester la connexion vers le Portable 2.
   - *Question 2 : Le test est-il réussi ? À quoi sert concrètement la commande "ping" d'après le résultat affiché ?*
   - *Question 3 : À quelle couche du modèle TCP/IP appartient l'adresse IP (192.168.1.20) utilisée ici ?*

---

## Partie 2 : Le Routage (Couche Internet approfondie)

Nous allons maintenant connecter notre réseau local à un autre réseau extérieur (comme si nous nous connections à Internet).

1. Repassez en mode **Conception**.
2. Ajoutez un **Routeur** sur l'espace de travail.
3. Ajoutez un **Serveur** et reliez-le au routeur.
4. Reliez également le commutateur (Switch) de votre premier réseau local au routeur.
5. **Configuration du Routeur :**
   Le routeur fait le pont entre deux réseaux, il a donc besoin d'une adresse IP pour chacun d'eux (une "patte" dans chaque réseau) :
   - Côté réseau local (Interface 1) : `192.168.1.254`
   - Côté serveur (Interface 2) : `10.0.0.254`
6. **Configuration du Serveur :** 
   - Adresse IP : `10.0.0.50`
   - Passerelle (Gateway) : `10.0.0.254` *(C'est l'adresse du routeur, sa "porte de sortie")*.
7. **Configuration des Portables :**
   - Retournez dans la configuration des portables 1 et 2 et renseignez l'adresse de la **Passerelle** : `192.168.1.254`.
8. En mode **Simulation**, ouvrez la ligne de commande du Portable 1 et faites un `ping 10.0.0.50`.
   - *Question 4 : Expliquez avec vos mots le rôle de la "Passerelle" (Gateway) sur un ordinateur. Que se passerait-il si l'on oubliait de la configurer sur le Portable 1 ?*

---

## Partie 3 : Service Web et Ports (Couches Transport et Application)

L'adresse IP permet de trouver la machine, mais comment trouver le bon logiciel sur le serveur ciblé ? C'est le rôle des ports (Couche Transport).

1. En mode **Simulation**, cliquez sur le Serveur (`10.0.0.50`) et installez le logiciel **Serveur Web**. Démarrez-le.
   - *Observez bien : sur quel numéro de **port** le serveur Web est-il en écoute ?*
2. Sur le Portable 1, installez le logiciel **Navigateur Web**.
3. Ouvrez le navigateur et tapez l'adresse `http://10.0.0.50`. Une page d'accueil (le site web du serveur) devrait s'afficher.

### Observation des échanges à la loupe
Filius permet de regarder "à l'intérieur" des câbles pour analyser les protocoles.
4. Faites un clic droit sur le Portable 1 et choisissez **Afficher les échanges de données**.
5. Rechargez la page web dans le navigateur du Portable 1.
6. Dans la fenêtre d'échange, observez les différentes lignes apparues et cliquez dessus pour explorer le détail des couches sur la droite.
   - *Question 5 : Quel protocole de la couche **Application** est utilisé pour récupérer et afficher la page web ?*
   - *Question 6 : Quel protocole de la couche **Transport** est utilisé pour cet échange web ? (Regardez les détails du segment).*
   - *Question 7 : On remarque que la communication commence par 3 messages "à vide" (SYN, SYN+ACK, ACK) avant même que la page web ne soit demandée. Rappelez-vous du rôle du "centre de tri postal" : pourquoi ce protocole spécifique a-t-il besoin de faire cela ?*

---

## Partie 4 : Nom de domaine DNS (Couche Application)

Les humains préfèrent retenir des mots (`www.google.com`) plutôt que des suites de chiffres (`10.0.0.50`). Nous allons configurer l'annuaire du réseau : un serveur DNS.

1. En mode **Conception**, supprimez le câble entre le serveur web et le routeur. Mettez un Switch à la place pour pouvoir relier plusieurs serveurs au routeur.
2. Ajoutez un nouveau Serveur et reliez-le à ce switch.
3. Configurez ce nouveau serveur : 
   - IP : `10.0.0.53`
   - Passerelle : `10.0.0.254`
4. En mode **Simulation**, installez-y le logiciel **Serveur DNS**.
5. Dans le Serveur DNS, ajoutez un nouvel enregistrement (Type A) :
   - Nom de domaine : `www.nsi-lycee.fr`
   - Adresse IP : `10.0.0.50` (l'adresse de notre serveur Web).
   - Cliquez sur "Ajouter" et **démarrez le serveur DNS**.
6. Sur vos Portables 1 et 2, en mode **Conception**, configurez enfin le champ **Serveur DNS** avec l'adresse IP de notre annuaire : `10.0.0.53`.
7. En mode **Simulation**, retournez sur le navigateur web du Portable 1. Tapez l'URL `http://www.nsi-lycee.fr`. La page doit s'afficher magiquement !

### Observation finale
8. Videz la fenêtre **"Afficher les échanges de données"** du Portable 1, puis rechargez la page `www.nsi-lycee.fr`.
   - *Question 8 : Quel protocole de la couche **Transport** est utilisé pour interroger le serveur DNS ? À l'inverse de la question 7, pourquoi utiliser celui-ci pour une requête DNS ?*
   - *Question 9 : Pour afficher `www.nsi-lycee.fr`, votre ordinateur a dû envoyer deux requêtes distinctes (faisant appel à deux protocoles de la couche Application différents). Quelles sont-elles et dans quel ordre se déroulent-elles ?*

---

## 📝 Bilan de TP : Synthèse des Couches

À la fin de ce TP, vous devez être capable de relier concrètement ce que vous avez manipulé aux 4 couches du modèle TCP/IP étudiées précédemment :

- **Couche Accès Réseau (Matérielle)** : L'utilisation des câbles virtuels, le placement des switchs, la présence des adresses MAC sur chaque carte réseau.
- **Couche Internet (Routage)** : La configuration des adresses IP, l'utilisation du routeur et de la notion de "passerelle" pour sortir du réseau local.
- **Couche Transport (Connexion)** : L'importance du **port 80** pour cibler le service web, la différence visible entre l'utilisation de **TCP** (fiable, avec la poignée de main SYN/ACK) et **UDP** (rapide, utilisé pour le DNS).
- **Couche Application (Usage)** : L'installation de logiciels métiers (Navigateur, Serveur Web, Serveur DNS) discutant via leurs propres langages (**HTTP**, **DNS**).
