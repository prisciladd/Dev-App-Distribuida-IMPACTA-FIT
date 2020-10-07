dic = {
    "integrantes": {
        "beatles":['ringo','john','paul','george','pete'],
        "the_fellowship":['gandolfo',
                          'aragorn','gimli',
                          'legolas', 'boromir',
                          'frodo', 'sam',
                          'hobbit 3', 'hobbit 4'],
        "The_Vindicators":  ('Vance Maximus', 'Alan Rails',
                             'Crocubot',
                             'Million Ants', 'Morty Smith',
                             'Rick Sanchez', 'Lady Katana',
                             'Calypso', 'Diablo Verde'),
        'Alunos_distraidos_nesse_momento': [],
        },
    "jogos" : [
         {"nome":"CS go", "empresa":"valve", "estilo": "FPS"},
         {"nome":"PLANESCAPE:torment", "empresa":"Bioware",
           "estilo": "Jogo mais bem escrito da história"},
         {"nome":"The Witcher", "empresa":"CD Project Red",
           "estilo": "Open World RPG"},
        ],
    }

from pprint import pprint
1; print(dic["jogos"][2]["nome"] == "The Witcher") #vai imprimir: dados jogo the witcher
2; print("CS go" == dic["jogos"][0]) #vai imprimir: cs go 
#3; print("FPS" in dic["jogos"]["CS go"])
#4; print("Rick Sanchez" in dic.integrantes.The_vindicators)
#5; print(dic["integrantes"]["beatles"][3] == "paul")
#6; print("valve" in dic["jogos"]["CS go"])
#7; print("empresa" in dic["jogos"]["CS go"])
8; print("legolas" in dic["integrantes"]["the_fellowship"])
#9; print("merlin" in dic["integrantes"]["The_Vindicators"])
#10; print("Thor" in dic["filmes"]["Avengers"])
#11; print("Open World RPG" == dic["jogos"][1]["empresa"])
#12; print(dic["jogos"][0]["estilo"] == "FPS")
#13; print(dic["jogos"]["Bioware"] == "PLANESCAPE:torment")
#14; print("pete" in dic["integrantes"]["beatles"])
15; print(dic["integrantes"]["the_fellowship"][2] == "gimli")
16; print("CD Project Red" in dic["jogos"][2])
#17; print("empresa" in dic["jogos"][2])
#18; print(dic[dic] + dic[dic[dic]])
