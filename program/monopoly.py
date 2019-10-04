from cases import *
from card import *
import random as rdm

des = [1,2,3,4,5,6]

position = 0

def lancer_des():

    double = False

    premier_de = rdm.choice(des)
    deuxieme_de = rdm.choice(des)
    total = premier_de + deuxieme_de

    print(str(premier_de) + " + " + str(deuxieme_de) + " = " + str(total))

    if premier_de == deuxieme_de:
        double = True
        print("Bravo, vous avez fait un double !")
    else :
        double = False

    return(double, total, premier_de, deuxieme_de)

def position(deplacement, position):

    global position

    cases_max = nombre_case

    cases_deplacement = position + deplacement

    if (cases_deplacement > cases_max):
        cases_deplacement = cases_deplacement - cases_max
        position = cases_deplacement
    else:
        position = cases_deplacement

    return(position)

lancer_des()
 

