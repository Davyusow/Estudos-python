#!/usr/bin/env python3

n1 = int(input('Digite um número'))
ano = n1%4
if(ano==0):
    print('{} é um ano bissexto',n1)
else:
    print('{} não é um ano bissexto',n1)
