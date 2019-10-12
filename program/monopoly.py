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
bonusDepart = 60

def nomJoueur(nom, numeroJoueur):
    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE player 
                        SET name = ?
                    WHERE numero = ?""", (nom, numeroJoueur))
    conn.commit()
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

        c.execute("""   UPDATE player
                            SET double = ?
                        WHERE numero = ?""", (double, numeroJoueur) )
        conn.commit()

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

    c.execute("""   UPDATE player 
                        SET position = ?
                    WHERE numero = ?""", (positionFinal, numeroJoueur))
    conn.commit()
    joueurActuel[3] = positionFinal

def calcul_case(position_deplacement):

    conn = sqlite3.connect('cases.db')
    c = conn.cursor()

    t = (position_deplacement,)

    c.execute('SELECT * FROM cases WHERE id_case = ? ', t)
    case = c.fetchone()

    return(case)


def modifierProprietaire(position, joueur, nomJoueur):
    conn = sqlite3.connect('cases.db')
    c = conn.cursor()

    c.execute("""   UPDATE cases 
                        SET ownername = ?
                    WHERE id_case = ?""", (nomJoueur, position) )
    c.execute("""   UPDATE cases 
                        SET owner = ?
                    WHERE id_case = ?""", (joueur, position) )

    conn.commit()

def modifArgent(joueur, dépense, argentJoueur):
    argentJoueur = argentJoueur + dépense

    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE player 
                        SET argent = ?
                    WHERE numero = ?""", (argentJoueur, joueur) )
    conn.commit()
    joueurActuel[2] = argentJoueur
        
def achatCase(proprio, nomproprio, money, case, coutcase):
    modifierProprietaire(case, j, nomproprio)
    modifArgent(j, coutcase, money)

def TP(joueur, positionTP):

    if  not joueurActuel[5]:
        conn = sqlite3.connect('player.db')
        c = conn.cursor()

        c.execute("""   UPDATE player
                            SET position = ?
                        WHERE numero = ?""", (positionTP, joueur) )
        conn.commit()
    else :
        nombreCarte = joueurActuel[5]
        carteRestantes = nombreCarte - 1
        conn = sqlite3.connect('player.db')
        c = conn.cursor()

        c.execute("""   UPDATE player
                            SET carteSortieBibli = ?
                        WHERE numero = ?""", (carteRestantes, joueur))
        conn.commit()
        print("Vous aviez une carte sortie de bibliothèque")

def allerBibli(joueur):
    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE player 
                        SET position = ?
                    WHERE numero = ?""", (10, joueur) )
    c.execute("""   UPDATE player
                        SET bibliotheque = 1
                    where numero = ?""", (joueur,))
    conn.commit()
    
def sortieBibli(joueur):
    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE player 
                        SET bibliotheque = ?
                    WHERE numero = ?""", (0, joueur) )
    
    conn.commit()

def ajoutCarteSortieBibli(joueur):
    nombreCarte = joueurActuel[5]
    nombreCarte += 1
    conn = sqlite3.connect('player.db')
    c = conn.cursor()

    c.execute("""   UPDATE player 
                        SET carteSortieBibli = ?
                    WHERE numero = ?""", (nombreCarte, joueur) )
    
    conn.commit()

def donsAJoueurs(joueur, montant):
    don = 3 * montant
    modifArgent(joueur, don, joueurActuel[2])

    i = 0
    while i > 5:
        if i != joueur:
            player = joueurActuel(i)
            player[2] = player[2] - montant
            conn = sqlite3.connect('player.db')
            c = conn.cursor()

            c.execute("""   UPDATE player 
                                SET argent = ?
                            WHERE numero = ?""", (player[2], player) )
            c.commit()
            i +=  1
        else:
            i += 1

def donsdeJoueurs(joueur, montant):


## Jeux

while not quitter:

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

                        if joueurActuel[5] :
                            if double:
                                sortieBibli(j)
                            else:
                                print("Vous devez faire un double pour sortir de Bibliothèque.")
                        
                        if not joueurActuel[5]:
                            deplacement(total, j, joueurActuel[3])

                            print("Votre nouvelle position : ", joueurActuel[3])

                            caseActuelle = calcul_case(joueurActuel[3])

                            id_case, name, type_case, color, cost, rent, owner = caseActuelle

                            print("La case sur laquelle vous vous trouvez est celle-ci : " + caseActuelle[1])

                            if caseActuelle[6] == 'Jeux':   #Effet case jeux
                                if caseActuelle[1] == 'case départ':
                                    modifArgent(joueurActuel[1], bonusDepart, joueurActuel[2])

                                elif caseActuelle[1] == 'case chance': #Effet case chance
                                    carteChance = chance()
                                    print("Vous tirez la carte : \n" + carteChance[1])

                                    if carteChance[0] == 1: #Carte gain ou perte d'argent
                                        modifArgent(joueurActuel[1], carteChance[2], joueurActuel[2])

                                    elif carteChance[0] == 2: #Carte TP
                                        joueurActuel[3] = carteChance[2]
                                        TP(j, carteChance[2])

                                    elif carteChance[0] == 3: #Carte TP bibli
                                        joueurActuel[3] = carteChance[2]
                                        TP(j, carteChance[2])
                                        allerBibli(j)
                                    
                                    elif carteChance[0] == 4: #Carte sortie de Bibli
                                        ajoutCarteSortieBibli(j)
                                    
                                    elif carteChance[0] == 5: #Carte dons à tous les joueurs
                                        donsAJoueurs(j, carteChance[2])

                                    elif carteChance[0] == 6: #Carte dons de tous les joueurs
                                        donsAJoueurs(j, carteChance[2])
                                
                                elif caseActuelle[1] == 'case taxe': #Effet case taxe
                                    modifArgent(j, caseActuelle[5], joueurActuel[2])

                                elif caseActuelle[1] == 'case Aller à la bibliothèque': #Effet case aller à la bibli
                                    allerBibli[j]
                            elif caseActuelle[6] == 'Banquier': #Effet case classique
                                if joueurActuel[2] >= caseActuelle[4]

                                    reponseAchat = input("Voulez-vous achetez cette case ? \n")

                                    if reponseAchat == 'oui': #Achat case
                                        achatCase(j, joueurActuel[1], joueurActuel[2], joueurActuel[3], caseActuelle[4])
                                    #elif reponseAchat == 'non': #Mise aux enchères ?
                            else:
                                proprio = caseActuelle[6]
                                if joueurActuel[2] >= caseActuelle[4]: #Si le joueur a assez d'argent
                                    modifArgent(j, caseActuelle[5], joueurActuel[2])
                                    proprio = joueurActuel[caseActuelle[7]]
                                    modifArgent(caseActuelle[7], caseActuelle[5], proprio[2])
                                else :
                                    #Banqueroute
                            
                            #Construire maison

                            #Construire Hotel

                            #Vendre maison / hotel

                            #Hypothèque case

                            #Dé-hypothèquer case

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