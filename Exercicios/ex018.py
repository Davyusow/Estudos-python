#!/usr/bin/env python3
import math

n1 = float(input('Digite um ângulo que você deseja: '))
n2 = math.radians(n1) #as funções sin,cos e tan precisam de um valor em radianos, logo, math.radians faz a conversão
print('O ângulo de {:.2f}° tem o seno de {:.2f}'.format(n1,math.sin(n2)))
print('O ângulo de {:.2f}° tem o cosseno de {:.2f}'.format(n1,math.cos(n2)))
print('O ângulo de {:.2f}° tem a tangente de {:.2f}'.format(n1,math.tan(n2)))
