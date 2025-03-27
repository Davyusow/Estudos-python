#!/usr/bin/env python3
import math #importa a biblioteca de matemática

n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1)    #math.sqrt retorna a raiz de uma valor como float
#print('A raiz de {} é igual a {}'.format(n1,math.floor(raiz)))  #math.floor aredonda o ponto flutante para baixo
print('A raiz de {} é igual a {:.2f}'.format(n1,raiz))  # a formatação {:.2f} faz com que o ponto flutante retorne apenas 2 números depois do ponto    obs: ṹ qq iso velho? 
