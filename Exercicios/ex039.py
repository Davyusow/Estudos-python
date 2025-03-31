#!/usr/bin/env python3
from datetime import date

anoAtual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = anoAtual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,anoAtual))


if(idade<18):
    print('Ainda faltam {} anos para o alistamento\n'
    'Seu alistamento será em {}'.format(18-idade,(18-idade)+anoAtual))
elif(idade>18):
    print('Você já deveria ter se alistado há {} anos\n'
    'Seu alistamento foi em {}'.format(idade-18,anoAtual-(idade-18)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
