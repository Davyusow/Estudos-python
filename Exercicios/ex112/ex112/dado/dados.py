#!/usr/bin/env python3

def leiaDinheiro(txt):
    while(True):
        dinheiro = str(input(txt))
        if(dinheiro.replace(".","").isnumeric()):
            dinheiro = float(dinheiro)
            break
        elif(dinheiro.replace(",","").isnumeric()):
            dinheiro = dinheiro.replace(",",".")
            dinheiro = float(dinheiro)
            break
        else:
            print('{}Valor inválido!{}'.format('\033[31m','\033[m'))
    return dinheiro
