#!/usr/bin/env python3
i=0
soma = 0
n1 = 0
while(n1 != 999):
    n1 = int(input('Insira o número: '))
    if(n1 != 999): soma+=n1 ; i+=1
print('Foram digitados {} números, onde a soma deles é igual a {}'.format(i,soma))
