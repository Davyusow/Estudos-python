#!/usr/bin/env python3
from datetime import date

ano = date.today().year
idade=0
maior = 0
menor = 0
for i in range(0,7):
    idade = int(input('Digite o seu ano de Nascimento: '))
    if((ano-idade)>18):
        maior+=1
    else:
        menor+=1
print('{} pessoas são maiores de idade\nE {} pessoas são menores de idade'.format(maior,menor))
