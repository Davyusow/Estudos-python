#!/usr/bin/env python3
soma = 0 ; cont = 0
while(True):
    n1 = int(input('Insira um valor inteiro [999 para parar]: '))
    if(n1 == 999): break
    soma += n1
    cont += 1
print(f'A soma dos valores {cont} é {soma}!')
