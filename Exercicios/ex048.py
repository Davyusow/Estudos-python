#!/usr/bin/env python3

s = 0
cont = 0
for i in range(1,501,2):    #mais otimizado
    if(i % 3 == 0):
        s+=i
        cont+=1
print('A soma entre os {} valores solicitados é: {}'.format(cont,s))
