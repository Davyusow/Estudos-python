#!/usr/bin/env python3

n1 = float(input('Digite a distância da viagem em km: '))

print('Você está prestes a começar uma viagem de {:.1f}km'.format(n1))
if(n1>200):
    print('E o preço da sua passagem será de R${:.2f}'.format(n1*0.45))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(n1*0.5))
