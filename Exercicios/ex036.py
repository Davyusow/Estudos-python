#!/usr/bin/env python3

casa = float(input('Insira o valor da Casa: R$'))
salario = float(input('Insira o valor do salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/(anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,prestacao))
if(prestacao>salario*0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')
