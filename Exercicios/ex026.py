#!/usr/bin/env python3

frase = str(input('Digite uma frase: '))
frase = frase.strip()
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.upper().find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))