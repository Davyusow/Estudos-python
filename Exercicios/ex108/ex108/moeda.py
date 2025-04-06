#!/usr/bin/env python3
def metade(m):
    resultado = m/2
    return f'{resultado:.2f}'.replace('.',',')

def dobro(m):
    resultado = m*2
    return f'{resultado:.2f}'.replace('.',',')

def aumentar(m,p):
    resultado = m * (1 + (p/100))
    return f'{resultado:.2f}'.replace('.',',')

def diminuir(m,p):
    resultado = m - (m * (p/100))
    return f'{resultado:.2f}'.replace('.',',')

def moeda(p):
    return f'{p:.2f}'.replace('.',',')