#!/usr/bin/env python3
from random import randint; from time import sleep
def Sorteador():
    Lista = []
    print('Sorteando 5 valores da lista: ')
    for i in range(0,5):
        Lista.append(randint(0,10))
        print(Lista[i],end=" ",flush=True)
        sleep(0.5)
    print('PRONTO!')
    return Lista
def Somador(Lista):
    soma = 0
    for i in range(0,len(Lista)):
        soma+=Lista[i]
    print(f'Somando os valores pares de {Lista}, temos {soma}')



num = Sorteador()
Somador(num)
