import time
from config import *
from erreur import *
import fonction_chemin_cython
#from matplotlib.pyplot import imshow,show
from log import *

class Chemin():
	
	def __init__(self,carte, position_ini):
		dx = Config().get_dx()
		self.carte = carte.get_map()
		
		self.P1 = (int(position_ini[0]/dx),int(position_ini[1]/dx)) #On traduit les coordonnees en mm en coordonnees sur la carte
		self.angle_ini = position_ini[2]
		calcul = self.calcul_chemin()
		self.liste_direction, self.point_chemin, self.liste_point = calcul
		self.chemin = [self.liste_direction, self.point_chemin]
		

	
	def calcul_chemin(self):
		"""Renvoie trois composantes : la premiere est la direction du robot, la deuxieme est les points auxquels le robot tourne et le troisieme l'ensemble des points par lequel le robot passe"""
		
		#TestChemin est une classe permettant de chronometrer ce temps de calcul. S'il est trop long, on abandonne le calcul et on affiche une erreur
		test = TestChemin(10)
		#imshow(self.carte)
		#show()
		
		Log().debut_calcul_chemin()
		test.start()
		#Log().affiche_carte(self.carte)
		print(self.carte[self.P1[0]][self.P1[1]])
		
		calcul = fonction_chemin_cython.fonction_trouver_chemin(self.carte, self.P1)
		dx = Config().get_dx()
		for k in range(len(calcul[1])):
			calcul[1][k] = (int(calcul[1][k][0]*dx),int(calcul[1][k][1]*dx)) #On traduit les coordonnees de la carte en mm
		test.stop()
		Log().fin_calcul_chemin()
		try:
			assert len(calcul[0])!=0
		except AssertionError:
			#print("Le calcul du chemin s'est mal deroule")
			pass
		
		
		return calcul


	
	def get_chemin(self):
		return self.chemin
	
	def get_liste_point(self):
		return self.liste_point
		 
