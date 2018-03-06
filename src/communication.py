import time
from config import *
from smbus import SMBus
from log import *
from depart import *

class Communication():
	
	#LA CLASSE COMMUNICATION DOIT VERIFIER QUE LE ROBOT EST EN ETAT D'AVANCER !!!!!!!!
	
	adr_DSPic_mot = Config().get_adresse_mot()
	adr_DSPic_cap = Config().get_adresse_cap()
	bus = SMBus(1) #On communique sur le bus I2C 1
	temps_attente = 0.2 #Temps d'attente entre deux communication pour savoir si le robot s'est arrete
	
	@classmethod
	def get_donnees(self):
		"""Communique avec le DSPic pour connaitre la valeur des positions du robot et son etat dans une tache"""
		
		#On recoit les donnees en format brut qu'il faut ensuite traiter
		recu = self.bus.read_i2c_block_data(self.adr_DSPic_mot,10)
		
		#On bidouille les bits pour les remettre dans le bon ordre (voir documentation)
		for k in range(2,9):
			recu[k] += recu[k+1]//128*128-recu[k]//128*128
		#Le premier byte n'est pas lu car il bug :D, le deuxieme n'est que la commande
		[etat, x_poids_faible, x_poids_fort, y_poids_faible, y_poids_fort,theta_poids_faible, theta_poids_fort] = [recu[k] for k in range(2,9)] 
		
		#La commande << permet de shifter pour tranformer le byte de poids fort en nombre reel (1<<8 = 256 soit 1 00000000 en binaire)
		x = (x_poids_fort<<8) + x_poids_faible
		y = (y_poids_fort<<8) + y_poids_faible
		theta = ((theta_poids_fort<<8) + theta_poids_faible)%360
		#etat vaut 0 si le robot peut bouger
		return (x,y,theta,etat)
	
	@classmethod
	def set_donnees(self,x,y,theta):
		#On commence par verifier si le robot est arrete
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		#On modifie sa position
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,0, [int(x)%256, int(x)>>8, int(y)%256, int(y)>>8, int(theta)%256, int(theta)>>8] )  #On commence par dire au DSPic ce que l'on va faire : 0 = set_donnees
		#On verifie que le robot est en revenu a l'etat initial
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None
	


	
	@classmethod
	def avancer_dist(self,longueur):
		"""Verifie que le robot est en etat d'avancer et avance ensuite de la longueur indiquee"""
		#On commence par verifier si le robot est arrete
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,20, [int(longueur)%256,int(longueur)>>8]) #On dit au DSPic que l'on veut avancer (commande 20 = avancer)
		
		#On attend que le robot ait fini son action
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None

	@classmethod
	def reculer_dist(self,longueur):
		"""Verifie que le robot est en etat de reculer et recule ensuite de la longueur indiquee"""
		#On commence par verifier si le robot est arrete
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,21, [int(longueur)%256,int(longueur)>>8])  #On dit au DSPic que l'on veut reculer (commande 21 = reculer)
		
		#On attend que le robot ait fini son action
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None

	@classmethod
	def tourner(self,theta):
		"""Verifie que le robot est en etat de tourner et tourne ensuite de la longueur indiquee"""
		#On commence par verifier si le robot est arrete
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		Log().tourner_robot(theta)
		#if theta > 180:
		#	theta = (360-theta)%360
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,22, [int(theta)%256,int(theta)>>8] )#On dit au DSPic que l'on veut tourner (commande 22 = tourner)
		
		#On attend que le robot ait fini son action
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None
	
	@classmethod
	def pause(self):
		"""Met le mouvement du robot en pause"""
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,30,[]) #On commence par dire au DSPic ce que l'on va faire : 30 = pause
		return None

        @classmethod
        def shutdown(self):
                """Eteint la carte de commande moteur"""
                self.bus.write_i2c_block_data(self.adr_DSPic_mot,33,[]) #On commence par dire au DSPic ce que l'on va faire : 33 = shutdown
                return None

	@classmethod
	def delete(self):
		"""Supprime le mouvement en pause"""
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,32, []) #On commence par dire au DSPic ce que l'on va faire : 32 = delete
		return None

	@classmethod
	def play(self):
		"""Reprend le mouvement du robot"""
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,31, []) #On commence par dire au DSPic ce que l'on va faire : 31 = play
		return None

	@classmethod
	def shutdown(self):
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,33, []) #On commence par dire au DSPic ce que l'on va faire : 33 = shutdown
		return None
	
	@classmethod
	def get_distance(self):
		'''Renvoie la distance avant et arriere captee par les capteurs ultrason'''
		#On recoit les donnees en format brut qu'il faut ensuite traiter
		#recu = self.bus.read_i2c_block_data(self.adr_DSPic_cap,10)
		
		#Le premier byte n'est pas lu car il bug :D, le deuxieme n'est que la commande
		#[distance_av_poids_fort, distance_av_poids_faible, distance_ar_poids_fort, distance_ar_poids_faible] = [recu[k] for k in range(2,6)] 
		#distance_av = (distance_av_poids_fort<<8) + distance_av_poids_faible
		#distance_ar = (distance_ar_poids_fort<<8) + distance_ar_poids_faible
		#return [distance_av, distance_ar]
		return [10000, 10000]
	
	@classmethod
	def avancer(self,P1):
		"""Dis au robot d'avancer jusqu'au point de coordonnees donnees"""
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		Log().avancer_robot_position(int(P1[0]), int(P1[1]))
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,24, [int(P1[0])%256,int(P1[0])>>8, int(P1[1])%256, int(P1[1])>>8]) #On dit au DSPic que l'on veut avancer (commande 24 = avancer en donnant des coordonnees)
		#On attend que le robot ait fini son action
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None
	
	@classmethod
	def reculer(self,P1):
		"""Dis au robot d'avancer jusqu'au point de coordonnees donnees"""
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		Log().reculer_robot_position(int(P1[0]), int(P1[1]))
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,25, [int(P1[0])%256,int(P1[0])>>8, int(P1[1])%256, int(P1[1])>>8]) #On dit au DSPic que l'on veut reculer (commande 25 = reculer en donnant des coordonnees)
		#On attend que le robot ait fini son action
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None
	
	@classmethod
	def set_pid(self):
		#kpv,kiv,kdv,kp,ki, kd, vmax, vmin, vmaxt, vmint = chargement_PID()
		kpv,kiv,kdv,kp,ki, kd, vmax, vmin, vmaxt, vmint, coeff_distance, coeff_theta, coeff_a_position, coeff_theta_position = chargement_PID()
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		#self.bus.write_i2c_block_data(self.adr_DSPic_mot,1, [int(kpv)%256,int(kpv)>>8, int(kiv)%256, int(kiv)>>8, int(kdv)%256,int(kdv)>>8, int(kp)%256, int(kp)>>8]) #, int(ki)%256,int(ki)>>8, int(kd)%256, int(kd)>>8, int(vmax)%256, int(vmin)%256, int(vmaxt)%256, int(vmintint)%256])
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,1, [int(kp)%256,int(kp)>>8, int(ki)%256, int(ki)>>8, int(kd)%256,int(kd)>>8])
		#time.sleep(0.0001)
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,2, [int(kpv)%256,int(kpv)>>8, int(kiv)%256, int(kiv)>>8, int(kdv)%256,int(kdv)>>8, int(kp)%256, int(kp)>>8]);
		#time.sleep(0.0001)
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,3, [int(vmax)%256, int(vmin)%256, int(vmaxt)%256, int(vmint)%256])
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,4, [int(coeff_distance)%256,int(coeff_distance)>>8, int(coeff_theta)%256, int(coeff_theta)>>8]);
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,5, [int(coeff_a_position)%256,int(coeff_a_position)>>8, int(coeff_theta_position)%256, int(coeff_theta_position)>>8]);
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None
	
	@classmethod
	def tourner_roues_puissance(self, puissance):
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		self.bus.write_i2c_block_data(self.adr_DSPic_mot,23, [int(puissance)%256,int(puissance)>>8])
		donnees = self.get_donnees()
		while (donnees[3] != 0):
			donnees = self.get_donnees()
			time.sleep(self.temps_attente)
		return None
	
	
		
