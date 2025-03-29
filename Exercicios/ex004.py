#!/usr/bin/env python3

texto = str(input('Digite algo: '))

print('O tipo primitivo deste valor é: {}'.format(type(texto)))
print('Só tem espaços?: {}'.format(texto.isspace()))
print('É um número?: {}'.format(texto.isnumeric()))
print('É alfabético?: {}'.format(texto.isalpha()))
print('É um alfanumérico?: {}'.format(texto.isalnum()))
print('Está em maiúsculas?: {}'.format(texto.isupper()))
print('Está em minúsculas?: {}'.format(texto.islower()))
print('Está capitalizada?: {}'.format(texto.istitle()))
