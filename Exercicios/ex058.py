#!/usr/bin/env python3
from random import randint
from time import sleep

print('-='*25)
print('Vou pensar em um número de 0 a 10, tente adivinhar')
print('-='*25)

tentativas = 1; acertou = False
n1 = randint(0,10)

while(acertou == False):    
    n2 = int(input('Tente acertar: '))
    if(n2>=0 and n2<=10): # O 'and' adiciona outra condição ao programa, no caso obriga o número a estar entre 0 e 5
        print('Processando...')
        sleep(2)    #faz uma espera de 2 segundos
        if(n2 == n1 ):
            print('{}Parabéns você acertou!\n'
            'Foram necessárias {} tentativas!{}'.format('\033[34m',tentativas,'\033[m'))
            acertou == True
            break
        else:
            if(n2>n1):
                print('Menor que isso, tente novamente!')
            elif(n2<n1):
                print('Maior que isso, tente novamente!')
            tentativas += 1
    else:
        print('{}O número precisa estar entre 0 e 10!, tente novamente!{}'.format('\033[31m','\033[m'))
