#!/usr/bin/env python3

resultado = True
escolha = 0
while(escolha != 5):
    if(resultado):
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
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
    #a escolha == 4 está omitida pois se o valor for 4 apenas irá reiniciar o loop
    #assim como a escolha 5 que iria apenas sair do programa
    else:
        print('Opção inválida!')
        resultado = False
print('Fim')
