#!/usr/bin/env python3

def isTrasposta(matriz1,matriz2):
    resultado = False
    if(len(matriz1) == len(matriz2[0]) and len(matriz1[0]) == len(matriz2)):
        for x in range(len(matriz1)):
            for y in range(len(matriz1[0])):
                if(matriz1[x][y] == matriz2[y][x]):
                    print(f'{matriz1[x][y]} = {matriz2[y][x]} ? {matriz1[x][y] == matriz2[y][x]}')
                    resultado = True
                else:
                    resultado = False
                    break
            if(resultado == False):
                break
    else:
        print("Tamanhos incompatívies")
    return resultado

matriz1 = [[1,2,3],
          [4,5,6]]
matriz2 = [[1,4],
          [2,5],
          [3,6]]
print(isTrasposta(matriz1,matriz2))
