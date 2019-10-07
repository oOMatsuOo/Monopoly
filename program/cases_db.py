import sqlite3

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
case_depart = "Case départ"
bonus = "Bonus"
malus = "Malus"
jeux = "Jeux"
batiment = "Batiment"
banquier = "Banquier"
transport = "Transport"
intercom = "Intercom"

BRUN       = 'brun'
BLEU_CLAIR = 'bleu clair'
MAUVE      = 'mauve'
ORANGE     = 'orange'
ROUGE      = 'rouge'
JAUNE      = 'jaune'
VERT       = 'vert'
BLEU_FONCE = 'bleu foncé'
NOIR       = 'noir'

nombre_case = 39

conn = sqlite3.connect('cases.db')
c = conn.cursor()
c.execute( """ 
        CREATE TABLE IF NOT EXISTS cases (
            id integer,
            name text NOT NULL,
            type text NOT NULL,
            color test NOT NULL,
            cost integer,
            rent integer,
            owner text NOT NULL
        ) 
        """)

cases = [(0, case_depart, bonus_malus, 'noir', 0, 20, jeux),
            (2, "case_chance_1", bonus_malus, 'noir', 0,  0, jeux),
            (4, "case_taxe_inverse", bonus_malus, 'noir', 0,  5, jeux),
            (7, "case_chance_2", bonus_malus, 'noir', 0,  0, jeux),
            (17, "case_chance_3", bonus_malus, 'noir', 0,  0, jeux),
            (22, "case_chance_4", bonus_malus, 'noir', 0,  0, jeux),
            (33, "case_chance_5", bonus_malus, 'noir', 0,  0, jeux),
            (36, "case_chance_6", bonus_malus, 'noir', 0,  0, jeux),
            (34, "case_taxe_luxe", bonus_malus, 'noir', 0, 30, jeux),
            (1, "case_brune_1", batiment, BRUN, 5, 2, banquier),
            (3, "case_brune_2", batiment, BRUN, 5, 3, banquier),
            (6, "case_bleue_1", batiment, BLEU_CLAIR, 8, 4, banquier),
            (8, "case_bleue_2", batiment, BLEU_CLAIR, 8, 4, banquier),
            (9, "case_bleue_3", batiment, BLEU_CLAIR, 9, 5, banquier),
            (11, "case_mauve_1", batiment, MAUVE, 12, 7, banquier),
            (13, "case_mauve_2", batiment, MAUVE, 12, 7, banquier),
            (14, "case_mauve_3", batiment, MAUVE, 13, 8, banquier),
            (16, "case_orange_1", batiment, ORANGE, 17, 12, banquier),
            (18, "case_orange_2", batiment, ORANGE, 17, 12, banquier),
            (19, "case_orange_3", batiment, ORANGE, 19, 14, banquier),
            (21, "case_rouge_1", batiment, ROUGE, 23, 18, banquier),
            (23, "case_rouge_2", batiment, ROUGE, 23, 18, banquier),
            (24, "case_rouge_3", batiment, ROUGE, 26, 20, banquier),
            (26, "case_jaune_1", batiment, JAUNE, 30, 24, banquier),
            (27, "case_jaune_2", batiment, JAUNE, 30, 24, banquier),
            (29, "case_jaune_3", batiment, JAUNE, 35, 29, banquier),
            (31, "case_verte_1", batiment, JAUNE, 40, 35, banquier),
            (32, "case_verte_2", batiment, JAUNE, 40, 35, banquier),
            (34, "case_verte_3", batiment, JAUNE, 45, 37, banquier),
            (36, "case_bleue_1", batiment, JAUNE, 50, 40, banquier),
            (39, "case_bleue_2", batiment, JAUNE, 55, 45, banquier),
            (5, "case_transport_1", batiment, transport, 20, 10, banquier),
            (15, "case_transport_2", batiment, transport, 20, 10, banquier),
            (25, "case_transport_3", batiment, transport, 20, 10, banquier),
            (35, "case_transport_4", batiment, transport, 20, 10, banquier),    
            (12, "case_intercom_1", batiment, intercom, 25, 10, banquier),
            (28, "case_intercom_2", batiment, intercom, 25, 10, banquier)]


c.executemany(" INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?)", cases)

for row in c.execute("SELECT * FROM cases"):
    print(row)