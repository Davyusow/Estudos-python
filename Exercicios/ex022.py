#!/usr/bin/env python3

nome = str(input('Digite seu nome: '))
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
tam = len(nome) - nome.count(' ')
print('Quantas letras ao todo?: {}'.format(tam))
particao = nome.split()
print('Quantas letras tem o primeiro nome?: {}'.format(len(particao[0])))
