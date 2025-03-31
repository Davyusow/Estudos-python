#!/usr/bin/env python3

n1 = int(input('Digite um número inteiro: '))

print('Escolha um número para conversão: ')
escolha = int(input('[1] converter para BINÁRIO\n'
'[2] converter para OCTAL\n'
'[3] converter para HEXADECIMAL\n'
'Sua opção: '))

if(escolha == 1):
    print('{} convertido para BINÁRIO é igual a {}'.format(n1,bin(n1)[2:])) #o [2:] omite um prefixo retornado pela função
elif(escolha == 2):
    print('{} convertido para OCTAL é igual a {}'.format(n1,oct(n1)[2:]))   
elif(escolha == 3):
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1,hex(n1)[2:]))
else:
    print('Opção inválida')
