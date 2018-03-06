import time
from config import *

class Communication():
	
	#LA CLASSE COMMUNICATION DOIT VERIFIER QUE LE ROBOT EST EN ETAT D'AVANCER !!!!!!!!
	
	
	
	@classmethod
	def get_donnees(self):
		"""Communique avec le DSPic pour connaitre la valeur des positions du robot et son etat dans une tache"""
		
		x = 20
		y = 100
		theta = 10
		etat = 0
		#etat vaut 0 si le robot peut bouger
		return (x,y,theta,etat)
	
	@classmethod
	def set_donnees(self,x,y,theta):
		#On commence par verifier si le robot est arrete
		return None
	


	
	@classmethod
	def avancer(self,longueur):
		return None

	@classmethod
	def reculer(self,longueur):
		"""Verifie que le robot est en etat de reculer et recule ensuite de la longueur indiquee"""
		return None

	@classmethod
	def tourner(self,theta):
		"""Verifie que le robot est en etat de tourner et tourne ensuite de la longueur indiquee"""
		return None
	
	@classmethod
	def pause(self):
		"""Met le mouvement du robot en pause"""
		return None

	@classmethod
	def delete(self):
		"""Supprime le mouvement en pause"""
		return None

	@classmethod
	def play(self):
		"""Reprend le mouvement du robot"""
		return None
	@classmethod
	def reculer_pos(self, position):
		"""Reprend le mouvement du robot"""
		return None
	
	@classmethod
	def avancer_pos(self, position):
		"""Reprend le mouvement du robot"""
		return None
	

	@classmethod
	def shutdown(self):
		return None
	
	@classmethod
	def get_distance(self):
		'''Renvoie la distance avant et arriere captee par les capteurs ultrason'''
		
		distance_av = 1000
		distance_ar = 1000
		return [distance_av, distance_ar]
	
	@classmethod
	def avancer_pos(self,P1):
		"""Dis au robot d'avancer jusqu'au point de coordonnees donnees"""
		
		return None
	
	@classmethod
	def set_pid(self):
		return None
