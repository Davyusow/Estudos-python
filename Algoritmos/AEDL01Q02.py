#!/usr/bin/env python3

def potencia(base, potencia):
    resultado = base
    for indice in range(potencia-1):
        resultado *= base
    return resultado

def somaVetores(vetor1,vetor2,tam):
    numerador = 0
    divisor = 0
    for indice in range(tam):
        numerador += potencia(vetor1[indice],2) + potencia(vetor2[indice],2)
        divisor += vetor1[indice]*vetor2[indice]
    print(numerador)
    print(divisor)
    return numerador/divisor


vetor1 = [1,2,3]
vetor2 = [1,2,3]

resultado = somaVetores(vetor1,vetor2,3)
print(vetor1)
print(vetor2)
print(resultado)
