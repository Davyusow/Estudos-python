#!/usr/bin/env python3

n1 = int(input('Digite um número: '))

print('-'*12)

for i in range(1,n1+1):
    print('{} X {} = {}'.format(n1,i,n1*i))
 
print('-'*12)
