#!/usr/bin/env python3
def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


Nome = str(input('Nome do Jogador: '))
Gols = str(input('Número de Gols: '))
if((Nome).strip() == ''):
    Nome = '<descohecido>'
if(Gols.isnumeric()): 
    Gols = int(Gols)
else:
    Gols = 0
ficha(Nome,Gols)
