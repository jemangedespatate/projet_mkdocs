# Activité Introductive : Jigsaw sur le modèle TCP/IP

## Objectifs de l'activité
- Comprendre l'architecture en couches d'Internet.
- Étudier le rôle de chaque couche du modèle TCP/IP.
- Développer sa capacité à synthétiser et expliquer un concept technique.
- Travailler en coopération (méthode Jigsaw).

---

## Phase 1 : Les Ateliers Experts

*Formez 4 groupes d'experts. Chaque groupe travaille sur l'un des ateliers ci-dessous. Votre objectif est de devenir le spécialiste de cette couche du modèle TCP/IP pour pouvoir l'expliquer ensuite à vos camarades.*

---

### Atelier 1 : La Couche Application

**Texte 1 : Le rôle de la couche Application**  
Cette couche regroupe les protocoles (règles de communication) utilisés par vos logiciels (navigateur web, messagerie, jeux en ligne). Son rôle principal est de mettre en forme les données pour qu'elles soient compréhensibles par les utilisateurs et les logiciels finaux. 

**Texte 2 : L'analogie de la lettre**  
Si l'on compare la communication réseau à l'envoi d'un courrier classique, la couche Application représente le moment où vous rédigez le contenu de la lettre sur une feuille de papier, dans une langue compréhensible par votre correspondant (français, anglais, etc.). Vous définissez ce que vous voulez dire.

**Texte 3 : Les protocoles phares**  
Chaque service internet a son propre langage (protocole) à cette couche :
- **HTTP / HTTPS** : Pour naviguer sur le Web (transférer des pages web).
- **SMTP, IMAP, POP** : Pour envoyer et recevoir des emails.
- **DNS** : Pour traduire un nom de domaine (`www.google.fr`) en adresse IP compréhensible par la machine.

**Questions pour guider l'expertise :**
1. Quelle est la fonction principale de la couche Application ?
2. Quel protocole entre en jeu lorsque vous consultez un site web ? Et lorsque vous envoyez un email ?
3. La couche Application se préoccupe-t-elle de la manière dont les données circulent dans les câbles ?
4. Donnez un exemple de logiciel que vous utilisez tous les jours et qui dépend directement de cette couche.

---

### Atelier 2 : La Couche Transport

**Texte 1 : Le rôle de la couche Transport**  
La couche Transport récupère les données pour les découper en petits morceaux appelés **segments**. Elle s'occupe de gérer la connexion de bout en bout entre les deux ordinateurs communicants. Elle utilise des **ports** (sortes de portes numérotées) pour s'assurer que les données arrivent au bon logiciel sur l'ordinateur cible (par exemple le port 80 pour le web, le port 25 pour les mails).

**Texte 2 : L'analogie du centre de tri postal**  
Imaginez que vous deviez envoyer un livre entier par la poste, mais que vous n'ayez que de petites enveloppes. La couche Transport est comme le centre de tri qui va découper le livre page par page, mettre chaque page dans une enveloppe numérotée, et vérifier à l'arrivée que toutes les pages sont bien reçues et dans le bon ordre.

**Texte 3 : TCP et UDP, deux visions différentes**  
Il existe deux protocoles majeurs dans cette couche :
- **TCP** (Transmission Control Protocol) : Il est fiable. Il vérifie que chaque segment arrive à destination. S'il en manque un, il demande un renvoi. Il est utilisé pour le Web ou le transfert de fichiers où l'intégrité est primordiale.
- **UDP** (User Datagram Protocol) : Il est très rapide, mais ne vérifie pas la réception. S'il y a une perte, tant pis. Il est utilisé pour le streaming vidéo ou les jeux en ligne en temps réel.

**Questions pour guider l'expertise :**
1. Pourquoi est-il souvent nécessaire de découper les données (en segments) avant de les envoyer sur le réseau ?
2. Expliquez la différence de fonctionnement et d'objectif entre TCP et UDP.
3. À quoi sert le numéro de "port" dans cette couche ?
4. Que se passerait-il si le "centre de tri postal" oubliait de numéroter les enveloppes avant de les expédier ?
5. Dans le cas du transfert d'un fichier très important, le protocole UDP serait-il un bon choix ? Pourquoi ?

---

### Atelier 3 : La Couche Internet

**Texte 1 : Le rôle de la couche Internet**  
Cette couche s'occupe de l'adressage logique et du routage. Elle organise les données en **paquets** en y ajoutant une adresse d'expédition et de destination : **l'adresse IP** (Internet Protocol). Son but est de trouver le meilleur chemin à travers les multiples réseaux mondiaux pour atteindre l'ordinateur cible.

