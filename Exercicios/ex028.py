#!/usr/bin/env python3
from random import randint
from time import sleep
print('-='*25)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-='*25)

n1 = randint(0,5)
n2 = int(input('Tente acertar: '))

if(n1>=0 and n2<=5): # o 'and' adiciona outra condição ao programa, no caso obriga o número a estar entre 0 e 5
    print('Processando...')
    sleep(2)    #faz uma espera de 2 segundos
    if(n2 == n1 ):
        print('Parabéns você acertou!')
    else:
        print('você errou, tente novamente!')
else:
    print('O número precisa estar entre 0 e 5!, tento novamente!')
    
