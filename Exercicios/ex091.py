#!/usr/bin/env python3
from random import randint; from time import sleep
from operator import itemgetter #outra alternativa

Jogadores = [{'Nome':'Jogador1','Dado':randint(1,6)},
             {'Nome':'Jogador2','Dado':randint(1,6)},
             {'Nome':'Jogador3','Dado':randint(1,6)},
             {'Nome':'Jogador4','Dado':randint(1,6)}]
for i in Jogadores:
    print(f'O {i["Nome"]} tirou {i["Dado"]}') 
    sleep(1)
Jogadores.sort(key=lambda x:x['Dado'],reverse=True)
#ranking = {}
#ranking = sorted(Jogadores.items(),key=itemgetter) ;teria que mudar a estrutura da Lista Jogadores mas organiza sim
print('Ranking dos Jogadores: ')
for i in range(0,len(Jogadores)):
    print(f'{i+1}° lugar: {Jogadores[i]["Nome"]} com {Jogadores[i]["Dado"]}')
