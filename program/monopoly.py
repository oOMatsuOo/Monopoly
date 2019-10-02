from cases import *
from card import *
import random as rdm

des = [1,2,3,4,5,6]

def lancer_des():

    double = False

    premier_de = rdm.choice(des)
    deuxieme_de = rdm.choice(des)
    total = premier_de + deuxieme_de

    print(str(premier_de) + " + " + str(deuxieme_de) + " = " + str(total))

    if premier_de == deuxieme_de:
        double = True
        print("Bravo, vous avez fait un double !")

    return(double, total, premier_de, deuxieme_de)

lancer_des()