#!/usr/bin/env python3

dis = float(input('Digite a distância'))

if(dis<=200):
    print('O preço da viagem é de {}'.format(dis*0.5))
else:
    print('O preço da viagem é de {}'.format(dis*0.45))
