#!/usr/bin/env python3
def funcao():
    n1 = 4
    print(f'n1 local vale {n1}')
def exemplo():
    global n1   #faz a função usar a variável global e não a local
    n1 +=2

n1 = 2
funcao()
print(f'n1 global vale {n1}')


