#!/usr/bin/env python3

while(True):
    n1 = int(input('Escolha um valor: '))
    if(n1 < 0): break
    print('{}'.format('-'*15))
    for i in range(1,11):
        print(f'{n1} x {i:2} = {n1*i}')
    print('{}'.format('-'*15))
print('Fim')
