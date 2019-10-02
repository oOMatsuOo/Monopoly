#case type : [Emplacement, Type, Couleur, Cout d'achat, Loyer de base / revenus, Propriétaire]

# si case rue -> couleur , si case Bonus/Malus -> Bonus
# pour les cartes sans propriétaires -> Jeux

BRUN       = (165, 42, 42)
BLEU_CLAIR = (  0,191,255)
MAUVE      = (128,  0,128)
ORANGE     = (255, 69,  0)
ROUGE      = (139,  0,  0)
JAUNE      = (255,215,  0)
VERT       = (  0,128,  0)
BLEU_FONCE = (  0,  0,139)



Bonus = "Bonus"
Bonus_Malus = "Bonus ou Malus"
Jeux = "Jeux"

#Cases spéciales 

case_depart = [0, Bonus_Malus, Bonus, 20, Jeux]

#Cases brunes

case_brune_1 = [1, batiment, BRUN, 5, 2, banquier]
case_brune_2 = [3, batiment, BRUN, 5, 3, banquier]

#Cases bleues

case_bleue_1 = [6, batiment, BLEU, 8, 4, banquier]
case_bleue_2 = [8, batiment, BLEU, 8, 4, banquier]
case_bleue_3 = [9, batiment, BLEU, 9, 5, banquier]

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

case_jaune_1 = [22, batiment, JAUNE, 30, 24, banquier]
case_jaune_2 = [23, batiment, JAUNE, 30, 24, banquier]
case_jaune_3 = [25, batiment, JAUNE, 35, 29, banquier]

#Cases vertes

case_verte_1 = [27, batiment, JAUNE, 40, 35, banquier]
case_verte_1 = [28, batiment, JAUNE, 40, 35, banquier]
case_verte_1 = [30, batiment, JAUNE, 40, 35, banquier]