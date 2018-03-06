import logging
import time
import logging.config
from logging.handlers import TimedRotatingFileHandler

class Log():
	
	logging.config.fileConfig('../cfg/log.cfg')
	TimedRotatingFileHandler(filename='../log/logs.log',when='s',utc=True).doRollover()
	
	# create logger
	action = logging.getLogger('Action')
	chemin = logging.getLogger('Chemin')
	carte = logging.getLogger('Cartes')
	position = logging.getLogger('Coords')
	communication = logging.getLogger('Transm')
	
	
	@classmethod
	def debut(self):
		self.action.info("Allumage du robot")
		return None
	
	@classmethod
	def recommence(self, action):
		self.action.info("L'action "+action+" a ete recommencee")
		return None
	
	@classmethod
	def edition_action(self):
		self.action.critical("Le fichier des actions a ete mal edite")
		return None
	
	@classmethod
	def action_longue(self, action):
		self.action.warning("L'action "+action+" a ete trop longue a executee")
		return None
	
	@classmethod
	def fin_action(self, action, temps):
		self.action.info("L'action "+ action+ " a ete execute en "+ temps+ " secondes")
		return None
	
	@classmethod
	def calcul_chemin_long(self, action):
		self.chemin.warning("Le calcul du chemin de l'action "+ action+ " a pris trop de temps. La carte est nettoyee.")
		return None
	
	@classmethod
	def annuler_action(self, action):
		self.action.warning("On annule l'action "+ action + " et on passe a la suivante")
		return None
	
	@classmethod
	def obstacle(self, action):
		self.action.warning("L'action "+ action+ " a ete interrompu pour cause d'obstacles sur les voies")
		return None
	
	@classmethod
	def demarrage_cote(self, cote):
		self.action.info("On commence a "+ cote)
		return None
	
	@classmethod
	def recommence(self, action):
		self.action.error("On annule l'action "+ action+" et on passe a la suivante")
		return None
	
	@classmethod
	def debut_calcul(self):
		self.action.info("On commence le calcul des differentes cartes")
		return None
	
	@classmethod
	def debut_competition(self):
		self.action.info("Debut de la competition")
		return None
	
	@classmethod
	def fin(self):
		self.action.info("Fin du programme")
		return None
	
	@classmethod
	def debut_calcul_chemin(self):
		self.chemin.info("Debut du calcul du chemin de l'action")
		return None
	
	@classmethod
	def fin_calcul_chemin(self):
		self.chemin.info("Fin du calcul du chemin")
		return None
	
	@classmethod
	def debut_calcul_carte_cache(self, numero):
		self.carte.info("Debut du calcul (en cache) de la carte numero "+ str(numero))
		return None
	
	@classmethod
	def fin_calcul_carte_cache(self, numero, temps):
		self.carte.info("Fin du calcul (en cache) de la carte numero "+ str(numero)+" en "+str(temps))
		return None
	
	@classmethod
	def calcul_chemin(self, chemin):
		self.chemin.critical("Le calcul des chemins est incoherent, il vaut "+ chemin)
		return None
	
	@classmethod
	def debut_action(self, action):
		self.action.info("Debut de l'execution de l'action : "+ action)
		return None
	
	@classmethod
	def position_robot(self, x, y, theta, etat):
		self.position.info("Position du robot x = "+str(x)+", y = "+str(y)+", theta = "+str(theta)+", etat = "+str(etat))
		return None 
	
	@classmethod
	def chemin_robot(self, chemin):
		self.chemin.debug("Chemin du robot : "+str(chemin))
		return None
	
	@classmethod
	def tourner_robot(self, angle):
		self.communication.info("Communication au DSPic : tourner de "+ str(angle))
		return None
	
	@classmethod
	def avancer_robot_position(self, x,y):
		self.communication.info('Communication au DSPic : avancer en position x = '+str(x)+", y = " + str(y))
		return None
	
	@classmethod
	def reculer_robot_position(self, x,y):
		self.communication.info('Communication au DSPic : reculer en position x = '+str(x)+", y = " + str(y))
		return None
	
	@classmethod
	def edition_obstacle(self):
		self.carte.critical("Le fichier de configuration des obstacles a ete mal edite")
		return None
	
	@classmethod
	def edition_PID(self):
		self.communication.critical("Le fichier de configuration du PID a ete mal edite")
		return None

        @classmethod
        def affiche_carte(self, carte):
                self.carte.debug(str(carte))
                return None
	
	
	
