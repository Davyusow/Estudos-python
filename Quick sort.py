#!/usr/bin/env python3


def quickSort(vetor,primeiro,ultimo):
    if (primeiro < ultimo):
        chave = particionar(vetor,primeiro,ultimo)
        quickSort(vetor,primeiro,chave-1)
        quickSort(vetor,chave + 1,ultimo)


def particionar(vetor,primeiro,ultimo):
    ultimoValor = vetor[ultimo]
    indice = primeiro - 1
    for comparador in range(primeiro,ultimo-1):
        if(vetor[comparador] <= ultimoValor):
            indice += 1
            temp = vetor[indice]
            vetor[indice] = vetor[comparador]
            vetor[comparador] = temp
    return indice+1


conjunto = [9,8,7,6,5,4,3,2,1]
print(conjunto)
quickSort(conjunto,0,8)
print(conjunto)
