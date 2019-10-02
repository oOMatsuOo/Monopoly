import random as rdm

#Liste de tous les messages

#Message type [type du message, message]
#1 = Gain ou perte d'argent
#2 = Téléportation
#3 = Prison
#4 = Sortie de prison
#5 = Gain de tous les joueurs ou dons à tous les joueurs

message_positif_1 = [1, "Félicitation, vous avez validé "]
message_positif_2 = [1, "Problème avec MyUliege, vous venez de valider "]
message_positif_3 = [2, "Le 48 ne s'est pas arrêter à votre arrêt, vous vous retrouvez à "]
message_negatif_1 = [1, "Vous venez de signer votre exam', vous perdez "]
message_negatif_2 = [1, "Problème ave MyUliege, vous venez de perdre "]
message_negatif_3 = [3, "Vous avez été prit en train de dormir en cours, vous êtes envoyé à la bibilothèque"]

fin_message = " crédits."

all_message = [message_negatif_1, message_negatif_2, message_positif_1, message_positif_2]
montant = [2, 5, 10]

#Ajouter la TP dans les cartes chances
#Ajouter la carte prison et les sorties de prison
#Ajouter les cartes "anniversaires" et "Jour de bonté"

def chance ():

    message = rdm.choice(all_message)
    credit = rdm.choice(montant)

    card = message + str(credit) + fin_message
    
    return (card)