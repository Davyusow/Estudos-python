#!/usr/bin/env python3
s=0
c=0
for i in range(0,6):
    n1 = int(input('Digite o {}° número: '.format(i+1)))
    if(n1 % 2 == 0):
        s+=n1
        c+=1
print('Você informou {} números pares, onde a soma deles é: {}'.format(c,s))
