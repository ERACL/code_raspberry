import time
from log import *

#############################################################################
################# Detection du cote de demarrage ############################
#############################################################################

""" 
La convention de demarrage est la suivante :
	- l'interrupteur est passant si le robot commence a droite (quand on le voit de l'exterieur cote demarrage)
	- l'interrupteur est bloquant s'il commence a gauche
 """

def cote(PIN1,PIN2):
	
	connecte = 1
	return connecte



def chargement_PID():
	"""Regle les differentes valeurs du PID du DSPic """
	fichier = open("../cfg/PID.cfg", "r")
	ligne = fichier.read().split("\n")
	kpv,kiv,kdv,kp,ki, kd, vmax, vmin, vmaxt, vmint = None,None,None,None,None,None,None,None,None,None
	for i in range(len(ligne)-1):
		k = ligne[i]
		L = k.split(" = ")
		if L[0] == "kpv" :
			kpv = int(L[1])
		elif L[0] == "kiv" :
			kiv = int(L[1])
		elif L[0] == "kdv" :
			kdv = int(L[1])
		elif L[0] == "kp" :
			kp = int(L[1])
		elif L[0] == "ki" :
			ki = int(L[1])
		elif L[0] == "kd" :
			kd = int(L[1])
		elif L[0] == "vmax" :
			vmax = int(L[1])
		elif L[0] == "vmin" :
			vmin = int(L[1])
		elif L[0] == "vmaxt" :
			vmaxt = int(L[1])
		elif L[0] == "vmint" :
			vmint = int(L[1])
		else:
			Log().edition_PID()
	return kpv,kiv,kdv,kp,ki, kd, vmax, vmin, vmaxt, vmint

