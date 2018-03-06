class Obstacle():
	
	#temp vaut False si l'obstacle est permanent et True s'il est temporaire
	#carte est du type Carte (toujours utile de le savoir)

	def __init__(self,carte,P1,P2,temp):
		self.temp = temp
		self.P1 = P1
		self.P2 = P2
		self.carte = carte
		carte.ajouter_obs(self,P1,P2)
	
	def delete(self):
		self.carte.retirer_obs(self.P1,self.P2)
		return None
	
	def get_temp(self):
		return self.temp
	
	def get_coordonnees(self):
		"""renvoie les coordonnees du rectangle a tester pour savoir si l'obstacle a ete pris en compte"""
		X_min = min( self.P1[0], self.P2[0] )
		Y_min = min( self.P1[1], self.P2[1] )
		X_max = max( self.P1[0], self.P2[0] )
		Y_max = max( self.P1[1], self.P2[1] )
		
		return X_min, X_max, Y_min, Y_max
