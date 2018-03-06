import time
from multiprocessing import Queue
from log import *

class Calcul_carte():
	
	def __init__(self,liste_action):
		self.liste_action = liste_action
		return None
		
		
	
	def start(self,q):
		for k in range(len(self.liste_action)):
			Log().debut_calcul_carte_cache(k)
			carte, temps = self.liste_action[k].calcul_carte(True)
			q.put(carte)
			self.liste_action[k].set_carte_fini_calculee(1)
			Log().fin_calcul_carte_cache(k,temps)
		return None
		
	
		
		
	
	
	
	
	
	
