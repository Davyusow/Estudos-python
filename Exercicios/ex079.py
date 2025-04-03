#!/usr/bin/env python3

n1 = list()
prox = 'S'
while(True):
    if(prox == 'S'):
        while(True):
            teste = int(input('Insira um número: '))
            if(teste in  n1):
                print('{}O número já está inserido na lista, tente outro!{}'.format('\033[31m','\033[m'))
            else:   #elif(teste not in n1)
                n1.append(teste)
                break
    prox = str(input('Deseja inserir outro número? [S/N] ')).strip().upper()
    if(prox != 'S' and prox != 'N'):
        print('{}Opção Inválida!{}'.format('\033[31m','\033[m'))
    elif(prox == 'N'): break
n1.sort()
print('Os números em ordem crescente são: ')
for i in n1:
    print(i)
