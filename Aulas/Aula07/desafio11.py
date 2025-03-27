#!/usr/bin/env python3

n1 = int(input('Digite a altura da parede: '))
n2 = int(input('Digite a largura da parede: '))
n3 = n1*n2  #àrea
n4 = n3//2  #litros de tinta necessária

print('Para pintar {}m² de parede, serão necessários {}L de tinta'.format(n3,n4))
