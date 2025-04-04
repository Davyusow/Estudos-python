#!/usr/bin/env python3

Jogadores = [];jogador = {}

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = []
jogador['Total'] = 0
for i in range(0,partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['Total']+=jogador['Gols'][i]
Jogadores.append(jogador.copy())
jogador.clear()

while(True):
    prox = str(input(f'{"-"*50}\nDeseja continuar?[S/N] ')).strip().upper()[0]
    if(prox != 'N' and prox != 'S'):
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
    elif(prox == 'N'):break
    elif(prox == 'S'):
        jogador['Nome'] = str(input('Nome do jogador: '))
        partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
        print("-"*50)
        jogador['Gols'] = []
        jogador['Total'] = 0
        for i in range(0,partidas):
            jogador['Gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
            jogador['Total']+=jogador['Gols'][i]
        Jogadores.append(jogador.copy())
        jogador.clear()
print(f'{"Cod.":<5}{"Nome":<15}{"Gols":<20}{"Total":<10}')
for i in range(0,len(Jogadores)):
    print(f'{i:<5}{Jogadores[i]["Nome"]:<15}{str(Jogadores[i]["Gols"]):<20}{Jogadores[i]["Total"]:<10}')
while(True):
    prox = int(input(f'{"-"*50}\nDeseja ver os dados de qual jogador?[999 para parar]: '))
    if(prox >= 0 and prox <len(Jogadores)):
        print(f'Mostrando os dados de {Jogadores[prox]["Nome"]}')
        for i in range(0,len(Jogadores[prox]['Gols'])):
            print(f'No Jogo {i+1} fez {Jogadores[prox]["Gols"][i]} gols.')
    elif(prox == 999):break
    else:print('{}Opção inválida!{}'.format('\033[31m','\033[m'))

