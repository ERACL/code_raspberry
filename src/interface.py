import os
from communication import *
import sys
import time

class Interface():
	
	def __init__(self):
		self.menu()
		return None
	
	def menu_commande(self):
		print('\n\nBienvenue dans le menu de commande du robot en direct ! Voici les differentes options :')
		print('\n1. avancer(distance)')
		print('\n2. reculer(distance)')
		print('\n3. avancer(position)')
		print('\n4. reculer(position)')
		print('\n5. tourner(angle)')
		print('\n6. get_donnees()')
		print('\n7. set_donnees(x,y,theta)')
		print('\n8. set_pid()')
		print('\n9. tourner_roues_puissance(puissance)')
		print('\n10. pause()')
		print('\n11. delete()')
		print('\n12. quitter')
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			try:
				reponse = input("\nEntrez votre reponse : \n")
				reponse = int(reponse)
				if (reponse == 1) or (reponse == 2) or (reponse == 3) or (reponse == 4) or (reponse == 5) or (reponse == 6) or (reponse == 7) or (reponse == 8) or (reponse == 9) or (reponse == 10) or (reponse == 11) or (reponse == 12):
					reponse_valide = True
				else:
					print("\nVotre reponse n'est pas valide")
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print(sys.exc_info()[0])
				print("\nVotre reponse n'est pas valide")
		return reponse
	
	def menu(self):
		while True:
			entree = self.menu_commande()
			bibliotheque = {
			  1: self.avancer_dist,
			  2: self.reculer_dist,
			  3: self.avancer_pos,
			  4: self.reculer_pos,
			  5: self.tourner,
			  6: self.get_donnees,
			  7: self.set_donnees,
			  8: self.set_pid,
			  9: self.tourner_roues_puissance,
			  10: self.pause,
			  11: self.delete,
			  12: self.shutdown,
			}
			bibliotheque[entree]()
		return None
	
	def avancer_dist(self):
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nDe combien souhaitez-vous avancer?\n")
			try:
				reponse = int(reponse)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		try:
			Communication().avancer_dist(reponse)
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
		return None
	
	def avancer_pos(self):
		reponse_valide = False
		x = None
		while (reponse_valide == False):
			x = input("\nCoordonnees X finales ?\n")
			try:
				x = int(x)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		reponse_valide = False
		y = None
		while (reponse_valide == False):
			y = input("\nCoordonnees Y finales ?\n")
			try:
				y = int(y)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		
		try:
			Communication().avancer((x,y))
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
		return None
	
	def reculer_pos(self):
		reponse_valide = False
		x = None
		while (reponse_valide == False):
			x = input("\nCoordonnees X finales ?\n")
			try:
				x = int(x)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		reponse_valide = False
		y = None
		while (reponse_valide == False):
			y = input("\nCoordonnees Y finales ?\n")
			try:
				y = int(y)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		
		try:
			Communication().reculer((x,y))
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
		return None
	
	def reculer_dist(self):
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nDe combien souhaitez-vous reculer?\n")
			try:
				reponse = int(reponse)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		try:
			Communication().reculer_dist(reponse)
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
		return None
	
	
	def tourner(self):
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nDe combien souhaitez-vous tourner?\n")
			try:
				reponse = int(reponse)
				reponse = reponse%360
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		try:
			Communication().tourner(reponse)
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
		return None
		
	def get_donnees(self):
		try:
			print(Communication().get_donnees())
			time.sleep(3)
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
	
	def set_donnees(self):
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nQue vaut le nouveau x ?\n")
			try:
				reponse = int(reponse)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		x = reponse
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nQue vaut le nouveau y ?\n")
			try:
				reponse = int(reponse)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		y = reponse
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nQue vaut le nouveau theta ?\n")
			try:
				reponse = int(reponse)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		theta = reponse
		try:
			Communication().set_donnees(x,y,theta)
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
		return None
	
	def shutdown(self):
		try:
			Communication().shutdown()
		except IOError:
			print(sys.exc_info()[0])
		os._exit(1)
	
	def pause(self):
		try:
			Communication().pause()
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
	
	def delete(self):
		try:
			Communication().delete()
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
	
	def tourner_roues_puissance(self):
		reponse_valide = False
		reponse = None
		while (reponse_valide == False):
			reponse = input("\nRentrez la puissance moteur voulu (entier entre 0 et 200)\n")
			try:
				reponse = int(reponse)
				reponse_valide = True
			except IOError:
				print(sys.exc_info()[0])
				os._exit(1)
			except SystemExit:
				print(sys.exc_info()[0])
				os._exit(1)
			except KeyboardInterrupt:
				print(sys.exc_info()[0])
				os._exit(1)
			except EOFError:
				print(sys.exc_info()[0])
				os._exit(1)
			except:
				print("\nVotre reponse n'est pas valide")
		try:
			Communication().tourner_roues_puissance(reponse)
		except IOError:
			print(sys.exc_info()[0])
			os._exit(1)
	
	def set_pid(self):
		try:
			Communication().set_pid()
		except IOError as detail:
			print(sys.exc_info()[0])
			print(detail)
			os._exit(1)
		except SystemExit:
			print(sys.exc_info()[0])
			os._exit(1)
		except KeyboardInterrupt:
			print(sys.exc_info()[0])
			os._exit(1)
		except EOFError:
			print(sys.exc_info()[0])
			os._exit(1)
		except:
			print(sys.exc_info()[0])
			os._exit(1)
		
	

	

