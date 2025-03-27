#!/usr/bin/env python3

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
exponencial = pow(n1,n2)
#print('A soma vale {},A subtracao vale {} e A multiplicacao vale {}'.format(soma,subtracao,multiplicacao), end='') #o end='' faz com que a linha não seja pulada
#print(' A divisao vale {},A divisao inteira vale {} e A exponencial vale {}'.format(divisao,divisaoInteira,exponencial))

print('A soma vale {}\nA subtracao vale {}\nA multiplicacao vale {}'.format(soma,subtracao,multiplicacao))
print(' A divisao vale {}\nA divisao inteira vale {}\nA exponencial vale {}'.format(divisao,divisaoInteira,exponencial))