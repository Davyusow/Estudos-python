#!/usr/bin/env python3

print('Os números pares de 1 à 50 são: ')
for i in range(1,51):
    if(i % 2 == 0):
        print('{} é par'.format(i))
