#!/usr/bin/env python3

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]# o primeiro colchete é tratado como o y, e os próximo como a coordenada x
somaPar = 0;soma3Col = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Insira o valor para [{i}, {j}]: '))
        if(matriz[i][j] % 2 == 0 ): somaPar+=matriz[i][j]
        if(j==2): soma3Col+=matriz[i][j]
maior2x=matriz[1][0]

for i in range(0,3):
    for j in range(0,3):
        if(matriz[1][j]>maior2x): maior2x = matriz[1][j]    #eu sei q iso ta muito feio
        print(f'[ {matriz[i][j]:^5} ]',end='')
    print()

print(f'A soma dos pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {soma3Col}')
print(f'O maior valor da segunda linha é {maior2x}')
