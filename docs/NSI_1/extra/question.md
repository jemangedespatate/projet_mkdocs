## question 1

nom : Maillet Odin
groupe : #2BFAFA
difficulte : moyenne
énoncé : 

Bastien a ecrit un code python suivant:
```
liste[0],liste[1] = liste[1],liste[0]
```
Que permet-il d'effectuer ?

réponse : il permet d'échanger les deux premiers éléments de la liste

## question 2

nom : Maillet Odin
groupe : #2BFAFA
difficulte : difficile
énoncé : 

Jeanne a ecrit le code suivant :
```
import math

x1 = 2
x2 = 5
y1 = 2
y2 = 6

def distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

distance(x1,x2,y1,y2)
```
Quel résultat est attendu ?

réponse : 5

## question 3

nom : Antonin
groupe : #2BFAFA
difficulte : moyenne
énoncé : 

comment passer d'une base 10 à une base 2 ?

réponse : 

- on divise par 2
- on note le reste
- on lit les restes à l'envers

## question 4

nom : Margaret
groupe : #2BFAFA
difficulte : moyenne
énoncé : 

dans un fichier html relié à un fichier css, comment donner une apparence différente à deux paragraphes qui possèdent la même classe ?

réponse : 

mettre des <id>

## question 5

nom : Antonin
groupe : #2BFAFA
difficulte : facile
énoncé : 

quelle est la différence entre un tri par insertion et un tri par sélection ?

réponse :

le tri par sélection parcourt la liste pour trouver le plus petit alors que le tri par insertion met la valeur directement à son emplacement dans la nouvelle liste

## question 6

nom : Margaret
groupe : #2BFAFA
difficulte : difficile
énoncé : 

en langage assembleur, faire 5*3 et enregistrer le résultat en mémoire place 100

réponse : 

```
MOV R0, #5
boucle :
SUB R0, R0, #1
ADD R1, R1, #3
CMP R0, #0
BNE boucle
STR R1, 100
HALT
```

## question 7

nom : Antonin
groupe : #2BFAFA
difficulte : moyenne
énoncé : 

quelle est la date de la création de l'architecture de Von Neumann ?

réponse : 1946

## question 8

nom : Margaret
groupe : #2BFAFA
difficulte : moyenne
énoncé : 

en langage assembleur, effectuer le calcul 5 + 2 et le ranger en mémoire place 60

réponse : 

MOV R0, #5
MOV R1, #2
ADD R1, R0, R1
STR R1, 60

## question 9

nom : Antonin
groupe : #2BFAFA
difficulte : moyenne
énoncé : 

à quoi sert la première ligne d'un fichier csv ?

réponse : 

