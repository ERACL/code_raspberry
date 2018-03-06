from threading import Thread
from config import *
from communication import *
from log import *
import time

class Robot(Thread):
	
	def __init__(self,depart):
		Thread.__init__(self)
		if (depart == "droite"):  #Mettre un test pour savoir si on commence a droite
			self.x = Config().get_x_init_d()
			self.y = Config().get_y_init_d()
			self.theta = Config().get_theta_init_d()
		else:
			self.x = Config().get_x_init_g()
			self.y = Config().get_y_init_g()
			self.theta = Config().get_theta_init_g()
		Communication().set_donnees(self.x,self.y,self.theta)
		self.etat = True
		self.on = True
		self.action_en_cours = None
		
	def run(self):
		tini = time.time()
		compteur = 0
		while (self.on): #self.on permet de commander l'execution de cette Thread. Il est mis a False quand on veut arreter la Thread
			donnees = Communication().get_donnees() 
			self.x, self.y,self.theta, self.etat = donnees[0],donnees[1],donnees[2],donnees[3]
			compteur+=1
			if (compteur%5 == 0):
				compteur = 0
				Log().position_robot(self.x, self.y,self.theta, self.etat)
			time.sleep(0.1)
		return None

	def get_position(self):
		return (self.x,self.y)

	def get_angle(self):
		return self.theta
	
	def arret_robot(self):
		Communication().pause()
		donnees = Communication.get_donnees()
		self.x, self.y,self.theta = donnees[0],donnes[1],donnees[2]
		return None

	def redemarrage_robot(self):
		Communcation().play()
		return None
	
	def get_donnees(self):
		return (self.x,self.y,self.theta, self.etat)
	
	def stop(self):
		self.on = False
		return None
	
	def get_action_en_cours(self):
		"""Permet d'obtenir l'action en cours d'execution par le robot. Si aucune n'est en cours, elle vaut None"""
		return self.action_en_cours
	
	def set_action_en_cours(self, action):
		"""Permet de changer l'action en cours d'execution par le robot"""
		self.action_en_cours = action
		return None
		


