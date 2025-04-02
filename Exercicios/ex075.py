#!/usr/bin/env python3

n1 = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))

print(n1)
if(9 in n1):
    print(f'O número 9 aparece {n1.count(9)} vezes')

if(3 in n1):
    print(f'O primeiro número 3 foi digitado na posição {n1.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição')

for i in range(0,4):
    if(n1[i] % 2 == 0):
        print(f'{n1[i]} é par')