elle sert à donner un nom aux valeurs de la colonne en dessous et à une clé aux valeurs si un dictionnaire est créé (tout ce qui s'approche de cette réponse est correct, à l'appréciation du professeur (c'est moi))

## question 10

nom : Margaret
groupe : #2BFAFA
difficulte : facile
énoncé : 

que renvoie la ligne de code: print(liste[-1]) ?

réponse : elle renvoie le dernier élément de la liste

## question 11

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

quel est le type de `True` et de `False` en python?

réponse : 

```
bool
```

## question 12

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

comment faire une puissance sur Python?

réponse : 

```
**
```

## question 13

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

que va afficher le code suivant?

```
for i in range(8):
    print(i)
```
réponse : 

```
0
1
2
3
4
5
6
7
```

## question 14

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

comment ecrire une liste dans Python ?

réponse : 

```
avec les crochets: []
```

## question 15

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

quelle est la difference entre une liste et un tuple en python?

réponse : 

```
une liste est mutable et un tuple est immuable
```

## question 16

nom : Auguste 
groupe : Rose
difficulte : moyen
énoncé : 

que va faire ce programme?

```
liste=[
    eleve1 = { meilleur= 19.5, pire = 5, moyenne= 17, appr="Bien"},
    eleve2 = { meilleur= 20, pire = 20, moyenne= 20, appr="Tres bien"},
    eleve3 = { meilleur= 10, pire = 3, moyenne= 6.75, appr="Mauvais"}
]

print(liste[eleve1]["appr"])
```

réponse : 

```
une erreur car on ne peut pas accéder a un dictionnaire avec un indice
```

## question 17

nom : Auguste 
groupe : Rose
difficulte : moyen
énoncé : 

quels sont les composants essentiels d'un ordinateur?

processeur, carte mère, ram, alimentation, ventilateur

réponse : 

tous sauf le ventilateur


## question 18

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

Que permet le hashtag dans le langage assembleur?

réponse : 

de prendre la valeur numerique de la valeur

## question 19

nom : Auguste 
groupe : Rose
difficulte : moyen
énoncé : 

Quels sont les trois type de language ? donner des exemples

réponse : 

- machine : binaire
- bas niveau : assembleur
- langage evolué : python, java, c++, etc.

## question 20

nom : Auguste 
groupe : Rose
difficulte : moyen
énoncé : 

que signifie k-nn ?

réponse : 

```
K-nearest neighbors (k plus proches voisins)
k-plus-proches voisins
```

## question 21

nom : Auguste 
groupe : Rose
difficulte : facile
énoncé : 

Comment fonctionne la recherche dichotomique ?

réponse : 

```
on divise la liste en deux jusqu'a trouver la valeur
```

## question 22

nom : Auguste 
groupe : Rose
difficulte : moyen
énoncé : 

Comment lie-t-on une page web a une page html ?

réponse : 

```
<link rel="stylesheet" href="style.css">
```

## question 23

nom : Auguste 
groupe : Rose
difficulte : moyen
énoncé : 

que signifie html?

réponse : 

```
HyperText Markup Language
```

## question 24

nom : Auguste 
groupe : Rose
difficulte : difficile
énoncé : 

mettre 315 en binaire

réponse : 

```
100111001
```

## question 25

nom : Auguste 
groupe : Rose
difficulte : difficile
énoncé : 

mettre le nombre binaire 110001011 en decimal

réponse : 

```
395
```

# question 26

nom : Nathan D 
groupe : Rose
difficulte : facile
énoncé : 

quelle est la difference entre un int et un float en python?

réponse : 

```
un int est un nombre entier
un float est un nombre decimal
```

## question 27

nom : Nathan D 
groupe : Rose
difficulte : facile
énoncé : 

quelle-est le type de a ?

```
a = "123"
```

réponse : 

```
str
```

## question 28

nom : Nathan D 
groupe : Rose
difficulte : difficile
énoncé : 

que retourne la fonction ?

```
a = 10
b = 0
while a > 0:
    b += 1
return b
```

réponse : 

```
rien, la boucle est infinie
```

## question 29

nom : Nathan D 
groupe : Rose
difficulte : difficile
énoncé : 

qu'est ce qu'un registre en assembleur ?

réponse : 

```
endroit dans le CPU ou sont stocker des valeurs de facon ephemere
```

## question 30

nom : Nathan D 
groupe : Rose
difficulte : facile
énoncé : 

qu'elle est le principe du tri par insertion ?

réponse : 

```
On insere les valeurs au fur et a mesure dans une partie considerer comme deja trier
```

## question 31

nom : Nathan D 
groupe : Rose
difficulte : difficile
énoncé : 

en CSS, a quoi sert display: flex ?

réponse : 

```
cela permet de mettre cote a cote differents elements dans un html
```

## question 32

nom : Nathan D 
groupe : Rose
difficulte : difficile
énoncé : 

dans le CSS, a quoi servent les @keyframes ?

réponse : 

```
Sert a definir les etapes principales d'une animation
```

## question 33

nom : Nathan D 
groupe : Rose
difficulte : facile
énoncé : 

utiliser l'inteligence artificielle est-il ecologique ?

réponse : 

```
non, ca pollue
```

## question 34

nom : Lilou 
groupe : #2BFAFA
difficulte : facile
énoncé : 

A quel type de valeur est associer float ?

réponse : 

```
les nombres decimaux
```

## question 35

nom : Lilou 
groupe : #2BFAFA
difficulte : facile
énoncé : 

A quoi sert l'instruction LDR ?

réponse : 

```
charge une valeur dans l'adresse donner dans un registre
```

## question 36

nom : Lilou 
groupe : #2BFAFA
difficulte : moyen
énoncé : 

quel probleme pourrait-il avoir si l'on choisie un nombre pair avec KNN ?

réponse : 

```
si le nombre est pair, il se pourrait qu'il y est autant d'element dans chaque groupe 
```

## question 37

nom : Lilou 
groupe : #2BFAFA
difficulte : moyen
énoncé : 

quelle est la balise pour creer un bouton sur html?

réponse : 

```
<button></button>
```

## question 38

nom : Lilou 
groupe : #2BFAFA
difficulte : moyen
énoncé : 

qui a inventé le tout premier ordinateur ?

réponse : 

```
alan turing
```

## question 39

nom : Anonyme
groupe : Rose
difficulte : moyen
énoncé : 

qu'est ce qu'un str?
- un nombre entier
- une chaine de caractere
- un nombre decimal

réponse : 

```
une chaine de caracteres
```

## question 40

nom : Anonyme
groupe : Rose
difficulte : difficile
énoncé : 

quel nombre affiche se programme ?

```
a = 0
i = 5
while i >= 0:
    a += i
    for i in range(3):
        a += i
    i = i - 1
print(a)
```

- 20
- 60
- 100

réponse : 

```
60
```

## question 41

nom : Anonyme
groupe : Rose
difficulte : moyenne
énoncé : 

que fait l'action Fetch ?

réponse : 

```
rechercher
```

## question 42

nom : Anonyme
groupe : Rose
difficulte : moyen
énoncé : 

A quoi sert la commande LDR en language assembleur ?

réponse : 

```
charger depuis la memoire 
```

## question 43

nom : Anonyme
groupe : Rose
difficulte : difficile
énoncé : 

de quelle(s) nationnalité(s) était Von Neumann ?

réponse : 

```
Hongro-américain
```

## question 44

nom : Anonyme
groupe : Rose
difficulte : facile
énoncé : 

que signifie KNN?

- k-nearest neighbors
- k-Nocturn Nissan
- k-Nicolas Narcotraficant
- k-nearest Neldoors

réponse : 

```
k-nearest neighbors
```

## question 46

nom : Anonyme
groupe : Rose
difficulte : facile
énoncé : 

quel est la balise pour un lien ?

réponse : 

```
a
```

## question 47

nom : Gregoire
groupe : Vert
difficulte : facile
énoncé : 

il vaut mieux avoir un ssd ou un hdd pour les performance ?

réponse : 

```
Un ssd
```

## question 48

nom : Gregoire
groupe : Vert
difficulte : difficile
énoncé : 

citer les 4 grande partie d'un ordinateur selon le modèle de Von Neumann

réponse : 

```
UC
Memoire
entrée/sortie
Bus
```

## question 49

nom : Gregoire
groupe : Vert
difficulte : moyen
énoncé : 

citez les grandes etapes du cycle d'execution du modele de von neumann

réponse : 

```
1. Fetch
2. Decode
3. Execute
4. REPC
```

## question 50

nom : Gregoire
groupe : Vert
difficulte : facile

énoncé : 

expliquez le principe du tri a bulle 

réponse : 

```
On parcourt la liste plusieurs fois, et a chaque fois on compare les elements deux a deux, si le premier est plus grand que le second on les échange.
```

## question 52

nom : Gregoire
groupe : Vert
difficulte : moyen
énoncé : 

citez les deux parties principales d'une page web en html?

réponse : 

```
head et body
```

## question 53

nom : Gregoire
groupe : Vert
difficulte : facile
énoncé : 

citez 3 balise courament utiliser dans le HTML

réponse : 

```
p, h1, h2, h3, h4, h5, h6, div, span, a, img, button, input ...
```

## question 54

nom : Gregoire
groupe : Vert
difficulte : facile
énoncé : 

Alan Turing fut connue pourquoi? citez 2 exemples

réponse : 

```
- la resolution de l'enigme Enigma
- le developpement de l'informatique
```

## question 55

nom : Gregoire
groupe : Vert
difficulte : moyen

énoncé : 

vaut-il mieux mettre de beau nom de variable ou des lettres dans un programme?

réponse : 

```
De beaux nom de variables
```

## question 56

nom : Gabin
groupe : Vert
difficulte : facile
énoncé : 

est-ce que le javascript est associer au html pour cree une identité visuellle a un site ?
réponse : 

```
Non, c'est le CSS
```

## question 57

nom : Gabin
groupe : Vert
difficulte : difficile
énoncé : 

quelles sont les avantage d'un fichier csv par rapport a un dictionnaire en python?

réponse : 

```
- stocker dans le disque plutot que dans la memoire vive
- lisible avec d'autre application, pas besoin de python
- grande quantitée de données
```

## question 58

nom : Gabin
groupe : Vert
difficulte : moyen
énoncé : 

en assembleur, que signifie l'instruction BNE ?

réponse : 

```
les elements comparer sont differents
```

## question 59

nom : Gabin
groupe : Vert
difficulte : facile
énoncé : 

quelle est la formule de la distance euclidienne ?

réponse : 

```
sqrt((x2-x1)^2 + (y2-y1)^2)
```

## question 60

nom : Gabin
groupe : Vert
difficulte : facile
énoncé : 

donner 4 nom de domaine pour un site web

réponse : 

```
.fr, .com, .org, .net
```

## question 61

nom : Gabin
groupe : Vert
difficulte : moyen
énoncé : 

qu'est ce qu'un ransomware ?

réponse : 

```
Un logiciel malveillant qui chiffre les données apres les avoir copier, et demande une rançon pour les déchiffrer
```

## question 62

nom : Elouan
groupe : Rose
difficulte : facile
énoncé : 

quelle est la difference entre for et while ?   

réponse : 

```
for donne un nombre de tour precis, while donne une condition a remplir
```

## question 63

nom : Elouan
groupe : Rose
difficulte : difficile
énoncé : 

que renvoie le programme ?

```
mode = True
a = 0
i = 5
while True :
    a = a + i
    i = i - 1
    if i == 0:
        mode = False

print(a)
```

réponse : 

```
rien, la boucle est infinie
```

## question 64

nom : Elouan
groupe : Rose
difficulte : moyen
énoncé : 

Quelle est la memoire la plus rapide auquel le CPU peut acceder?

réponse : 

```
les registres
```

## question 65

nom : Elouan
groupe : Rose
difficulte : facile
énoncé : 

dans k-nn que risque-t-on avec un k trop grand?

réponse : 

```
Le resultat est moins precis, les groupes sont moins bien separer
```

## question 66

nom : Elouan
groupe : Rose
difficulte : difficile
énoncé : 

quelle est la complexiter d'un programme possedant une boucle dans une boucle dans une boucle?

réponse : 

```
O(n^3)
```

## question 67

nom : Elouan
groupe : Rose
difficulte : moyen
énoncé : 

quelle est le meilleur moyen de chercher dans une liste non triée

réponse : 

```
recherche ligne par ligne
```

## question 68

nom : Elouan
groupe : Rose
difficulte : facile
énoncé : 

comment s'appele la machine qui partage les site et ce qui les recoivent ? 

réponse :

```
serveur et client
```

## question 69

nom : Elouan
groupe : Rose
difficulte : facile
énoncé : 

quelle est la norme la plus utiliser pour traduire le code machine en caractere ?

réponse :

```
UTF-8
```

## question 70

nom : Elouan
groupe : Rose
difficulte : moyen
énoncé : 

combien il y a t'il de combinaison de couleur dans le système de couleur RGB?

réponse :

```
256^3 = 16 777 216
```

## question 71

nom : Elouan
groupe : Rose
difficulte : moyen
énoncé : 

est-ce que le RGB ameliore t'il la frequence d'image par seconde ?

réponse :

```
Non, il sert simplement a faire mal au porte monaie
```

## question 72

nom : Noah
groupe : Rose
difficulte : facile
énoncé : 

A quoi sert un str

réponse:

```
 une chaine de caractere
```

## question 73

nom : Noah
groupe : Rose
difficulte : difficile
énoncé : 

comment appele t'on la technique pour diviser un tableau en plusieurs parties

réponse:

```
le slicing
```

## question 74

nom : Noah
groupe : Rose
difficulte : moyen
énoncé : 

quand a etait creer le modele de von neumann?

réponse:

```
1946
```

## question 75

nom : Noah
groupe : Rose
difficulte : facile
énoncé : 

comment recupere-t-on le reste en python?

réponse:

```
%
```

## question 76

nom : Noah
groupe : Rose
difficulte : moyen
énoncé : 

en quoi consiste la recherche dichotomique ?

réponse:

```
Il faut diviser le tableau en 2 et comparer l'element du milieu avec l'element recherche
```

## question 77

nom : Noah
groupe : Rose
difficulte : moyen
énoncé : 

quel est la formule pour calculer la distance ?

réponse:

```
sqrt((x2-x1)^2 + (y2-y1)^2)
```

## question 78

nom : Noah
groupe : Rose
difficulte : facile
énoncé : 

comment faire pour ecrire un paragraphe en html

réponse:

```
<p></p>
```

## question 79

nom : Noah
groupe : Rose
difficulte : facile
énoncé : 

10 en nombre binaire

réponse:

```
1010
```

## question 80

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

qu'est-ce qu'il se passe si l'on ecrit : `while l:`


réponse:

```
tant que la liste n'est pas vide, la boucle continue
```

## question 81

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

est-ce que ce code fonctionne et pourquoi ?

```python
liste = []
for i in range(5):
    if i%2 = 0:
        liste.append(i)
```

réponse:

```
non, il manque un = a la ligne 2
```

## question 82

nom : Anonyme
groupe : Rouge
difficulte : facile
énoncé : 

quel est le nom du paquet(package) que l'on importe pour lire/ecrire sur un fichier csv?

réponse:

```
csv
```

## question 83

nom : Anonyme
groupe : Rouge
difficulte : facile
énoncé : 

peut-on avoir un dictionnaire dans une liste dans un dictionnaire?

réponse:

```
oui
```

## question 84

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

que fait l'instruction BEQ en assembleur ?

réponse:

```
BEQ signifie seulement si les elements sont égaux
```

## question 85

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

avec quel commande place-t-on une valeur de la memoire dans un registre ?

réponse: 

```
STR
```

## question 86

nom : Anonyme
groupe : Rouge
difficulte : facile
énoncé : 

que signifie PC en assembleur ?

réponse: 

```
Programme counter
```

## question 87

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

a quelle categorie appartient le disque dur ?

- entree/sortie
- memoire
- unité de control
- bus

réponse: 

```
entree/sortie
```

## question 88

nom : Anonyme
groupe : Rouge
difficulte : difficile
énoncé : 

donner 4 type de tri

réponse: 

```
selection, insertion, fusion, rapide, a bulles, ...
```

## question 89

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

donner la formule de la distance euclidienne entre 2 points

réponse: 

```
sqrt((x2-x1)^2 + (y2-y1)^2)
```

## question 90

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

qu'elle est la complexité du tri par selection?

réponse: 

```
O(n^2)
```

## question 91

nom : Anonyme
groupe : Rouge
difficulte : facile
énoncé : 

dans knn, la valeur de k doit etre pair ou impaire?

réponse: 

```
impair
```

## question 92

nom : Anonyme
groupe : Rouge
difficulte : difficile
énoncé : 

quelle est l'adresse ip de localhost?
- 0.0.0.1
- 255.0.0.1
- 127.0.0.1

réponse: 

```
127.0.0.1
```

## question 93

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

ou mettre la balise script dans un fichier html?

réponse: 

```
n'importe ou dans le html
```

## question 94

nom : Anonyme
groupe : Rouge
difficulte : difficile
énoncé : 

Que fait la postion absolute si la position relative est sur le body ?

réponse: 

```
il place le container dans le coin haut gauche de la page
```

## question 95

nom : Anonyme
groupe : Rouge
difficulte : facile
énoncé : 

quel est le nom de la balise pour le texte

réponse: 

```
<p></p>
```

## question 96

nom : Anonyme
groupe : Rouge
difficulte : moyen
énoncé : 

comment Alan Turing est mort ?

réponse: 

```
manger une pomme empoisonner
```

## question 97

nom : Samuel
groupe : vert
difficulte : facile
énoncé : 

qu'elle est la difference entre int et float ? 

réponse: 

```
float est un nombre avec virgule, int est un nombre entier
```

## question 98

nom : Yusuf
groupe : vert
difficulte : facile
énoncé : 

qu'elle est la diference entre une liste et un tuple ?

réponse: 

```
une liste peut etre modifier(mutable), un tuple ne peut pas etre modifier
```

## question 99

nom : Samuel
groupe : vert
difficulte : facile
énoncé : 

quelle est la commande en assembleur permettant de recuperer une valeur stocker dans une adresse ?

réponse: 

```
LDR
```

## question 100

nom : Yusuf
groupe : vert
difficulte : difficile
énoncé : 

quelle est le role d'un noyau kernel ?

réponse: 

```
il permet de faire le lien entre le programme et les composants
```

## question 101

nom : Samson
groupe : vert
difficulte : facile
énoncé : 

pourquoi le modele de von neumann est-il revolutionnaire ?

réponse: 

```
car il permet de stocker les instructions et les donnees dans la meme memoire
```

## question 102

nom : Samson
groupe : vert
difficulte : facile
énoncé : 

quelle est le cycle d'executions d'un ordinateur ?

réponse: 

```
fetch, decode, execute, re-pc
```

## question 103

nom : Samuel
groupe : vert
difficulte : moyen
énoncé : 

quelles sont le commandes a utiliser pour comparer 2 nombre et sauter a la ligne se le premier est plus grand que l'autre ?

réponse: 

```
CMP
BGT
```

## question 104

nom : Yusuf
groupe : vert
difficulte : moyen
énoncé : 

quelle est l'algorithme d'ia que nous avons vue en classe ?

réponse: 

```
knn
```

## question 105

nom : Samson
groupe : vert
difficulte : moyen
énoncé : 

quelle est la definition d'un algorithme ?

réponse: 

```
une suite d'instruction
```

## question 106

nom : Samuel
groupe : vert
difficulte : difficile
énoncé : 

Comment est mort alan turing ?

réponse: 

```
manger une pomme empoisonner
```

## question 107

nom : Samson
groupe : vert
difficulte : moyen
énoncé : 

quelle est la diference entre python et html?

réponse: 

```
python est un langage de programmation, html est un langage de description
```

## question 108

nom : Odin
groupe : #2BFAFA
difficulte : facile
énoncé : 

qu'effectue l'unité de controle dans le modele de von neumann?
- transporte les informations
- decoder les instructions
- stocker le code 
- communiquer avec l'exterieur 

réponse: 

```
decoder les instructions 
```

## question 109

nom : Odin
groupe : #2BFAFA
difficulte : facile
énoncé : 

que permet le CSS ?

réponse: 

```
de faire da la mise en forme et du style d'une page web
```

## question 110

nom : Odin
groupe : #2BFAFA
difficulte : facile
énoncé : 

quelle est le prerequis pour effectuer une recherche dichotomique?

réponse: 

```
Une liste trié
```

## question 111

nom : Odin
groupe : #2BFAFA
difficulte : facile
énoncé : 

quelle est la notation hexadecimale de 27 ?

réponse: 

```
1B
```

