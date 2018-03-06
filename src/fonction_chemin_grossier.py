from math import sqrt
from config import *
def fonction_chemin_grossier(depart, arrivee, Map, angle_ini, angle_fin):
	"""L'objectif de cette fonction est de trouver le deplacement global du robot. Il est ici assimile a une case carree."""
	
	nb_case_bord = int( Config().get_largeur_robot_max()/Config().get_dx() )
	
	X = len(Map)
	Y =  len(Map[0])
	
	#################################################################################
	##### Deplacement du robot lorsque sa position initiale ou sa position ##########
	#### finale est trop proche d'un mur (on force alors un certain deplacement) ####
	#################################################################################
	
	deplacement_bord_ini = []
	deplacement_bord_fin = []
	liste_point_bord_ini = []
	liste_point_bord_fin = []
	
	#######################################################
	##### On commence par regarder le depart du robot #####
	#######################################################
	
	####### Si le robot demarre de trop pret du bord gauche du terrain ###########
	
	if (depart[0] < nb_case_bord): 
		
		if (angle_ini <= 95) and (angle_ini >= 85) : #Si le robot pointe vers l'interieur du terrain au depart du trajet
			
			obstacle_detection = False
			for i in range((nb_case_bord-depart[0])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((i+depart[0],depart[1]))
				if (Map[i+depart[0]][depart[1]] == 0.5):
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["dr"]*(nb_case_bord-depart[0])) #fav pour dire "Forcer a aller a AVancer sans tourner avant"
				depart[0] = nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		elif (angle_ini <= 275) and (angle_ini >= 265):  #Si le robot pointe vers l'exterieur du terrain
			obstacle_detection = False
			for i in range((nb_case_bord-depart[0])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((i+depart[0],depart[1]))
				if (Map[i+depart[0]][depart[1]] == 0.5): 
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["dre"]*(nb_case_bord-depart[0])) #dre pour dire Droite en REculant
				depart[0] = nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		else:
			print("Le robot demarre pres du bord droit avec un angle de", angle_ini)
	
	########## Si le robot demarre de trop pret du bord droit du terrain #############
	elif (depart[0] > X-nb_case_bord): 
			
		if (angle_ini <= 95) and (angle_ini >= 85) : #Si le robot pointe vers l'exterieur du terrain au depart du trajet
			
			obstacle_detection = False
			for i in range( depart[0]-(X-nb_case_bord) ):	 #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((depart[0]-i,depart[1]))
				if (Map[depart[0]-i][depart[1]] == 0.5):
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["gre"]*( depart[0]-(X-nb_case_bord) ) ) #gre pour dire Gauche en REculant
				depart[0] = X - nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
			
		elif (angle_ini <= 275) and (angle_ini >= 265):  #Si le robot pointe vers l'interieur du terrain
			obstacle_detection = False
			for i in range((nb_case_bord-depart[0])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((depart[0]-i,depart[1]))
				if (Map[depart[0]-i][depart[1]] < 0):  
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["av"]*(nb_case_bord-depart[0])) #av pour dire AVancer 
				depart[0] = X - nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
	
	########## Si le robot demarre de trop pret du bord haut du terrain #############
	elif (depart[1] < nb_case_bord): 
		
		if (angle_ini <= 185) and (angle_ini >= 175) : #Si le robot pointe vers l'interieur du terrain au depart du trajet
			
			obstacle_detection = False
			for i in range((nb_case_bord-depart[1])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((depart[0],depart[1]+i))
				if (Map[depart[0]][depart[1]+i] < 0): 
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["de"]*(nb_case_bord-depart[0])) #de pour dire DEscend
				depart[1] = nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		elif ((angle_ini <= 5) and (angle_ini >=0)) or ((angle_ini >= 355) and (angle_ini <= 360)) :  #Si le robot pointe vers l'exterieur du terrain
			obstacle_detection = False
			for i in range((nb_case_bord-depart[1])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((depart[0],depart[1]+i))
				if (Map[depart[0]][depart[1]+i] < 0): 
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["dre"]*(nb_case_bord-depart[0])) #dre pour dire Descendre en REculant
				depart[1] = nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		else:
			print("Le robot demarre pres du bord droit avec un angle de", angle_ini)
	
	########## Si le robot demarre de trop pret du bord bas du terrain #############
	elif (depart[1] > Y-nb_case_bord): #Si le robot demarre de trop pret du bord droit du terrain
			
		if (angle_ini <= 185) and (angle_ini >= 175): #Si le robot pointe vers l'exterieur du terrain au depart du trajet
			
			obstacle_detection = False
			for i in range( depart[1]-(Y-nb_case_bord) ):	 #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((depart[0],depart[1]-i))
				if (Map[depart[0]][depart[1]-i] < 0):
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_ini.extend(["mre"]*( depart[1]-(Y-nb_case_bord) ) ) #mre pour Monter en REculant
				depart[1] = Y - nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
			
		elif ((angle_ini <= 5) and (angle_ini >=0)) or ((angle_ini >= 355) and (angle_ini <= 360)):  #Si le robot pointe vers l'interieur du terrain
			obstacle_detection = False
			for i in range(depart[1]-(Y-nb_case_bord)): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_ini.append((depart[0],depart[1]-i))
				if (Map[depart[0]][depart[1]-i] < 0):
					obstacle_detection = True
					break
			if (detection_obstacle == False):
				deplacement_bord_ini.extend(["mo"]*(depart[1]-(Y-nb_case_bord))) #mo pour dire MOnter 
				depart[1] = Y - nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
	
	#############################################
	
	##########################################################
	##########################################################
	
	
	#######################################################
	######## On regarde ensuite l'arrivee du robot ########
	#######################################################
	
	
	####### Si le robot arrive de trop pret du bord gauche du terrain ###########
	
	if (arrivee[0] < nb_case_bord): 
		
		if (angle_fin == 90) : #Si le robot pointe vers l'interieur du terrain au depart du trajet
			
			print("La position d'arrivee du robot est etrange")
			print(arrivee, angle_fin)
		
		elif (angle_fin == 270):  #Si le robot pointe vers l'exterieur du terrain
			obstacle_detection = False
			for i in range((nb_case_bord-arrivee[0])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_fin.append((arrivee[0]+i,arrivee[1]))
				if (Map[i+arrivee[0]][arrivee[1]] < 0): 
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_fin.extend(["dr"]*(nb_case_bord-arrivee[0])) #dre pour dire Droite en REculant
				arrivee[0] = nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		else:
			print("Le robot arrive pres du bord droit avec un angle de", angle_fin)
	
	########## Si le robot arrive de trop pret du bord droit du terrain #############
	elif (arrivee[0] > X-nb_case_bord): 
			
		if (angle_fin == 90) : #Si le robot pointe vers l'exterieur du terrain au depart du trajet
			
			obstacle_detection = False
			for i in range( arrivee[0]-(X-nb_case_bord) ):	 #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_fin.append((arrivee[0]-i,arrivee[1]))
				if (Map[arrivee[0]-i][arrivee[1]] < 0):
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_fin.extend(["gre"]*( arrivee[0]-(X-nb_case_bord) )) #gre pour dire Gauche en REculant
				arrivee[0] = X - nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		elif (angle_fin == 270):  #Si le robot pointe vers l'interieur du terrain
			
			print("La position d'arrivee du robot est etrange")
			print(arrivee, angle_fin)
	
	########## Si le robot arrive de trop pret du bord haut du terrain #############
	elif (arrivee[1] < nb_case_bord): 
		
		if (angle_fin == 180) : #Si le robot pointe vers l'interieur du terrain a l'arrivee du trajet
			
			print("La position d'arrivee du robot est etrange")
			print(arrivee, angle_fin)
		
		elif (angle_fin == 0) :  #Si le robot pointe vers l'exterieur du terrain
			obstacle_detection = False
			for i in range((nb_case_bord-arrivee[1])): #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_fin.append((arrivee[0],arrivee[1]+i))
				if (Map[arrivee[0]][arrivee[1]+i] < 0):
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_fin.extend(["mo"]*(nb_case_bord-arrivee[0])) #mo pour MOnter
				arrivee[1] = nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		else:
			print("Le robot arrive pres du bord droit avec un angle de", angle_fin)
	
	########## Si le robot arrive de trop pret du bord bas du terrain #############
	elif (arrivee[1] > Y-nb_case_bord): #Si le robot demarre de trop pret du bord droit du terrain
			
		if (angle_fin == 180): #Si le robot pointe vers l'exterieur du terrain au depart du trajet
			
			obstacle_detection = False
			for i in range( arrivee[1]-(Y-nb_case_bord) ):	 #On verifie qu'il n'y a pas d'obstacle sur le trajet que l'on veut imposer
				liste_point_bord_fin.append((arrivee[0],arrivee[1]-i))
				if (Map[arrivee[0]][arrivee[1]-i] < 0):
					obstacle_detection = True
					break
			if (obstacle_detection == False):
				deplacement_bord_fin.extend(["de"]*( arrivee[1]-(Y-nb_case_bord) ) ) #de pour DEscendre
				arrivee[1] = Y - nb_case_bord #On place le robot a l'endroit qu'il est apres avoir force le deplacement
		
		elif (angle_fin == 0):  #Si le robot pointe vers l'interieur du terrain
			print("La position d'arrivee du robot est etrange")
			print(arrivee, angle_fin)
	
	#############################################
	
	##########################################################
	##########################################################
	
	
	
	##################################################################################
	##################################################################################
	##################################################################################
	
	L1 = [depart]
	# Listes des dernieres cases a points positifs que l'on a visitees
	
	L2 = [arrivee]
	# Listes des dernieres cases a points negatifs que l'on a visitees
	
	fin = []
	#fin stockera les coordonnees finales du point de rencontre
	
	compteur = 0
	stop = False
	Map[depart[0]][depart[1]] = 0
	Map[arrivee[0]][arrivee[1]] = 0 
	while not(stop):
	#Les deux goutes d'huiles se rependent dans la Map. Lorsqu'elles se renctontrent, stop vaut True et on sort de la boucle for.
		compteur+=1
		M = []
		for k in L1:
			if (k[0]>0) and (Map[k[0]-1][k[1]]<=0) : #Si la position x (k[0]) du point est <0 alors on peut regarder en k[0]-1. On utilise ici une subtilite de Python : si la premiere condition n'est pas respectee alors la deuxieme n'est pas regardee (si elle l'etait cela entrainerait une erreur dans notre cas).
				M.append((k[0]-1,k[1]))
				if Map[k[0]-1][k[1]]==0 :
					Map[k[0]-1][k[1]]=compteur
				else :
					stop = True
					fin =(Map[k[0]-1][k[1]],k[0]-1,k[1])
					break
			
			if (k[0]<X-1) and (Map[k[0]+1][k[1]]<=0) :
				M.append((k[0]+1,k[1]))
				if Map[k[0]+1][k[1]]==0 :
					Map[k[0]+1][k[1]]=compteur
				else :
					stop = True
					fin =(Map[k[0]+1][k[1]],k[0]+1,k[1])
					break
			
			if (k[1]>0) and (Map[k[0]][k[1]-1]<=0) :
				M.append((k[0],k[1]-1))
				if Map[k[0]][k[1]-1]==0 :
					Map[k[0]][k[1]-1]=compteur
				else :
					stop = True
					fin =(Map[k[0]][k[1]-1],k[0],k[1]-1)
					break
			
			if (k[1]<Y-1) and (Map[k[0]][k[1]+1]<=0) :
				M.append((k[0],k[1]+1))
				if Map[k[0]][k[1]+1]==0 :
					Map[k[0]][k[1]+1]=compteur
				else :
					stop = True
					fin =(Map[k[0]][k[1]+1],k[0],k[1]+1)
					break
			
			if (k[1]>0) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]-1][k[1]-1]<=0):
			#Lorsque l'on se deplace en diagonale, on rajoute en plus la condition qu'il ne doit pas y avoir d'obstacle (Map[][] == 0.5) sur les cases adjacentes a la diagonale.
				M.append((k[0]-1,k[1]-1))
				if Map[k[0]-1][k[1]-1]==0 :
					Map[k[0]-1][k[1]-1]=compteur
				else :
					stop = True
					fin =(Map[k[0]-1][k[1]-1],k[0]-1,k[1]-1)
					break
			if (k[1]<Y-1) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]-1][k[1]+1]<=0):
				M.append((k[0]-1,k[1]+1))
				if Map[k[0]-1][k[1]+1]==0 :
					Map[k[0]-1][k[1]+1]=compteur
				else :
					stop = True
					fin =(Map[k[0]-1][k[1]+1],k[0]-1,k[1]+1)
					break
			if (k[1]<Y-1) and (k[0]<Y-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]+1][k[1]+1]<=0):
				M.append((k[0]+1,k[1]+1))
				if Map[k[0]+1][k[1]+1]==0 :
					Map[k[0]+1][k[1]+1]=compteur
				else :
					stop = True
					fin =(Map[k[0]+1][k[1]+1],k[0]+1,k[1]+1)
					break
			if (k[1]>0) and (k[0]<Y-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]+1][k[1]-1]<=0):
				M.append((k[0]+1,k[1]-1))
				if Map[k[0]+1][k[1]-1]==0 :
					Map[k[0]+1][k[1]-1]=compteur
				else :
					stop = True
					fin =(Map[k[0]+1][k[1]-1],k[0]+1,k[1]-1)
					break
		L1[:] = M[:]
		M = [] 
		compteur = -compteur
		#On s'interesse a l'autre goutte de depart 
		if not(stop):
			for k in L2:
				if (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]-1][k[1]]>=0) :
					M.append((k[0]-1,k[1]))
					if Map[k[0]-1][k[1]]==0 :
						Map[k[0]-1][k[1]]=compteur
					else :
						stop = True
						fin =(Map[k[0]-1][k[1]],k[0]-1,k[1])
						break
				if (k[0]<X-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]+1][k[1]]>=0):
					M.append((k[0]+1,k[1]))
					if Map[k[0]+1][k[1]]==0 :
						Map[k[0]+1][k[1]]=compteur
					else :
						stop = True
						fin =(Map[k[0]+1][k[1]],k[0]+1,k[1])  
						break
				if (k[1]>0) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]][k[1]-1]>=0):
					M.append((k[0],k[1]-1))
					if Map[k[0]][k[1]-1]==0 :
						Map[k[0]][k[1]-1]=compteur
					else :
						stop = True
						fin =(Map[k[0]][k[1]-1],k[0],k[1]-1)
						break
				if (k[1]<Y-1) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]][k[1]+1]>=0):
					M.append((k[0],k[1]+1))
					if Map[k[0]][k[1]+1]==0 :
						Map[k[0]][k[1]+1]=compteur
					else :
						stop = True
						fin =(Map[k[0]][k[1]+1],k[0],k[1]+1)
						break
				if (k[1]>0) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]-1][k[1]-1]!=0.5) and (Map[k[0]-1][k[1]-1]>=0):
					M.append((k[0]-1,k[1]-1))
					if Map[k[0]-1][k[1]-1]==0 :
						Map[k[0]-1][k[1]-1]=compteur	
					else :
						stop = True
						fin =(Map[k[0]-1][k[1]-1],k[0]-1,k[1]-1)	
						break
				if (k[1]<Y-1) and (k[0]>0) and (Map[k[0]-1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]-1][k[1]+1]!=0.5) and (Map[k[0]-1][k[1]+1]>=0):
					M.append((k[0]-1,k[1]+1))
					if Map[k[0]-1][k[1]+1]==0 :
						Map[k[0]-1][k[1]+1]=compteur
					else :
						stop = True
						fin =(Map[k[0]-1][k[1]+1],k[0]-1,k[1]+1)
						break
				if (k[1]<Y-1) and (k[0]<X-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]+1]!=0.5) and (Map[k[0]+1][k[1]+1]!=0.5) and (Map[k[0]+1][k[1]+1]>=0):
					M.append((k[0]+1,k[1]+1))	
					if Map[k[0]+1][k[1]+1]==0 :
						Map[k[0]+1][k[1]+1]=compteur
					else :
						stop = True
						fin =(Map[k[0]+1][k[1]+1],k[0]+1,k[1]+1)
						break
				if (k[1]>0) and (k[0]<Y-1) and (Map[k[0]+1][k[1]]!=0.5) and (Map[k[0]][k[1]-1]!=0.5) and (Map[k[0]+1][k[1]-1]!=0.5) and (Map[k[0]+1][k[1]-1]>=0):
					M.append((k[0]+1,k[1]-1))	
					if Map[k[0]+1][k[1]-1]==0 :
						Map[k[0]+1][k[1]-1]=compteur	
					else :
						stop = True
						fin =(Map[k[0]-1][k[1]+1],k[0]-1,k[1]+1)
						break
			
		compteur = -compteur
		L2[:] = M[:]

		
		

	#Il faut maintenant remonter pour trouver le chemin le plus court
	
	#On determine le niveau auquel on s'est arrête a chaque demi-chemin
	compteur_p = 0
	compteur_n = 0
	
	if (fin[0]<0):
		compteur_p = compteur
		compteur_n = fin[0]
	else:
		compteur_n = -compteur
		compteur_p = fin[0] 
	
	
	#On remonte la partie positive du chemin
	chemin_p = [0]*(compteur_p)
	point = (fin[1],fin[2])
	liste_point = [] #Contient la liste de tous les points par lesquels on est passe  
	Map[depart[0]][depart[1]] = 0
	Map[arrivee[0]][arrivee[1]] = 0
	for k in range(compteur_p-1,-1,-1):
		liste_point.append(point)
		Map[point[0]][point[1]]=10
		if (Map[point[0]-1][point[1]]==k):
			chemin_p[k]="de" #pour descend
			point = (point[0]-1,point[1])
			continue
		if (Map[point[0]+1][point[1]]==k):
			chemin_p[k]="mo" #pour monte
			point = (point[0]+1,point[1])
			continue
		if (Map[point[0]][point[1]-1]==k):
			chemin_p[k]="dr" #pour droite
			point = (point[0],point[1]-1)
			continue
		if (Map[point[0]][point[1]+1]==k):
			chemin_p[k]="ga" #pour gauche
			point = (point[0],point[1]+1)
			continue
		if (Map[point[0]-1][point[1]-1]==k):
			chemin_p[k]="dedr" #pour descend a droite
			point = (point[0]-1,point[1]-1)
			continue
		if (Map[point[0]+1][point[1]-1]==k):
			chemin_p[k]="modr" #pour monte a droite
			point = (point[0]+1,point[1]-1)
			continue
		if (Map[point[0]-1][point[1]+1]==k):
			chemin_p[k]="dega" #pour descend a gauche
			point = (point[0]-1,point[1]+1)
			continue
		if (Map[point[0]+1][point[1]+1]==k):
			chemin_p[k]="moga" #pour monte a gauche
			point = (point[0]+1,point[1]+1)
			continue
		liste_point.append(point)
	
	#On parcourt maintenant le chemin en partant de l'arrivee
	liste_point_envers = []
	chemin_n = [0]*(abs(compteur_n))
	point = (fin[1],fin[2])
	for k in range(compteur_n+1,1):
		liste_point_envers.append(point)
		Map[point[0]][point[1]]=10
		if (Map[point[0]+1][point[1]]==k):
			chemin_n[k-1]="de" #pour descend
			point = (point[0]+1,point[1])
			continue
		if (Map[point[0]-1][point[1]]==k):
			chemin_n[k-1]="mo" #pour monte
			point = (point[0]-1,point[1])
			continue
		if (Map[point[0]][point[1]+1]==k):
			chemin_n[k-1]="dr" #pour droite
			point = (point[0],point[1]+1)
			continue
		if (Map[point[0]][point[1]-1]==k):
			chemin_n[k-1]="ga" #pour gauche
			point = (point[0],point[1]-1)
			continue
		if (Map[point[0]+1][point[1]+1]==k):
			chemin_n[k-1]="dedr" #pour descend a droite
			point = (point[0]+1,point[1]+1)
			continue
		if (Map[point[0]-1][point[1]+1]==k):
			chemin_n[k-1]="modr" #pour monte a droite
			point = (point[0]-1,point[1]+1)
			continue
		if (Map[point[0]+1][point[1]-1]==k):
			chemin_n[k-1]="dega" #pour descend a gauche
			point = (point[0]+1,point[1]-1)
			continue
		if (Map[point[0]-1][point[1]-1]==k):
			chemin_n[k-1]="moga" #pour monte a gauche
			point = (point[0]-1,point[1]-1)
			continue
	liste_point_envers.append(point)
	#On recolle maintenant les deux listes de points qui ont ete parcourus et on met ces listes dans le bon ordre
	liste_point = liste_point_bord_ini + liste_point + liste_point_envers[::-1] + liste_point_bord_fin[::-1]
	chemin = deplacement_bord_ini+chemin_p+chemin_n+deplacement_bord_fin
	
	return (chemin,liste_point)

