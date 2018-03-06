
from config import *
from communication import *
from math import sqrt
from carte import *
import fonction_chemin_cython
import time
from log import *
#from matplotlib.pyplot import imshow, show

class Carte_action():
	
	def __init__(self, position, carte):
		dx = Config().get_dx()
		self.position = (int(position[0]/dx), int(position[1]/dx)) #position de l'action effectuee dans la carte pixellisee
		self.map = carte
		
	
	def calcul_carte(self, booleen):
		if booleen == True:
			self.map = Carte().get_map()
		debut = time.time()
		print(Config().get_dx())
		print(self.position)
		fonction_chemin_cython.fonction_calcul_carte(self.map, self.position)
		return self.map,time.time() - debut
	
	def get_map(self):
		return self.map
	
	def set_map(self,carte):
		self.map = carte
		return None
	
