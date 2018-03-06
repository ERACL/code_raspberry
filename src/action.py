from deplacement import *
from communication import *
from multiprocessing import Value
import time
from erreur import *
from math import pi, cos, sin
from config import *
from carte import *
from carte_action import *
from log import *

#from matplotlib.pyplot import imshow, show

class Action():
	
	def __init__(self,robot,position,action, action_suivante):
		self.action_suivante = action_suivante
		self.carte = Carte_action(position, None)
		self.position = position #Position a laquelle l'action est realisee
		self.action = action
		self.robot = robot
		self.nb_annulation = 0
		self.action_annulee = False #Vaut True lorsque le calcule du parcours a mis trop de temps
		self.action_interrompue = False #Vaut True lorsque l'action doit etre interrompue pour cause d'obstacle
		self.carte_fini_calculee = Value("i",0)
		self.obstacle_detecte = False #Vaut False lorsque le chemin a emprunter est celui par defaut et True lorsque de nouveaux obstacles ont ete detectes et que donc le chemin a ete modifie
		
	
	def executer(self):
		"""Execute l'action"""
		Log().debut_action(self.action)
		
		## On lance le chronometre (fonctionnant par Thread + Erreur) ##
		###### pour connaitre le temps d'execution de l'action #########
		test_ActionInterrompue = TestAction_Interrompue(self)
		test_ActionInterrompue.start()
		################################################################
		
		#### On effectue tout ce qu'il faut pour l'action (calcul du ####
		## chemin, deplacement du robot et activation des actionneurs) ##
		while self.carte_fini_calculee == False :
			time.sleep(0.2)
		
		self.deplacer()
		
		self.verifier_et_corriger()
		self.action_a_realiser()
		##################################################################
		
		###### On stoppe le chronometre/Thread et on affiche le temps de l'action ########
		test_ActionInterrompue.stop()
		###########################################################################
		
		return None
	
	
	
	def action_a_realiser(self):
		"""Cette fonction gere toute la partie de l'action qui n'est pas un deplacement (activation de pinces...)"""
		if (self.action == "recalage_avant"):
			#recalage recale le robot par l'avant. Le mur est cense etre a 30 mm devant nous
			theta = self.robot.get_angle()
			position = self.robot.get_position()
			distance_mur = 30
			distance_avant_centre_de_rotation = 20 ############### FAUT METTRE C DANS LE FICHIER DE CONFIGURATION ###############
			Communication().avancer(distance_mur+5) #Mettre une fonction particuliere qui by_pass le PID
			Communication().reculer(distance_mur) #AVEC PID celle la
			
			#### A partir de la ca pu la merde ####
			precision = 5
			if abs(theta - 90) < precision:
				y_robot = Config().get_largeur_terrain() - distance_mur
				x_robot = position[0]+distance_mur*cos(theta/180*pi)/sin(theta/180*pi) 
				Communication.set_donnees([x_robot, y_robot,90])
			elif abs(theta - 180) < precision:
				x_robot = Config().get_longueur_terrain() - distance_mur 
				y_robot = position[1]+distance_mur*cos((theta-90)/180*pi)/sin((theta-90)/180*pi) 
				Communication.set_donnees([x_robot, y_robot,90])
			elif abs(theta-270)< precision:
				y_robot = distance_mur
				x_robot = position[0]+distance_mur*cos((theta-180)/180*pi)/sin((theta-180)/180*pi) 
				Communication().set_donnees([x_robot, y_robot, 180])
			elif (abs(theta-360) < precision) or (theta < precision):
				x_robot 
			#if 
			##########################################
		return None
	
	def deplacer(self):
		"""deplacer gere le deplacement du robot a l'endroit ou l'action doit etre realisee"""
		
		deplacement = Deplacement(self.robot,self.position,self.carte) #On demande au robot de calculer le deplacement et de se deplacer
		
		
		test = self.verifier_et_corriger()
		#On peut placer ici un time pour verifier que le deplacement ne prenne pas trop de temps
		while (test != "bien place"):
			if (test=="position fausse"):
				Deplacement(self.robot,self.position, self.carte)
			else:
				theta_robot = self.robot.get_donnees()[2]
				theta = self.position[2] - theta_robot 
				if (theta<0):
					theta += 360
				Communication().tourner(theta)
				test = self.verifier_et_corriger()
		return None
	
	def verifier_et_corriger(self):
		"""Cette fonction verifie la position du robot et le cas echeant le replace pour qu'il soit a la position demandee"""
		######## On charge les differentes precisions presentes dans le fichier de config ##########
		precision = Config().get_precision()
		precision_theta = Config().get_precision_theta()
		############################################################################################
		
		####### On charge la position de l'action et la position du robot ###########
		donnees = self.robot.get_donnees()
		x_action = self.position[0]
		y_action = self.position[1]
		theta_action = self.position[2]
		#############################################################################
		
		##### On calcule la distance entre la position du robot et la position de l'action a realiser #####
		###### Si la distance a l'endroit vise ou si l'angle est trop imprecis, on le fait savoir #########
		delta_x = x_action-donnees[0]
		delta_y = y_action-donnees[1]
		delta_theta = theta_action-donnees[2]
		if sqrt(delta_x**2+delta_y**2)>precision:
			#self.deplacer(self.robot,self.position)
			return "position fausse"
		if (abs(delta_theta)>precision_theta):
			return "angle faux"
		###################################################################################################
		
		############## Sinon, c'est qu'on est bien place #################
		return "bien place"
	
	def calcul_carte(self, booleen):
		"""Calcule la carte de l'action. Si booleen vaut True, alors il faut calculer la carte a partir de la carte de base (sans obstacle supplementaire). Si le booleen vaut False, la carte self.carte.map sera utilisee comme base pour calculer le chemin"""
		carte = self.carte.calcul_carte(booleen)
		return carte
	
	
	
	def set_action_annule(self, booleen):
		"""Modifie le caractere annule ou non-annule de l'action"""
		self.action_annulee = booleen
		return None
	
	def get_action_annulee(self):
		"""Retourne un booleen pour savoir si l'action en cours a ete annulee (=calcul du chemin trop long) (renvoie True) ou pas (renvoie False)"""
		return self.action_annulee
	
	def get_action_interrompue(self):
		return self.action_interrompue
	
	def set_action_interrompue(self, booleen):
		"""Modifie l'interruption de l'action"""
		self.action_interrompue = booleen
		return None
	
	def incrementer_annulation(self):
		"""Augmente le nombre d'annulation de 1"""
		self.nb_annulation += 1
		return None
	
	def get_nb_annulation(self):
		return self.nb_annulation
	
	def get_position(self):
		"""Renvoie la position a laquelle l'action est realisee"""
		return self.position
	
	def get_carte_fini_calculee(self):
		"""Renvoie True si le calcul de la carte a ete fini et false sinon"""
		return self.carte_fini_calculee.value
	
	def set_carte_fini_calculee(self, entier):
		"""carte_fini_calculee vaut 1 si la carte de l'action a deja ete calculee et 0 sinon"""
		self.carte_fini_calculee.value = entier
	
	def get_carte(self):
		return self.carte
	
	def set_carte(self, carte_action):
		self.carte = carte_action
	
	def get_action(self):
		return self.action
