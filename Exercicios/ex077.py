#!/usr/bin/env python3

frase = ('casa','pedra','rua','parede','porta')

for i in frase:
    if('a','e','i','o','u' in i):
        print(f'A palavra {i.upper()} tem as vogais:', end=' ')
        if('a' in i):print('a ', end='')
        if('e' in i):print('e ', end='')
        if('i' in i):print('i ', end='')
        if('o' in i):print('o ', end='')
        if('u' in i):print('u ', end='')
        print('\n')
