#!/usr/bin/env python3

from random import randint
from time import sleep

cont = 0
while(True):
    fase = 0    #0 reinicia desde o inicio, 1 prossegue para a escolha de números, 2 finaliza o jogo
    print('\n{} Par ou Ímpar! {}\n'.format('='*5,'='*5))    #título
    jogadorE = int(input('Escolha entre ímpar ou Par[1/2]: '))  #jogadorE é a escolha entre par ou ímpar
    if(jogadorE == 1): fase = 1
    elif(jogadorE == 2): fase = 1
    else: print('{}Escolha 1 para ímpar e 2 para par, tente novamente!{}'.format('\033[31m','\033[m'))  #se a escolha for inválida
    while(fase == 1):   #enquanto estiver na fase 1:
        jogadorN = int(input('Escolha um número entre 1 e 10: ')) #número do jogador
        if(jogadorN <1 or jogadorN > 10): # se for um valor inváldo
            print('{}Opção inválida!, o número precisa estar entre 1 e 10!{}'.format('\033[31m','\033[m'))
        else:
            computadorN = randint(1,10)  #número do computador
            print('Ímpar ou..',end=' ')
            print(' Par!')
            sleep(1)
            if(jogadorE == 1):  #e for ímpar
                print('Você escolheu Ímpar e o computador Par\n'
                f'você escolheu {jogadorN} e o computador {computadorN}')
                if((jogadorN + computadorN) % 2 == 0):
                    print(f'a soma foi {jogadorN+computadorN} que é par, você perdeu!')
                    fase = 2
                    break
                else:
                    print(f'a soma foi {jogadorN+computadorN} que é ímpar, você venceu!')
                    cont+=1
                    break
            else:   #se for par:
                print('Você escolheu Par e o computador Ímpar\n'
                f'você escolheu {jogadorN} e o computador {computadorN}')
                if((jogadorN + computadorN) % 2 == 1): 
                    print(f'a soma foi {jogadorN+computadorN} que é ímpar, você perdeu!')
                    fase = 2
                    break
                else: 
                    print(f'a soma foi {jogadorN+computadorN} que é par, você venceu!')
                    cont+=1
                    break
    if(fase == 2): break
print(f'\nVocê venceu {cont} vezes!')    
