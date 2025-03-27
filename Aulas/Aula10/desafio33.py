#!/usr/bin/env python3

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if(n1>n2):
    if(n1>n3):
        print('{} é o maior'.format(n1))
    else:
        print('{} é o maior'.format(n3))
else:
    print('{} é maior'.format(n2))

if(n3<n2):
    if(n3<n1):
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n1))
else:
    print('{} é menor'.format(n2))

