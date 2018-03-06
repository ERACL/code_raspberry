from chemin import *
from erreur import *
from communication import *
from calcul_carte import *
from math import sqrt, acos, asin, pi
class Deplacement():
	
	def __init__(self,robot,position_fin,carte):
		self.position_fin = position_fin 
		self.position_ini = robot.get_donnees()
		self.carte = carte
		
		self.chemin = Chemin(carte,self.position_ini)
		self.robot = robot
		
		self.aller_a()
	
	
	def tourner(self,theta_ini,theta_fin):
		"""Met tout en oeuvre pour orienter le robot dans le bon sens. Si l'angle est trop petit, cette fonction ne fait rien"""
		theta = theta_fin - theta_ini
		precision = Config().get_precision_theta()
		if (theta<0):
			theta += 360 #La convention de communication est un angle entre 0 et 360
		if abs(theta)>precision and abs(360-theta)>precision: #On ne tourne que si l'angle est superieur a la precision donnee dans le fichier de config
			Communication().tourner(theta)
		return None

	def deplacement_elem(self,deplacement):
		
		theta = None
		if (deplacement[0] == "de") or (deplacement[0] == 'mre'):
			theta = 180
		elif (deplacement[0] == 'mo') or (deplacement[0] == 'dre'): 
			theta = 0
		elif (deplacement[0] == "dr") or (deplacement[0] == 'gre'):
			theta = 270
		elif (deplacement[0] == 'ga') or (deplacement[0] == 'rre'): #rre pour "Right en reculant" ou plus simplement droite en reculant
			theta = 90
		elif (deplacement[0] == 'dedr'):
			theta = 225
		elif (deplacement[0] == 'modr'):
			theta = 315
		elif (deplacement[0] == 'dega'):
			theta = 135
		elif (deplacement[0] == 'moga'):
			theta = 45
		else:
			try:
				assert True == False
			except AssertionError:
				Log().calcul_chemin(deplacement[0])
		donnees = self.robot.get_donnees()
		self.tourner(donnees[2],theta)
		if ( len(deplacement[0]) == 3 ) : #Cette condition n'est remplie que si le robot doit reculer
			Communication().reculer(deplacement[1])
		else:
			Communication().avancer(deplacement[1])
		return None
	
	def deplacement_elem_recule(self,deplacement):
		Communication().reculer(deplacement[1])
		return None
		 
	def aller_a(self):
		precision = Config().get_precision()
		trajet = self.chemin.get_chemin()
		distance_bord = int(Config().get_largeur_robot_max())
		largeur_terrain = Config().get_largeur_terrain()
		longueur_terrain = Config().get_longueur_terrain()
		Log().chemin_robot(trajet)
		if len(trajet[1]) == 0:
			#print("Le robot est deja bien place")
			pass
		else:
			if self.position_ini[0]<distance_bord:
				trajet[0] = ["mre"]+trajet[0][:]
				trajet[1] = [(distance_bord,trajet[1][0][0][1])]+trajet[1][:]
			elif self.position_ini[1]<distance_bord:
				trajet[0] = ["rre"]+trajet[0][:]
				trajet[1] = [(trajet[1][0][0][0],distance_bord)]+trajet[1][:]
			elif self.position_ini[0]>longueur_terrain - distance_bord:
				trajet[0] = ["mre"]+trajet[0][:]
				trajet[1] = [(longueur_terrain - distance_bord,trajet[1][1][0][1])]+trajet[1][:]
			elif self.position_ini[1]>largeur_terrain - distance_bord:
				trajet[0] = ["gre"]+trajet[0][:]
				trajet[1] = [(trajet[1][0][0][0], largeur_terrain - distance_bord)]+trajet[1][:]
			trajet[1][-1] = (self.position_fin[0],self.position_fin[1]) #On remplace l'endroit de la derniere etape calculee par l'endroit reel de la derniere etape --> Diminution de l'imprecision due a la pixellisation du deplacement
		Log().chemin_robot(trajet)
		########## On lance le deplacement du robot ##########
		
		nb_etape_deplacement = len(trajet[0])
		for k in range(nb_etape_deplacement):
			self.deplacement_elem((trajet[0][k],trajet[1][k]))
		position_fin = self.robot.get_donnees()
		delta = sqrt((position_fin[0]-self.position_fin[0])**2+(position_fin[1]-self.position_fin[1])**2)
		
		if delta > precision :
			#Ici, le robot n'est pas a l'endroit souhaite : On refait le deplacement a partir de l'endroit arrive
			theta = acos((position_fin[0]-self.position_fin[0])/delta)
			if asin((position_fin[1]-self.position_fin[1])/delta) < 0:
				theta = 2*pi-theta
			theta = 360*theta/(2*pi)
			theta_ini = self.robot.get_donnees()[2]
			reculer = True
			print(theta-theta_ini)
			if ((theta-theta_ini)%360 > 90) and ((theta-theta_ini)%360 < 270) :
				theta = (theta-theta_ini-180)%360
				reculer = False
			else:
				theta = (theta-theta_ini)%360
			Communication().tourner(theta)
			if reculer == True:
				Communication().reculer(self.position_fin)
			else:
				Communication().avancer(self.position_fin)
			if delta > precision :
				#Mettre un log d'erreur de deplacement
				pass		

				
		return None
	
	def get_chemin_bien_calcule(self):
		return self.chemin.chemin_bien_calcule



