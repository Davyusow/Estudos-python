#!/usr/bin/env python3

nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu segundo nome é: {}'.format(nome[len(nome)-1]))