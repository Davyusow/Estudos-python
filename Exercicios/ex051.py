#!/usr/bin/env python3

n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(n1,n1+razao*10,razao):
    print(i,end=' → ')
print('Fim!')
