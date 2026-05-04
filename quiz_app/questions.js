const questionsData = [
  {
    "nom": "Maillet Odin",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "Bastien a ecrit un code python suivant:\n```\nliste[0],liste[1] = liste[1],liste[0]\n```\nQue permet-il d'effectuer ?",
    "reponse": "il permet d'échanger les deux premiers éléments de la liste"
  },
  {
    "nom": "Maillet Odin",
    "groupe": "Cyan",
    "difficulte": "difficile",
    "enonce": "Jeanne a ecrit le code suivant :\n```\nimport math\n\nx1 = 2\nx2 = 5\ny1 = 2\ny2 = 6\n\ndef distance(x1,x2,y1,y2):\n    return math.sqrt((x2-x1)**2 + (y2-y1)**2)\n\ndistance(x1,x2,y1,y2)\n```\nQuel résultat est attendu ?",
    "reponse": "5"
  },
  {
    "nom": "Antonin",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "comment passer d'une base 10 à une base 2 ?",
    "reponse": "- on divise par 2\n- on note le reste\n- on lit les restes à l'envers"
  },
  {
    "nom": "Margaret",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "dans un fichier html relié à un fichier css, comment donner une apparence différente à deux paragraphes qui possèdent la même classe ?",
    "reponse": "mettre des <id>"
  },
  {
    "nom": "Antonin",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "quelle est la différence entre un tri par insertion et un tri par sélection ?",
    "reponse": "le tri par sélection parcourt la liste pour trouver le plus petit alors que le tri par insertion met la valeur directement à son emplacement dans la nouvelle liste"
  },
  {
    "nom": "Margaret",
    "groupe": "Cyan",
    "difficulte": "difficile",
    "enonce": "en langage assembleur, faire 5*3 et enregistrer le résultat en mémoire place 100",
    "reponse": "```\nMOV R0, #5\nboucle :\nSUB R0, R0, #1\nADD R1, R1, #3\nCMP R0, #0\nBNE boucle\nSTR R1, 100\nHALT\n```"
  },
  {
    "nom": "Antonin",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "quelle est la date de la création de l'architecture de Von Neumann ?",
    "reponse": "1946"
  },
  {
    "nom": "Margaret",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "en langage assembleur, effectuer le calcul 5 + 2 et le ranger en mémoire place 60",
    "reponse": "MOV R0, #5\nMOV R1, #2\nADD R1, R0, R1\nSTR R1, 60"
  },
  {
    "nom": "Antonin",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "à quoi sert la première ligne d'un fichier csv ?",
    "reponse": "elle sert à donner un nom aux valeurs de la colonne en dessous et à une clé aux valeurs si un dictionnaire est créé (tout ce qui s'approche de cette réponse est correct, à l'appréciation du professeur (c'est moi))"
  },
  {
    "nom": "Margaret",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "que renvoie la ligne de code: print(liste[-1]) ?",
    "reponse": "elle renvoie le dernier élément de la liste"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quel est le type de `True` et de `False` en python?",
    "reponse": "```\nbool\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "comment faire une puissance sur Python?",
    "reponse": "```\n**\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "que va afficher le code suivant?\n\n```\nfor i in range(8):\n    print(i)\n```",
    "reponse": "```\n0\n1\n2\n3\n4\n5\n6\n7\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "comment ecrire une liste dans Python ?",
    "reponse": "```\navec les crochets: []\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quelle est la difference entre une liste et un tuple en python?",
    "reponse": "```\nune liste est mutable et un tuple est immuable\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "que va faire ce programme?\n\n```\nliste=[\n    eleve1 = { meilleur= 19.5, pire = 5, moyenne= 17, appr=\"Bien\"},\n    eleve2 = { meilleur= 20, pire = 20, moyenne= 20, appr=\"Tres bien\"},\n    eleve3 = { meilleur= 10, pire = 3, moyenne= 6.75, appr=\"Mauvais\"}\n]\n\nprint(liste[eleve1][\"appr\"])\n```",
    "reponse": "```\nune erreur car on ne peut pas accéder a un dictionnaire avec un indice\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "quels sont les composants essentiels d'un ordinateur?\n\nprocesseur, carte mère, ram, alimentation, ventilateur",
    "reponse": "tous sauf le ventilateur"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "Que permet le hashtag dans le langage assembleur?",
    "reponse": "de prendre la valeur numerique de la valeur"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "Quels sont les trois type de language ? donner des exemples",
    "reponse": "- machine : binaire\n- bas niveau : assembleur\n- langage evolué : python, java, c++, etc."
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "que signifie k-nn ?",
    "reponse": "```\nK-nearest neighbors (k plus proches voisins)\nk-plus-proches voisins\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "Comment fonctionne la recherche dichotomique ?",
    "reponse": "```\non divise la liste en deux jusqu'a trouver la valeur\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "Comment lie-t-on une page web a une page html ?",
    "reponse": "```\n<link rel=\"stylesheet\" href=\"style.css\">\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "que signifie html?",
    "reponse": "```\nHyperText Markup Language\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "mettre 315 en binaire",
    "reponse": "```\n100111001\n```"
  },
  {
    "nom": "Auguste",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "mettre le nombre binaire 110001011 en decimal",
    "reponse": "```\n395\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quelle est la difference entre un int et un float en python?",
    "reponse": "```\nun int est un nombre entier\nun float est un nombre decimal\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quelle-est le type de a ?\n\n```\na = \"123\"\n```",
    "reponse": "```\nstr\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "que retourne la fonction ?\n\n```\na = 10\nb = 0\nwhile a > 0:\n    b += 1\nreturn b\n```",
    "reponse": "```\nrien, la boucle est infinie\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "qu'est ce qu'un registre en assembleur ?",
    "reponse": "```\nendroit dans le CPU ou sont stocker des valeurs de facon ephemere\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "qu'elle est le principe du tri par insertion ?",
    "reponse": "```\nOn insere les valeurs au fur et a mesure dans une partie considerer comme deja trier\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "en CSS, a quoi sert display: flex ?",
    "reponse": "```\ncela permet de mettre cote a cote differents elements dans un html\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "dans le CSS, a quoi servent les @keyframes ?",
    "reponse": "```\nSert a definir les etapes principales d'une animation\n```"
  },
  {
    "nom": "Nathan D",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "utiliser l'inteligence artificielle est-il ecologique ?",
    "reponse": "```\nnon, ca pollue\n```"
  },
  {
    "nom": "Lilou",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "A quel type de valeur est associer float ?",
    "reponse": "```\nles nombres decimaux\n```"
  },
  {
    "nom": "Lilou",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "A quoi sert l'instruction LDR ?",
    "reponse": "```\ncharge une valeur dans l'adresse donner dans un registre\n```"
  },
  {
    "nom": "Lilou",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "quel probleme pourrait-il avoir si l'on choisie un nombre pair avec KNN ?",
    "reponse": "```\nsi le nombre est pair, il se pourrait qu'il y est autant d'element dans chaque groupe \n```"
  },
  {
    "nom": "Lilou",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "quelle est la balise pour creer un bouton sur html?",
    "reponse": "```\n<button></button>\n```"
  },
  {
    "nom": "Lilou",
    "groupe": "Cyan",
    "difficulte": "moyenne",
    "enonce": "qui a inventé le tout premier ordinateur ?",
    "reponse": "```\nalan turing\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "qu'est ce qu'un str?\n- un nombre entier\n- une chaine de caractere\n- un nombre decimal",
    "reponse": "```\nune chaine de caracteres\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "quel nombre affiche se programme ?\n\n```\na = 0\ni = 5\nwhile i >= 0:\n    a += i\n    for i in range(3):\n        a += i\n    i = i - 1\nprint(a)\n```\n\n- 20\n- 60\n- 100",
    "reponse": "```\n60\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "que fait l'action Fetch ?",
    "reponse": "```\nrechercher\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "A quoi sert la commande LDR en language assembleur ?",
    "reponse": "```\ncharger depuis la memoire \n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "de quelle(s) nationnalité(s) était Von Neumann ?",
    "reponse": "```\nHongro-américain\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "que signifie KNN?\n\n- k-nearest neighbors\n- k-Nocturn Nissan\n- k-Nicolas Narcotraficant\n- k-nearest Neldoors",
    "reponse": "```\nk-nearest neighbors\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quel est la balise pour un lien ?",
    "reponse": "```\na\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "il vaut mieux avoir un ssd ou un hdd pour les performance ?",
    "reponse": "```\nUn ssd\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "difficile",
    "enonce": "citer les 4 grande partie d'un ordinateur selon le modèle de Von Neumann",
    "reponse": "```\nUC\nMemoire\nentrée/sortie\nBus\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "citez les grandes etapes du cycle d'execution du modele de von neumann",
    "reponse": "```\n1. Fetch\n2. Decode\n3. Execute\n4. REPC\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "expliquez le principe du tri a bulle",
    "reponse": "```\nOn parcourt la liste plusieurs fois, et a chaque fois on compare les elements deux a deux, si le premier est plus grand que le second on les échange.\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "citez les deux parties principales d'une page web en html?",
    "reponse": "```\nhead et body\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "citez 3 balise courament utiliser dans le HTML",
    "reponse": "```\np, h1, h2, h3, h4, h5, h6, div, span, a, img, button, input ...\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "Alan Turing fut connue pourquoi? citez 2 exemples",
    "reponse": "```\n- la resolution de l'enigme Enigma\n- le developpement de l'informatique\n```"
  },
  {
    "nom": "Gregoire",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "vaut-il mieux mettre de beau nom de variable ou des lettres dans un programme?",
    "reponse": "```\nDe beaux nom de variables\n```"
  },
  {
    "nom": "Gabin",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "est-ce que le javascript est associer au html pour cree une identité visuellle a un site ?",
    "reponse": "```\nNon, c'est le CSS\n```"
  },
  {
    "nom": "Gabin",
    "groupe": "Vert",
    "difficulte": "difficile",
    "enonce": "quelles sont les avantage d'un fichier csv par rapport a un dictionnaire en python?",
    "reponse": "```\n- stocker dans le disque plutot que dans la memoire vive\n- lisible avec d'autre application, pas besoin de python\n- grande quantitée de données\n```"
  },
  {
    "nom": "Gabin",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "en assembleur, que signifie l'instruction BNE ?",
    "reponse": "```\nles elements comparer sont differents\n```"
  },
  {
    "nom": "Gabin",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "quelle est la formule de la distance euclidienne ?",
    "reponse": "```\nsqrt((x2-x1)^2 + (y2-y1)^2)\n```"
  },
  {
    "nom": "Gabin",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "donner 4 nom de domaine pour un site web",
    "reponse": "```\n.fr, .com, .org, .net\n```"
  },
  {
    "nom": "Gabin",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "qu'est ce qu'un ransomware ?",
    "reponse": "```\nUn logiciel malveillant qui chiffre les données apres les avoir copier, et demande une rançon pour les déchiffrer\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quelle est la difference entre for et while ?",
    "reponse": "```\nfor donne un nombre de tour precis, while donne une condition a remplir\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "que renvoie le programme ?\n\n```\nmode = True\na = 0\ni = 5\nwhile True :\n    a = a + i\n    i = i - 1\n    if i == 0:\n        mode = False\n\nprint(a)\n```",
    "reponse": "```\nrien, la boucle est infinie\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "Quelle est la memoire la plus rapide auquel le CPU peut acceder?",
    "reponse": "```\nles registres\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "dans k-nn que risque-t-on avec un k trop grand?",
    "reponse": "```\nLe resultat est moins precis, les groupes sont moins bien separer\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "quelle est la complexiter d'un programme possedant une boucle dans une boucle dans une boucle?",
    "reponse": "```\nO(n^3)\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "quelle est le meilleur moyen de chercher dans une liste non triée",
    "reponse": "```\nrecherche ligne par ligne\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "comment s'appele la machine qui partage les site et ce qui les recoivent ?",
    "reponse": "```\nserveur et client\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "quelle est la norme la plus utiliser pour traduire le code machine en caractere ?",
    "reponse": "```\nUTF-8\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "combien il y a t'il de combinaison de couleur dans le système de couleur RGB?",
    "reponse": "```\n256^3 = 16 777 216\n```"
  },
  {
    "nom": "Elouan",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "est-ce que le RGB ameliore t'il la frequence d'image par seconde ?",
    "reponse": "```\nNon, il sert simplement a faire mal au porte monaie\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "A quoi sert un str",
    "reponse": "```\n une chaine de caractere\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "difficile",
    "enonce": "comment appele t'on la technique pour diviser un tableau en plusieurs parties",
    "reponse": "```\nle slicing\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "quand a etait creer le modele de von neumann?",
    "reponse": "```\n1946\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "comment recupere-t-on le reste en python?",
    "reponse": "```\n%\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "en quoi consiste la recherche dichotomique ?",
    "reponse": "```\nIl faut diviser le tableau en 2 et comparer l'element du milieu avec l'element recherche\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "moyenne",
    "enonce": "quel est la formule pour calculer la distance ?",
    "reponse": "```\nsqrt((x2-x1)^2 + (y2-y1)^2)\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "comment faire pour ecrire un paragraphe en html",
    "reponse": "```\n<p></p>\n```"
  },
  {
    "nom": "Noah",
    "groupe": "Rose",
    "difficulte": "facile",
    "enonce": "10 en nombre binaire",
    "reponse": "```\n1010\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "qu'est-ce qu'il se passe si l'on ecrit : `while l:`",
    "reponse": "```\ntant que la liste n'est pas vide, la boucle continue\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "est-ce que ce code fonctionne et pourquoi ?\n\n```python\nliste = []\nfor i in range(5):\n    if i%2 = 0:\n        liste.append(i)\n```",
    "reponse": "```\nnon, il manque un = a la ligne 2\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "facile",
    "enonce": "quel est le nom du paquet(package) que l'on importe pour lire/ecrire sur un fichier csv?",
    "reponse": "```\ncsv\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "facile",
    "enonce": "peut-on avoir un dictionnaire dans une liste dans un dictionnaire?",
    "reponse": "```\noui\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "que fait l'instruction BEQ en assembleur ?",
    "reponse": "```\nBEQ signifie seulement si les elements sont égaux\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "avec quel commande place-t-on une valeur de la memoire dans un registre ?",
    "reponse": "```\nSTR\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "facile",
    "enonce": "que signifie PC en assembleur ?",
    "reponse": "```\nProgramme counter\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "a quelle categorie appartient le disque dur ?\n\n- entree/sortie\n- memoire\n- unité de control\n- bus",
    "reponse": "```\nentree/sortie\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "difficile",
    "enonce": "donner 4 type de tri",
    "reponse": "```\nselection, insertion, fusion, rapide, a bulles, ...\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "donner la formule de la distance euclidienne entre 2 points",
    "reponse": "```\nsqrt((x2-x1)^2 + (y2-y1)^2)\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "qu'elle est la complexité du tri par selection?",
    "reponse": "```\nO(n^2)\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "facile",
    "enonce": "dans knn, la valeur de k doit etre pair ou impaire?",
    "reponse": "```\nimpair\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "difficile",
    "enonce": "quelle est l'adresse ip de localhost?\n- 0.0.0.1\n- 255.0.0.1\n- 127.0.0.1",
    "reponse": "```\n127.0.0.1\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "ou mettre la balise script dans un fichier html?",
    "reponse": "```\nn'importe ou dans le html\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "difficile",
    "enonce": "Que fait la postion absolute si la position relative est sur le body ?",
    "reponse": "```\nil place le container dans le coin haut gauche de la page\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "facile",
    "enonce": "quel est le nom de la balise pour le texte",
    "reponse": "```\n<p></p>\n```"
  },
  {
    "nom": "Anonyme",
    "groupe": "Rouge",
    "difficulte": "moyenne",
    "enonce": "comment Alan Turing est mort ?",
    "reponse": "```\nmanger une pomme empoisonner\n```"
  },
  {
    "nom": "Samuel",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "qu'elle est la difference entre int et float ?",
    "reponse": "```\nfloat est un nombre avec virgule, int est un nombre entier\n```"
  },
  {
    "nom": "Yusuf",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "qu'elle est la diference entre une liste et un tuple ?",
    "reponse": "```\nune liste peut etre modifier(mutable), un tuple ne peut pas etre modifier\n```"
  },
  {
    "nom": "Samuel",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "quelle est la commande en assembleur permettant de recuperer une valeur stocker dans une adresse ?",
    "reponse": "```\nLDR\n```"
  },
  {
    "nom": "Yusuf",
    "groupe": "Vert",
    "difficulte": "difficile",
    "enonce": "quelle est le role d'un noyau kernel ?",
    "reponse": "```\nil permet de faire le lien entre le programme et les composants\n```"
  },
  {
    "nom": "Samson",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "pourquoi le modele de von neumann est-il revolutionnaire ?",
    "reponse": "```\ncar il permet de stocker les instructions et les donnees dans la meme memoire\n```"
  },
  {
    "nom": "Samson",
    "groupe": "Vert",
    "difficulte": "facile",
    "enonce": "quelle est le cycle d'executions d'un ordinateur ?",
    "reponse": "```\nfetch, decode, execute, re-pc\n```"
  },
  {
    "nom": "Samuel",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "quelles sont le commandes a utiliser pour comparer 2 nombre et sauter a la ligne se le premier est plus grand que l'autre ?",
    "reponse": "```\nCMP\nBGT\n```"
  },
  {
    "nom": "Yusuf",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "quelle est l'algorithme d'ia que nous avons vue en classe ?",
    "reponse": "```\nknn\n```"
  },
  {
    "nom": "Samson",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "quelle est la definition d'un algorithme ?",
    "reponse": "```\nune suite d'instruction\n```"
  },
  {
    "nom": "Samuel",
    "groupe": "Vert",
    "difficulte": "difficile",
    "enonce": "Comment est mort alan turing ?",
    "reponse": "```\nmanger une pomme empoisonner\n```"
  },
  {
    "nom": "Samson",
    "groupe": "Vert",
    "difficulte": "moyenne",
    "enonce": "quelle est la diference entre python et html?",
    "reponse": "```\npython est un langage de programmation, html est un langage de description\n```"
  },
  {
    "nom": "Odin",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "qu'effectue l'unité de controle dans le modele de von neumann?\n- transporte les informations\n- decoder les instructions\n- stocker le code \n- communiquer avec l'exterieur",
    "reponse": "```\ndecoder les instructions \n```"
  },
  {
    "nom": "Odin",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "que permet le CSS ?",
    "reponse": "```\nde faire da la mise en forme et du style d'une page web\n```"
  },
  {
    "nom": "Odin",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "quelle est le prerequis pour effectuer une recherche dichotomique?",
    "reponse": "```\nUne liste trié\n```"
  },
  {
    "nom": "Odin",
    "groupe": "Cyan",
    "difficulte": "facile",
    "enonce": "quelle est la notation hexadecimale de 27 ?",
    "reponse": "```\n1B\n```"
  }
];