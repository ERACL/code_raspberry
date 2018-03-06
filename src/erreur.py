import time
from threading import Thread

class CheminFaux(Exception):
	pass

class ActionLongue(Exception):
	pass

class ErreurActionneur(Exception):
	pass

class ErreurAnnuleAction(Exception):
	pass

class ErreurInterromptAction(Exception):
	pass

class TestAction_Annule(Thread):
	def __init__(self,action):
		Thread.__init__(self)
		self.on = True
		self.action = action
		
	def run(self):
		while (self.on == True) and (self.action.get_action_annule() == False) :
			time.sleep(0.1)
		if (self.on == True):
			self.action.incrementer_annulation()
			raise ErreurAnnuleAction
  
	def stop(self):
		self.on = False
		return None
	
class TestAction_Interrompue(Thread):
	
	def __init__(self, action):
		Thread.__init__(self)
		self.on = True
		self.action = action
	
	def run(self):
		while (self.on == True) and (self.action.get_action_interrompue() == False) :
			time.sleep(0.1)
		if (self.on == True):
			raise ErreurInterromptAction
  
	def stop(self):
		self.on = False
		return None


class TestChemin(Thread):
	
	def __init__(self,temps):
		Thread.__init__(self)
		self.temps = temps
		self.on = True
	
	def run(self):
		debut = time.time()
		while (time.time()<debut + self.temps) and (self.on == True):
			time.sleep(0.2)
		if (self.on == True):
			raise CheminFaux
		return None
	
	def stop(self):
		self.on = False
		return None

class TestAction(Thread):
	
	def __init__(self,temps):
		Thread.__init__(self)
		self.temps = temps
		self.on = True
		self.debut = None
	
	def run(self):
		debut = time.time()
		self.debut = debut
		while (time.time()<debut+self.temps):
			time.sleep(0.2)
		if (self.on == True):
			raise ActionLongue
		return None
	
	def stop(self):
		self.on = False
		return None 
	
	def get_temps(self):
		return time.time() - self.debut	

class Chrono(Thread):
	
	def __init__(self, temps, objet):
		Thread.__init__(self)
		self.temps = temps
		self.on = False
		self.debut = None
		self.objet = objet #objet est l'objet sur lequel on appliquera le marqueur "chronometre"
	
	def run(self):
		self.on = True
		debut = time.time()
		self.debut = debut
		while (time.time() < debut+self.temps):
			time.sleep(0.1)
		self.objet.fin_chronometre()
		return None
		
