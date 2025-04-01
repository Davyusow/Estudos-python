#!/usr/bin/env python3

for i in range(0,10):   #para i no alcance de 1 até 10 faça
    print(i)
print('Fim')

for i in range(10,0,-1):  #o terceiro valor do argumendo do range é o passo
    print(i)
#
n = int(input('\nDigite um número: '))

for i in range(0,n+1):
    print(i)
print('FIM')

s = 0

for i in range(0,4):
    n = int(input('Digite um valor: '))
    s+=n
print(s)
