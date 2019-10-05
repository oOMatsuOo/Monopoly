#case type : Position = ["Nom, Type, Couleur, Cout d'achat, Loyer de base / revenus, Propriétaire]

# si case rue -> couleur , si case bonus/Malus -> bonus
# pour les cartes sans propriétaires -> Jeux

import sqlite3
from sqlite3 import Error

BRUN       = (165, 42, 42)
BLEU_CLAIR = (  0,191,255)
MAUVE      = (128,  0,128)
ORANGE     = (255, 69,  0)
ROUGE      = (139,  0,  0)
JAUNE      = (255,215,  0)
VERT       = (  0,128,  0)
BLEU_FONCE = (  0,  0,139)
NOIR       = (  0,  0,  0)


bonus_malus = "Bonus ou Malus"
bonus = "Bonus"
malus = "Malus"
jeux = "Jeux"
batiment = "Batiment"
banquier = "Banquier"
transport = "Transport"
intercom = "Intercom"

nombre_case = 39
 
def main():
    try:
        conn = sqlite3.connect('cases.db')
        cursor = conn.cursor()
        cursor.execute( """ 
        CREATE TABLE IF NOT EXISTS cases (
            id integer PRIMARY KEY,
            name text NOT NULL,
            type text NOT NULL,
            color text NOT NULL,
            cost integer,
            rent integer,
            owner text NOT NULL
        ) 
        """)
        conn.commit()
    except sqlite3.OperationalError:
        print('Erreur la table existe déjà')
    except Exception as e:
        print("Erreur")
        conn.rollback()
    finally:
        conn.close

