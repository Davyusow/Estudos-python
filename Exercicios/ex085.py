#!/usr/bin/env python3

numeros = [[],[],[]] #[x][0] são todos os números; [x][1] são os ímpares; [x][2] são os pares 

for i in range(0,7):
    numeros[0].append(int(input('Insira um número: ')))
    if(numeros[0][i] % 2 == 1):
        numeros[1].append(numeros[0][i])
    else:
        numeros[2].append(numeros[0][i])
numeros[1].sort(); numeros[2].sort() #organiza em ordem os números ímpares e pares
print(f'Os números Ímpares são: {numeros[1]}')
print(f'Os números pares são: {numeros[2]}')
