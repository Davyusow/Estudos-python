#!/usr/bin/env python3

tempo = int(input('Quantos anos tem seu carro: '))
if (tempo<=3):
    print('Carro novo')
else:
    print('Carro velho')
print('Fim')

print('Carro novo'if tempo<=3 else 'carro velho')   #condição simplificada