def db_donnees():

    conn = sqlite3.connect("cases.db")
    c = conn.cursor()

    cases = [(0, "case_depart", bonus_malus, bonus, 20, jeux),(2, "case_chance_1", bonus_malus, bonus,  0, jeux),(4, "case_taxe_inverse", bonus_malus, bonus,  5, jeux),(7, "case_chance_2", bonus_malus, bonus,  0, jeux),(17, "case_chance_3", bonus_malus, bonus,  0, jeux),(22, "case_chance_4", bonus_malus, bonus,  0, jeux)]
    """
    cases_append((33, "case_chance_5", bonus_malus, bonus,  0, jeux)
    cases_append((36, "case_chance_6", bonus_malus, bonus,  0, jeux)
    cases_append((34, "case_taxe_luxe",    bonus_malus, malus, 30, jeux)

    cases_append((1, "case_brune_1", batiment, BRUN, 5, 2, banquier)
    cases_append((3, "case_brune_2", batiment, BRUN, 5, 3, banquier)

    cases_append((6, "case_bleue_1", batiment, BLEU_CLAIR, 8, 4, banquier)
    cases_append((8, "case_bleue_2", batiment, BLEU_CLAIR, 8, 4, banquier)
    cases_append((9, "case_bleue_3", batiment, BLEU_CLAIR, 9, 5, banquier)

    cases_append((11, "case_mauve_1", batiment, MAUVE, 12, 7, banquier)
    cases_append((13, "case_mauve_2", batiment, MAUVE, 12, 7, banquier) 
    cases_append((14, "case_mauve_3", batiment, MAUVE, 13, 8, banquier)

    cases_append((16, "case_orange_1", batiment, ORANGE, 17, 12, banquier))
    cases_append((18, "case_orange_2", batiment, ORANGE, 17, 12, banquier))
    cases_append((19, "case_orange_3", batiment, ORANGE, 19, 14, banquier))

    cases_append((21, "case_rouge_1", batiment, ROUGE, 23, 18, banquier))
    cases_append((23, "case_rouge_2", batiment, ROUGE, 23, 18, banquier))
    cases_append((24, "case_rouge_3", batiment, ROUGE, 26, 20, banquier))

    cases_append((26, "case_jaune_1", batiment, JAUNE, 30, 24, banquier))
    cases_append((27, "case_jaune_2", batiment, JAUNE, 30, 24, banquier))
    cases_append((29, "case_jaune_3", batiment, JAUNE, 35, 29, banquier))

    cases_append((31, "case_verte_1", batiment, JAUNE, 40, 35, banquier))
    cases_append((32, "case_verte_2", batiment, JAUNE, 40, 35, banquier))
    cases_append((34, "case_verte_3", batiment, JAUNE, 45, 37, banquier))

    cases_append((36, "case_bleue_1", batiment, JAUNE, 50, 40, banquier))
    cases_append((39, "case_bleue_2", batiment, JAUNE, 55, 45, banquier))

    cases_append((5, "case_transport_1", batiment, transport, 20, banquier))
    cases_append((15, "case_transport_2", batiment, transport, 20, banquier))
    cases_append((25, "case_transport_3", batiment, transport, 20, banquier))
    cases_append((35, "case_transport_4", batiment, transport, 20, banquier))

    cases_append((12, "case_intercom_1", batiment, intercom, 25, banquier))
    cases_append((28, "case_intercom_2", batiment, intercom, 25, banquier))

    """
    c.executemany(" INSERT INTO cases (?, ?, ?, ?, ?, ?)",cases)
    for row in c.execute("SELECT * FROM cases"):
        print(row)
    """


#Cases spéciales 

case_0  = ["case_depart",       bonus_malus, bonus, 20, jeux]
case_2  = ["case_chance_1",     bonus_malus, bonus,  0, jeux]
case_4  = ["case_taxe_inverse", bonus_malus, bonus,  5, jeux]
case_7  = ["case_chance_2",     bonus_malus, bonus,  0, jeux]
case_17 = ["case_chance_3",     bonus_malus, bonus,  0, jeux]
case_22 = ["case_chance_4",     bonus_malus, bonus,  0, jeux]
case_33 = ["case_chance_5",     bonus_malus, bonus,  0, jeux]
case_36 = ["case_chance_6",     bonus_malus, bonus,  0, jeux]
case_34 = ["case_taxe_luxe",    bonus_malus, malus, 30, jeux]

#Cases brunes

case_1 = ["case_brune_1", batiment, BRUN, 5, 2, banquier]
case_3 = ["case_brune_2", batiment, BRUN, 5, 3, banquier]

#Cases bleues

case_6 = ["case_bleue_1", batiment, BLEU_CLAIR, 8, 4, banquier]
case_8 = ["case_bleue_2", batiment, BLEU_CLAIR, 8, 4, banquier]
case_9 = ["case_bleue_3", batiment, BLEU_CLAIR, 9, 5, banquier]

#Cases mauves

case_11 = ["case_mauve_1", batiment, MAUVE, 12, 7, banquier]
case_13 = ["case_mauve_2", batiment, MAUVE, 12, 7, banquier]
case_14 = ["case_mauve_3", batiment, MAUVE, 13, 8, banquier]

#Cases oranges

case_16 = ["case_orange_1", batiment, ORANGE, 17, 12, banquier]
case_18 = ["case_orange_2", batiment, ORANGE, 17, 12, banquier]
case_19 = ["case_orange_3", batiment, ORANGE, 19, 14, banquier]

#Cases rouges

case_21 = ["case_rouge_1", batiment, ROUGE, 23, 18, banquier]
case_23 = ["case_rouge_2", batiment, ROUGE, 23, 18, banquier]
case_24 = ["case_rouge_3", batiment, ROUGE, 26, 20, banquier]

#Cases jaunes

case_26 = ["case_jaune_1", batiment, JAUNE, 30, 24, banquier]
case_27 = ["case_jaune_2", batiment, JAUNE, 30, 24, banquier]
case_29 = ["case_jaune_3", batiment, JAUNE, 35, 29, banquier]

#Cases vertes

case_31 = ["case_verte_1", batiment, JAUNE, 40, 35, banquier]
case_32 = ["case_verte_2", batiment, JAUNE, 40, 35, banquier]
case_34 = ["case_verte_3", batiment, JAUNE, 45, 37, banquier]

#Cases bleues

case_36 = ["case_bleue_1", batiment, JAUNE, 50, 40, banquier]
case_39 = ["case_bleue_2", batiment, JAUNE, 55, 45, banquier]

#Cases transport

case_5  = ["case_transport_1", batiment, transport, 20, banquier]
case_15 = ["case_transport_2", batiment, transport, 20, banquier]
case_25 = ["case_transport_3", batiment, transport, 20, banquier]
case_35 = ["case_transport_4", batiment, transport, 20, banquier]

#Cases inter-communales

case_12 = ["case_intercom_1", batiment, intercom, 25, banquier]
case_28 = ["case_intercom_2", batiment, intercom, 25, banquier]
"""