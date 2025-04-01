#!/usr/bin/env python3
cont = 0
fatorial = int(input('Insira um número para encontrar seu fatorial: '))
cont = fatorial
print('{}! = '.format(fatorial),end='')
while(cont>0):
    if(cont != 1):
        print('{} x '.format(cont),end='')
        cont -=1
        fatorial*=cont
    else:
        print('{} = {}'.format(cont,fatorial))
        cont = 0
