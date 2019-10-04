from cases import *
from card import *
import random as rdm

des = [1,2,3,4,5,6]

position = 0
reponse = "oui"

def lancer_des():

    double = False

    premier_de = rdm.choice(des)
    deuxieme_de = rdm.choice(des)
    total = premier_de + deuxieme_de

    if premier_de == deuxieme_de:
        double = True
    else :
        double = False

    return(double, total, premier_de, deuxieme_de)

def deplacement(deplacement):

    global position

    cases_max = nombre_case

    cases_deplacement = position + deplacement

    if (cases_deplacement > cases_max):
        cases_deplacement = cases_deplacement - cases_max
        position = cases_deplacement
    else:
        position = cases_deplacement

    return(position)

##

reponse = input("Voulez-vous jouer ?\n")

if (reponse == "oui"):

    double, total, premier_de, deuxieme_de = (lancer_des())
    deplacement(total)
    print("Votre nouvelle position : ")
    print(position)
    
    while (reponse == "oui"):

        reponse = input("Voulez-vous continuer ?\n")

        if(reponse == "oui"):
            double, total, premier_de, deuxieme_de = (lancer_des())
            deplacement(total)
            print("Votre nouvelle position : ")
            print(position)
        else:
            print("Au revoir.")
else:
    print("Au revoir.")


