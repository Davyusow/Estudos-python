#!/usr/bin/env python3

n1 = float(input('Qual o salário atual do funcionário?: R$'))
print('Um funcionário que ganhava R${:.2f}\nCom um aumento de 15%, passa a receber R${:.2f}'.format(n1,n1*1.15))
