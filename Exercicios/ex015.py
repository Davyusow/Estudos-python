#!/usr/bin/env python3

n1 = float(input('Digite a quantidade de kilometros(km) percorridos com o carro alugado: '))
n2 = int(input('Digite a quantidade de dias em que o carro foi alugado: '))
total = (60*n2)+(0.15*n1)
print('O total a pagar é de R${:.2f}'.format(total))
