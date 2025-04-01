#!/usr/bin/env python3


n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
escolha = 0
while(escolha != 5):
    
    escolha = int(input('{} Escolha uma Opção: {}\n'
    '[ 1 ] SOMAR\n'
    '[ 2 ] MULTIPLICAR\n'
    '[ 3 ] MAIOR\n'
    '[ 4 ] NOVOS NÚMEROS\n'
    '[ 5 ] SAIR DO PROGRAMA\nOpção: '.format('-'*4,'-'*4)))
    if(escolha>=1 and escolha<=5):
        if(escolha == 1):
            print('Resultado : {} + {} = {}'.format(n1,n2,n1+n2))
        if(escolha == 2):
            print('Resultado : {} X {} = {}'.format(n1,n2,n1*n2))
        if(escolha == 3):
            if(n1>n2): print('O maior é {}'.format(n1))
            elif(n2>n1): print('O maior é {}'.format(n2))
            else: print('Os dois valores são iguais!')
        if(escolha == 4):
            n1 = int(input('Digite o 1° valor: '))
            n2 = int(input('Digite o 2° valor: '))
    #assim como a escolha 5 que iria apenas sair do programa
    else:
        print('{}Opção inválida!{}'.format('\033[31m','\033[m'))
print('Fim')
