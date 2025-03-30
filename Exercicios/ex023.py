#!/usr/bin/env python3

n1 = str(input('Informe um número: '))
n1 = n1.zfill(4)    #preenche a esquerda da String de tamanho 4 com zeros

print('Unidade: {}'.format(n1[3]))
print('Dezena: {}'.format(n1[2]))
print('Centena: {}'.format(n1[1]))
print('Milhar: {}'.format(n1[0]))

