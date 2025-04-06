#!/usr/bin/env python3
def leiaint(titulo):
    while(True):
        num = str(input(titulo))
        if(num.isnumeric() == True):
            break
        else:
            print('{}Erro! Digite um número inteiro válido!{}'.format('\033[31m','\033[m'))
    return num

n1 = leiaint('Insira um número: ')
print(f'Você digitou o número {n1}')
