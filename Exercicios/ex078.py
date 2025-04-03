#!/usr/bin/env python3

n = list()

for i in range(0,5): n.append(int(input(f'Insira o {i+1}° valor: ')))

maior = n.index(max(n))
menor = n.index(min(n))

print(f'O maior valor foi {max(n)} na posição',end=' ')
if n.count(max(n)) > 1:
    for i in range (0,5):
        if(max(n) == n[i]): print(i+1,end=' ')
    print('')
else:
    print(maior+1)

print(f'O menor valor foi {min(n)} na posição',end=' ')
if n.count(min(n)) > 1:
    for i in range (0,5):
        if(min(n) == n[i]): print(i+1,end=' ')
    print('')
else:
    print(menor+1)
