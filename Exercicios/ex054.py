#!/usr/bin/env python3
from datetime import date

ano = date.today().year
lista = [0,0,0,0,0,0,0]
quantidade = 0
for i in range(0,7):
    lista[i] = int(input('Digite o seu ano de Nascimento: '))
for i in range(0,7):
    if((ano-lista[i])>18):
        quantidade+=1

if(quantidade>0):
    print('{} pessoas são maiores de idade!'.format(quantidade))
else:
    print('Nenhuma pessoa é maior de idade ainda!')
