from threading import Thread
from math import sin, pi, cos
import time
from communication import *
from config import *
from obstacle import *
from math import *
from carte import *
from erreur import *

#On definit le zero degree VERS LE HAUT dans MA carte

#Toutes les distances sont en mm

class Ultrason(Thread):
	
	def __init__(self, robot):
		Thread.__init__(self) #Ligne necessaire au fonctionnement de la Thread (on initialise l'objet Thread)
		self.robot = robot
		self.carte = Carte()
		self.active = True #Si active vaut False, on ne prend pas en compte les capteurs
		self.on = True #Permet d'eteindre la Thread a la fin
		self.temps_attente = 5 #Temps d'attente lorsque l'on a detecte un obstacle pour savoir s'il s'en va
		self.distance_arret = Config().get_distance_arret()
		self.chronometre = False
		self.precision = 10
		
	
	def run(self) :
		while (self.on == True) : #Tant que les ultrason sont en etat "on"
			if (self.active == False):
				time.sleep(0.1)
			else:
				[distance_av, distance_ar] = Communication().get_distance()
				#####################################################
				### Premier cas, le robot est en train d'avancer. ###
				#####################################################
				if (donnees[4] == 1): #Si le robot est en train d'avancer
					if (distance_av < distance_arret):
						longueur_centre_capteur = int(Config().get_largeur_du_robot()/2)
						longueur_centre_obstacle = longeur_centre_capteur + distance_av
						if self.carte.verification(longueur_centre_obstacle + precision, self.robot.get_donnees()) == False: #Si l'obstacle n'avait pas encore ete detecte
							Communication().pause()
							position = self.robot.get_donnees()
							#### POSITIONNEMENT DE L'OBSTACLE DETECTE ##########
							L = Config().get_longueur_robot_max()
							theta = position[2]*pi/180
							X_min_obstacle = position[0] + int(sin(theta)*(distance) - L*cos(theta))
							X_max_obstacle = position[0] + int(sin(theta)*(distance) + L*(cos(theta)+sin(theta)))
							Y_min_obstacle = position[1] + int(-cos(theta)*(distance) - L*(cos(theta)+sin(theta)))
							Y_max_obstacle = position[1] + int(-cos(theta)*(distance) + L*sin(theta))
							####################################################
							chrono = Chrono(self.temps_attente)
							self.debut_chronometre()
							chrono.start()
							self.carte.ajouter_obstacle((X_min_obstacle,Y_min_obstacle), (X_max_obstacle, Y_max_obstacle))
							self.robot.get_action_en_cours().get_carte().set_map(self.carte.get_map()) #On met la nouvelle carte avec l'obstacle en plus sur la nouvelle carte pour calculer la nouvelle carte
							
							nouvelle_carte = self.robot.get_action_en_cours().calcul_carte(False) #On lance le calcul de la nouvelle carte pendant le temps d'attente pour savoir si l'obstacle repartira apres.
							self.robot.get_action_en_cours().get_carte().set_map(nouvelle_carte)
							while (self.chronometre == False): #Si le temps d'attente n'est pas encore passe
								time.sleep(0.1)
							
							[distance_av, distance_ar] = Communication().get_distance() #Apres avoir attendu le temps reglementaire, on regarde si l'obstacle est toujours la
							if (distance_av < distance_arret) :
								Communication().delete()
								self.robot.get_action_en_cours().set_action_annule(True) #On annule l'action
							else:
								Communication().play()
				
				######################################################
				######################################################
				if (donnees[4] == 2): #Si le robot est en train de reculer
					if (distance_ar < distance_arret):
						longueur_centre_capteur = int(Config().get_largeur_du_robot()/2)
						longueur_centre_obstacle = longeur_centre_capteur + distance_ar
						if self.carte.verification(longueur_centre_obstacle + precision, self.robot.get_donnees()) == False: #Si l'obstacle n'avait pas encore ete detecte
							Communication().pause()
							position = self.robot.get_donnees()
							########### POSITIONNEMENT DE L'OBSTACLE DETECTE #################
							L = Config().get_longueur_robot_max()
							theta = position[2]*pi/180
							X_min_obstacle = position[0] + int(sin(theta)*(distance) - L*cos(theta))
							X_max_obstacle = position[0] + int(sin(theta)*(distance) + L*(-cos(theta)+sin(theta)))
							Y_min_obstacle = position[1] + int(-cos(theta)*(distance) + L*(cos(theta)-sin(theta)))
							Y_max_obstacle = position[1] + int(-cos(theta)*(distance) + L*sin(theta))
							##################################################################
							chrono = Chrono(self.temps_attente)
							self.debut_chronometre()
							chrono.start()
							self.carte.ajouter_obstacle((X_min_obstacle,Y_min_obstacle), (X_max_obstacle, Y_max_obstacle))
							self.robot.get_action_en_cours().get_carte().set_map(self.carte.get_map()) #On met la nouvelle carte avec l'obstacle en plus sur la nouvelle carte pour calculer la nouvelle carte
							
							nouvelle_carte = self.robot.get_action_en_cours().calcul_carte(False) #On lance le calcul de la nouvelle carte pendant le temps d'attente pour savoir si l'obstacle repartira apres.
							self.robot.get_action_en_cours().get_carte().set_map(nouvelle_carte)
							while (self.chronometre == False): #Si le temps d'attente n'est pas encore passe
								time.sleep(0.1)
							
							[distance_av, distance_ar] = Communication().get_distance() #Apres avoir attendu le temps reglementaire, on regarde si l'obstacle est toujours la
							if (distance_av < distance_arret) :
								Communication().delete()
								self.robot.get_action_en_cours().set_action_annule(True) #On annule l'action
							else:
								Communication().play()
				
							
	
	def debut_chronometre(self):
		"""Initialise le marqueur de fin pour une mesure de temps"""
		self.chronometre = False
	
	def fin_chronometre(self):
		"""Marque que le temps a attendre est ecoule"""
		self.chronometre = True
	
	def stop(self):
		self.on = False
	
		
