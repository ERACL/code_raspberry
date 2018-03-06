import time
from multiprocessing import Process, Value

class Proc():
	
	def __init__(self):
		self.on = Value('i',1)
	def fonction(self, test):
		debut = time.time()
		while time.time()-debut<5:
			print("Le process est en train de calculer...", test)
			time.sleep(0.5)
		self.on.value = 0
		return None

if __name__ == '__main__':
	proc = Proc()
	p = Process(target=proc.fonction, args=("14",)).start()
	while proc.on.value == 1:
		print("En attente de la fin du calcul", proc.on.value)
		time.sleep(0.5)
	print("Le process a fini de calculer !")
	p.join()
