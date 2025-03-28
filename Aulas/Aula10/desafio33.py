#!/usr/bin/env python3

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = 0
menor = 0
if(n1>n2):
    if(n1>n3):
        maior = n1
    else:
        maior = n3
if(n2>n1):
    if(n2>n3):
        maior = n2
    else:
        maior = n3
    

if(n1<n2):
    if(n1<n3):
        menor = n1
    else:
        menor = n3
if(n2<n1):
    if(n2<n3):
        menor = n2
    else:
        menor = n3

print('{} é o maior, e o {} é o menor'.format(maior,menor))