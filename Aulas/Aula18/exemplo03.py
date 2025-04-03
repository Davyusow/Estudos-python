#!/usr/bin/env python3

galera = list();dado = list()

for i in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()    #limpa os valores de dado
print(dado)
print(galera)

for p in galera:
    if(p[1]>=21): print(p[0])
