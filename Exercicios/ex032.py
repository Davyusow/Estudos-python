#!/usr/bin/env python3
from datetime import date

n1 = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
n1 = n1 if (n1!=0) else date.today().year   # date.today().year pega o ano atual do horário do sistema
if(n1 % 4 == 0 and n1%100 != 0 or n1 % 400 ==0):    #se n1 for divisível por 4 e múltiplo de 100 ou n1 for divisível por 400
    print('{} é um ano bissexto'.format(n1))
else:
    print('{} não é um ano bissexto'.format(n1))

