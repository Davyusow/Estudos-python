#!/usr/bin/env python3

n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 0

while(cont<9):
    print('{} '.format(n1+razao),end=' → ')
    n1+=razao
    cont+=1
print('{} '.format(n1+razao))
