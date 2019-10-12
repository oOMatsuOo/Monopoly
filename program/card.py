import random as rdm
import sqlite3

#Liste de tous les messages

#Message type [type du message, message]
#1 = Gain ou perte d'argent
#2 = Téléportation
#3 = Prison
#4 = Sortie de prison
#5 = Dons à tous les joueurs
#6 = Dons de tous les joueurs

message1 = [1, "Félicitation, vous avez validé "]
message2 = [1, "Problème avec MyUliege, vous venez de valider "]
message3 = [2, "Le 48 ne s'est pas arrêter à votre arrêt, vous vous retrouvez à "]
message4 = [1, "Vous venez de signer votre exam', vous perdez "]
message5 = [1, "Problème ave MyUliege, vous venez de perdre "]
message6 = [3, "Vous avez été prit en train de dormir en cours, vous êtes envoyé à la bibilothèque"]

fin_message = " crédits."

all_message = [message1, message2, message3, message4, message5, message6]
montant = [5, 10, 20]
cases = [6, 19, 27]
annif = [2, 5, 10]

#Ajouter la TP dans les cartes chances
#Ajouter la carte prison et les sorties de prison
#Ajouter les cartes "anniversaires" et "Jour de bonté"

def chance ():

    message = rdm.choice(all_message)
    typeCard = message[0]

    if typeCard == 1: #Si la carte est un gain ou une perte d'argent
        credit = rdm.choice(montant)
        card = message[1] + str(credit) + fin_message

        return (typeCard, card, credit)

    elif typeCard == 2: #Si la carte est une TP
        numeroCase = rdm.choice(cases)

        conn = sqlite3.connect('cases.db')
        c = conn.cursor()
        c.execute('SELECT * FROM cases WHERE id_case = ? ', numeroCase)
        caseCarte = c.fetchone()

        card = message[1] + caseCarte[1]

        return(typeCard, card, numeroCase)

    elif typeCard == 3: #Si la carte est une TP bibli
        card = message[1]

        numeroCase = 10
        bibilotheque = 1

        return(typeCard, card, numeroCase, bibilotheque)

    elif typeCard == 4: #Si la carte est une carte sortie de bibli
        card = message[1]

        bibilotheque = 0

        return(typeCard, card, bibilotheque)

    elif typeCard == 5: #Si la carte est une carte don à tous les joueurs
        credit = -(rdm.choice(annif))

        card = message[1] + str(-credit) + fin_message

        return(typeCard, card, credit)
    
    elif typeCard == 6: #Si la carte est une carte don de tous les joueurs
        credit = rdm.choice(annif)

        card = message[1] + str(credit) + fin_message

        return(typeCard, card, credit)