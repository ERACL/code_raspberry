from math import sqrt
from config import *
import time





def fonction_trouver_chemin(Map, position_ini):
	#On remonte le chemin depuis la position initiale du robot
	cdef int compteur = Map[position_ini[0]][position_ini[1]] #La valeur de compteur est le nombre detapes minimales qu'il y a pour realiser le deplacement souhaite
	cdef int[2] point = [position_ini[0],position_ini[1]]
	cdef int k
	print(compteur)
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
	point_chemin.append(point)
	point_chemin = point_chemin[1:]
	return (liste_direction, point_chemin, liste_point)

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################


def fonction_calcul_carte(Map, position_fin):
	"""Trace un degrade sur la carte en partant du point position_fin pour pouvoir trouver le chemin depuis n'importe quel point de depart sur la carte"""
	L1 = [position_fin]
	cdef int X = len(Map)
	cdef int Y =  len(Map[0])
	
	cdef int distance_bord = int(Config().get_largeur_robot_max()/Config().get_dx())
	cdef int proche_haut 
	cdef int proche_bas 
	cdef int proche_gauche 
	cdef int proche_droit 
	
	# Listes des dernieres cases a points positifs que l'on a visitees
	cdef int k
	cdef int nb_case = 1
	
	cdef int compteur = 0
	cdef int stop = 0
	Map[position_fin[0]][position_fin[1]] = -1 #On met un -1 sur la position d'arrivee 
	while not(stop==1):
	#Les deux goutes d'huiles se rependent dans la Map. Lorsqu'elles se renctontrent, stop vaut True et on sort de la boucle for.
		compteur+=1
		
		M = []
		if (len(L1)==0):
			stop = 1
		for k in range(len(L1)):
			if (L1[k][0]>0) and (Map[L1[k][0]-1][L1[k][1]]==0) and L1[k][1]>distance_bord and L1[k][1]<Y-distance_bord : #Si la position x (L1[k][0]) du point est <0 alors on peut regarder en L1[k][0]-1. On utilise ici une subtilite de Python : si la premiere condition n'est pas respectee alors la deuxieme n'est pas regardee (si elle l'etait cela entrainerait une erreur dans notre cas).
				M.append((L1[k][0]-1,L1[k][1]))
				Map[L1[k][0]-1][L1[k][1]]=compteur
				
			if (L1[k][0]<X-1) and (Map[L1[k][0]+1][L1[k][1]]==0)  and L1[k][1]>distance_bord and L1[k][1]<Y-distance_bord and L1[k][0]:
				M.append((L1[k][0]+1,L1[k][1]))
				Map[L1[k][0]+1][L1[k][1]]=compteur
			
			if (L1[k][1]>0) and (Map[L1[k][0]][L1[k][1]-1]==0) and L1[k][0]>distance_bord and L1[k][0]<X-distance_bord:
				M.append((L1[k][0],L1[k][1]-1))
				Map[L1[k][0]][L1[k][1]-1]=compteur
			
			if (L1[k][1]<Y-1) and (Map[L1[k][0]][L1[k][1]+1]==0) and L1[k][0]>distance_bord and L1[k][0]<X-distance_bord:
				M.append((L1[k][0],L1[k][1]+1))
				Map[L1[k][0]][L1[k][1]+1]=compteur
			
			if L1[k][0]<X-distance_bord and L1[k][0]>distance_bord and L1[k][1]>distance_bord and L1[k][1]<Y-distance_bord:
				if (L1[k][1]>0) and (L1[k][0]>0) and (Map[L1[k][0]-1][L1[k][1]]!=-2) and (Map[L1[k][0]][L1[k][1]-1]!=-2) and (Map[L1[k][0]-1][L1[k][1]-1]==0):
				#Lorsque l'on se deplace en diagonale, on rajoute en plus la condition qu'il ne doit pas y avoir d'obstacle (Map[][] == -2 en cas d'obstacle) sur les cases adjacentes a la diagonale.	
					M.append((L1[k][0]-1,L1[k][1]-1))
					Map[L1[k][0]-1][L1[k][1]-1]=compteur
					
				if (L1[k][1]<Y-1) and (L1[k][0]>0) and (Map[L1[k][0]-1][L1[k][1]]!=-2) and (Map[L1[k][0]][L1[k][1]+1]!=-2) and (Map[L1[k][0]-1][L1[k][1]+1]==0):
					M.append((L1[k][0]-1,L1[k][1]+1))
					Map[L1[k][0]-1][L1[k][1]+1]=compteur
					
				if (L1[k][1]<Y-1) and (L1[k][0]<Y-1) and (Map[L1[k][0]+1][L1[k][1]]!=-2) and (Map[L1[k][0]][L1[k][1]+1]!=-2) and (Map[L1[k][0]+1][L1[k][1]+1]==0):
					M.append((L1[k][0]+1,L1[k][1]+1))
					Map[L1[k][0]+1][L1[k][1]+1]=compteur
					
				if (L1[k][1]>0) and (L1[k][0]<Y-1) and (Map[L1[k][0]+1][L1[k][1]]!=-2) and (Map[L1[k][0]][L1[k][1]-1]!=-2) and (Map[L1[k][0]+1][L1[k][1]-1]==0):
					M.append((L1[k][0]+1,L1[k][1]-1))
					Map[L1[k][0]+1][L1[k][1]-1]=compteur
						
		L1[:] = M[:]
	return None
