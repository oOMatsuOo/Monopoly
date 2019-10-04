#case type : [Emplacement, Type, Couleur, Cout d'achat, Loyer de base / revenus, Propriétaire]

# si case rue -> couleur , si case bonus/Malus -> bonus
# pour les cartes sans propriétaires -> Jeux

BRUN       = (165, 42, 42)
BLEU_CLAIR = (  0,191,255)
MAUVE      = (128,  0,128)
ORANGE     = (255, 69,  0)
ROUGE      = (139,  0,  0)
JAUNE      = (255,215,  0)
VERT       = (  0,128,  0)
BLEU_FONCE = (  0,  0,139)


bonus_malus = "Bonus ou Malus"
bonus = "Bonus"
malus = "Malus"
jeux = "Jeux"
batiment = "Batiment"
banquier = "Banquier"
transport = "Transport"
intercom = "Intercom"

nombre_case = 39

#Cases spéciales 

case_depart       = [ 0, bonus_malus, bonus, 20, jeux]
case_chance_1     = [ 2, bonus_malus, bonus,  0, jeux]
case_taxe_inverse = [ 4, bonus_malus, bonus,  5, jeux]
case_chance_2     = [ 7, bonus_malus, bonus,  0, jeux]
case_chance_3     = [17, bonus_malus, bonus,  0, jeux]
case_chance_4     = [22, bonus_malus, bonus,  0, jeux]
case_chance_5     = [33, bonus_malus, bonus,  0, jeux]
case_chance_6     = [36, bonus_malus, bonus,  0, jeux]
case_taxe_luxe    = [34, bonus_malus, malus, 30, jeux]

#Cases brunes

case_brune_1 = [1, batiment, BRUN, 5, 2, banquier]
case_brune_2 = [3, batiment, BRUN, 5, 3, banquier]

#Cases bleues

case_bleue_1 = [6, batiment, BLEU_CLAIR, 8, 4, banquier]
case_bleue_2 = [8, batiment, BLEU_CLAIR, 8, 4, banquier]
case_bleue_3 = [9, batiment, BLEU_CLAIR, 9, 5, banquier]

#Cases mauves

case_mauve_1 = [11, batiment, MAUVE, 12, 7, banquier]
case_mauve_2 = [13, batiment, MAUVE, 12, 7, banquier]
case_mauve_3 = [14, batiment, MAUVE, 13, 8, banquier]

#Cases oranges

case_orange_1 = [16, batiment, ORANGE, 17, 12, banquier]
case_orange_2 = [18, batiment, ORANGE, 17, 12, banquier]
case_orange_3 = [19, batiment, ORANGE, 19, 14, banquier]

#Cases rouges

case_rouge_1 = [21, batiment, ROUGE, 23, 18, banquier]
case_rouge_2 = [23, batiment, ROUGE, 23, 18, banquier]
case_rouge_3 = [24, batiment, ROUGE, 26, 20, banquier]

#Cases jaunes

case_jaune_1 = [26, batiment, JAUNE, 30, 24, banquier]
case_jaune_2 = [27, batiment, JAUNE, 30, 24, banquier]
case_jaune_3 = [29, batiment, JAUNE, 35, 29, banquier]

#Cases vertes

case_verte_1 = [31, batiment, JAUNE, 40, 35, banquier]
case_verte_2 = [32, batiment, JAUNE, 40, 35, banquier]
case_verte_3 = [34, batiment, JAUNE, 45, 37, banquier]

#Cases bleues

case_bleue_1 = [36, batiment, JAUNE, 50, 40, banquier]
case_bleue_2 = [39, batiment, JAUNE, 55, 45, banquier]

#Cases transport

case_transport_1 = [ 5, batiment, transport, 20, banquier]
case_transport_2 = [15, batiment, transport, 20, banquier]
case_transport_3 = [25, batiment, transport, 20, banquier]
case_transport_4 = [35, batiment, transport, 20, banquier]

#Cases inter-communales

case_intercom_1 = [12, batiment, intercom, 25, banquier]
case_intercom_2 = [28, batiment, intercom, 25, banquier]

