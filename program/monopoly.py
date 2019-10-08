from cases_db import *
from card import *
import random as rdm
import sqlite3

des = [1,2,3,4,5,6]

position = 0
reponse = "oui"
jeux = True
quitter = False

def player(nom):
    return{
        'argent' : 2000,
        'position' : 0,
        'possesion' : 0,
        'nom' : nom
    }



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

def deplacement(deplacement, positionPlayer):

    cases_max = nombre_case

    cases_deplacement = positionPlayer + deplacement

    if (cases_deplacement > cases_max):
        cases_deplacement = cases_deplacement - cases_max
        positionFinal = cases_deplacement
    else:
        positionFinal = cases_deplacement

    return(positionFinal)

def calcul_case(position_deplacement):

    conn = sqlite3.connect('cases.db')
    c = conn.cursor()

    #t = str(position_deplacement)
    t = (position_deplacement,)

    c.execute('SELECT * FROM cases WHERE id_case = ? ', t)
    case = c.fetchone()

    id_case, name, type_case, color, cost, rent, owner = case

    return(case)


def modifierProprietaire(position, joueur):
    conn = sqlite3.connect('cases.db')
    c = conn.cursor()

    c.execute("""   UPDATE cases 
                        SET owner = ?
                    WHERE id_case = ?""", (joueur, position) )
        
def achatCase(proprio, money)




## Jeux

while( not quitter ):

    reponse_menu = input("Voulez-vous jouer ?\n")   # -> Menu, option : Jeux

    if(reponse_menu == "oui" or reponse == 'o'):
        
        jeux = True #Initialitation des variables , pour commencer à jouer

        while(jeux):

            """nombreJoueur = input("Combien y a t-il de joueurs ?")  # Nombre de joueurs
            for
            nomJoueur = input("Quel est votre nom ?\n")
            joueur1 = player(nomJoueur)
            position = 0"""

            reponse = input("Voulez-vous lancer les dés ?\n") #Lancer les dés pour commencer à jouer

            if(reponse == "oui" or reponse == 'o' ):

                double, total, premier_de, deuxieme_de = (lancer_des())
                deplacement(total)

                print("Votre nouvelle position : ", position )
                caseActuelle = calcul_case(position)
                id_case, name, type_case, color, cost, rent, owner = caseActuelle

                print("La case sur laquelle vous vous trouvez est celle-ci : " + caseActuelle[1])

                reponse_achat = input("Voulez-vous acheter la case ?\n")

                if reponse_achat == "oui":
                    modifierProprietaire(position, joueur1)

            elif(reponse == "non" or reponse == 'n'):
                print("Au revoir.")
                jeux = False

            elif(reponse == 'exit' or reponse == 'e'):
                print("Au revoir.")
                jeux = False
                quitter = True

            else:
                print("Je n'ai pas compris votre réponse.\n")

    elif(reponse_menu == "non" or reponse == 'n'):
        print("Au revoir.")
        quitter = True

    else :
        print("Je n'ai pas compris votre réponse.\n")