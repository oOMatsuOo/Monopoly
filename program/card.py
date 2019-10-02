import random as rdm

fin_message = " crédits."

#Liste de tous les messages

message_positif_1 = "Félicitation, vous avez validé "
message_positif_2 = "Problème avec MyUliege, vous venez de valider "
message_negatif_1 = "Vous venez de signer votre exam', vous perdez "
message_negatif_2 = "Problème ave MyUliege, vous venez de perdre "

all_message = [message_negatif_1, message_negatif_2, message_positif_1, message_positif_2]
montant = [2, 5, 10]

#Ajouter la TP dans les cartes chances
#Ajouter la carte prison et les sorties de prison
#Ajouter les cartes "anniversaires" et "Jour de bonté"

def chance ():
    credit = rdm.choice(montant)
    message = rdm.choice(all_message)

    card = message + str(credit) + fin_message
    
    return (card)