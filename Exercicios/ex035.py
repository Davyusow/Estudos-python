#!/usr/bin/env python3

n1 = float(input('Digite o 1° segmento: '))
n2 = float(input('Digite o 2° segmento: '))
n3 = float(input('Digite o 3° segmento: '))

if(n1+n2>n3 and n1+n3>n2 and n2+n3>n1): #A soma de quaisquer dois lados deve ser maior que o terceiro lado
    print('Os 3 segmentos podem formar um triângulo')
else:
    print('Os 3 segmentos não podem formar um triângulo')

