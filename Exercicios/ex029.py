#!/usr/bin/env python3

km = int(input('Qual a velocidade atual do carro? '))

if(km >80):
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h\nVocê deve pagar uma multa de R${:.2f}!'.format(float((km-80)*7)))
print('Tenha um bom dia! Dirija com segurança!')
