from cases_db import *
from card import *
import random as rdm
import sqlite3

des = [1,2,3,4,5,6]

position = 0
reponse = "oui"
jeux = True
quitter = False 

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

"""def calcul_case(position_deplacement):

    conn = sqlite3.connect('cases.db')
    c = conn.cursor()
    c.execute("SELECT id, name, type, color, cost, rent, owner FROM cases")

    case_emplacement = c.fetchone()

    id_case, nom_case, type_case, couleur, cout_achat, loyer, proprietaire = case_emplacement

    c.close()

    return(case_emplacement)"""

## Jeux

while( not quitter ):

    reponse_menu = input("Voulez-vous jouer ?\n")   # -> Menu, option : Jeux

    if(reponse_menu == "oui"):

        jeux = True #Initialitation des variables , pour commencer à jouer
        position = 0

        while(jeux):

            reponse = input("Voulez-vous lancer les dés ?\n") #Lancer les dés pour commencer à jouer

            if(reponse == "oui"):

                double, total, premier_de, deuxieme_de = (lancer_des())
                deplacement(total)
                print("Votre nouvelle position : ")
                print(position)
                #print(calcul_case(position))

            elif(reponse == "non"):

                print("Au revoir.")
                jeux = False

            else:
                print("Je n'ai pas compris votre réponse.\n")

    elif(reponse_menu == "non"):
        print("Au revoir.")
        quitter = True

    else :
        print("Je n'ai pas compris votre réponse.\n")