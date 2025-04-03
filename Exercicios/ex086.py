#!/usr/bin/env python3

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]# o primeiro colchete é tratado como o y, e os próximo como a coordenada x

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Insira o valor para [{i}, {j}]: '))
for i in range(0,3):
    for j in range(0,3):
        print(f'[ {matriz[i][j]:^5} ]',end='')
    print()
