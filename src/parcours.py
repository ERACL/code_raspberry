from action import *
from config import *
from erreur import *
from calcul_carte import *
from log import *
from multiprocessing import Process, Queue
import time
import os

class Parcours():
	def __init__(self,robot,temps,depart):
		#robot represente la classe robot, temps le temps d'une epreuve de la competition et depart le cote par lequel on commence.
		self.robot = robot
		self.temps = temps
		self.depart = depart
		self.nb_tentatives = Config().get_nb_tentatives()
		self.liste_action = []
		self.charger_actions()
		self.creer_actions()
		### On demarre en parallele le calcul des cartes de toutes les actions ###
		calcul_des_cartes = Calcul_carte(self.liste_action)
		self.q = Queue()
		Log().debut_calcul()
		Process(target = calcul_des_cartes.start, args=(self.q,)).start()
		#### INTEGRER ICI UN TEST POUR SAVOIR QUAND DEMARRE LE ROBOT ####
		Log().debut_competition()
		self.demarrer()
		return None
	
	def charger_actions(self):
		"""Charge les actions depuis le fichier actions.cfg"""
		##### On charge le fichier actions.cfg dans lequel sont contenues toutes les actions a effectuer ######
		repertoire = ""
		if (self.depart == "gauche"):
			repertoire = "../cfg/actions_g.cfg"
		else:
			repertoire = "../cfg/actions_d.cfg"
		fichier = open(repertoire, "r")
		ligne = fichier.read().split("\n")
		noms = []
		positions_x = [] 
		positions_y = []
		positions_theta = []
		
		### La, il s'agit de bidouillage de fichier texte dont le but est d'extraire les differentes actions ###
		try:
			for k in range(len(ligne)-1):
				donnees = ligne[k].split(" ")
				noms.append(donnees[0])
				coordonnees = donnees[1].split(",")
				positions_x.append(int(coordonnees[0]))
				positions_y.append(int(coordonnees[1]))
				positions_theta.append(int(coordonnees[2]))
			self.liste_action = []
			for k in range(len(ligne)-1):
				self.liste_action.append((noms[k],(positions_x[k],positions_y[k],positions_theta[k])))
		except:
			Log().edition_action()
			os._exit(1)
		return None
	
	def creer_actions(self):
		"""Les objets Actions sont crees dans cette fonction"""
		#Chaque action a comme attribu son action suivante (utile pour cache le temps de calcul du chemin de l'action suivante). La creation des actions est donc fait dans le sens anti-chronologique
		self.liste_action[-1] = Action(self.robot, self.liste_action[-1][1], self.liste_action[-1][0], None) #La derniere action a 'None' en action suivante
		for k in range(len(self.liste_action)-2,-1,-1):
			self.liste_action[k]=Action(self.robot,self.liste_action[k][1],self.liste_action[k][0],self.liste_action[k+1])
		return None
	
	def demarrer(self):
		fini = False
		compteur = 0 #compteur va parcourir les numeros des actions mais peut valloir deux fois la meme valeur pour refaire une action
		while (fini==False):
			
			try:
				### On lance le chronometre pour savoir en combien de temps se deroule l'action et l'annuler en cas d'action trop longue ###
				k = self.liste_action[compteur]
				
				
				### On modifie l'action en cours du robot ###
				self.robot.set_action_en_cours(k)
				while k.get_carte_fini_calculee() == 0 :
					time.sleep(0.1)
				chrono = TestAction(self.temps)
				chrono.start()	
				k.get_carte().set_map(self.q.get())
				### On lance le debut de l'action ######
				k.executer()
				
				### S'il n'y a pas d'erreur, c'est que l'action s'est bien deroulee et on arrete le chronometre ###
				Log().fin_action(k.get_action(), str(chrono.get_temps()))
				chrono.stop()
				
				### Sinon, c'est qu'il y a eu une erreur (materialisee par une Exception) ####
			except ActionLongue:
				k.incrementer_annulation()
				Log().action_longue(k.get_action())
				k.annule_action()
				
			except CheminFaux:
				k.incrementer_annulation() #On augmente le nombre de tentatives
				Log().calcul_chemin_long(k.get_action())
				self.carte.entretien()
				if (k.get_nb_annulation() <= self.nb_tentatives):
					compteur = compteur-1
					Log().recommencer_action(k.get_action())
				else:
					k.annule_action()
					Log().annuler_action(k.get_action())
			
			except ErreurInterromptAction:
				k.incrementer_annulation() #On augmente le nombre de tentatives
				Log().obstacle(k.get_action())
				### On verifie que l'action n'a pas depasse son nombre de tentatives. ###
				if (k.get_nb_annulation() <= self.nb_tentatives):
					compteur = compteur-1
					Log().recommence(k.get_action())
				else:
					k.annule_action()
					Log().suivante(k.get_action())
				
			### On incremente le compteur puis on regarde si l'on a parcouru toute les actions et si elles se sont toutes bien passees ### 
			compteur += 1
			
			if (compteur==len(self.liste_action)):
				fini = True
			
		return None
		
