#!/usr/bin/env python3

Jogadores = [];jogador = {}

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
print("-"*50)
jogador['gols'] = []
jogador['Total'] = 0
for i in range(0,partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['Total']+=jogador['gols'][i]
Jogadores.append(jogador.copy())
jogador.clear()

while(True):
    prox = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if(prox != 'N' and prox != 'S'):
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    elif(prox == 'N'):break
    elif(prox == 'S'):
        jogador['Nome'] = str(input('Nome do jogador: '))
        partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
        print("-"*50)
        jogador['gols'] = []
        jogador['Total'] = 0
        for i in range(0,partidas):
            jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
            jogador['Total']+=jogador['gols'][i]
        Jogadores.append(jogador.copy())
        jogador.clear()
for i in Jogadores:
    print("-"*50,'\n',i,'\n',"-"*50)
    print(f'O campo nome tem o valor {i["Nome"]}')
    print(f'O campo gols tem o valor {i["gols"]}')
    print(f'O i jogou {partidas} partidas')
    for j in range(0,len(i['gols'])):
        print(f'Na partida {j+1} fez {i["gols"][j]} gols')
    print(f'Foi um total de {i["Total"]} gols')
