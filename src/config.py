import os

#Cette classe a pour objectif de charger le fichier de configuration "config.cfg"

class Config():
	
	fichier = open("../cfg/config.cfg", "r")
	ligne = fichier.read().split("\n")
	for i in range(len(ligne)-1):
		k = ligne[i]
		L = k.split(" = ")
		assert len(L)==2
		if L[0] == "largeur_du_robot" :
			largeur_du_robot = int(L[1])
		elif L[0] == "longueur_du_robot" :
			longueur_du_robot = int(L[1])
		elif L[0] == "largeur_terrain" :
			largeur_terrain = int(L[1])
		elif L[0] == "longueur_terrain" :
			longueur_terrain = int(L[1])
		elif L[0] == "ecart_de_surete" :
			ecart_de_surete = int(L[1])
		elif L[0] == "X" : #X et Y sont la taille de la carte
			X = int(L[1])		
		elif L[0] == "x_init_g" : 
			x_init_g = int(L[1])
		elif L[0] == "y_init_g" : 
			y_init_g = int(L[1])
		elif L[0] == "theta_init_g" : 
			theta_init_g = int(L[1])
		elif L[0] == "x_init_d" : 
			x_init_d = int(L[1])
		elif L[0] == "y_init_d" : 
			y_init_d = int(L[1])
		elif L[0] == "theta_init_d" : 
			theta_init_d = int(L[1])
		elif L[0] == "precision":
			precision = int(L[1])
		elif L[0] == "precision_theta":
			precision_theta = int(L[1])
		elif L[0] == "adresse_mot":
			adresse_mot = int(L[1],16)
		elif L[0] == "adresse_cap":
			adresse_cap = int(L[1],16)
		elif L[0] == "largeur_robot_max":
			largeur_robot_max = int(L[1])
		elif L[0] == "nb_tentatives":
			nb_tentatives = int(L[1])
		elif L[0] == "distance_arret":
			distance_arret = int(L[1])
		elif L[0] == "longueur_robot_max":
			longueur_robot_max = int(L[1])
		else:
			try:
				assert True==False
			except AssertionError:
				print("Le fichier de configuration a ete mal encode")
	dx = float(longueur_terrain)/float(X)
	Y = int(largeur_terrain/dx)
	

	def __init__(self):
		return None
	
	@classmethod
	def get_largeur_du_robot(self):
		return self.largeur_du_robot
	
	@classmethod
	def get_longueur_du_robot(self):
		return self.longueur_du_robot
	
	@classmethod
	def get_largeur_terrain(self):
		return self.largeur_terrain
	
	@classmethod
	def get_longueur_terrain(self):
		return self.longueur_terrain
	
	@classmethod
	def get_ecart_de_surete(self):
		return self.ecart_de_surete
	
	@classmethod
	def get_dx(self):
		return self.dx
	
	@classmethod
	def get_Y(self):
		return self.Y
	
	@classmethod
	def get_X(self):
		return self.X
	
	@classmethod
	def get_x_init_d(self):
		return self.x_init_d
	
	@classmethod
	def get_y_init_d(self):
		return self.y_init_d
	
	@classmethod
	def get_theta_init_d(self):
		return self.theta_init_d
	
	@classmethod
	def get_x_init_g(self):
		return self.x_init_g
	
	@classmethod
	def get_y_init_g(self):
		return self.y_init_g
	
	@classmethod
	def get_theta_init_g(self):
		return self.theta_init_g
	
	@classmethod
	def get_precision(self):
		return self.precision

	@classmethod
	def get_precision_theta(self):
		return self.precision_theta
	
	@classmethod
	def get_adresse_mot(self):
		return self.adresse_mot
	
	@classmethod
	def get_adresse_cap(self):
		return self.adresse_cap
	
	@classmethod
	def get_largeur_robot_max(self):
		return self.largeur_robot_max
	
	@classmethod
	def get_nb_tentatives(self):
		return self.nb_tentatives
	
	@classmethod
	def get_distance_arret(self):
		return self.distance_arret
		
	
	
