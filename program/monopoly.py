from cases_db import *
from card import *
import random as rdm
import sqlite3

des = [1,2,3,4,5,6]

position = 0
reponse = "oui"
jeux = True
quitter = False
j = 1
joueurBanqueroute = 0
bonusDepart = 200

def nomJoueur(nom, numeroJoueur):
    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE cases 
                        SET name = ?
                    WHERE numero = ?""", (nom, numeroJoueur))
    print('Bonjour ' + nom)

def joueurActuel(numero):
    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    t = (numero,)

    c.execute('SELECT * FROM player WHERE id_case = ? ', t)
    joueur = c.fetchone()

    return(joueur)

def lancer_des(numeroJoueur):

    premier_de = rdm.choice(des)
    deuxieme_de = rdm.choice(des)
    total = premier_de + deuxieme_de

    if premier_de == deuxieme_de:
        double = 1
        conn = sqlite3.connect('player.db')
        c = conn.cursor()

        c.execute("""   UPDATE cases 
                            SET double = ?
                        WHERE numero = ?""", (double, numeroJoueur) )

    return(double, total, premier_de, deuxieme_de)

def deplacement(deplacement, numeroJoueur, positionPlayer):

    cases_max = nombre_case

    cases_deplacement = positionPlayer + deplacement

    if (cases_deplacement > cases_max):
        cases_deplacement = cases_deplacement - cases_max
        positionFinal = cases_deplacement
    else:
        positionFinal = cases_deplacement

    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE cases 
                        SET position = ?
                    WHERE numero = ?""", (positionFinal, numeroJoueur))
    joueurActuel[3] = positionFinal

def calcul_case(position_deplacement):

    conn = sqlite3.connect('cases.db')
    c = conn.cursor()

    t = (position_deplacement,)

    c.execute('SELECT * FROM cases WHERE id_case = ? ', t)
    case = c.fetchone()

    return(case)


def modifierProprietaire(position, joueur):
    conn = sqlite3.connect('cases.db')
    c = conn.cursor()

    c.execute("""   UPDATE cases 
                        SET owner = ?
                    WHERE id_case = ?""", (joueur, position) )

def modifArgent(joueur, dépense, argentJoueur):
    argentJoueur = argentJoueur + dépense

    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE cases 
                        SET argent = ?
                    WHERE name = ?""", (argentJoueur, joueur) )
    joueurActuel[2] = argentJoueur
        
def achatCase(proprio, money, case):
    if proprio == 'Banquier':
        reponse_achat = input("Voulez-vous acheter la case ?\n")
        
        if reponse_achat == 'oui':
            modifierProprietairecccc




## Jeux

while( not quitter ):

    reponse_menu = input("Voulez-vous jouer ?\n")   # -> Menu, option : Jeux

    if(reponse_menu == "oui" or reponse == 'o'):
        
        jeux = True #Initialitation des variables , pour commencer à jouer

        while(jeux):

            nombreJoueur = input("Combien y a t-il de joueurs ? (entre 1 et 4)\n")  # Nombre de joueurs
            intNombreJoueur = int(nombreJoueur)

            if(intNombreJoueur <= 0):

                print("Le nombre de joueur est incorrect.")

            elif(intNombreJoueur <= 4):

                while(j < intNombreJoueur):
                    J = str(j)

                    nomJoueur(input("Quel est votre nom ?\n"),j)

                    j += 1
                
                j = 1

                while (joueurBanqueroute < (intNombreJoueur - 1)):

                    joueurActuel = joueurActuel(j)

                    reponse = input("Voulez-vous lancer les dés ?\n") #Lancer les dés pour commencer à jouer
    
                    if(reponse == "oui" or reponse == 'o' ):
                    
                        double, total, premier_de, deuxieme_de = (lancer_des(j))
                        print(premier_de + " + " + deuxieme_de + " = " + total)
                        deplacement(total, j, joueurActuel[3])

                        print("Votre nouvelle position : ", joueurActuel[3])

                        caseActuelle = calcul_case(joueurActuel[3])

                        id_case, name, type_case, color, cost, rent, owner = caseActuelle

                        print("La case sur laquelle vous vous trouvez est celle-ci : " + caseActuelle[1])

                        if caseActuelle[6] == 'Jeux':   #Effet case jeux
                            if caseActuelle[1] == 'Case départ':
                                modifArgent(joueurActuel[1], bonusDepart, joueurActuel[2])

                            elif caseActuelle[1] == 'case chance':
                                chance()

                        elif caseActuelle[6] == 'Banquier' # Achat case
                            if joueurActuel[2] >= caseActuelle[4]:

                                reponse_achat = input("Voulez-vous acheter la case ?\n")

                                if reponse_achat == 'oui':
                                    modifierProprietaire(joueurActuel[3], joueurActuel[1])
                                    modifArgent(joueurActuel[1], caseActuelle[4], joueurActuel[2])
                        else:   #Payer joueur proprio



                    elif(reponse == "non" or reponse == 'n'):
                        print("Au revoir.")
                        jeux = False

                    elif(reponse == 'exit' or reponse == 'e'):
                        print("Au revoir.")
                        jeux = False
                        quitter = True

                    else:
                        print("Je n'ai pas compris votre réponse.\n")
                    
                    if not double :
                        double = False
                        if j > 4:
                            j += 1
                        else:
                            j = 1

            else:
                print("Le nombre de joueur est incorrect.")

    elif(reponse_menu == "non" or reponse == 'n'):
        print("Au revoir.")
        quitter = True

    else :
        print("Je n'ai pas compris votre réponse.\n")