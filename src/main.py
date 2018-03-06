from math import sqrt
import time
import threading
import sys
import signal
import sys

from config import *
from communication import *
from depart import *
from log import *


#La fonction cote permet de savoir de quel cote on demarre

PIN1 = 26
PIN2 = 21

depart = cote(PIN1, PIN2)
if (depart):
	depart = "droite"
else:
	depart = "gauche"

Log().demarrage_cote(depart)

#### On charge les caleurs du PID depuis le fichier de configuration PID.cfg ######
#Communication().set_pid()
####################################################################################

#On charge le fichier de configuration
config = Config()
com = Communication()

from robot import *
robot = Robot(depart)
robot.start()


from interface import *

def arret(signal1, frame):
	Communication().shutdown()
	robot.stop()
	sys.exit(1)
	return None

def menu_commande(signal1, frame):
	Communication().pause()
	Communication().delete()
	robot.stop()
	signal.signal(signal.SIGINT, arret)
	interface = Interface()

signal.signal(signal.SIGINT, menu_commande)

time.sleep(100)
print("Appuie sur ")




from obstacle import *
from action import *
from deplacement import *
from chemin import *
from parcours import *
from ultrason import *

ultrason = Ultrason(robot)

parcours = Parcours(robot, 100, depart)
robot.stop()
ultrason.stop()
Log().fin()
print("FIN")




