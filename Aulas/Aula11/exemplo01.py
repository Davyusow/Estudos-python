#!/usr/bin/env python3

#Padrão ANSI
#\033[0:33:44m0
#Primeiro valor dentro do colchete:
#0 = sem estilo; 1 = negrito; 4 = sublinhado; 7 fundo e cor invertida
#Segundo valor dentro do colchete (cor do texto):
#30 = branco; 31 = vermelho; 32 = verde; 33 = amarelo; 34 = azul; 35 = roxo; 36 = ciano; 37 = cinza
#Terceiro valor dentro do colchete (cor do fundo):
#40 = branco; 41 = vermelho; 42 = verde; 43 = amarelo; 44 = azul; 45 = roxo; 46 = ciano; 47 = cinza

#print('\033[0;30;41mTeste')
#print('\033[4;33;44mTeste')
#print('\033[1;34;43mTeste')
#print('\033[30;42mTeste')
#print('\033[mTeste')
#print('\033[7;30mTeste')

a=3 ; b= 5
print('Os valores são \033[32m{} e \033[31m{}'.format(a,b))

nome = 'Davyusow'
print('Prazer em te conhecer, {}{}{}!'.format('\033[4;34m',nome,'\033[m'))
cores = {'limpa':'\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m'}
print('Prazer em te conhecer, {}{}{}!'.format(cores['azul'],nome,cores['limpa']))


