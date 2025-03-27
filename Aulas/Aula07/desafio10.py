#!/usr/bin/env python3

n1 = float(input('Digite quantos reais você possui: '))

if(n1>3.27):
    print('Com R${} você pode comprar ${} dólares'.format(n1,n1//3.27))
else:
    print('Você não pode comprar dólares com este valor')