**Texte 2 : L'analogie du GPS et des carrefours**  
La couche Internet fonctionne comme un immense système GPS. Le courrier est remis à des aiguilleurs appelés **routeurs**. Chaque routeur lit l'adresse IP de destination et décide de la route à prendre au prochain croisement. Si une route est bloquée (panne), le routeur calcule dynamiquement un chemin alternatif.

**Texte 3 : L'adresse IP**  
L'adresse IP (IPv4 ou IPv6) est unique à un instant T pour chaque équipement connecté à Internet. Elle permet de localiser l'appareil mondialement (comme une adresse postale avec le pays, la ville, la rue et le numéro). Le protocole dominant ici est le protocole **IP**.

**Questions pour guider l'expertise :**
1. Quel est le rôle principal d'un routeur dans la couche Internet ?
2. À quoi sert concrètement une adresse IP lors de l'envoi d'un paquet de données ?
3. Que se passe-t-il au niveau de cette couche si une ligne internet entre deux grandes villes est physiquement coupée ?
4. D'après vous, l'adresse IP est-elle fixée définitivement à la fabrication de l'ordinateur ou peut-elle changer selon le réseau sur lequel on se connecte ?

---

### Atelier 4 : La Couche Accès Réseau

**Texte 1 : Le rôle de la couche Accès Réseau**  
Cette couche transforme les données en impulsions électriques, lumineuses ou ondes électromagnétiques pour les envoyer physiquement sur le support (câble, fibre, air). Les données à ce stade sont organisées en **trames**. Elle utilise une adresse physique matérielle fixe sur l'équipement : **l'adresse MAC**.

**Texte 2 : L'analogie des moyens de transport**  
Dans la métaphore du courrier, la couche Accès Réseau représente le moyen de locomotion physique lui-même : est-ce que le colis va voyager par un avion cargo (fibre optique), par une camionnette (câble Ethernet) ou par un bateau (Wi-Fi) ?

**Texte 3 : Les supports de transmission et matériels**  
Cette couche intègre le matériel électronique des cartes réseaux, des antennes ou des câbles. Elle gère par exemple :
- **Ethernet** pour les câbles réseau en cuivre.
- **Wi-Fi** ou **4G/5G** pour les ondes radio.
- **Fibre optique** pour la transmission par impulsions lumineuses.
Les équipements typiques sont les câbles, les cartes réseaux de nos PC et les switchs (commutateurs).

**Questions pour guider l'expertise :**
1. Sous quelles formes physiques les données peuvent-elles voyager à travers les réseaux ?
2. Quelle est la différence de fonction entre une adresse IP et une adresse MAC ?
3. Si vous connectez votre ordinateur à une box avec un câble RJ45 au lieu du Wi-Fi, cela change-t-il le fonctionnement de cette couche ? Pourquoi ?
4. Pourquoi l'adresse MAC est-elle souvent comparée à la plaque d'immatriculation gravée sur le châssis d'une voiture en usine ?
5. Expliquez pourquoi aucune donnée ne pourrait jamais quitter votre ordinateur sans cette couche précise.

---

## Phase 2 : Mise en commun et Trace écrite

*Recomposez de nouveaux groupes (les "groupes d'apprentissage") de manière à avoir **au moins un expert de chaque atelier** dans chaque nouveau groupe.*

### Étape A : Partage des connaissances
Tour à tour, chaque expert dispose de **3 à 4 minutes** pour présenter sa couche réseau aux autres membres du groupe en s'appuyant sur ce qu'il a compris et sur les réponses aux questions de son atelier. L'objectif est que tous les membres du groupe comprennent l'ensemble du modèle TCP/IP de bout en bout.

### Étape B : Production de la trace écrite
En groupe, vous allez produire une synthèse commune de vos échanges.

**Travail à réaliser :**
Sur une feuille ou un document numérique, construisez un **schéma du modèle TCP/IP** qui synthétise son fonctionnement global.
Votre schéma devra obligatoirement faire apparaître pour chacune des 4 couches, de haut en bas (Application, Transport, Internet, Accès Réseau) :
1. Le nom de la couche.
2. Une courte phrase résumant son rôle essentiel.
3. L'unité de donnée manipulée (Message, Segment, Paquet ou Trame).
4. Au moins deux exemples de protocoles ou d'équipements qui lui sont associés.
