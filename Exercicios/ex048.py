#!/usr/bin/env python3

print('A soma entre os números ímpares e múltiplos de 3 de 1 a 500 são: ')
s = 0
for i in range(1,501):
    if(i % 2 != 0 and i % 3 == 0):
        s+=i
print(s)
