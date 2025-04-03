#!/usr/bin/env python3
from random import randint
from time import sleep

Jogos = []  #todos os jogos
jogo = []   #jogo temporário
quantidade = 0
print('{}\n{:^30}\n{}'.format('-'*30,'Mega Sena','-'*30))

quantidade = int(input('Quantos jogos deseja que eu sorteie? '))
for i in range(0,quantidade):
    while(True):
        num = randint(0,60)
        if num not in jogo:
            jogo.append(num)
        if (len(jogo) == 6): break
    jogo.sort()
    Jogos.append(jogo[:])
    jogo.clear()
    print(f'Jogo {i+1}: {Jogos[i]}')
    sleep(1)
