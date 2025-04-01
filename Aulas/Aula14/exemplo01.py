#!/usr/bin/env python3

for i in range(1,10):
    print(i)
print('Fim')

i=1

while(i<10):    #enquanto i menor que 10, faça
    print(i); i +=1
print('Fim')

i=1

for i in range(1,5):
    n = int(input('Digite um valor: '))
print('Fim')

impar = 0; par = 0

while(n != 0):
    n = int(input('Digite um valor: '))
    if(n % 2 == 0 and n != 0):
        par+=1
    elif(n %2 != 0 and n != 0):
        impar+=1
print('Foram digitados {} números pares e {} ímpares'.format(par,impar))
