#!/usr/bin/env python3

a = [2,3,4,7]
b = a     #semelhante à um ponteiro
b = a[:]  #faz uma cópia de todos os valores
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


