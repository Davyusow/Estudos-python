#!/usr/bin/env python3

n1 = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da PA: '))

for i in range(n1,n1+razao*11,razao):
    print(i)

