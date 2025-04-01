#!/usr/bin/env python3

n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 0
tam = 10

while(cont<tam):
    if(cont == tam-2):
        print('{} '.format(n1+razao),end='')
    else:
        print('{} '.format(n1+razao),end=' → ')
    n1+=razao
    cont+=1
    if(cont == tam-1):
        tam = int(input('\nDeseja ver mais algum termo? se sim quantos? '))
        if(tam != 0): tam = cont + tam + 1
print('A progressão foi finalizada com {} termos mostrados'.format(cont+1))
