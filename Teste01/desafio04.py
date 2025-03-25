#!/usr/bin/env python3
n = input('Digite algo: ')

try:
    if '.' in n:
        float(n)  # Tenta converter para float
        print('A variável é um ponto flutuante (float)')
    else:
        int(n)  # Tenta converter para int
        print('A variável é um inteiro')
except ValueError:
    print('A variável é uma string')