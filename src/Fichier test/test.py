from config import *
from fonction_chemin import *
from matplotlib.pyplot import imshow, show
import time


X = Config().get_X()
Y = Config().get_Y()
Map = [[0 for i in range(X)] for j in range(Y) ]
depart = [40,40]
arrivee = [1, 40]

angle_ini = 90
angle_fin = 180
debut = time.time()
fonction_calcul_carte(Map, arrivee)

fonction_trouver_chemin(Map, depart)
print(time.time() - debut)

import fonction_chemin_cython
Map = [[0 for i in range(X)] for j in range(Y) ]


debut = time.time()
fonction_chemin_cython.fonction_calcul_carte(Map, arrivee)
fonction_chemin_cython.fonction_trouver_chemin(Map, depart)
print(time.time() - debut)
imshow(Map)
show()
