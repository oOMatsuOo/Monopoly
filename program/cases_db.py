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

bonus_malus = 'Bonus ou Malus'
case_depart = 'Case départ'
bonus = 'Bonus'
malus = 'Malus'
jeux = 'Jeux'
batiment = 'Batiment'
banquier = 'Banquier'
transport = 'Transport'
intercom = 'Intercom'
bibliothèque = 'Bibliothèque'
parking = 'Parking'
allerBibliothèque = 'Aller à la bibliothèque'

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
            id_case text NOT NULL,
            name text NOT NULL,
            type text NOT NULL,
            color test NOT NULL,
            cost real,
            rent real,
            ownername text NOT NULL,
            owner real
        ) 
        """)

cases =     [(0, 'case départ', bonus_malus, 'noir', 0, 20, jeux, 0),
            (2, 'case chance', bonus_malus, 'noir', 0,  0, jeux, 0),
            (4, 'case taxe', bonus_malus, 'noir', 0,  5, jeux, 0),
            (7, 'case chance', bonus_malus, 'noir', 0,  0, jeux, 0),
            (17, 'case chance', bonus_malus, 'noir', 0,  0, jeux, 0),
            (22, 'case chance', bonus_malus, 'noir', 0,  0, jeux, 0),
            (33, 'case chance', bonus_malus, 'noir', 0,  0, jeux, 0),
            (36, 'case chance', bonus_malus, 'noir', 0,  0, jeux, 0),
            (34, 'case taxe', bonus_malus, 'noir', 0, -30, jeux, 0),

            (1, 'case brune 1', batiment, BRUN, 5, 2, banquier, 0),
            (3, 'case brune 2', batiment, BRUN, 5, 3, banquier, 0),

            (6, 'case bleue 1', batiment, BLEU_CLAIR, 8, 4, banquier, 0),
            (8, 'case bleue 2', batiment, BLEU_CLAIR, 8, 4, banquier, 0),
            (9, 'case bleue 3', batiment, BLEU_CLAIR, 9, 5, banquier, 0),

            (11, 'case mauve 1', batiment, MAUVE, 12, 7, banquier, 0),
            (13, 'case mauve 2', batiment, MAUVE, 12, 7, banquier, 0),
            (14, 'case mauve 3', batiment, MAUVE, 13, 8, banquier, 0),

            (16, 'case orange 1', batiment, ORANGE, 17, 12, banquier, 0),
            (18, 'case orange 2', batiment, ORANGE, 17, 12, banquier, 0),
            (19, 'case orange 3', batiment, ORANGE, 19, 14, banquier, 0),

            (21, 'case rouge 1', batiment, ROUGE, 23, 18, banquier, 0),
            (23, 'case rouge 2', batiment, ROUGE, 23, 18, banquier, 0),
            (24, 'case rouge 3', batiment, ROUGE, 26, 20, banquier, 0),

            (26, 'case jaune 1', batiment, JAUNE, 30, 24, banquier, 0),
            (27, 'case jaune 2', batiment, JAUNE, 30, 24, banquier, 0),
            (29, 'case jaune 3', batiment, JAUNE, 35, 29, banquier, 0),

            (31, 'case verte 1', batiment, VERT, 40, 35, banquier, 0),
            (32, 'case verte 2', batiment, VERT, 40, 35, banquier, 0),
            (34, 'case verte 3', batiment, VERT, 45, 37, banquier, 0),

            (36, 'case bleue 1', batiment, BLEU_FONCE, 50, 40, banquier, 0),
            (39, 'case bleue 2', batiment, BLEU_FONCE, 55, 45, banquier, 0),

            (5, 'case transport 1', batiment, transport, 20, 10, banquier, 0),
            (15, 'case transport 2', batiment, transport, 20, 10, banquier, 0),
            (25, 'case transport 3', batiment, transport, 20, 10, banquier, 0),
            (35, 'case transport 4', batiment, transport, 20, 10, banquier, 0), 

            (12, 'case intercom 1', batiment, intercom, 25, 10, banquier, 0),
            (28, 'case intercom 2', batiment, intercom, 25, 10, banquier, 0),

            (10, 'case Bibliothèque', batiment, bibliothèque, 0, 0, jeux, 0),
            (20, 'case Parking gratuit', batiment, parking, 0, 0, jeux, 0),
            (30, 'case Aller à la bibliothèque', batiment, allerBibliothèque, 0, 0, jeux, 0)]


c.executemany(' INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?, ?)', cases)

conn.commit()



conn = sqlite3.connect('player.db')
c = conn.cursor()

c.execute( """ 
        CREATE TABLE IF NOT EXISTS player (
            numero real,
            name TEXT NOT NULL,
            argent real,
            position real,
            bibliotheque real,
            carteSortieBibli real,
            double real
        ) 
        """)

joueur = [(1, 'Emilie', 200, 0, 0, 0, 0),
            (2, 'Amandine', 200, 0, 0, 0, 0),
            (3, 'Noémie', 200, 0, 0, 0, 0),
            (4, 'Nicolas', 200, 0, 0, 0, 0)]

c.executemany('INSERT INTO player VALUES (?, ?, ?, ?, ?, ?, ?)', joueur)

conn.commit()