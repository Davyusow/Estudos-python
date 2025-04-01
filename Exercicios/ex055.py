#!/usr/bin/env python3

peso = float(input('Digite o seu peso: '))
maior = peso
menor = peso
for i in range(1, 5):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi: {}kg'.format(maior))
print('O menor peso foi: {}kg'.format(menor))
