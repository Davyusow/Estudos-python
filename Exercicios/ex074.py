#!/usr/bin/env python3

from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(numeros)
print(f'O maior número foi: {max(numeros)}\n' #encontra o menor valor da tupla
f'O menor número foi: {min(numeros)}')  #encontra o menor valor da tupla
