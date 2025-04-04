#!/usr/bin/env python3

Jogador = {}
Jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {Jogador["Nome"]} jogou? '))
print("-"*50)
Jogador['gols'] = []
Jogador['Total'] = 0
for i in range(0,partidas):
    Jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    Jogador['Total']+=Jogador['gols'][i]
print("-"*50,'\n',Jogador,'\n',"-"*50)
print(f'O campo nome tem o valor {Jogador["Nome"]}')
print(f'O campo gols tem o valor {Jogador["gols"]}')
print(f'O jogador jogou {partidas} partidas')
for i in range(0,len(Jogador['gols'])):
    print(f'Na partida {i+1} fez {Jogador["gols"][i]} gols')
print(f'Foi um total de {Jogador["Total"]} gols')
