##################################################
######## Element concernant la Carte #############
##################################################

Elle est codée de la manière suivante :
	- L'axe des x est l'axe vertical orienté vers le haut
	- L'axe des y est l'axe horizontal orienté vers la droite
	- theta est l'angle que fait l'orientation du robot avec l'axe x. Il est croissant dans le sens non-trigonométrique et c'est un nombre en degrés compris entre 0 et 359.

La "largeur du terrain" est selon y
La "longueur du terrain" est selon x
L'origine du terrain est dans le coin en haut à gauche


###################################################
######## Fichiers de configuration ################
###################################################


Les fichiers de configurations sont en .cfg.

Les formalismes des fichiers de config sont les suivants :

config.cfg
Le fichier config.cfg permet de régler tous les paramètres réglables du code. Il doit être en harmonie avec la classe Config (chaque paramètre dans config.cfg doit se retrouver dans la classe). Chaque paramètre est défini par son nom puis les caractères " = " puis la valeur donnée.
Exemple:
---------------------
largeur_du_robot = 1
longueur_du_robot = 3
longueur_terrain = 300
largeur_terrain = 200
ecart_de_surete = 5
X = 300
x_init_d = 0
y_init_d = 0
theta_init_d = 0
x_init_g = 0
y_init_g = 0
theta_init_g = 0
precision = 5
precision_theta = 5
----------------------



action.cfg: 
Une action se définit par 5 caractéristiques : son nom, sa position x de réalisation (en mm), sa position y de réalisation (en mm), l'angle d'orientation du robot (en degré entre 0 et 360) et un temps de réalisation maximum (int en seconde). Chaque action doit être séparée par un retour à la ligne. LES COORDONNÉES DOIVENT ÊTRE COHÉRENTES AVEC LES DIMENSIONS DU TERRAIN ENTRÉES DANS config.cfg.
Exemple:
-------------------
deplacer 10,5,45,20
pincer 50,60,90,50
-------------------




obstacle.cfg:
Un obstacle est nécessairement rectangulaire. Il se définit donc par ses deux points extrémaux (il est mieux de préciser au début le coin haut gauche meme si normalement ce n'est pas nécessaire). Chaque obstacle est séparé par un retour à la ligne. Le nom de l'obstacle n'est pas lu. LES COORDONNÉES DOIVENT ÊTRE COHÉRENTES AVEC LES DIMENSIONS DU TERRAIN ENTRÉES DANS config.cfg.
Exemple:
-------------------
100,100,120,199, Premier obstacle
100,100,120,199, Second obstacle
-------------------


