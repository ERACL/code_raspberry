
from config import *
from communication import *
from obstacle import *
from math import sqrt, cos, sin, pi
from log import *

class Carte():
	
	def __init__(self):
		self.X = Config().get_X()
		self.Y = Config().get_Y()
		self.surete = 10
		self.map = [[0 for i in range(self.Y)] for j in range(self.X) ]
		self.liste_obstacle = []
		self.init_obstacle()
	
	def init_obstacle(self):
		"""Cette fonction a pour objectif de placer les obstacles qui sont fixes et permanent sur la carte"""
		fichier = open("../cfg/obstacles.cfg", "r")
		ligne = fichier.read().split("\n")
		dx = Config().get_dx()
		P1, P2 = None, None
		try:
			for k in range(len(ligne)-1):
				donnees = ligne[k].split(",")
				P1 = (int(int(donnees[0])),int(int(donnees[1])))
				P2 = (int(int(donnees[2])),int(int(donnees[3]))) 
				self.liste_obstacle.append(Obstacle(self,P1,P2,False))
		except:
			Log().edition_obstacle() #log concernant l'edition des obstacles
		return None
	
	def entretien(self):
		"""entretien retire tous les obstacles temporaires de la carte"""
		liste_obstacle = []
		for obstacle in self.liste_obstacle:
			if (obstacle.get_temp() == True):
				obstacle.delete()
			else:
				liste_obstacle.append(obstacle)
		self.liste_obstacle = liste_obstacle
		return None
	
	def ajouter_obstacle(self, P1, P2):
		"""Ajoute un obstacle detecte par les ultrasons (l'obstacle ne sera que temporaire"""
		self.liste_obstacle.append(Obstacle(self,P1,P2,True))
	
	def ajouter_obs(self,obstacle,P1,P2):
		"""Fonction qui realise toutes les procedures pour ajouter un obstacle"""
		longueur_du_robot = Config().get_longueur_du_robot()
		ecart_de_surete = Config().get_ecart_de_surete()
		longueur_terrain = Config().get_longueur_terrain()
		largeur_terrain = Config().get_largeur_terrain()
		dx = Config().get_dx()
		###### On traduit les coordonnees de l'obstacle dans la carte pixellisee #########
		
		P3 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
		P4 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
		
		L = longueur_du_robot+ecart_de_surete
		P3 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
		P4 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
		P3 = (min(P3[0]+L/2,longueur_terrain),min(P3[1]+L/2,largeur_terrain))
		P4 = (max(P4[0]-L/2,0),max(P4[1]-L/2,0))
		P3 = (int(P3[0]/dx),int(P3[1]/dx))  
		P4 = (int(P4[0]/dx),int(P4[1]/dx))
		#On ecrit ensuite les positions de l'obstacle en prenant en compte l'ecart de securite et la largeur du robot
		for i in range(P4[0],P3[0]+1):
			for j in range(P4[1],P3[1]+1):
				self.map[i][j] = -2
		return None
	
	def retirer_obs(self,P1,P2):
		"""pour retirer un obstacle, ne pas utiliser cette fonction mais la commande obstacle.delete()"""
		print("On a retire l'obstacle :", P1, P2)
		longueur_du_robot = Config().get_longueur_du_robot()
		ecart_de_surete = Config().get_ecart_de_surete()
		longueur_terrain = Config().get_longueur_terrain()
		largeur_terrain = Config().get_largeur_terrain()
		dx = Config().get_dx()
		
			
		###### On traduit les coordonnees de l'obstacle dans la carte pixellisee #########
		P1 = (int(P1[0]/dx), int(P1[1]/dx) ) 
		P2 = (int(P2[0]/dx), int(P2[1]/dx) )
		
		
		#On retire ensuite les positions de l'obstacle en prenant en compte l'ecart de securite et la largeur du robot
		L = longueur_du_robot+ecart_de_surete
		P3 = (max(P1[0],P2[0]),max(P1[1],P2[1]))
		P4 = (min(P1[0],P2[0]),min(P1[1],P2[1]))
		P3 = (min(P3[0]+L/2,longueur_terrain),min(P3[1]+L/2,largeur_terrain))
		P4 = (max(P4[0]-L/2,0),max(P4[1]-L/2,0))
		P3 = (int(P3[0]/dx),int(P3[1]/dx))  
		P4 = (int(P4[0]/dx),int(P4[1]/dx))
		for i in range(P3[0],P4[0]+1):
			for j in range(P3[1],P4[1]+1):
				self.map[i][j] = 0
		return None
	
	def get_map(self):
		return self.map
	
	
	def verification(self, distance, position):
		"""Regarde si l'obstacle situe a une certaine distance de la position du robot a ete deja pris en compte. Renvoie True s'il a deja ete pris en compte et False sinon"""
		X_obstacle = position[0] + sin(position[2]*pi/180)*distance
		Y_obstacle = position[1] -cos(position[2]*pi/180)*distance
		for obstacle in self.liste_obstacle:
			X_min, X_max, Y_min, Y_max = obstacle.get_position()
			if (X_obstacle > X_min) and (X_obstacle < X_max) and (Y_obstacle > Y_min) and (Y_obstacle < Y_max) :  
				return True
		return False
	
	
	
