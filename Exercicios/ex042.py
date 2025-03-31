#!/usr/bin/env python3

n1 = float(input('Digite o 1° segmento: '))
n2 = float(input('Digite o 2° segmento: '))
n3 = float(input('Digite o 3° segmento: '))

if(n1+n2>n3 and n1+n3>n2 and n2+n3>n1): #A soma de quaisquer dois lados deve ser maior que o terceiro lado
    if(n1 == n2 or n1 == n3 or n2 == n3):
        if(n1==n2 and n2 == n3):
            print('Os 3 segmentos formam um triângulo EQUILÁTERO')
        else:
            print('Os 3 segmentos formam um triângulo ISÓCELES')
    else:
        print('Os 3 segmentos formam um triângulo ESCALENO')
else:
    print('Os 3 segmentos não podem formar um triângulo')

