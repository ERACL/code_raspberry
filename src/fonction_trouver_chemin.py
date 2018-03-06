def fonction_trouver_chemin(Map, position_ini):
	#On remonte le chemin depuis la position initiale du robot
	compteur = Map[position_ini[0]][position_ini[1]] #La valeur de compteur est le nombre detapes minimales qu'il y a pour realiser le deplacement souhaite
	point = [position_ini[0],position_ini[1]]
	point_chemin = [] #Contient la liste des points a envoyer au DSPic
	liste_point = [] #Contient la liste de tous les points par lesquels on est passe
	liste_direction = [] #Contient la liste des directions pour atteindre les points envoyes au DSPic
	
	for k in range(compteur-1,-1,-1):
		liste_point.append(point)
		if (Map[point[0]-1][point[1]]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "de")) == False:
				liste_direction.append("de") #pour descend
				point_chemin.append(point)
			point = (point[0]-1,point[1])
		elif (Map[point[0]+1][point[1]]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "mo")) == False:
				liste_direction.append("mo") #pour monte
				point_chemin.append(point)
			point = (point[0]+1,point[1])
		elif (Map[point[0]][point[1]-1]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "dr")) == False:
				liste_direction.append("dr") #pour droite
				point_chemin.append(point)
			point = (point[0],point[1]-1)
		elif (Map[point[0]][point[1]+1]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "ga")) == False:
				liste_direction.append("ga") #pour gauche
				point_chemin.append(point)
			point = (point[0],point[1]+1)
		elif (Map[point[0]-1][point[1]-1]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "dedr")) == False:
				liste_direction.append("dedr") #pour descend a droite
				point_chemin.append(point)
			point = (point[0]-1,point[1]-1)
		elif (Map[point[0]+1][point[1]-1]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "modr")) == False:
				liste_direction.append("modr") #pour monte a droite
				point_chemin.append(point)
			point = (point[0]+1,point[1]-1)
		elif (Map[point[0]-1][point[1]+1]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "dega")) == False:
				liste_direction.append("dega") #pour descend a gauche
				point_chemin.append(point)
			point = (point[0]-1,point[1]+1)
		elif (Map[point[0]+1][point[1]+1]==k):
			if ((len(liste_direction) != 0) and (liste_direction[-1] == "moga")) == False:
				liste_direction.append("moga") #pour monte a gauche
				point_chemin.append(point)
			point = (point[0]+1,point[1]+1)
	
	return (liste_direction, point_chemin, liste_point)
