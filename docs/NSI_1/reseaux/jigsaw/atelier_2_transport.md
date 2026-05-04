# Atelier 2 : La Couche Transport

## Documents de travail

**Texte 1 : Le rôle de la couche Transport**  
La couche Transport récupère les données pour les découper en petits morceaux appelés **segments**. Elle s'occupe de gérer la connexion de bout en bout entre les deux ordinateurs communicants. Elle utilise des **ports** (sortes de portes numérotées) pour s'assurer que les données arrivent au bon logiciel sur l'ordinateur cible (par exemple le port 80 pour le web, le port 25 pour les mails).

**Texte 2 : L'analogie du centre de tri postal**  
Imaginez que vous deviez envoyer un livre entier par la poste, mais que vous n'ayez que de petites enveloppes. La couche Transport est comme le centre de tri qui va découper le livre page par page, mettre chaque page dans une enveloppe numérotée, et vérifier à l'arrivée que toutes les pages sont bien reçues et dans le bon ordre.

**Texte 3 : TCP et UDP, deux visions différentes**  
Il existe deux protocoles majeurs dans cette couche :
- **TCP** (Transmission Control Protocol) : Il est fiable. Il vérifie que chaque segment arrive à destination. S'il en manque un, il demande un renvoi. Il est utilisé pour le Web ou le transfert de fichiers où l'intégrité est primordiale.
- **UDP** (User Datagram Protocol) : Il est très rapide, mais ne vérifie pas la réception. S'il y a une perte, tant pis. Il est utilisé pour le streaming vidéo ou les jeux en ligne en temps réel.

---

## Questions pour guider l'expertise

1. Pourquoi est-il souvent nécessaire de découper les données (en segments) avant de les envoyer sur le réseau ?
2. Expliquez la différence de fonctionnement et d'objectif entre TCP et UDP.
3. À quoi sert le numéro de "port" dans cette couche ?
4. Que se passerait-il si le "centre de tri postal" oubliait de numéroter les enveloppes avant de les expédier ?
5. Dans le cas du transfert d'un fichier très important, le protocole UDP serait-il un bon choix ? Pourquoi ?

!!! important "RÈGLE D'OR"
    **INTERDICTION DE PRENDRE DES NOTES !**  
    L'objectif est de comprendre le maximum. À la fin du temps imparti, ce document vous sera retiré.
