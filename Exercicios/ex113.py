#!/usr/bin/env python3
def leiaInteiro(txt):
    while(True):
        try:
            n1 = int(input(txt))
        except KeyboardInterrupt:
            print('{}O usuário preferiu não inserir este número!{}'.format('\033[31m','\033[m'))
            n1 = 0
            break
        except:
            print('{}Por favor, insira um número inteiro válido!{}'.format('\033[31m','\033[m'))
        else:
            break
    return n1

def leiaFloat(txt):
    while(True):
        try:
            n1 = float(input(txt))
        except KeyboardInterrupt:
            print('{}O usuário preferiu não inserir este número!{}'.format('\033[31m','\033[m'))
            n1 = 0
            break
        except:
            print('{}Por favor, insira um número real válido!{}'.format('\033[31m','\033[m'))
        else:
            break
    return n1


n1 = leiaInteiro("Insira um valor inteiro: ")
n2 = leiaFloat('Insira um valor real: ')
print(f'O valor inteiro foi {n1} e o real {n2}')
